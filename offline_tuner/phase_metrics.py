"""
Multi-run aggregation and metrics database management.

Builds and maintains metrics_database.json — the central repository
of historical run data that drives the scoring model.
"""
import json
import logging
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional, Tuple
import numpy as np

from .feature_extractor import RunMetrics, PhaseMetrics
from .config import OUT_DIR, KNOWN_PHASES, TRACKED_METRICS

log = logging.getLogger('Nav2Tuner.PhaseMetrics')


@dataclass
class PhaseStats:
    """Aggregated statistics for one phase across all runs."""
    phase_name: str = ""
    count: int = 0
    mean_time: float = 0.0
    best_time: float = float('inf')
    worst_time: float = 0.0
    std_time: float = 0.0
    mean_dir_switches: float = 0.0
    mean_replans: float = 0.0
    mean_cpu: float = 0.0
    mean_smoothness: float = 0.0
    mean_path_len: float = 0.0
    mean_planner_hz: float = 0.0
    mean_avg_speed: float = 0.0


class PhaseMetricsDB:
    """Manages the persistent metrics_database.json.

    Lifecycle:
      1. Load existing DB (or create empty template)
      2. Add new runs to it
      3. Recompute aggregated statistics
      4. Save to disk

    The DB is the data backbone — score_model reads from it to
    decide which scoring strategy to use.
    """

    def __init__(self, db_path: Optional[Path] = None):
        self.db_path = Path(db_path) if db_path else OUT_DIR / "metrics_database.json"
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.data: Dict = self._load_or_create()
        self._runs: List[Dict] = self.data.get('runs', [])

    def _load_or_create(self) -> Dict:
        """Load existing DB or create empty template."""
        if self.db_path.exists():
            try:
                with open(self.db_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                log.info(f"Loaded database: {data.get('run_count', 0)} runs")
                return data
            except (json.JSONDecodeError, KeyError) as e:
                log.warning(f"Corrupt database, creating new: {e}")
        return self._empty_template()

    @staticmethod
    def _empty_template() -> Dict:
        return {
            'version': 2,
            'updated': None,
            'run_count': 0,
            'phase_statistics': {},
            'feature_correlations': {},
            'runs': [],
        }

    @property
    def run_count(self) -> int:
        return len(self._runs)

    def add_runs(self, runs: List[RunMetrics]) -> int:
        """Add new runs, recompute aggregates, save to disk.
        Returns new run_count.
        """
        added = 0
        # Build dedup index: canonical path + content hash
        existing_canonical = {
            str(Path(r.get('source', '')).resolve()): r
            for r in self._runs
        }
        existing_hashes = {self._run_hash(r) for r in self._runs}

        for rm in runs:
            # Dedup by canonical source path
            canonical = str(Path(rm.source).resolve())
            if canonical in existing_canonical:
                log.debug(f"Skipping duplicate path: {rm.source}")
                continue

            run_dict = {
                'source': rm.source,
                'timestamp': rm.timestamp,
                'total_time': rm.total_time,
                'total_path_len': rm.total_path_len,
                'total_dir_switches': rm.total_dir_switches,
                'total_replans': rm.total_replans,
                'cpu_avg_overall': rm.cpu_avg_overall,
                'goal_reached': rm.goal_reached,
                'planner_hz_overall': rm.planner_hz_overall,
                'n_total_points': rm.n_total_points,
                'phases': {k: v.to_dict() for k, v in rm.phases.items()},
                'params': rm.nav2_config,  # ★ Nav2 YAML snapshot
            }

            # Content dedup: skip if an identical run already exists
            rh = self._run_hash(run_dict)
            if rh in existing_hashes:
                log.debug(f"Skipping content duplicate: {rm.source} (matches existing run)")
                continue

            existing_canonical[canonical] = run_dict
            existing_hashes.add(rh)
            self._runs.append(run_dict)
            added += 1

        if added > 0:
            self._recompute()
            self.save()
            log.info(f"Added {added} runs → {self.run_count} total, "
                     f"correlations: {len(self.data['feature_correlations'])} features")
        return added

    def _recompute(self) -> None:
        """Recompute phase statistics and feature correlations."""
        self.data['run_count'] = self.run_count
        self.data['phase_statistics'] = self._compute_phase_stats()
        if self.run_count >= 2:
            self.data['feature_correlations'] = self.compute_correlations()
        self.data['updated'] = self._now_iso()

    def _compute_phase_stats(self) -> Dict[str, Dict]:
        """Aggregate per-phase statistics across all runs."""
        stats: Dict[str, Dict] = {}
        for phase_name in KNOWN_PHASES:
            times, dirs, replans, cpus, smooths, paths, hzs, speeds = (
                [], [], [], [], [], [], [], []
            )
            for run in self._runs:
                ph = run.get('phases', {}).get(phase_name)
                if ph:
                    times.append(ph.get('elapsed', 0))
                    dirs.append(ph.get('dir_switches', 0))
                    replans.append(ph.get('plan_changes', 0))
                    cpus.append(ph.get('cpu_avg', 0))
                    smooths.append(ph.get('smoothness', 0))
                    paths.append(ph.get('path_len', 0))
                    hzs.append(ph.get('planner_frequency', 0))
                    speeds.append(ph.get('avg_speed', 0))

            if times:
                arr_t = np.array(times, dtype=np.float64)
                stats[phase_name] = {
                    'count': len(times),
                    'mean_time': float(np.mean(arr_t)),
                    'best_time': float(np.min(arr_t)),
                    'worst_time': float(np.max(arr_t)),
                    'std_time': float(np.std(arr_t)),
                    'mean_dir_switches': float(np.mean(dirs)),
                    'mean_replans': float(np.mean(replans)),
                    'mean_cpu': float(np.mean(cpus)),
                    'mean_smoothness': float(np.mean(smooths)),
                    'mean_path_len': float(np.mean(paths)),
                    'mean_planner_hz': float(np.mean(hzs)),
                    'mean_avg_speed': float(np.mean(speeds)),
                }
        return stats

    def compute_correlations(self) -> Dict[str, float]:
        """Compute corr(metric, total_time) across all runs.

        Returns dict like {'dir_switches': 0.87, 'jerk': 0.81, ...}.
        Absolute values are used for scoring weights.
        """
        if self.run_count < 2:
            return {}

        # Collect feature vectors
        total_times = np.array([r['total_time'] for r in self._runs],
                               dtype=np.float64)

        correlations = {}

        # Per-run features
        features_simple = {
            'total_path_len': [r.get('total_path_len', 0) for r in self._runs],
            'total_dir_switches': [r.get('total_dir_switches', 0) for r in self._runs],
            'total_replans': [r.get('total_replans', 0) for r in self._runs],
            'cpu_avg_overall': [r.get('cpu_avg_overall', 0) for r in self._runs],
            'planner_hz_overall': [r.get('planner_hz_overall', 0) for r in self._runs],
        }
        for name, vals in features_simple.items():
            arr = np.array(vals, dtype=np.float64)
            if np.std(arr) > 1e-9:
                corr = np.corrcoef(arr, total_times)[0, 1]
                if not np.isnan(corr):
                    correlations[name] = float(corr)

        # Per-phase features: only use runs that actually contributed the phase
        for phase_name in KNOWN_PHASES:
            for metric in ['elapsed', 'dir_switches', 'plan_changes', 'smoothness',
                           'avg_speed', 'planner_frequency']:
                vals = []
                matched_times = []
                for run in self._runs:
                    ph = run.get('phases', {}).get(phase_name)
                    if ph:
                        vals.append(ph.get(metric, 0))
                        matched_times.append(run.get('total_time', 0))
                if len(vals) >= 2:
                    arr = np.array(vals, dtype=np.float64)
                    times_arr = np.array(matched_times, dtype=np.float64)
                    if np.std(arr) > 1e-9 and np.std(times_arr) > 1e-9:
                        corr = np.corrcoef(arr, times_arr)[0, 1]
                        if not np.isnan(corr):
                            key = f"{phase_name}.{metric}"
                            correlations[key] = float(corr)

        return correlations

    def attach_rosbag_metrics(self, bag_path: str, metrics) -> None:
        """Match a rosbag to its CSV run by timestamp, attach extracted metrics."""
        if not self._runs:
            log.debug("No CSV runs to attach rosbag metrics to")
            return

        # Extract timestamp from bag directory name (e.g. stage3_20260627_111607)
        bag_ts = _extract_timestamp(Path(bag_path).name)
        if not bag_ts:
            return

        # Find closest CSV run by timestamp
        best_run = None
        best_diff = float('inf')
        for run in self._runs:
            run_ts = _extract_timestamp(run.get('timestamp', ''))
            if run_ts:
                diff = abs(bag_ts - run_ts)
                if diff < best_diff and diff < 600:  # within 10 minutes
                    best_diff = diff
                    best_run = run

        if best_run is not None:
            best_run['rosbag_metrics'] = {
                'planner_hz': metrics.planner_hz,
                'cmd_vel_hz': metrics.cmd_vel_hz,
                'odom_hz': metrics.odom_hz,
                'tracking_error_mean': metrics.tracking_error_mean,
                'tracking_error_max': metrics.tracking_error_max,
                'velocity_jerk': metrics.velocity_jerk,
                'velocity_oscillation': metrics.velocity_oscillation,
                'avg_speed': metrics.avg_speed,
            }
            log.info("Attached rosbag metrics to run %s (diff=%.0fs)",
                     best_run.get('timestamp', '?'), best_diff)
            self.save()

    def get_phase_stats(self, phase_name: str) -> Optional[Dict]:
        """Get aggregated stats for a specific phase."""
        return self.data.get('phase_statistics', {}).get(phase_name)

    def get_best_run(self) -> Optional[Dict]:
        """Return the run with the lowest total_time."""
        if not self._runs:
            return None
        return min(self._runs, key=lambda r: r.get('total_time', float('inf')))

    def get_feature_matrix(self) -> Tuple[np.ndarray, np.ndarray]:
        """Returns (X, y) where X is feature matrix, y is total_time.

        Used for ML model training in score_model.py.
        """
        if self.run_count < 2:
            return np.empty((0, 0)), np.empty((0,))

        # Build features from each run
        feature_rows = []
        for run in self._runs:
            feats = [
                run.get('total_path_len', 0),
                run.get('total_dir_switches', 0),
                run.get('total_replans', 0),
                run.get('cpu_avg_overall', 0),
                run.get('planner_hz_overall', 0),
            ]
            # Add per-phase elapsed times
            for phase_name in KNOWN_PHASES:
                ph = run.get('phases', {}).get(phase_name, {})
                feats.append(ph.get('elapsed', 0))
                feats.append(ph.get('smoothness', 0))
                feats.append(ph.get('avg_speed', 0))
            feature_rows.append(feats)

        X = np.array(feature_rows, dtype=np.float64)
        y = np.array([r['total_time'] for r in self._runs], dtype=np.float64)
        return X, y

    def save(self) -> None:
        """Write database to disk."""
        self.data['runs'] = self._runs
        with open(self.db_path, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
        log.debug(f"Database saved: {self.db_path}")

    def get_rosbag_features(self) -> Dict[str, np.ndarray]:
        """Return rosbag feature matrix (X) and total_times (y) for ML training.
        Only returns runs that have rosbag_metrics attached."""
        feats, times = [], []
        for run in self._runs:
            rb = run.get('rosbag_metrics')
            if rb and run.get('total_time', 0) > 0:
                feats.append([
                    rb.get('planner_hz', 0),
                    rb.get('cmd_vel_hz', 0),
                    rb.get('tracking_error_mean', 0),
                    rb.get('tracking_error_max', 0),
                    rb.get('velocity_jerk', 0),
                    rb.get('velocity_oscillation', 0),
                    rb.get('avg_speed', 0),
                ])
                times.append(run['total_time'])
        if feats:
            return {'X': np.array(feats, dtype=np.float64),
                    'y': np.array(times, dtype=np.float64)}
        return {'X': np.empty((0, 7)), 'y': np.empty((0,))}

    @staticmethod
    def _run_hash(run: Dict) -> int:
        """Content-based dedup hash: (total_time, path_len, phase elapsed times).
        Two runs with the same timing profile within 0.1% tolerance are duplicates."""
        tt = round(run.get('total_time', 0), 1)
        pl = round(run.get('total_path_len', 0), 2)
        phases = run.get('phases', {})
        phase_elapsed = tuple(
            round(phases.get(p, {}).get('elapsed', 0), 1)
            for p in KNOWN_PHASES
        )
        return hash((tt, pl, phase_elapsed))

    @staticmethod
    def _now_iso() -> str:
        from datetime import datetime
        return datetime.now().isoformat()

    # ── Summary statistics for display ──

    def summary(self) -> str:
        """Return a human-readable summary string."""
        if self.run_count == 0:
            return "No historical data — using heuristic scoring."

        lines = [f"Metrics Database: {self.run_count} runs"]
        best = self.get_best_run()
        if best:
            lines.append(f"  Best: {best['total_time']:.1f}s")
        lines.append(f"  Feature correlations:")
        for k, v in sorted(self.data.get('feature_correlations', {}).items(),
                           key=lambda x: -abs(x[1]))[:10]:
            lines.append(f"    {k:<40s} r={v:+.3f}")
        return '\n'.join(lines)


def _extract_timestamp(name: str) -> Optional[float]:
    """Extract unix timestamp from a filename like 'trajectory_20260627_112257'
    or 'stage3_20260627_111607'. Returns seconds since epoch or None."""
    import re
    from datetime import datetime
    m = re.search(r'(\d{8})_(\d{6})', name)
    if m:
        try:
            dt = datetime.strptime(f"{m.group(1)}{m.group(2)}", '%Y%m%d%H%M%S')
            return dt.timestamp()
        except ValueError:
            pass
    return None
