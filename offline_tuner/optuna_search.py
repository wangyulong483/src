"""
Optuna TPE search with tiered parameter spaces and --freeze support.

Integrates with GPU pre-screening results from gpu_search.py.
Progress logging at 500-trial intervals (not 100).
"""
import logging
import os
import time
import json
from datetime import datetime
from fnmatch import fnmatch
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np

from . import config as _cfg
from .config import DEFAULTS, PARAM_SPACE, TIERS, OUT_DIR
from .score_model import ScoreModel

log = logging.getLogger('Nav2Tuner.Optuna')


class OptunaTieredSearch:
    """Optuna TPE optimization with tiered parameter spaces.

    Usage:
      model = ScoreModel(db)
      search = OptunaTieredSearch(model, tier="default", freeze=["planner.*"])
      study = search.run(n_trials=5000, n_jobs=24)
      search.print_results()
      search.save_results()
    """

    def __init__(
        self,
        score_model: ScoreModel,
        tier: str = "default",
        freeze: Optional[List[str]] = None,
        seed_params: Optional[List[Dict]] = None,
        n_startup_trials: int = 50,
    ):
        self.score_model = score_model
        self.tier = tier if tier in TIERS else 'default'
        self.freeze_patterns = freeze or []
        self.seed_params = seed_params or []
        self.n_startup_trials = n_startup_trials

        self.param_keys = self._resolve_params()
        self.study = None
        self.best_score = float('inf')
        self.trial_count = 0
        self._frozen_values: Dict[str, float] = {}

        log.info(f"OptunaTieredSearch: tier={self.tier}, "
                 f"params={len(self.param_keys)}/{len(PARAM_SPACE)}, "
                 f"frozen={len(self._frozen_values)}, "
                 f"seeds={len(self.seed_params)}")

    def _resolve_params(self) -> List[str]:
        """Return active param list based on tier and freeze patterns."""
        active = list(TIERS.get(self.tier, TIERS['default']))

        # Apply freeze patterns
        self._frozen_values = {}
        for pattern in self.freeze_patterns:
            removed = []
            for key in list(active):
                if fnmatch(key, pattern):
                    removed.append(key)
                    self._frozen_values[key] = DEFAULTS[key]
            for key in removed:
                active.remove(key)

        return active

    def _full_params(self, active_params: Dict[str, float]) -> Dict[str, float]:
        """Fill in all 27 params from active + frozen + DEFAULTS."""
        p = dict(DEFAULTS)       # start with all defaults
        p.update(self._frozen_values)  # override with frozen values
        p.update(active_params)        # override with active (sampled) values
        return p

    def _suggest_params(self, trial) -> Dict[str, float]:
        """Sample from active param space. Returns FULL dict (all 27 params)
        filled with DEFAULTS for any param not in the active tier."""
        p = {}
        for key in self.param_keys:
            lo, hi, kind = PARAM_SPACE[key]
            if kind == 'float':
                val = trial.suggest_float(key, lo, hi)
            elif kind == 'int':
                val = trial.suggest_int(key, int(lo), int(hi))
            else:
                val = (lo + hi) / 2
            p[key] = val

        return self._full_params(p)

    def _objective(self, trial) -> float:
        """Objective function: score_model.compute_score(params)."""
        params = self._suggest_params(trial)
        score = self.score_model.compute_score(params)
        self.trial_count += 1

        if score < self.best_score:
            self.best_score = score
            diffs = []
            for k, v in params.items():
                d = DEFAULTS.get(k)
                if d is not None and d != 0 and abs(v - d) / max(abs(d), 0.001) > 0.03:
                    diffs.append(f"{k.split('.')[-1]}={v:.3g}")
            diff_str = ', '.join(diffs[:4])
            log.info(f"  ★ #{self.trial_count}: score={score:.4f} | {diff_str}")

        # Progress every 500 trials
        if self.trial_count % 500 == 0:
            log.info(f"  Progress: {self.trial_count}, best={self.best_score:.4f}")

        return score

    def run(self, n_trials: int = 5000, n_jobs: Optional[int] = None) -> Optional[object]:
        """Execute Optuna TPE search. Returns optuna.Study or None."""
        try:
            import optuna
            from optuna.samplers import TPESampler
        except ImportError:
            log.error("Optuna not installed. Run: pip install optuna")
            return None

        if n_jobs is None:
            n_jobs = 1  # ★ Numba A* is 0.01ms — multiprocessing overhead dominates

        log.info(f"{'='*60}")
        log.info(f"Optuna TPE Search: {n_trials} trials × {n_jobs} workers")
        log.info(f"Tier: {self.tier} ({len(self.param_keys)} params), "
                 f"Frozen: {len(self._frozen_values)}")
        log.info(f"Scoring: {self.score_model.strategy} "
                 f"(baseline={self.score_model.baseline_score():.4f})")
        log.info(f"{'='*60}")

        # ★ Persistent study: accumulate trials across sessions via joblib
        sampler = TPESampler(seed=42, n_startup_trials=self.n_startup_trials)
        study_path = _cfg.RUN_OUT_DIR / "study.pkl"
        self.study = _load_or_create_study(study_path, sampler)

        # Warm start from ALL historical seed params
        if self.seed_params:
            enqueued = 0
            for sp in self.seed_params:
                trial_params = {k: sp[k] for k in self.param_keys if k in sp}
                if trial_params:
                    self.study.enqueue_trial(trial_params)
                    enqueued += 1
            log.info(f"Warm start: {enqueued} known configs enqueued "
                     f"(study has {len(self.study.trials)} prior trials)")

        # ★ Callback: log best params after every trial (fixes lost params bug)
        def _save_best_callback(study, frozen_trial):
            if frozen_trial.state != optuna.trial.TrialState.COMPLETE:
                return
            if frozen_trial.number == study.best_trial.number:
                log.info(f"  [BEST] trial#{frozen_trial.number} score={frozen_trial.value:.4f} "
                         f"params={{{', '.join(f'{k}={v:.4g}' for k,v in frozen_trial.params.items())}}}")

        t0 = time.time()
        try:
            self.study.optimize(
                self._objective, n_trials=n_trials, n_jobs=n_jobs,
                callbacks=[_save_best_callback],
                show_progress_bar=True,
            )
        except KeyboardInterrupt:
            log.warning("Search interrupted by user")
        elapsed = time.time() - t0

        # Save study for next session
        try:
            import joblib
            study_path = _cfg.RUN_OUT_DIR / "study.pkl"
            joblib.dump(self.study, study_path)
            log.info(f"Study saved: {study_path} ({len(self.study.trials)} trials)")
        except ImportError:
            pass

        log.info(f"\nSearch complete! {elapsed:.0f}s ({elapsed/60:.1f}min)")
        log.info(f"Best score: {self.study.best_value:.4f}")
        log.info(f"Baseline:   {self.score_model.baseline_score():.4f}")

        return self.study

    def run_batch(self, n_trials=10000, batch_size=500, n_workers=None,
                  gpu_prescreen=50000):
        """Two-stage GPU-accelerated optimization.

        Phase 1: GPU batch pre-screening
          - Sobol sample gpu_prescreen params
          - GPU batch generate costmaps
          - Multiprocess parallel A* scoring
          - Pareto rank → seed top 10% into Optuna

        Phase 2: Optuna Ask-and-Tell batch optimization
          - study.ask() for batch_size trials
          - Parallel evaluate entire batch (GPU costmaps + multiprocess A*)
          - study.tell(trial, score)
          - TPE updates → next batch smarter
        """
        import multiprocessing as mp
        if n_workers is None:
            n_workers = min(mp.cpu_count() or 4, 16)

        try:
            import optuna
            from optuna.samplers import TPESampler
        except ImportError:
            log.error("Optuna required: pip install optuna")
            return None

        log.info(f"{'='*60}")
        log.info(f"GPU Batch Optimization: {n_trials} trials")
        log.info(f"Batch size: {batch_size}, Workers: {n_workers}")
        log.info(f"GPU pre-screen: {gpu_prescreen} samples")
        log.info(f"Tier: {self.tier} ({len(self.param_keys)} params)")
        log.info(f"{'='*60}")

        # ── Phase 1: GPU pre-screening ─────────────────
        seed_params = None
        if gpu_prescreen > 0 and hasattr(self.score_model, '_gpu_batch'):
            seed_params = self._gpu_prescreen(gpu_prescreen, n_workers)

        # ── Phase 2: Ask-and-Tell batch optimization ────
        sampler = TPESampler(seed=42, n_startup_trials=min(100, batch_size))
        self.study = optuna.create_study(direction='minimize', sampler=sampler)

        # Seed with GPU pre-screen results
        if seed_params:
            for sp in seed_params[:max(500, batch_size)]:
                trial_params = {k: sp[k] for k in self.param_keys if k in sp}
                if trial_params:
                    self.study.enqueue_trial(trial_params)
            log.info("Enqueued %d GPU seed trials", min(len(seed_params), max(500, batch_size)))

        self.best_score = float('inf')
        self.trial_count = 0
        t0 = time.time()
        batches = (n_trials + batch_size - 1) // batch_size

        for batch_i in range(batches):
            remaining = n_trials - self.trial_count
            current_batch = min(batch_size, remaining)
            if current_batch <= 0:
                break

            # Ask TPE for next batch
            trials_batch = []
            for _ in range(current_batch):
                trial = self.study.ask()
                params = self._suggest_params_from_trial(trial)
                # Store params in trial for tell
                trials_batch.append((trial, params))

            # Parallel evaluate entire batch
            scores = self._evaluate_batch([p for _, p in trials_batch], n_workers)

            # Tell Optuna the results
            for (trial, _), score in zip(trials_batch, scores):
                self.study.tell(trial, score)
                self.trial_count += 1
                if score < self.best_score:
                    self.best_score = score

            # Log progress
            elapsed = time.time() - t0
            rate = self.trial_count / max(elapsed, 0.1)
            log.info("Batch %d/%d: %d trials, best=%.4f, %.1f trial/s, %.0fs elapsed",
                     batch_i + 1, batches, self.trial_count,
                     self.best_score, rate, elapsed)

        elapsed = time.time() - t0
        log.info(f"\nBatch optimization complete! {elapsed:.0f}s ({elapsed/60:.1f}min)")
        log.info(f"Best score: {self.study.best_value:.4f}")
        log.info(f"Rate: {self.trial_count/elapsed:.1f} trials/s")
        return self.study

    def _gpu_prescreen(self, n_samples, n_workers):
        """Phase 1: GPU-accelerated batch pre-screening."""
        from .gpu_search import GPUPreScreener, GPUCostmapBatch
        import multiprocessing as mp

        log.info("Phase 1: GPU pre-screening %d samples...", n_samples)
        t0 = time.time()

        # Generate Sobol samples
        screener = GPUPreScreener(self.score_model, use_gpu=True)
        samples, keys = screener.generate_samples(n_samples, self.param_keys)
        params_list = screener.sample_to_params(samples, keys)

        # GPU batch: generate all unique costmaps in one pass
        try:
            seeder = _GPUPathScorer(self.score_model)
            scores = seeder.score_batch(params_list, n_workers)
        except Exception as e:
            log.warning("GPU pre-screen failed: %s, using CPU", e)
            scores = np.array([self.score_model.compute_score(p) for p in params_list])

        # Pareto rank and select top
        ranks = screener.pareto_rank(scores)
        top_k = max(2000, n_samples // 10)
        front0 = np.where(ranks == 0)[0]
        if len(front0) >= top_k // 2:
            top_idx = np.argsort(scores[front0])[:top_k]
            top_idx = front0[top_idx]
        else:
            top_idx = np.argsort(scores)[:top_k]

        top_params = [params_list[i] for i in top_idx]
        log.info("Phase 1 done: %d → %d seeds (%.1fs, best=%.4f)",
                 n_samples, len(top_params), time.time()-t0, scores[top_idx[0]])
        return top_params

    def _evaluate_batch(self, params_list, n_workers):
        """Evaluate a batch of params in parallel (GPU costmaps + multiprocess A*)."""
        try:
            seeder = _GPUPathScorer(self.score_model)
            return seeder.score_batch(params_list, n_workers)
        except Exception:
            return np.array([self.score_model.compute_score(p) for p in params_list])

    def _suggest_params_from_trial(self, trial):
        """Convert Optuna trial to full param dict (same as _suggest_params)."""
        p = {}
        for key in self.param_keys:
            lo, hi, kind = PARAM_SPACE[key]
            if kind == 'float':
                val = trial.suggest_float(key, lo, hi)
            elif kind == 'int':
                val = trial.suggest_int(key, int(lo), int(hi))
            else:
                val = (lo + hi) / 2
            p[key] = val
        return self._full_params(p)

    def get_top_params(self, n: int = 10) -> List[Tuple[Dict, float]]:
        """Return top N parameter sets and their scores."""
        if self.study is None:
            return []
        trials = sorted(
            [t for t in self.study.trials if t.value is not None],
            key=lambda t: t.value,
        )
        return [(t.params, t.value) for t in trials[:n]]

    def get_param_importance(self) -> Dict[str, float]:
        """Optuna's built-in parameter importance (skip if >5000 trials — fANOVA O(N²))."""
        if self.study is None:
            return {}
        completed = [t for t in self.study.trials if t.state.name == 'COMPLETE' and t.value is not None]
        if len(completed) > 3000:
            log.info("Parameter Importance: skipped (>3000 trials, fANOVA O(N²) too slow)")
            return {}
        try:
            import optuna
            return optuna.importance.get_param_importances(self.study)
        except Exception:
            return {}

    def print_results(self, top_n: int = 15) -> None:
        """Log top N results with formatted diff against DEFAULTS."""
        if self.study is None:
            log.warning("No results to print")
            return

        log.info(f"\n{'='*60}")
        log.info(f"TOP {top_n} Parameter Sets")
        log.info(f"{'='*60}")

        top = self.get_top_params(top_n)
        for i, (params, score) in enumerate(top):
            diffs = []
            for k, v in sorted(params.items()):
                d = DEFAULTS.get(k)
                if d is not None and d != 0 and abs(v - d) / max(abs(d), 0.001) > 0.03:
                    diffs.append(f"{k.split('.')[-1]}={v:.3g}")
            diff_str = ', '.join(diffs[:5])
            log.info(f"  #{i+1:<3} score={score:.4f}  |  {diff_str}")

        # Parameter importance (skip if too slow — fANOVA is O(N²))
        try:
            import optuna
            if len(self.study.trials) <= 3000:
                importances = optuna.importance.get_param_importances(self.study)
                log.info(f"\nParameter Importance (Optuna):")
                log.info("-" * 50)
                for k, v in sorted(importances.items(), key=lambda x: -x[1])[:15]:
                    bar = '█' * max(1, int(v * 50))
                    log.info(f"  {k.split('.')[-1]:<35s} {v:.3f} {bar}")
            else:
                log.info(f"\nParameter Importance: skipped (>5000 trials, too slow)")
        except (KeyboardInterrupt, Exception):
            log.info(f"\nParameter Importance: skipped")

    def print_best_vs_baseline(self) -> None:
        """Print best params vs baseline side by side."""
        if self.study is None:
            return

        best = self.study.best_params
        log.info(f"\n{'='*60}")
        log.info("Best vs Baseline (changes > 3%):")
        log.info(f"{'Parameter':<45s} {'Default':>8s} → {'Best':<8s}")
        log.info("-" * 65)
        changes = 0
        for k in sorted(best.keys()):
            d = DEFAULTS.get(k)
            v = best[k]
            if d is not None and d != 0 and abs(v - d) / max(abs(d), 0.001) > 0.03:
                log.info(f"  {k:<45s} {d:>7.3f} → {v:<7.3f}")
                changes += 1
        if changes == 0:
            log.info("  Current config already optimal! (no changes > 3%)")

    def save_results(self) -> Path:
        """Save best_params JSON + complete trial history + analysis report."""
        if self.study is None:
            log.warning("No results to save")
            return None

        ts = datetime.now().strftime('%Y%m%d_%H%M%S')
        out_dir = _cfg.RUN_OUT_DIR
        out_dir.mkdir(parents=True, exist_ok=True)

        # 1. Best params JSON
        result = {
            'best_score': self.study.best_value,
            'best_params': self.study.best_params,
            'n_trials': len([t for t in self.study.trials if t.state.name == 'COMPLETE']),
            'n_pruned': len([t for t in self.study.trials if t.state.name == 'PRUNED']),
            'baseline_score': self.score_model.baseline_score(),
            'scoring_strategy': self.score_model.strategy,
            'tier': self.tier,
            'frozen': self.freeze_patterns,
            'param_keys': self.param_keys,
            'timestamp': datetime.now().isoformat(),
        }
        json_path = out_dir / f"best_params_{ts}.json"
        with open(json_path, 'w') as f:
            json.dump(result, f, indent=2)
        log.info(f"Best params: {json_path}")

        # 2. Complete trial history CSV (for analysis)
        trials_path = out_dir / f"all_trials_{ts}.csv"
        with open(trials_path, 'w') as f:
            # Header: trial_number, score, param1, param2, ...
            param_names = sorted(self.study.best_params.keys())
            f.write('trial,score,' + ','.join(param_names) + '\n')
            for t in self.study.trials:
                if t.state.name == 'COMPLETE' and t.value is not None:
                    vals = [f"{t.params.get(k, DEFAULTS.get(k, 0)):.5f}" for k in param_names]
                    f.write(f"{t.number},{t.value:.6f}," + ','.join(vals) + '\n')
        log.info(f"Trial history: {trials_path} ({len(self.study.trials)} rows)")

        # 3. Analysis report (markdown)
        report_path = out_dir / f"analysis_report_{ts}.md"
        self._write_analysis_report(report_path)
        log.info(f"Analysis report: {report_path}")

        return json_path

    def _write_analysis_report(self, path: Path) -> None:
        """Generate comprehensive analysis report."""
        completed = [t for t in self.study.trials
                     if t.state.name == 'COMPLETE' and t.value is not None]
        if not completed:
            return

        scores = np.array([t.value for t in completed])
        best = self.study.best_trial

        lines = [
            f"# Auto Tuner Analysis Report",
            f"",
            f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"**Scoring**: {self.score_model.strategy} | **Tier**: {self.tier} | **Params**: {len(self.param_keys)}",
            f"",
            f"## Evolution",
            f"",
            f"| Metric | Value |",
            f"|--------|-------|",
            f"| CSV runs in DB | {self.score_model.db.run_count} |",
            f"| Prior trials (study) | {len(self.study.trials) - len(completed)} |",
            f"| New trials this run | {len(completed)} |",
            f"| Ridge model | {'Trained' if self.score_model._path_model is not None else 'Not trained (need ≥2 unique param sets)'} |",
            f"",
            f"## Summary",
            f"",
            f"| Metric | Value |",
            f"|--------|-------|",
            f"| Trials (completed) | {len(completed)} |",
            f"| Best score | {self.study.best_value:.4f} |",
            f"| Baseline score | {self.score_model.baseline_score():.4f} |",
            f"| Improvement | {(1 - self.study.best_value/self.score_model.baseline_score())*100:.1f}% |",
            f"| Mean score | {np.mean(scores):.4f} |",
            f"| Std score | {np.std(scores):.4f} |",
            f"| Median score | {np.median(scores):.4f} |",
            f"",
            f"## Best Parameters vs Baseline",
            f"",
            f"| Parameter | Default | Best | Change |",
            f"|-----------|---------|------|--------|",
        ]

        for k in sorted(best.params.keys()):
            d = DEFAULTS.get(k)
            v = best.params[k]
            if d is not None and d != 0:
                pct = (v - d) / abs(d) * 100
                if abs(pct) >= 1.0:
                    lines.append(f"| {k} | {d:.4f} | {v:.4f} | {pct:+.1f}% |")

        lines += [
            f"",
            f"## Top 10 Parameters",
            f"",
        ]
        top = self.get_top_params(10)
        for i, (params, score) in enumerate(top):
            diffs = [f"{k.split('.')[-1]}={v:.3g}" for k, v in sorted(params.items())
                     if k in best.params and abs(v - DEFAULTS.get(k, v)) / max(abs(DEFAULTS.get(k, 1)), 0.001) > 0.03]
            lines.append(f"{i+1}. score={score:.4f} — {', '.join(diffs[:4])}")

        lines += [
            f"",
            f"## Parameter Importance (Optuna)",
            f"",
        ]
        try:
            import optuna
            if len(self.study.trials) <= 3000:
                imp = optuna.importance.get_param_importances(self.study)
                for k, v in sorted(imp.items(), key=lambda x: -x[1])[:10]:
                    lines.append(f"- **{k.split('.')[-1]}**: {v:.3f}")
            else:
                lines.append("(skipped — >5000 trials, fANOVA O(N^2))")
        except Exception:
            lines.append("(unavailable)")

        with open(path, 'w') as f:
            f.write('\n'.join(lines) + '\n')


def resolve_tier(tier_arg: Optional[str]) -> str:
    """Map CLI tier argument to internal tier name."""
    if not tier_arg:
        return 'default'
    tier_arg = tier_arg.lower().strip()
    if tier_arg in ('tier1', 't1', '1'):
        return 'tier1'
    if tier_arg in ('full', 'all', '3'):
        return 'full'
    return 'default'


def parse_freeze_arg(freeze_str: Optional[str]) -> List[str]:
    """Parse comma-separated freeze patterns."""
    if not freeze_str:
        return []
    return [p.strip() for p in freeze_str.split(',') if p.strip()]


def _load_or_create_study(study_path, sampler):
    """Load existing study from disk, or create new one.
    Accumulates trials across sessions — evolution of the search space.
    """
    try:
        import joblib
        if study_path.exists():
            study = joblib.load(study_path)
            # Replace sampler with fresh one (old sampler state may be stale)
            study.sampler = sampler
            log.info("Study loaded: %d prior trials from %s",
                     len(study.trials), study_path.name)
            return study
    except (ImportError, Exception) as e:
        log.debug("Study load skipped: %s", e)

    import optuna
    return optuna.create_study(direction='minimize', sampler=sampler)


class _GPUPathScorer:
    """GPU-accelerated batch path scorer.

    Strategy:
      1. Group params by unique (inflation_radius, cost_scaling_factor)
      2. GPU batch generate costmaps for unique combos
      3. Map each param set to its costmap
      4. Multiprocessing Pool: parallel A* across all params
      5. Return scores array
    """

    def __init__(self, score_model):
        self.model = score_model
        # Init GPU batch on the base grid
        if (score_model._map_gen and score_model._map_gen.maps_available):
            base = score_model._map_gen.static_map.copy()
            if score_model._map_gen.keepout_map is not None:
                base[score_model._map_gen.keepout_map == 254] = 254
            from .gpu_search import GPUCostmapBatch
            self.gpu_batch = GPUCostmapBatch(base)
        else:
            self.gpu_batch = None

    def score_batch(self, params_list, n_workers):
        """Score a list of param dicts in parallel. Returns numpy array of scores."""
        n = len(params_list)
        if n == 0:
            return np.array([], dtype=np.float32)

        # Extract unique (inflation, cost_factor) combos
        infls = []
        cfs = []
        for p in params_list:
            ir = p.get('planner.inflation_radius.local',
                       p.get('planner.inflation_radius.global', 0.55))
            cf = p.get('planner.cost_scaling_factor.local',
                       p.get('planner.cost_scaling_factor.global', 3.0))
            infls.append(round(ir, 4))
            cfs.append(round(cf, 4))

        # Deduplicate: build unique costmap for each unique (ir, cf)
        unique_pairs = list(set(zip(infls, cfs)))
        pair_to_idx = {pair: i for i, pair in enumerate(unique_pairs)}

        # GPU batch generate costmaps for all unique pairs
        from .costmap_generator import CostmapData, RESOLUTION
        unique_costmaps = []
        if self.gpu_batch and unique_pairs:
            ir_arr = np.array([p[0] for p in unique_pairs], dtype=np.float32)
            cf_arr = np.array([p[1] for p in unique_pairs], dtype=np.float32)
            grids = self.gpu_batch.generate_batch(ir_arr, cf_arr)
            for i, (ir, cf) in enumerate(unique_pairs):
                unique_costmaps.append(CostmapData(
                    grid=grids[i], width=grids[i].shape[1], height=grids[i].shape[0],
                    resolution=RESOLUTION, origin_x=-2.65, origin_y=-4.5,
                    inflation_radius=ir, cost_scaling_factor=cf,
                ))

        # Map each param set to its pre-computed costmap
        param_costmaps = [unique_costmaps[pair_to_idx[(infls[i], cfs[i])]]
                          for i in range(n)]

        # Score: single A* per param (can parallelize with multiprocessing)
        # Single-threaded for small batches, multiprocess for large ones
        if n <= 50:
            scores = np.array([self._score_one(p, cm)
                              for p, cm in zip(params_list, param_costmaps)],
                              dtype=np.float32)
        else:
            import multiprocessing as mp
            with mp.Pool(min(n_workers, n)) as pool:
                tasks = [(p, cm) for p, cm in zip(params_list, param_costmaps)]
                scores = np.array(pool.starmap(self._score_one, tasks),
                                  dtype=np.float32)

        return scores

    @staticmethod
    def _score_one(params, costmap):
        """Score a single param set with given costmap. (Picklable for mp.Pool)."""
        from .astar_planner import AstarPlanner
        from .costmap_generator import P_POINT, VLM_CCW

        planner = AstarPlanner()
        result = planner.plan(costmap, P_POINT, VLM_CCW)

        if not result.reachable:
            return 999.0

        return (
            0.30 * result.path_len / 10.0 +
            0.20 * result.curvature_mean / 2.0 +
            0.20 * max(0, 0.5 - min(0.5, result.clearance_min)) / 0.5 +
            0.15 * result.cusp_count / 5.0 +
            0.10 * result.in_lethal_count / 10.0 +
            0.05 * result.total_cost / 200.0
        )
