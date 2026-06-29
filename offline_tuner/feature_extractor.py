"""
Feature extraction from trajectory CSV files.

Extracts per-phase and per-run metrics. Designed to work with both
CSV-loaded data and rosbag-extracted data (rosbag_loader produces
the same row dict format).
"""
import csv
import logging
from pathlib import Path
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
import numpy as np

from .config import KNOWN_PHASES

log = logging.getLogger('Nav2Tuner.Features')


@dataclass
class PhaseMetrics:
    """Per-phase computed metrics."""
    phase_name: str = ""
    elapsed: float = 0.0
    path_len: float = 0.0
    avg_speed: float = 0.0
    jerk: float = 0.0                       # mean(|diff(diff(vx))|)
    wobble: float = 0.0                     # std(wz)
    angular_oscillation: float = 0.0        # mean(|wz|)
    dir_switches: int = 0
    avg_plan_len: float = 0.0
    plan_changes: int = 0
    cpu_avg: float = 0.0
    cpu_max: int = 0
    curvature_mean: float = 0.0
    curvature_variance: float = 0.0
    heading_error_mean: float = 0.0
    planner_frequency: float = 0.0          # n_points / elapsed (proxy for Hz)
    goal_reached: bool = False
    smoothness: float = 0.0                 # composite: jerk + wobble + curvature
    n_points: int = 0

    def to_dict(self) -> Dict:
        return {
            'elapsed': self.elapsed, 'path_len': self.path_len,
            'avg_speed': self.avg_speed, 'jerk': self.jerk, 'wobble': self.wobble,
            'angular_oscillation': self.angular_oscillation,
            'dir_switches': self.dir_switches, 'avg_plan_len': self.avg_plan_len,
            'plan_changes': self.plan_changes, 'cpu_avg': self.cpu_avg,
            'cpu_max': self.cpu_max, 'curvature_mean': self.curvature_mean,
            'curvature_variance': self.curvature_variance,
            'planner_frequency': self.planner_frequency,
            'goal_reached': self.goal_reached, 'smoothness': self.smoothness,
            'n_points': self.n_points,
        }


@dataclass
class RunMetrics:
    """Aggregate metrics for a single trajectory run."""
    source: str = ""                        # file path
    timestamp: str = ""
    total_time: float = 0.0
    total_path_len: float = 0.0
    total_dir_switches: int = 0
    total_replans: int = 0
    phases: Dict[str, PhaseMetrics] = field(default_factory=dict)
    cpu_avg_overall: float = 0.0
    goal_reached: bool = False
    planner_hz_overall: float = 0.0
    n_total_points: int = 0
    nav2_config: Dict[str, float] = field(default_factory=dict)  # ★ 新增


class FeatureExtractor:
    """Extract metrics from trajectory CSV rows."""

    @staticmethod
    def load_csv(path: str) -> List[Dict]:
        """Load trajectory CSV, returns list of row dicts."""
        rows = []
        try:
            with open(path, newline='', encoding='utf-8') as f:
                for row in csv.DictReader(f):
                    rows.append({
                        'elapsed': float(row['elapsed_s']),
                        'x': float(row['x_m']), 'y': float(row['y_m']),
                        'yaw': float(row['yaw_rad']), 'state': row['state'],
                        'cmd_vx': float(row['cmd_vx']),
                        'cmd_wz': float(row['cmd_wz']),
                        'plan_pts': int(row['plan_pts']),
                        'plan_len': float(row['plan_len_m']),
                        'plan_ex': float(row['plan_end_x']),
                        'plan_ey': float(row['plan_end_y']),
                        'cpu': int(row['cpu_pct']),
                        'mem': int(row['mem_pct']),
                        'cpu_temp': int(row['cpu_temp_c']),
                    })
        except Exception as e:
            log.warning(f"Failed to load {path}: {e}")
            return []
        return rows

    @staticmethod
    def group_by_phase(rows: List[Dict]) -> Dict[str, List[Dict]]:
        """Split rows by 'state' field."""
        phases: Dict[str, List[Dict]] = {}
        for r in rows:
            phases.setdefault(r['state'], []).append(r)
        return phases

    def score_phase(self, rows: List[Dict], phase_name: str = "") -> Optional[PhaseMetrics]:
        """Compute PhaseMetrics for a contiguous list of rows."""
        if len(rows) < 3:
            return None

        n = len(rows)
        elapsed = rows[-1]['elapsed'] - rows[0]['elapsed']
        if elapsed <= 0:
            return None

        xs = np.array([r['x'] for r in rows], dtype=np.float64)
        ys = np.array([r['y'] for r in rows], dtype=np.float64)
        yaws = np.array([r['yaw'] for r in rows], dtype=np.float64)
        vx = np.array([r['cmd_vx'] for r in rows], dtype=np.float64)
        wz = np.array([r['cmd_wz'] for r in rows], dtype=np.float64)
        plan_lens = np.array([r['plan_len'] for r in rows], dtype=np.float64)
        plan_ex = np.array([r['plan_ex'] for r in rows], dtype=np.float64)
        plan_ey = np.array([r['plan_ey'] for r in rows], dtype=np.float64)
        cpus = np.array([r['cpu'] for r in rows if r['cpu'] >= 0], dtype=np.float64)

        # Distance
        path_len = float(np.sum(np.hypot(np.diff(xs), np.diff(ys))))

        # Speed
        avg_speed = path_len / elapsed

        # Jerk: mean absolute acceleration change (derivative of accel)
        if len(vx) >= 3:
            jerk = float(np.mean(np.abs(np.diff(np.diff(vx)))))
        else:
            jerk = 0.0

        # Wobble: standard deviation of angular velocity
        wobble = float(np.std(wz))

        # Angular oscillation: mean absolute angular velocity
        angular_oscillation = float(np.mean(np.abs(wz)))

        # Direction switches
        dir_switches = int(np.sum((vx[:-1] * vx[1:]) < -0.001))

        # Planning metrics
        avg_plan_len_val = float(np.mean(plan_lens)) if len(plan_lens) > 0 else 0.0
        plan_changes = int(np.sum(np.diff(plan_lens) != 0))

        # CPU
        cpu_avg = float(np.mean(cpus)) if len(cpus) > 0 else 0.0
        cpu_max = int(np.max(cpus)) if len(cpus) > 0 else 0

        # Curvature: from yaw changes normalized by path increment
        curv_mean, curv_var = self._compute_curvature(xs, ys, yaws)

        # Heading error: angle between current heading and direction to plan endpoint
        heading_err = self._compute_heading_error(xs, ys, yaws, plan_ex, plan_ey)

        # Planner frequency (proxy): points per second
        planner_freq = n / elapsed

        # Smoothness composite: weighted combination
        smoothness = self._compute_smoothness(jerk, wobble, curv_var)

        return PhaseMetrics(
            phase_name=phase_name, elapsed=elapsed, path_len=path_len,
            avg_speed=avg_speed, jerk=jerk, wobble=wobble,
            angular_oscillation=angular_oscillation, dir_switches=dir_switches,
            avg_plan_len=avg_plan_len_val, plan_changes=plan_changes,
            cpu_avg=cpu_avg, cpu_max=cpu_max,
            curvature_mean=curv_mean, curvature_variance=curv_var,
            heading_error_mean=heading_err,
            planner_frequency=planner_freq,
            goal_reached=(phase_name == 'RETURN_P'),
            smoothness=smoothness, n_points=n,
        )

    @staticmethod
    def _compute_curvature(xs: np.ndarray, ys: np.ndarray,
                           yaws: np.ndarray) -> Tuple[float, float]:
        """Compute mean curvature and curvature variance from path geometry.

        Curvature κ = |Δyaw| / Δs for each segment.
        """
        if len(xs) < 3:
            return 0.0, 0.0
        ds = np.hypot(np.diff(xs), np.diff(ys))
        dyaw = np.abs(np.diff(yaws))
        # Wrap dyaw to [-π, π]
        dyaw = np.minimum(dyaw, 2 * np.pi - dyaw)
        valid = ds > 0.001
        if not np.any(valid):
            return 0.0, 0.0
        curvatures = dyaw[valid] / ds[valid]
        return float(np.mean(curvatures)), float(np.var(curvatures))

    @staticmethod
    def _compute_heading_error(xs: np.ndarray, ys: np.ndarray,
                               yaws: np.ndarray, plan_ex: np.ndarray,
                               plan_ey: np.ndarray) -> float:
        """Mean absolute heading error: angle between current yaw and
        direction to plan endpoint."""
        if len(xs) < 2:
            return 0.0
        errors = []
        for i in range(len(xs)):
            dx = plan_ex[i] - xs[i]
            dy = plan_ey[i] - ys[i]
            if abs(dx) < 0.001 and abs(dy) < 0.001:
                continue
            target_yaw = np.arctan2(dy, dx)
            err = target_yaw - yaws[i]
            err = (err + np.pi) % (2 * np.pi) - np.pi  # wrap
            errors.append(abs(err))
        return float(np.mean(errors)) if errors else 0.0

    @staticmethod
    def _compute_smoothness(jerk: float, wobble: float, curv_var: float) -> float:
        """Composite smoothness score (0=perfectly smooth, higher=rougher).

        Normalized combination of jerk, wobble, and curvature variance.
        """
        # Normalize to roughly [0, 1] range for each component
        j_norm = min(jerk / 0.5, 1.0)
        w_norm = min(wobble / 0.5, 1.0)
        c_norm = min(curv_var / 2.0, 1.0)
        return j_norm * 0.4 + w_norm * 0.3 + c_norm * 0.3

    def analyze_run(self, csv_path: str) -> Optional[RunMetrics]:
        """Full analysis of one CSV file into RunMetrics."""
        rows = self.load_csv(csv_path)
        if not rows:
            return None

        phases = self.group_by_phase(rows)
        total_time = rows[-1]['elapsed'] - rows[0]['elapsed']

        phase_metrics: Dict[str, PhaseMetrics] = {}
        total_dir = 0
        total_replans = 0
        all_cpus = []

        for phase_name in KNOWN_PHASES:
            if phase_name in phases:
                pm = self.score_phase(phases[phase_name], phase_name)
                if pm:
                    phase_metrics[phase_name] = pm
                    total_dir += pm.dir_switches
                    total_replans += pm.plan_changes
                    if pm.cpu_avg > 0:
                        all_cpus.append(pm.cpu_avg)

        # Also score any unnamed phases
        for pname, prows in phases.items():
            if pname not in KNOWN_PHASES and len(prows) >= 3:
                pm = self.score_phase(prows, pname)
                if pm:
                    phase_metrics[pname] = pm

        # Overall path length (all rows)
        xs_all = np.array([r['x'] for r in rows], dtype=np.float64)
        ys_all = np.array([r['y'] for r in rows], dtype=np.float64)
        total_path = float(np.sum(np.hypot(np.diff(xs_all), np.diff(ys_all))))

        # Overall planner Hz
        planner_hz = len(rows) / total_time if total_time > 0 else 0.0

        goal_reached = 'DONE' in phases or (
            'RETURN_P' in phase_metrics and phase_metrics['RETURN_P'].goal_reached
        )

        # Try to load nav2 params from summary JSON
        nav2_config = self._load_summary_params(csv_path)

        return RunMetrics(
            source=csv_path,
            timestamp=Path(csv_path).stem,
            total_time=total_time,
            total_path_len=total_path,
            total_dir_switches=total_dir,
            total_replans=total_replans,
            phases=phase_metrics,
            cpu_avg_overall=float(np.mean(all_cpus)) if all_cpus else 0.0,
            goal_reached=goal_reached,
            planner_hz_overall=planner_hz,
            n_total_points=len(rows),
            nav2_config=nav2_config,
        )

    @staticmethod
    def _normalize_param_name(name: str) -> str:
        """Normalize param names from JSON to internal short form.

        Competition master writes full names (e.g. 'min_approach_linear_velocity')
        but offline_tuner uses short names (e.g. 'min_approach_linear_vel').
        """
        _RENAMES = {
            'controller.min_approach_linear_velocity': 'controller.min_approach_linear_vel',
            'controller.min_approach_linear_vel': 'controller.min_approach_linear_vel',
            'controller.xy_goal_tolerance': 'controller.xy_goal_tolerance',
        }
        return _RENAMES.get(name, name)

    @staticmethod
    def _load_summary_params(csv_path: str) -> Dict[str, float]:
        """Try to load nav2_config from the corresponding summary JSON."""
        import json as _json
        summary_path = Path(csv_path).with_suffix('')
        # Strip trailing timestamp suffix for summary lookup
        parent = Path(csv_path).parent
        stem = Path(csv_path).stem
        # Try exact match: trajectory_XXXXXX → trajectory_XXXXXX_summary.json
        json_path = parent / f"{stem}_summary.json"
        if not json_path.exists():
            # Try glob
            candidates = list(parent.glob(f"{stem[:20]}*_summary.json"))
            if candidates:
                json_path = candidates[0]
            else:
                return {}
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = _json.load(f)
            params = data.get('params', {})
            nav2 = params.get('nav2_config', {})
            # Normalize param names to internal short form
            if nav2:
                nav2 = {FeatureExtractor._normalize_param_name(k): v
                        for k, v in nav2.items()}
                log.info(f"Loaded nav2_config: {len(nav2)} params from {json_path.name}")
            return nav2
        except Exception:
            return {}

    def analyze_directory(self, dir_path: str) -> List[RunMetrics]:
        """Batch-analyze all CSVs in a directory (recursive)."""
        results = []
        p = Path(dir_path)
        if not p.exists():
            log.warning(f"Directory not found: {dir_path}")
            return results

        for csv_file in sorted(p.rglob('trajectory_*.csv')):
            # Skip plans.csv (plan history, not trajectory)
            if '_plans' in csv_file.name:
                continue
            rm = self.analyze_run(str(csv_file))
            if rm:
                results.append(rm)
                log.info(f"  Analyzed: {csv_file.name} ({rm.total_time:.1f}s, "
                         f"{len(rm.phases)} phases)")
        return results
