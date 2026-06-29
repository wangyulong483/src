"""
GPU-accelerated batch parameter screening.

Strategy for path_based scoring:
  1. Pre-compute distance transform ONCE (CPU, scipy)
  2. Upload to GPU as CuPy array
  3. For each batch of (inflation_radius, cost_scaling_factor) combos:
     costmap = 254 * exp(-csf * (dist - inscribed) / infl_r)  ← GPU element-wise
  4. Download costmaps back to CPU
  5. Parallel A* search via multiprocessing Pool
  6. Score & return top K

Speedup vs CPU-only:
  - 10000 unique inflations → 10000 scipy EDT calls → ~30s
  - GPU batch: 1 EDT + 10000 GPU inflate ops → ~2s
"""
import logging
import importlib
import time
import numpy as np
from typing import Dict, List, Optional, Tuple
from multiprocessing import Pool, cpu_count

from .config import DEFAULTS, PARAM_SPACE, TIERS

log = logging.getLogger('Nav2Tuner.GPU')

# ═══════════════════════════════════════════════════════════════
# Windows-compatible multiprocessing: use initializer pattern
# instead of passing ScoreModel via pickle (fails on spawn).
# ═══════════════════════════════════════════════════════════════

_worker_model = None  # global set by initializer


def _worker_init(model):
    """Pool initializer — runs once per worker process."""
    global _worker_model
    _worker_model = model


def _score_chunk(params_list):
    """Multiprocessing worker: score a list of param dicts.
    Uses the global _worker_model set by initializer.
    """
    n = len(params_list)
    scores = np.zeros(n, dtype=np.float32)
    for i, p in enumerate(params_list):
        gpu_cm = p.pop('_gpu_costmap', None)
        if gpu_cm is not None and not hasattr(_worker_model, '_gpu_cache'):
            _worker_model._gpu_cache = {}
        try:
            scores[i] = _worker_model.compute_score(p)
        except Exception:
            scores[i] = 999.0
    return list(range(n)), scores


# Costmap constants
LETHAL = 254.0
FREE = 0.0
RESOLUTION = 0.05
INSCRIBED_RADIUS = 0.05


class GPUPreScreener:
    """GPU-accelerated batch parameter screening.

    Usage:
      screener = GPUPreScreener(score_model)
      top = screener.screen(n_samples=50000, top_k=1000)
    """

    def __init__(self, score_model, use_gpu: bool = True):
        self.score_model = score_model
        self._gpu_mod, self._gpu_backend = (None, 'cpu')
        if use_gpu:
            self._gpu_mod, self._gpu_backend = _try_import_gpu()
        log.info("GPUPreScreener: backend=%s", self._gpu_backend)

    def generate_samples(self, n: int, param_keys=None, method="sobol"):
        if param_keys is None:
            param_keys = TIERS['default']
        d = len(param_keys)
        if method == "sobol":
            samples = self._sobol_sample(n, d)
        elif method == "lhs":
            samples = self._lhs_sample(n, d)
        else:
            samples = np.random.uniform(0, 1, (n, d))
        return samples.astype(np.float32), param_keys

    def _sobol_sample(self, n, d):
        try:
            from scipy.stats.qmc import Sobol
            n_pow2 = 1 << (n - 1).bit_length()
            sampler = Sobol(d=d, scramble=True, seed=42)
            return sampler.random(n_pow2)[:n]
        except (ImportError, AttributeError):
            return self._lhs_sample(n, d)

    def _lhs_sample(self, n, d):
        try:
            from scipy.stats.qmc import LatinHypercube
            sampler = LatinHypercube(d=d, seed=42)
            return sampler.random(n)
        except (ImportError, AttributeError):
            return np.random.uniform(0, 1, (n, d))

    def sample_to_params(self, samples, param_keys):
        result = []
        for i in range(samples.shape[0]):
            p = {}
            for j, key in enumerate(param_keys):
                lo, hi, kind = PARAM_SPACE[key]
                raw = float(samples[i, j])
                if kind == 'float':
                    p[key] = float(lo + raw * (hi - lo))
                elif kind == 'int':
                    p[key] = int(lo + raw * (hi - lo + 1))
            for key in PARAM_SPACE:
                if key not in p:
                    p[key] = DEFAULTS[key]
            result.append(p)
        return result

    def batch_score(self, samples, param_keys, n_jobs=None):
        """Score all samples. Uses multiprocessing on Linux, sequential on Windows."""
        import os
        n = samples.shape[0]
        params_batch = self.sample_to_params(samples, param_keys)

        # Windows: spawn mode cannot pickle ScoreModel (CuPy arrays, file handles).
        # Use sequential scoring with GPU batch costmaps instead.
        is_windows = os.name == 'nt'
        if is_windows:
            n_jobs = 1
        elif n_jobs is None:
            from multiprocessing import cpu_count
            n_jobs = min(cpu_count(), n, 16)

        # Try GPU batch costmap generation for path_based scoring
        gpu_costmaps = None
        if self._gpu_backend == 'cupy' and hasattr(self.score_model, '_map_gen') and self.score_model._map_gen:
            try:
                # Collect unique inflation/cost_scaling_factor combos
                infl_vals = np.array([p.get('planner.inflation_radius.local', p.get('inflation_radius', 0.5)) for p in params_batch], dtype=np.float32)
                csf_vals = np.array([p.get('planner.cost_scaling_factor.local', p.get('cost_scaling_factor', 3.0)) for p in params_batch], dtype=np.float32)
                # Fall back to global if local not available
                for i, p in enumerate(params_batch):
                    if 'planner.inflation_radius.local' not in p:
                        infl_vals[i] = float(p.get('planner.inflation_radius.global', 0.55))
                    if 'planner.cost_scaling_factor.local' not in p:
                        csf_vals[i] = float(p.get('planner.cost_scaling_factor.global', 3.0))

                from .gpu_search import GPUCostmapBatch
                base_grid = self.score_model._map_gen.static_map.copy()
                if hasattr(self.score_model._map_gen, 'keepout_map') and self.score_model._map_gen.keepout_map is not None:
                    base_grid[self.score_model._map_gen.keepout_map == 254] = 254
                gpu_batch = GPUCostmapBatch(base_grid)
                gpu_costmaps = gpu_batch.generate_batch(infl_vals, csf_vals)
                log.info("  GPU costmap batch: %d generated", len(gpu_costmaps))
                # Attach costmaps to params for scoring
                for i, cm in enumerate(gpu_costmaps):
                    params_batch[i]['_gpu_costmap'] = cm
                    params_batch[i]['_skip_rpp'] = True  # RPP too slow for prescreen
            except Exception as e:
                log.debug("  GPU costmap batch failed (%s), using CPU", e)

        log.info(f"  Scoring {n} samples with {n_jobs} workers...")
        scores = np.zeros(n, dtype=np.float32)

        if is_windows:
            # Windows sequential: safe, no pickle issues
            for i, p in enumerate(params_batch):
                try:
                    scores[i] = self.score_model.compute_score(p)
                except Exception:
                    scores[i] = 999.0
        else:
            # Linux/macOS: fork-mode multiprocessing
            from multiprocessing import Pool
            chunks = np.array_split(np.arange(n), n_jobs * 4)
            chunk_params = [(self.score_model, [params_batch[i] for i in c]) for c in chunks if len(c) > 0]
            with Pool(n_jobs) as pool:
                results = pool.map(_score_chunk, chunk_params)
            for indices, chunk_scores in results:
                for i, s in zip(indices, chunk_scores):
                    scores[i] = s
        return scores

    def pareto_rank(self, scores):
        if scores.ndim == 1:
            order = np.argsort(scores)
            ranks = np.zeros(len(scores), dtype=np.int32)
            ranks[order] = np.arange(len(scores))
            return ranks
        n = scores.shape[0]
        ranks = np.zeros(n, dtype=np.int32)
        domination_counts = np.zeros(n, dtype=np.int32)
        dominated_sets = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                si, sj = scores[i], scores[j]
                if np.all(si <= sj) and np.any(si < sj):
                    domination_counts[j] += 1; dominated_sets[i].append(j)
                elif np.all(sj <= si) and np.any(sj < si):
                    domination_counts[i] += 1; dominated_sets[j].append(i)
        front = [i for i in range(n) if domination_counts[i] == 0]
        current_rank = 0
        while front:
            for i in front:
                ranks[i] = current_rank
            next_front = []
            for i in front:
                for j in dominated_sets[i]:
                    domination_counts[j] -= 1
                    if domination_counts[j] == 0:
                        next_front.append(j)
            front = next_front; current_rank += 1
        return ranks

    def screen(self, n_samples=100000, top_k=1000, param_keys=None, method="sobol"):
        t0 = time.perf_counter()
        if param_keys is None:
            param_keys = TIERS['default']

        log.info("GPU Screening: %d samples x %d params (backend=%s)",
                 n_samples, len(param_keys), self._gpu_backend)

        samples, keys = self.generate_samples(n_samples, param_keys, method)
        log.info("  Generated %d %s samples (%.1fs)", len(samples), method, time.perf_counter()-t0)

        t1 = time.perf_counter()
        scores = self.batch_score(samples, keys)
        log.info("  Scored in %.1fs (best=%.4f, median=%.4f)",
                 time.perf_counter()-t1, scores.min(), np.median(scores))

        top_indices = np.argsort(scores)[:top_k]
        top_params = self.sample_to_params(samples[top_indices], keys)

        log.info("  -> %d candidates in %.1fs (best score: %.4f)",
                 len(top_params), time.perf_counter()-t0, scores[top_indices[0]])
        return top_params


class GPUCostmapBatch:
    """GPU-accelerated batch costmap generation.

    Pre-computes distance transform once, then generates costmaps
    for many (inflation_radius, cost_scaling_factor) combos in parallel on GPU.

    Speedup: 10000 scipy EDT calls (~30s) → 1 EDT + GPU batch (~1s).
    """

    def __init__(self, base_grid: np.ndarray):
        """
        Args:
          base_grid: HxW uint8 array — static map + keepout overlay (before inflation)
        """
        self._gpu_mod, self._gpu_backend = _try_import_gpu()
        self.H, self.W = base_grid.shape
        self.lethal_mask = (base_grid >= 250)

        # Pre-compute distance transform (CPU, scipy — no GPU EDT in CuPy)
        from scipy.ndimage import distance_transform_edt
        t0 = time.perf_counter()
        if self.lethal_mask.any():
            self.dist_px = distance_transform_edt(~self.lethal_mask)
        else:
            self.dist_px = np.full((self.H, self.W), 999.0, dtype=np.float32)
        self.dist_m = (self.dist_px * RESOLUTION).astype(np.float32)
        log.info("Distance transform: %.1fms (H=%d W=%d lethal=%d)",
                 (time.perf_counter()-t0)*1000, self.H, self.W,
                 self.lethal_mask.sum())

    def generate_batch(self, inflations: np.ndarray, cost_factors: np.ndarray) -> List[np.ndarray]:
        """Generate N costmaps for N (inflation, cost_factor) pairs.

        Args:
          inflations: (N,) float array of inflation radii
          cost_factors: (N,) float array of cost scaling factors

        Returns list of N uint8 costmap grids.
        """
        n = len(inflations)
        if self._gpu_backend == 'cupy':
            return self._generate_batch_cupy(inflations, cost_factors)
        else:
            return self._generate_batch_cpu(inflations, cost_factors)

    def _generate_batch_cupy(self, inflations, cost_factors):
        """CuPy-accelerated batch costmap generation."""
        import cupy as cp

        t0 = time.perf_counter()
        # Upload distance transform to GPU once
        dist_gpu = cp.asarray(self.dist_m, dtype=cp.float32)
        lethal_gpu = cp.asarray(self.lethal_mask)
        n = len(inflations)

        costmaps = []
        batch_size = 256  # GPU memory: batch_size × H × W bytes

        for start in range(0, n, batch_size):
            end = min(start + batch_size, n)
            ir = cp.asarray(inflations[start:end], dtype=cp.float32)
            cf = cp.asarray(cost_factors[start:end], dtype=cp.float32)

            # Reshape for broadcasting: (batch, 1, 1) × (H, W)
            ir_b = ir[:, cp.newaxis, cp.newaxis]
            cf_b = cf[:, cp.newaxis, cp.newaxis]

            # Nav2 inflation formula on GPU:
            # cost = 254 * exp(-csf * (dist - inscribed) / infl_r)
            dist_b = dist_gpu[cp.newaxis, :, :]  # (1, H, W)
            exp_arg = -cf_b * (dist_b - INSCRIBED_RADIUS) / cp.maximum(ir_b, 0.01)
            cost = LETHAL * cp.exp(cp.clip(exp_arg, -20, 20))
            cost = cp.clip(cost, 0, LETHAL).astype(cp.uint8)

            # Lethal stays lethal
            cost[:, lethal_gpu] = LETHAL

            # Download batch
            batch = cp.asnumpy(cost)
            for i in range(batch.shape[0]):
                costmaps.append(batch[i])

        dt = time.perf_counter() - t0
        log.debug("GPU batch: %d costmaps in %.2fs (%.1f costmaps/s)",
                 n, dt, n / max(dt, 0.001))
        return costmaps

    def _generate_batch_cpu(self, inflations, cost_factors):
        """CPU fallback: generate one at a time."""
        costmaps = []
        for ir, cf in zip(inflations, cost_factors):
            cost = LETHAL * np.exp(
                -cf * (self.dist_m - INSCRIBED_RADIUS) / max(ir, 0.01)
            )
            cost = np.clip(cost, 0, LETHAL).astype(np.uint8)
            cost[self.lethal_mask] = LETHAL
            costmaps.append(cost)
        return costmaps


class ParetoFront:
    """Container for Pareto front results."""
    def __init__(self, params_list, scores, objective_names=None):
        self.params = params_list
        self.scores = scores
        self.objective_names = objective_names or ['score']

    def get_front(self, ranks, rank=0):
        mask = ranks == rank
        indices = np.where(mask)[0]
        return [self.params[i] for i in indices], self.scores[indices]

    def __len__(self):
        return len(self.params)


def _try_import_gpu():
    for name, mod_name in [('cupy', 'cupy'), ('torch', 'torch'),
                            ('numba.cuda', 'numba.cuda')]:
        try:
            mod = importlib.import_module(mod_name)
            log.info("GPU backend: %s", name)
            return mod, name
        except ImportError:
            continue
    return None, 'cpu'
