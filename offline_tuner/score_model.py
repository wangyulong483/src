"""
Data-driven scoring model — the heart of the auto-tuner.

Strategy auto-selection:
  0 CSV                      → Heuristic (expert formula)
  1+ CSV, no map             → Correlation (corr(metric, time) weights)
  1+ CSV + static map        → ★ PathBased (A* on real map → predict time)
  30+ CSV + map              → PathBased + LightGBM (upgraded regressor)

The score function is called 10k-100k times during search — it must be fast.
"""
import logging
import importlib
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Callable
import numpy as np

from .config import DEFAULTS, PARAM_SPACE
from .phase_metrics import PhaseMetricsDB

log = logging.getLogger('Nav2Tuner.Score')

# Feature names for path_based Ridge regression
_PATH_FEATURES = [
    'path_len', 'curvature_mean', 'curvature_std',
    'clearance_min', 'clearance_mean', 'cusp_count',
    'in_lethal_count', 'total_cost',
]


class ScoreModel:
    """Multi-strategy scoring that auto-upgrades based on data volume.

    Usage:
      db = PhaseMetricsDB()
      model = ScoreModel(db)
      score = model.compute_score(params_dict)
      # Add new data → auto re-evaluates strategy
      model.add_data(new_runs)
    """

    def __init__(self, db: PhaseMetricsDB, map_dir: Optional[str] = None):
        self.db = db
        self.strategy: str = 'heuristic'
        self._weights: Optional[Dict[str, float]] = None
        self._ml_model = None
        self._ml_available: Optional[type] = None
        self._trained = False

        # Path-based scoring state
        self._path_model = None      # Ridge: path features → predicted_time
        self._rb_model = None        # Ridge: rosbag features → controller quality
        self._has_rosbag = False     # Whether rosbag data is available
        self._map_gen = None         # CostmapGenerator (lazy init)
        self._planner = None         # AstarPlanner (lazy init)
        self._map_dir = map_dir      # custom map directory (or None for default)
        self._gpu_batch = None       # GPUCostmapBatch (lazy init)

        self._auto_init()

    def _auto_init(self) -> None:
        """Select strategy based on data availability and train."""
        self.strategy = self._select_strategy()
        self._train()
        log.info(f"ScoreModel: strategy={self.strategy}, runs={self.db.run_count}")

    def _select_strategy(self) -> str:
        maps_ok = self._init_maps()
        has_csv = self.db.run_count >= 1

        if maps_ok:
            return 'path_based'  # ★ 有地图就优先用真实路径评估
        elif has_csv and self.db.run_count < 30:
            return 'correlation'
        elif has_csv:
            self._ml_available = _try_import_ml()
            return 'ml' if self._ml_available else 'correlation'
        else:
            return 'heuristic'

    def _init_maps(self) -> bool:
        """Try to load costmap generator. Returns True if maps available."""
        if self._map_gen is not None:
            return self._map_gen.maps_available
        try:
            from .costmap_generator import CostmapGenerator
            self._map_gen = CostmapGenerator()
            if self._map_dir:
                # Override map paths if custom dir provided
                import offline_tuner.costmap_generator as cg
                p = Path(self._map_dir)
                cg.ROOM_PGM = p / 'room.pgm'
                cg.ROOM_YAML = p / 'room.yaml'
                cg.KEEPOUT_PGM = p / 'keepout_mask.pgm'
            self._map_gen.load_maps()
            if self._map_gen.maps_available:
                from .astar_planner import AstarPlanner
                self._planner = AstarPlanner()
                log.info("Path-based scoring available: real map + A* planner")
                return True
        except Exception as e:
            log.debug("Map init skipped: %s", e)
        return False

    def _train(self) -> None:
        """Train the active scoring strategy."""
        if self.strategy == 'heuristic':
            self._trained = True
            return

        if self.strategy == 'path_based':
            self._train_path_model()
            self._trained = True
            return

        if self.strategy == 'correlation':
            correlations = self.db.compute_correlations()
            if not correlations:
                log.warning("No correlations computable, falling back to heuristic")
                self.strategy = 'heuristic'
                self._trained = True
                return
            # Weights = normalized |correlation|
            total = sum(abs(v) for v in correlations.values())
            if total < 1e-9:
                self.strategy = 'heuristic'
                self._trained = True
                return
            self._weights = {k: abs(v) / total for k, v in correlations.items()}
            log.info(f"Correlation weights: {len(self._weights)} features, "
                     f"top: {sorted(self._weights.items(), key=lambda x: -x[1])[:3]}")
            self._trained = True
            return

        if self.strategy == 'ml':
            X, y = self.db.get_feature_matrix()
            if X.shape[0] < 30:
                log.warning("ML requested but insufficient data, falling back to correlation")
                self.strategy = 'correlation'
                self._train()
                return
            try:
                model = self._ml_available()
                model.fit(X, y)
                self._ml_model = model
                log.info(f"ML model trained: {type(model).__name__}, "
                         f"samples={X.shape[0]}, features={X.shape[1]}")
            except Exception as e:
                log.warning(f"ML training failed: {e}, falling back to correlation")
                self.strategy = 'correlation'
                self._train()
                return
            self._trained = True

    def compute_score(self, params: Dict[str, float]) -> float:
        """Score a parameter set. Lower = better. Thread-safe, fast."""
        if self.strategy == 'heuristic':
            return self._score_heuristic(params)
        elif self.strategy == 'path_based':
            return self._score_path_based(params)
        elif self.strategy == 'correlation':
            return self._score_correlation(params)
        elif self.strategy == 'ml':
            return self._score_ml(params)
        return self._score_heuristic(params)

    # ── Path-based scoring (1+ CSVs + map) ─────────────────

    def _train_path_model(self) -> None:
        """Train mixed scoring model:

        1. Path model (A* features → total_time) from per-run params
        2. Controller model (rosbag features + params → controller quality)
           if rosbag data is available
        """
        if self._map_gen is None or self._planner is None:
            self.strategy = 'heuristic'
            return

        X_rows, y_vals, feature_sets = [], [], set()
        trained = 0

        for run in self.db._runs:
            total_time = run.get('total_time', 0)
            if total_time <= 0:
                continue

            run_params = run.get('params')
            if run_params:
                params = dict(DEFAULTS)
                params.update(run_params)
            else:
                params = dict(DEFAULTS)

            try:
                costmap = self._map_gen.generate(params)
                result = self._planner.plan(costmap)
                if result.reachable:
                    feats_tuple = (
                        round(result.path_len, 2),
                        round(result.curvature_mean, 3),
                        round(result.clearance_min, 2),
                        result.cusp_count,
                        result.in_lethal_count,
                        round(result.total_cost, 0),
                    )
                    X_rows.append([
                        result.path_len, result.curvature_mean, result.curvature_std,
                        result.clearance_min if result.clearance_min < 999 else 0.5,
                        result.clearance_mean, result.cusp_count,
                        result.in_lethal_count, result.total_cost,
                    ])
                    y_vals.append(total_time)
                    feature_sets.add(feats_tuple)
                    trained += 1
            except Exception as e:
                log.debug("Path training skip: %s", e)

        # Train controller model from rosbag features if available
        rb_data = self.db.get_rosbag_features()
        self._has_rosbag = len(rb_data['X']) >= 2
        self._rb_model = None

        if self._has_rosbag:
            try:
                from sklearn.linear_model import Ridge as _Ridge
                self._rb_model = _Ridge(alpha=1.0)
            except ImportError:
                self._rb_model = _NumpyRidge(alpha=1.0)
            self._rb_model.fit(rb_data['X'], rb_data['y'])
            preds = self._rb_model.predict(rb_data['X'])
            mae = np.mean(np.abs(preds - rb_data['y']))
            log.info("Rosbag controller model: %d runs, MAE=%.1fs",
                     len(rb_data['y']), mae)

        if trained < 2:
            log.warning("path_based: need >=2 trainable runs, using raw features")
            self._path_model = None
            return

        if len(feature_sets) < 2:
            log.info("Path model: all %d runs share same params — using raw path-feature scoring", trained)
            self._path_model = None
            return

        X = np.array(X_rows, dtype=np.float64)
        y = np.array(y_vals, dtype=np.float64)

        try:
            from sklearn.linear_model import Ridge
            self._path_model = Ridge(alpha=1.0)
        except ImportError:
            self._path_model = _NumpyRidge(alpha=1.0)

        self._path_model.fit(X, y)
        preds = self._path_model.predict(X)
        mae = np.mean(np.abs(preds - y))
        log.info("Path model trained: %d runs, MAE=%.1fs, coefs=%s",
                 trained, mae,
                 [f"{c:+.2f}" for c in self._path_model.coef_[:4]])

    def _score_path_based(self, params: Dict[str, float]) -> float:
        """Mixed scoring: path geometry + CSV correlation + controller quality.

        - A* on costmap (with random obstacles) → path_score
        - CSV correlation weights → csv_score (learned from historical data)
        - Rosbag controller model → ctrl_score
        - Blended: 0.4*path + 0.4*csv + 0.2*ctrl (or 0.5*path + 0.5*csv without rosbag)
        """
        if self._map_gen is None or self._planner is None:
            return self._score_heuristic(params)

        try:
            from .costmap_generator import VLM_CCW, VLM_CW, P_POINT

            # Use pre-computed GPU costmap if available (from prescreen batch)
            gpu_cm = params.pop('_gpu_costmap', None) if isinstance(params, dict) else None
            if gpu_cm is not None and isinstance(gpu_cm, np.ndarray):
                from .costmap_generator import CostmapData, ORIGIN_X, ORIGIN_Y
                costmap = CostmapData(
                    grid=gpu_cm, width=gpu_cm.shape[1], height=gpu_cm.shape[0],
                    resolution=0.05, origin_x=ORIGIN_X, origin_y=ORIGIN_Y,
                    inflation_radius=float(params.get('planner.inflation_radius.local', 0.55)),
                    cost_scaling_factor=float(params.get('planner.cost_scaling_factor.local', 3.0)),
                )
            elif gpu_cm is not None:
                costmap = gpu_cm  # already CostmapData
            else:
                costmap = self._generate_costmap_gpu(params)

            # Plan P→VLM both directions (single segment, always reachable)
            scores = []
            for goal in (VLM_CCW, VLM_CW):
                result = self._planner.plan(costmap, start_world=P_POINT, goal_world=goal)
                if not result.reachable:
                    scores.append(999.0)
                    continue

                if self._path_model is not None:
                    path_feats = np.array([[
                        result.path_len, result.curvature_mean, result.curvature_std,
                        result.clearance_min if result.clearance_min < 999 else 0.5,
                        result.clearance_mean, result.cusp_count,
                        result.in_lethal_count, result.total_cost,
                    ]], dtype=np.float64)
                    path_score = float(self._path_model.predict(path_feats)[0]) / 200.0
                else:
                    path_score = (
                        -0.10 * result.path_len / 7.0 +
                         0.15 * result.curvature_mean / 2.0 +
                         0.30 * max(0, 1.0 - result.clearance_min / 0.5) +
                         0.25 * result.cusp_count / 5.0 +
                         0.20 * result.in_lethal_count / 5.0 +
                         0.20 * result.total_cost / 200.0)
                scores.append(path_score)

            path_score = sum(scores) / len(scores) if scores else 999.0
            # Use CW result for controller features (it's representative)
            result = self._planner.plan(costmap, start_world=P_POINT, goal_world=VLM_CW)

            # ── CSV correlation score ──
            csv_score = self._score_csv_correlation(params)

            # ── Controller quality (rosbag model) ──
            ctrl_score = 0.0
            if self._has_rosbag and self._rb_model is not None:
                try:
                    rb_feats = self._extract_controller_features(params, result)
                    if rb_feats and len(rb_feats) > 0:
                        rb_arr = np.array([rb_feats], dtype=np.float64)
                        if rb_arr.shape[1] == self._rb_model.n_features_in_ if hasattr(self._rb_model, 'n_features_in_') else True:
                            ctrl_pred = float(self._rb_model.predict(rb_arr)[0])
                            ctrl_score = ctrl_pred / 200.0
                except Exception as e:
                    log.debug("Controller scoring failed: %s", e)

            # ── RPP simulation score (evolves with data; skipped in prescreen) ──
            if params.get('_skip_rpp'):
                rpp_score = 0.0  # prescreen — too expensive per sample
            else:
                rpp_score = self._score_rpp_simulation(costmap, params, result)

            # ── Blend: path + csv + controller + RPP ──
            n_runs = self.db.run_count
            w_rpp = self._rpp_weight(n_runs)
            w_path, w_csv, w_ctrl = self._blend_weights(n_runs, w_rpp)

            if self._path_model is not None:
                blended = w_path * path_score + w_csv * csv_score + w_ctrl * ctrl_score + w_rpp * rpp_score
            elif self._has_rosbag and self._rb_model is not None:
                blended = w_path * path_score + w_csv * csv_score + w_ctrl * ctrl_score + w_rpp * rpp_score
            else:
                keepout_penalty = 0.0
                if hasattr(result, 'keepout_cost') and result.keepout_cost:
                    keepout_penalty = 0.15 * result.keepout_cost / max(result.keepout_cost, 1.0)
                blended = w_path * path_score + w_csv * csv_score + w_rpp * rpp_score + keepout_penalty

            return blended

        except Exception as e:
            log.debug("Path scoring failed: %s, fallback to heuristic", e)
            return self._score_heuristic(params)

    def _score_csv_correlation(self, params: Dict[str, float]) -> float:
        """Score from historical CSV data — nearest-neighbor to known runs.

        For each historical run with known params + actual time:
          compute distance(params, run_params)
          weight = 1 / (distance + epsilon)
          score = weighted average of actual times / 200
        """
        runs_with_params = [r for r in self.db._runs
                           if r.get('params') and r.get('total_time', 0) > 0]
        if len(runs_with_params) < 2:
            return 0.3  # neutral

        total_weight = 0.0
        weighted_time = 0.0

        for run in runs_with_params:
            rp = run['params']
            # Euclidean distance in param space (normalized by param range)
            dist = 0.0
            n_keys = 0
            for k in PARAM_SPACE:
                if k in rp and k in params:
                    pv = float(params[k])
                    rv = float(rp[k])
                    lo, hi, _ = PARAM_SPACE[k]
                    span = max(hi - lo, 0.001)
                    # Normalize to [0, 1] range then compute squared difference
                    pv_norm = (pv - lo) / span
                    rv_norm = (rv - lo) / span
                    dist += (pv_norm - rv_norm) ** 2
                    n_keys += 1
            if n_keys > 0:
                dist = (dist / n_keys) ** 0.5
                w = 1.0 / (dist + 0.05)  # inverse distance weight
                weighted_time += w * run['total_time']
                total_weight += w

        if total_weight > 0:
            return (weighted_time / total_weight) / 200.0  # normalize to score scale

        return 0.3

    # ── Heuristic scoring (0 CSVs) ──────────────────────────

    # ═══════════════════════════════════════════════════════════════
    # RPP Simulator Scoring
    # ═══════════════════════════════════════════════════════════════

    def _score_rpp_simulation(self, costmap, params, result=None) -> float:
        """Run RPP simulator on the A* path and return normalized score.

        Args:
            costmap: CostmapData from path planning.
            params: Controller parameter dict.
            result: PathResult from A* plan (must be reachable with path pixels).
        """
        try:
            from .rpp_simulator import RPPSimulator

            if result is None or not result.reachable or not result.path:
                return 0.5  # neutral score if no path

            sim = RPPSimulator(costmap.grid, result.path, resolution=0.05)
            metrics = sim.run(params)
            return metrics.composite_score()
        except Exception as e:
            log.debug("RPP simulation failed: %s", e)
            return 0.5  # neutral

    @staticmethod
    def _rpp_weight(n_runs: int) -> float:
        """Evolving RPP weight: grows with real-world data.

        Evolution path:
          0-5 runs:   w_rpp=0.00 (not enough data to trust simulation)
          6-10:       w_rpp=0.05
          11-15:      w_rpp=0.10
          16-20:      w_rpp=0.15
          21-30:      w_rpp=0.20
          31+:        w_rpp=0.25
        """
        if n_runs <= 5:
            return 0.00
        elif n_runs <= 10:
            return 0.05
        elif n_runs <= 15:
            return 0.10
        elif n_runs <= 20:
            return 0.15
        elif n_runs <= 30:
            return 0.20
        else:
            return 0.25

    @staticmethod
    def _blend_weights(n_runs: int, w_rpp: float) -> tuple:
        """Compute blend weights that sum to 1.0, subtracting RPP's share proportionally."""
        if n_runs <= 5:
            # No RPP: original 0.40/0.40/0.20 split
            return (0.40, 0.40, 0.20)
        elif n_runs <= 10:
            # RPP 5%: path/csv/ctrl each reduced proportionally
            w_path, w_csv, w_ctrl = 0.38, 0.38, 0.19
        elif n_runs <= 15:
            w_path, w_csv, w_ctrl = 0.36, 0.36, 0.18
        elif n_runs <= 20:
            w_path, w_csv, w_ctrl = 0.34, 0.34, 0.17
        elif n_runs <= 30:
            w_path, w_csv, w_ctrl = 0.32, 0.32, 0.16
        else:
            w_path, w_csv, w_ctrl = 0.30, 0.30, 0.15

        return (w_path, w_csv, w_ctrl)

    @staticmethod
    def _score_heuristic(p: Dict[str, float]) -> float:
        """Preserved from original _analyze_plans.py compute_score().
        Expert-crafted heuristic for the 5m×5m Ackermann competition scenario.
        """
        s = 0.0

        # ── Efficiency (weight 0.35) ──
        v = p['controller.desired_linear_vel']
        s += 0.15 * abs(v - 0.50) / 0.20  # anchor: verified 70.1s gold (was 0.48)

        la = p['controller.lookahead_dist']
        s += 0.10 * abs(la - 0.65) / 0.15

        mi = p['planner.max_iterations']
        s += 0.05 * abs(mi - 1500) / 800  # anchor: 1500 (gold baseline, was 1200)

        mt = p['planner.max_planning_time']
        s += 0.05 * abs(mt - 1.5) / 1.0

        # ── Smoothness (weight 0.30) ──
        cp_val = p['planner.change_penalty']
        s += 0.10 * (1.0 if cp_val < 0.05 else abs(cp_val - 0.10) / 0.10)

        nsp = p['planner.non_straight_penalty']
        s += 0.08 * abs(nsp - 1.3) / 0.5

        aer = p['planner.analytic_expansion_ratio']
        s += 0.08 * abs(aer - 3.0) / 1.5

        mav = p['controller.max_angular_vel']
        s += 0.04 * abs(mav - 2.0) / 1.0

        # ── Safety (weight 0.25) ──
        csg = p['controller.cost_scaling_gain']
        s += 0.12 * abs(csg - 1.0) / 1.5

        # Inflation anchor: 0.55m verified best (LRN-20260615-001). 0.25m is "uncanny valley".
        ir_l = p['planner.inflation_radius.local']
        ir_g = p['planner.inflation_radius.global']
        s += 0.08 * (abs(ir_l - 0.55) + abs(ir_g - 0.55)) / 0.50

        csf_l = p['planner.cost_scaling_factor.local']
        csf_g = p['planner.cost_scaling_factor.global']
        s += 0.05 * (abs(csf_l - 3.0) + abs(csf_g - 3.0)) / 3.0  # anchor: 3.0 (gold baseline, was 2.5)

        # ── Consistency (weight 0.10) ──
        rp = p['planner.reverse_penalty']
        s += 0.05 * abs(rp - 2.0) / 2.0

        gt = p['controller.xy_goal_tolerance']
        s += 0.03 * abs(gt - 0.35) / 0.15

        aqb = p['planner.angle_quantization_bins']
        s += 0.02 * abs(aqb - 48) / 16

        return s

    # ── Correlation scoring (1-29 CSVs) ─────────────────────

    def _score_correlation(self, params: Dict[str, float]) -> float:
        """Score = sum(wi * normalized_metric_i(params)).
        wi = |corr(metric_i, total_time)| / sum(|corr_j|).

        Since we can't actually run the robot, we estimate metrics
        from params using physics-based approximations + historical regression.
        """
        features = self._param_to_features(params)
        if self._weights is None:
            return self._score_heuristic(params)

        score = 0.0
        for fname, fval in features.items():
            w = self._weights.get(fname, 0.0)
            if w > 0:
                # Normalize feature: higher is worse, center around 0
                score += w * abs(fval)
        return score

    # ── ML scoring (30+ CSVs) ───────────────────────────────

    def _score_ml(self, params: Dict[str, float]) -> float:
        """Predict total_time using trained ML model.
        Falls back to correlation if model unavailable.
        """
        if self._ml_model is None:
            return self._score_correlation(params)

        features = self._param_to_features_flat(params)
        try:
            pred = self._ml_model.predict([features])[0]
            return float(pred) / 100.0  # normalize to score scale
        except Exception as e:
            log.debug(f"ML predict failed: {e}")
            return self._score_correlation(params)

    # ── Parameter → Feature mapping ─────────────────────────

    def _param_to_features(self, params: Dict[str, float]) -> Dict[str, float]:
        """Map parameter dict to expected metric values.

        Uses physics-based approximations. As CSVs accumulate,
        could be replaced by learned linear regression models.
        """
        p = params
        d = DEFAULTS

        # Speed-related
        v_ratio = p['controller.desired_linear_vel'] / d['controller.desired_linear_vel']
        max_v_ratio = p['controller.max_linear_vel'] / d['controller.max_linear_vel']

        features = {}

        # avg_speed: proportional to desired velocity
        features['avg_speed'] = v_ratio - 1.0

        # dir_switches: affected by change_penalty and lookahead
        cp = p['planner.change_penalty']
        features['dir_switches'] = (0.10 - cp) / 0.10  # lower penalty → more switches

        # smoothness: composite
        la_ratio = p['controller.lookahead_dist'] / d['controller.lookahead_dist']
        features['smoothness'] = (
            0.4 * abs(la_ratio - 1.0) +
            0.3 * abs(v_ratio - 1.0) +
            0.3 * abs(cp - 0.10) / 0.10
        )

        # planner_frequency: affected by max_iterations and planning_time
        mi_ratio = d['planner.max_iterations'] / max(p['planner.max_iterations'], 100)
        mt_ratio = d['planner.max_planning_time'] / max(p['planner.max_planning_time'], 0.1)
        features['planner_frequency'] = (mi_ratio - 1.0) * 0.5 + (mt_ratio - 1.0) * 0.5

        # cpu_avg: affected by max_iterations, angle bins
        aqb_ratio = p['planner.angle_quantization_bins'] / d['planner.angle_quantization_bins']
        features['cpu_avg'] = (mi_ratio - 1.0) * 0.6 + (aqb_ratio - 1.0) * 0.4

        # Phase-specific elapsed estimates
        # CRUISE: driven by avg_speed
        features['CRUISE_CHANNEL.elapsed'] = -0.3 * (v_ratio - 1.0)
        # RETURN_P: driven by inflation (safety margin) and speed
        ir_ratio = p['planner.inflation_radius.local'] / d['planner.inflation_radius.local']
        features['RETURN_P.elapsed'] = 0.3 * (ir_ratio - 1.0) - 0.2 * (v_ratio - 1.0)

        # path_len: affected by inflation (wider = longer path around obstacles)
        features['total_path_len'] = 0.1 * (ir_ratio - 1.0)

        # replans: affected by planning speed and change_penalty
        features['total_replans'] = (
            -0.3 * (mi_ratio - 1.0) +
            0.2 * abs(cp - 0.10) / 0.10
        )

        return features

    def _generate_costmap_gpu(self, params):
        """Generate costmap — GPU-accelerated if CuPy available.

        First call: pre-computes distance transform, uploads to GPU.
        Subsequent calls: GPU element-wise inflation (~0.1ms vs 3ms CPU).
        """
        if self._map_gen is None:
            return None

        # Resolve params
        infl_r = params.get('planner.inflation_radius.local')
        if infl_r is None:
            infl_r = params.get('planner.inflation_radius.global', 0.55)
        csf = params.get('planner.cost_scaling_factor.local')
        if csf is None:
            csf = params.get('planner.cost_scaling_factor.global', 3.0)

        # Init GPU batch on first call (no keepout — competition disables it during cruise)
        if self._gpu_batch is None:
            try:
                base_grid = self._map_gen.static_map.copy()
                # NOTE: keepout NOT applied — tuner evaluates path quality through
                # the static environment. Actual competition disables keepout during
                # cruise/return phases, so evaluating with keepout is unrealistic.
                from .gpu_search import GPUCostmapBatch
                self._gpu_batch = GPUCostmapBatch(base_grid)
                log.info("GPU costmap batch initialized (%s, keepout excluded)",
                         self._gpu_batch._gpu_backend)
            except Exception as e:
                log.debug("GPU batch init failed: %s, using CPU", e)
                self._gpu_batch = False  # mark as failed

        # CPU costmap with obstacle injection (GPU batch only helps with prescreen)
        return self._map_gen.generate_with_obstacles(params)

    def _param_to_features_flat(self, params: Dict[str, float]) -> List[float]:
        """Flat feature list for ML model input. Must match training order."""
        p = params
        d = DEFAULTS
        feats = []

        # Speed
        feats.append(p['controller.desired_linear_vel'] / d['controller.desired_linear_vel'] - 1.0)
        feats.append(p['controller.max_linear_vel'] / d['controller.max_linear_vel'] - 1.0)
        # Lookahead
        feats.append(p['controller.lookahead_dist'] / d['controller.lookahead_dist'] - 1.0)
        feats.append(p['controller.min_lookahead_dist'] / d['controller.min_lookahead_dist'] - 1.0)
        feats.append(p['controller.max_lookahead_dist'] / d['controller.max_lookahead_dist'] - 1.0)
        # Planner
        feats.append(p['planner.max_iterations'] / max(d['planner.max_iterations'], 100) - 1.0)
        feats.append(p['planner.max_planning_time'] / max(d['planner.max_planning_time'], 0.1) - 1.0)
        feats.append(p['planner.angle_quantization_bins'] / d['planner.angle_quantization_bins'] - 1.0)
        feats.append(p['planner.change_penalty'] - 0.10)
        feats.append(p['planner.reverse_penalty'] / d['planner.reverse_penalty'] - 1.0)
        # Inflation
        feats.append(p['planner.inflation_radius.local'] / d['planner.inflation_radius.local'] - 1.0)
        feats.append(p['planner.inflation_radius.global'] / d['planner.inflation_radius.global'] - 1.0)
        feats.append(p['planner.cost_scaling_factor.local'] / d['planner.cost_scaling_factor.local'] - 1.0)
        # Cost
        feats.append(p['controller.cost_scaling_gain'] / d['controller.cost_scaling_gain'] - 1.0)
        feats.append(p['controller.cost_scaling_dist'] / d['controller.cost_scaling_dist'] - 1.0)
        # Approach
        feats.append(p['controller.xy_goal_tolerance'] / d['controller.xy_goal_tolerance'] - 1.0)
        feats.append(p['controller.min_approach_linear_vel'] / d['controller.min_approach_linear_vel'] - 1.0)

        return feats

    @staticmethod
    def _extract_controller_features(params: Dict[str, float],
                                     path_result) -> Optional[List[float]]:
        """Extract controller-quality features for rosbag Ridge model.

        Combines path geometry results with controller params to predict
        how well RPP will track this path.
        """
        if path_result is None or not path_result.reachable:
            return None
        return [
            params.get('controller.desired_linear_vel', 0.50) / 0.50,
            params.get('controller.lookahead_dist', 0.65) / 0.65,
            params.get('controller.max_angular_vel', 2.0) / 2.0,
            path_result.curvature_mean,
            path_result.curvature_std,
            path_result.cusp_count / 5.0,
            path_result.clearance_min if path_result.clearance_min < 999 else 0.5,
            getattr(path_result, 'keepout_incursion_count', 0) / 5.0,
        ]

    # ── Public helpers ──────────────────────────────────────

    def add_data(self, new_runs: List) -> None:
        """Add new runs, re-evaluate strategy, re-train."""
        self.db.add_runs(new_runs)
        self._auto_init()

    def get_feature_importance(self) -> Dict[str, float]:
        """Return feature importance dict for visualization.
        For heuristic: hardcoded. For correlation: weights. For ML: model-based.
        """
        if self.strategy == 'correlation' and self._weights:
            return dict(self._weights)
        if self.strategy == 'ml' and self._ml_model is not None:
            if hasattr(self._ml_model, 'feature_importances_'):
                return {f"feat_{i}": float(v) for i, v in
                        enumerate(self._ml_model.feature_importances_)}
        # Heuristic fallback: return approximate importance
        return {
            'desired_linear_vel': 0.15,
            'cost_scaling_gain': 0.12,
            'lookahead_dist': 0.10,
            'change_penalty': 0.10,
            'inflation_radius': 0.08,
            'non_straight_penalty': 0.08,
            'analytic_expansion_ratio': 0.08,
        }

    def baseline_score(self) -> float:
        """Score of current DEFAULTS config."""
        return self.compute_score(DEFAULTS)

    def __repr__(self) -> str:
        return (f"ScoreModel(strategy={self.strategy}, runs={self.db.run_count}, "
                f"baseline={self.baseline_score():.4f})")


# ── ML import helpers ───────────────────────────────────────

def _try_import_ml() -> Optional[type]:
    """Try importing ML regressors in order of preference.
    Returns the best available regressor class or None.
    """
    candidates = [
        ('lightgbm', 'LGBMRegressor'),
        ('xgboost', 'XGBRegressor'),
        ('sklearn.ensemble', 'RandomForestRegressor'),
    ]
    for mod_name, cls_name in candidates:
        try:
            mod = importlib.import_module(mod_name)
            cls = getattr(mod, cls_name)
            log.info(f"ML backend: {mod_name}.{cls_name}")
            return cls
        except ImportError:
            continue
    return None


def _try_import_gpu():
    """Try importing GPU backends. Returns (module, backend_name) or (None, 'cpu')."""
    for name, mod_name in [
        ('cupy', 'cupy'),
        ('numba.cuda', 'numba.cuda'),
        ('torch', 'torch'),
    ]:
        try:
            mod = importlib.import_module(mod_name)
            return mod, name
        except ImportError:
            continue
    return None, 'cpu'


class _NumpyRidge:
    """Minimal Ridge regression using numpy.linalg.lstsq with L2 penalty.
    Used when sklearn is unavailable."""

    def __init__(self, alpha: float = 1.0):
        self.alpha = alpha
        self.coef_: np.ndarray = np.array([])
        self.intercept_: float = 0.0

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        n, d = X.shape
        # Add intercept column
        X_aug = np.column_stack([X, np.ones(n)])
        # Ridge: (X^T X + αI)^{-1} X^T y
        I = np.eye(d + 1)
        I[-1, -1] = 0  # don't regularize intercept
        try:
            theta = np.linalg.solve(X_aug.T @ X_aug + self.alpha * I, X_aug.T @ y)
            self.coef_ = theta[:d]
            self.intercept_ = theta[d]
        except np.linalg.LinAlgError:
            theta, _, _, _ = np.linalg.lstsq(X_aug, y, rcond=None)
            self.coef_ = theta[:d]
            self.intercept_ = theta[d] if len(theta) > d else 0.0

    def predict(self, X: np.ndarray) -> np.ndarray:
        return X @ self.coef_ + self.intercept_
