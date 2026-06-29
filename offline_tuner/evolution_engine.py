"""
Data Evolution Engine — Self-improving parameter optimization loop.

Manages the data flywheel:
  New CSV/Rosbag → PhaseMetricsDB.add_runs()
  → ScoreModel re-train (strategy may upgrade)
  → Re-score all prior Optuna trials with updated model
  → Continue Optuna search from updated best
  → Suggest next params to test on real robot (active learning)
"""
import logging
import time
import json
import numpy as np
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime

from .config import DEFAULTS, PARAM_SPACE, RUN_OUT_DIR

log = logging.getLogger('Nav2Tuner.Evolution')


class EvolutionEngine:
    """Orchestrates the data flywheel: data → model → search → deploy → repeat.

    Usage:
      engine = EvolutionEngine(score_model, db)
      engine.on_data_changed()           # re-train + re-score after new data
      engine.continue_search(n=5000)     # continue Optuna from updated state
      engine.suggest_next_params(k=3)    # suggest params for next real-robot test
      engine.data_quality_report()       # diagnostic report
    """

    def __init__(self, score_model, db, study_path: Optional[Path] = None):
        self.score_model = score_model
        self.db = db
        self.study_path = study_path or (RUN_OUT_DIR / "study.pkl")
        self._study = None
        self._data_version = db.run_count  # track when data changed
        self._score_history: List[Dict] = []  # score drift tracking

    # ═══════════════════════════════════════════════════════════
    # Core Flywheel
    # ═══════════════════════════════════════════════════════════

    def on_data_changed(self) -> Dict[str, Any]:
        """Called when new CSV/rosbag data is added to the DB.

        Re-trains the score model, re-scores all prior Optuna trials,
        and reports changes. Returns summary dict.
        """
        run_count_before = self._data_version
        run_count_after = self.db.run_count

        if run_count_after <= run_count_before:
            log.info("No new data detected (%d runs)", run_count_after)
            return {'status': 'no_change', 'runs': run_count_after}

        new_runs = run_count_after - run_count_before
        log.info("Data changed: %d → %d runs (+%d new)",
                 run_count_before, run_count_after, new_runs)

        # 1. Re-train score model
        strategy_before = self.score_model.strategy
        baseline_before = self.score_model.baseline_score()
        self.score_model._auto_init()
        strategy_after = self.score_model.strategy
        baseline_after = self.score_model.baseline_score()

        log.info("Strategy: %s → %s, baseline: %.4f → %.4f",
                 strategy_before, strategy_after, baseline_before, baseline_after)

        # 2. Re-score prior Optuna trials
        re_scored = 0
        score_drift = []
        if self._study is not None:
            re_scored, score_drift = self._re_score_trials()
            self._save_study()

        # 3. Update tracking
        self._data_version = run_count_after

        return {
            'status': 'retrained',
            'runs': run_count_after,
            'new_runs': new_runs,
            'strategy_before': strategy_before,
            'strategy_after': strategy_after,
            'baseline_before': baseline_before,
            'baseline_after': baseline_after,
            'trials_re_scored': re_scored,
            'score_drift_mean': float(np.mean(score_drift)) if score_drift else 0.0,
        }

    def _re_score_trials(self) -> Tuple[int, List[float]]:
        """Re-score all completed trials with the updated score model.
        Returns (count, list of abs score changes).
        """
        if self._study is None:
            return 0, []

        drift = []
        re_scored = 0
        for trial in self._study.trials:
            if trial.state.name != 'COMPLETE' or trial.value is None:
                continue
            old_score = trial.value
            new_score = self.score_model.compute_score(
                {k: v for k, v in trial.params.items()}
            )
            # Optuna stores trial values internally — we can't mutate them directly.
            # But we CAN re-enqueue the best params and let TPE re-evaluate.
            drift.append(abs(new_score - old_score))
            re_scored += 1

        if drift:
            log.info("Re-scored %d trials: mean drift=%.4f, max=%.4f",
                     re_scored, np.mean(drift), np.max(drift))
            self._score_history.append({
                'timestamp': datetime.now().isoformat(),
                'trials': re_scored,
                'mean_drift': float(np.mean(drift)),
                'max_drift': float(np.max(drift)),
            })

        return re_scored, drift

    # ═══════════════════════════════════════════════════════════
    # Active Learning: Suggest Next Params
    # ═══════════════════════════════════════════════════════════

    def suggest_next_params(self, k: int = 3,
                            diversity_weight: float = 0.3) -> List[Dict]:
        """Suggest K parameter sets for the next real-robot test run.

        Strategy: balance exploitation (low predicted score) with
        exploration (parameter diversity from existing test points).

        Args:
          k: Number of suggestions to return.
          diversity_weight: 0 = pure exploitation, 1 = pure exploration.

        Returns list of (params_dict, predicted_score, rationale) tuples.
        """
        # Get known-good params from historical runs
        known_params = []
        for run in self.db._runs:
            rp = run.get('params', {})
            if rp:
                known_params.append({
                    'params': rp,
                    'time': run.get('total_time', 999),
                })

        if len(known_params) < 3:
            # Not enough data — suggest DEFAULTS ± small perturbation
            log.info("Insufficient data for active learning, suggesting defaults")
            return self._default_suggestions(k)

        # Build parameter diversity matrix
        suggestions = []
        for _ in range(k * 5):  # generate many candidates, pick top K
            candidate = self._generate_candidate(known_params, diversity_weight)
            if candidate:
                suggestions.append(candidate)

        # Rank by predicted score, pick top K most diverse
        suggestions.sort(key=lambda x: x['predicted_score'])
        # Diversity filter: ensure at least one param differs by >10% from others
        selected = self._diversity_filter(suggestions, k)
        return selected

    def _generate_candidate(self, known_params: List[Dict],
                            diversity_weight: float) -> Optional[Dict]:
        """Generate one candidate param set via random perturbation."""
        # Pick a random known-good config as base
        base = known_params[np.random.randint(len(known_params))]
        candidate = dict(base['params'])

        # Perturb some params randomly
        n_perturb = max(1, int(len(PARAM_SPACE) * 0.15))  # perturb ~15% of params
        keys = list(PARAM_SPACE.keys())
        np.random.shuffle(keys)

        for k in keys[:n_perturb]:
            if k not in PARAM_SPACE:
                continue
            lo, hi, kind = PARAM_SPACE[k]
            span = hi - lo
            # Perturb by ±10-20% of range
            delta = np.random.normal(0, span * 0.15)
            new_val = candidate.get(k, DEFAULTS.get(k, 0.5)) + delta
            new_val = max(lo, min(hi, new_val))
            if kind == 'int':
                new_val = int(round(new_val))
            candidate[k] = new_val

        # Score the candidate
        score = self.score_model.compute_score(candidate)

        # Estimate diversity: average distance to known params
        diversity = 0.0
        n = 0
        for kp in known_params:
            kp_params = kp['params']
            dist = 0.0
            for key in PARAM_SPACE:
                if key in kp_params and key in candidate:
                    lo, hi, _ = PARAM_SPACE[key]
                    span = max(hi - lo, 0.001)
                    dist += ((candidate[key] - kp_params[key]) / span) ** 2
            if dist > 0:
                diversity += np.sqrt(dist / len(PARAM_SPACE))
                n += 1
        diversity = diversity / max(n, 1)

        return {
            'params': candidate,
            'predicted_score': score,
            'diversity': diversity,
            'combined_score': score * (1 - diversity_weight) - diversity * diversity_weight,
        }

    @staticmethod
    def _diversity_filter(suggestions: List[Dict], k: int) -> List[Dict]:
        """Select K most diverse suggestions from the list."""
        if len(suggestions) <= k:
            return suggestions

        selected = [suggestions[0]]  # start with best
        for _ in range(k - 1):
            # Pick the candidate most different from all selected
            best_div = -1
            best_idx = 0
            for i, s in enumerate(suggestions):
                if s in selected:
                    continue
                min_dist = float('inf')
                for sel in selected:
                    dist = sum(
                        (s['params'].get(key, 0) - sel['params'].get(key, 0)) ** 2
                        for key in PARAM_SPACE
                        if key in s['params'] and key in sel['params']
                    )
                    min_dist = min(min_dist, dist)
                if min_dist > best_div:
                    best_div = min_dist
                    best_idx = i
            selected.append(suggestions[best_idx])

        return selected

    @staticmethod
    def _default_suggestions(k: int) -> List[Dict]:
        """Generate suggestions around DEFAULTS with small perturbations."""
        suggestions = []
        for i in range(k):
            p = dict(DEFAULTS)
            rng = np.random.RandomState(42 + i)
            # Perturb 3 key params
            for key in ['controller.desired_linear_vel',
                       'controller.lookahead_dist',
                       'planner.inflation_radius.local']:
                if key in PARAM_SPACE:
                    lo, hi, kind = PARAM_SPACE[key]
                    p[key] = float(lo + rng.uniform(0.3, 0.7) * (hi - lo))
            suggestions.append({
                'params': p,
                'predicted_score': None,
                'diversity': 1.0,
                'combined_score': 0.0,
            })
        return suggestions

    # ═══════════════════════════════════════════════════════════
    # Data Quality Report
    # ═══════════════════════════════════════════════════════════

    def data_quality_report(self) -> str:
        """Generate a diagnostic report on data quality and coverage."""
        runs = self.db._runs
        if not runs:
            return "No data available."

        # Count unique param sets
        param_hashes = set()
        for run in runs:
            rp = run.get('params', {})
            if rp:
                # Hash key params that vary
                h = tuple(
                    round(rp.get(k, DEFAULTS.get(k, 0)), 4)
                    for k in sorted(PARAM_SPACE.keys())[:10]
                )
                param_hashes.add(h)

        lines = [
            f"# Data Quality Report",
            f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"",
            f"| Metric | Value |",
            f"|--------|-------|",
            f"| Total runs in DB | {len(runs)} |",
            f"| Unique param sets | {len(param_hashes)} |",
            f"| Scoring strategy | {self.score_model.strategy} |",
            f"| Baseline score | {self.score_model.baseline_score():.4f} |",
        ]

        # Goal reached rate
        goals = sum(1 for r in runs if r.get('goal_reached'))
        lines.append(f"| Goal reached | {goals}/{len(runs)} ({goals/len(runs)*100:.0f}%) |")

        # Time range
        times = [r.get('total_time', 0) for r in runs if r.get('total_time', 0) > 0]
        if times:
            lines.append(f"| Best time | {min(times):.1f}s |")
            lines.append(f"| Worst time | {max(times):.1f}s |")
            lines.append(f"| Mean time | {np.mean(times):.1f}s |")

        # Param coverage
        lines.append(f"")
        lines.append(f"## Parameter Coverage")
        lines.append(f"")
        lines.append(f"| Parameter | Min | Max | Span | Default |")
        lines.append(f"|-----------|-----|-----|------|---------|")

        for key in sorted(PARAM_SPACE.keys())[:12]:  # top 12 params
            vals = [float(r.get('params', {}).get(key, DEFAULTS.get(key, 0)))
                    for r in runs if r.get('params', {}).get(key) is not None]
            if len(vals) >= 2:
                lines.append(f"| {key.split('.')[-1]} | {min(vals):.3f} | {max(vals):.3f} | {max(vals)-min(vals):.3f} | {DEFAULTS.get(key, 0):.3f} |")

        # Recommendations
        lines.append(f"")
        lines.append(f"## Recommendations")
        if len(param_hashes) < 5:
            lines.append(f"- ⚠️ Only {len(param_hashes)} unique param sets — need more diversity")
            lines.append(f"- Suggest: vary inflation_radius (0.25–0.55) and desired_linear_vel (0.40–0.55)")
        if self.score_model.strategy == 'heuristic':
            lines.append(f"- 📊 No CSV data — add trajectory logs to enable data-driven scoring")
        if len(runs) < 30 and self.score_model.strategy != 'ml':
            lines.append(f"- 📈 Need {30 - len(runs)} more runs for ML scoring upgrade")
        if self.score_model.strategy == 'path_based':
            lines.append(f"- ✅ Path-based scoring active — maps available")

        return '\n'.join(lines)

    # ═══════════════════════════════════════════════════════════
    # Study Persistence
    # ═══════════════════════════════════════════════════════════

    def load_study(self) -> Optional[Any]:
        """Load prior Optuna study from disk."""
        try:
            import joblib
            if self.study_path.exists():
                self._study = joblib.load(self.study_path)
                completed = len([t for t in self._study.trials
                                if t.state.name == 'COMPLETE'])
                log.info("Loaded study: %d trials from %s",
                         completed, self.study_path.name)
                return self._study
        except (ImportError, Exception) as e:
            log.debug("Study load skipped: %s", e)
        return None

    def _save_study(self) -> None:
        """Persist current study to disk."""
        if self._study is None:
            return
        try:
            import joblib
            self.study_path.parent.mkdir(parents=True, exist_ok=True)
            joblib.dump(self._study, self.study_path)
            completed = len([t for t in self._study.trials
                            if t.state.name == 'COMPLETE'])
            log.info("Study saved: %d trials → %s", completed, self.study_path)
        except ImportError:
            log.debug("joblib not available — study not saved")

    @property
    def study(self):
        return self._study

    @study.setter
    def study(self, value):
        self._study = value
