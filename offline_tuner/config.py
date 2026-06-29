"""
Shared constants: parameter search space, defaults, tier definitions, YAML path mapping.
No logic — pure data.
"""
from pathlib import Path

HERE = Path(__file__).parent
PROJECT_ROOT = HERE.parent

# Shared output root (metrics_database.json lives here)
OUT_DIR = PROJECT_ROOT / "tuning_results"

# Per-run output directory (set by _analyze_plans.py at startup)
# Each run gets tuning_results/out1/, out2/, out3/, ...
RUN_OUT_DIR: Path = OUT_DIR  # default, overwritten at runtime


def next_out_dir() -> Path:
    """Find and create the next available outN/ directory under tuning_results/.
    Returns e.g. tuning_results/out3/ if out1/ and out2/ already exist.
    """
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    n = 1
    while (OUT_DIR / f"out{n}").exists():
        n += 1
    run_dir = OUT_DIR / f"out{n}"
    run_dir.mkdir(parents=True, exist_ok=True)
    return run_dir

# ═══════════════════════════════════════════════════════════
# Parameter search space (27 params)
# ═══════════════════════════════════════════════════════════
PARAM_SPACE = {
    # RPP Controller (15 params)
    'controller.desired_linear_vel':         (0.30, 0.60, 'float'),
    'controller.lookahead_dist':             (0.50, 0.80, 'float'),
    'controller.min_lookahead_dist':         (0.20, 0.55, 'float'),
    'controller.max_lookahead_dist':         (0.70, 1.50, 'float'),
    'controller.lookahead_time':             (0.8, 2.0, 'float'),
    'controller.cost_scaling_gain':          (0.3, 3.0, 'float'),
    'controller.cost_scaling_dist':          (0.05, 0.25, 'float'),
    'controller.min_approach_linear_vel':    (0.05, 0.35, 'float'),
    'controller.approach_velocity_scaling_dist': (0.3, 1.0, 'float'),
    'controller.xy_goal_tolerance':          (0.15, 0.50, 'float'),
    'controller.max_linear_vel':             (0.40, 0.70, 'float'),
    'controller.max_angular_vel':            (1.0, 2.5, 'float'),
    'controller.max_linear_accel':           (0.8, 2.0, 'float'),
    'controller.regulated_linear_scaling_min_radius': (0.20, 0.45, 'float'),
    'controller.regulated_linear_scaling_min_speed':  (0.0, 0.25, 'float'),

    # Smac Planner (12 params)
    'planner.inflation_radius.local':        (0.10, 0.60, 'float'),
    'planner.inflation_radius.global':       (0.10, 0.60, 'float'),
    'planner.cost_scaling_factor.local':     (0.5, 6.0, 'float'),
    'planner.cost_scaling_factor.global':    (0.5, 6.0, 'float'),
    'planner.reverse_penalty':               (1.0, 5.0, 'float'),
    'planner.change_penalty':                (0.0, 0.30, 'float'),
    'planner.non_straight_penalty':          (0.8, 2.0, 'float'),
    'planner.analytic_expansion_ratio':      (1.5, 5.0, 'float'),
    'planner.max_iterations':                (500, 2500, 'int'),
    'planner.max_planning_time':             (0.5, 3.5, 'float'),
    'planner.angle_quantization_bins':       (40, 72, 'int'),
    'planner.cost_penalty':                  (2.0, 8.0, 'float'),
}

# ═══════════════════════════════════════════════════════════
# Defaults — 70.1s gold baseline (2026-06-25)
# ═══════════════════════════════════════════════════════════
DEFAULTS = {
    'controller.desired_linear_vel': 0.50,
    'controller.lookahead_dist': 0.65,
    'controller.min_lookahead_dist': 0.30,
    'controller.max_lookahead_dist': 0.90,
    'controller.lookahead_time': 1.2,
    'controller.cost_scaling_gain': 1.0,
    'controller.cost_scaling_dist': 0.12,
    'controller.min_approach_linear_vel': 0.22,
    'controller.approach_velocity_scaling_dist': 0.50,
    'controller.xy_goal_tolerance': 0.40,
    'controller.max_linear_vel': 0.60,
    'controller.max_angular_vel': 2.0,
    'controller.max_linear_accel': 1.2,
    'controller.regulated_linear_scaling_min_radius': 0.30,
    'controller.regulated_linear_scaling_min_speed': 0.18,
    'planner.inflation_radius.local': 0.55,
    'planner.inflation_radius.global': 0.55,
    'planner.cost_scaling_factor.local': 3.0,
    'planner.cost_scaling_factor.global': 3.0,
    'planner.reverse_penalty': 2.0,
    'planner.change_penalty': 0.10,
    'planner.non_straight_penalty': 1.3,
    'planner.analytic_expansion_ratio': 3.0,
    'planner.max_iterations': 1500,
    'planner.max_planning_time': 1.5,
    'planner.angle_quantization_bins': 48,
    'planner.cost_penalty': 4.0,
}

# ═══════════════════════════════════════════════════════════
# Tier definitions
# ═══════════════════════════════════════════════════════════
T1_PARAMS = [
    'controller.desired_linear_vel',
    'controller.lookahead_dist',
    'controller.cost_scaling_gain',
    'controller.cost_scaling_dist',
    'planner.inflation_radius.local',
    'planner.reverse_penalty',
    'planner.change_penalty',
]

T2_PARAMS = [
    'controller.min_lookahead_dist',
    'controller.max_lookahead_dist',
    'controller.lookahead_time',
    'controller.min_approach_linear_vel',
    'controller.approach_velocity_scaling_dist',
    'controller.xy_goal_tolerance',
    'controller.max_linear_vel',
    'controller.max_angular_vel',
    'planner.inflation_radius.global',
    'planner.cost_scaling_factor.local',
    'planner.cost_scaling_factor.global',
    'planner.non_straight_penalty',
]

T3_PARAMS = [
    'controller.max_linear_accel',
    'controller.regulated_linear_scaling_min_radius',
    'controller.regulated_linear_scaling_min_speed',
    'planner.analytic_expansion_ratio',
    'planner.max_iterations',
    'planner.max_planning_time',
    'planner.angle_quantization_bins',
    'planner.cost_penalty',
]

TIERS = {
    'tier1': T1_PARAMS,
    'default': T1_PARAMS + T2_PARAMS,
    'full': T1_PARAMS + T2_PARAMS + T3_PARAMS,
}

# ═══════════════════════════════════════════════════════════
# Internal param name → Nav2 YAML dotted path
# ═══════════════════════════════════════════════════════════
PARAM_TO_YAML_PATH = {
    'controller.desired_linear_vel':         'controller_server.ros__parameters.FollowPath.desired_linear_vel',
    'controller.lookahead_dist':             'controller_server.ros__parameters.FollowPath.lookahead_dist',
    'controller.min_lookahead_dist':         'controller_server.ros__parameters.FollowPath.min_lookahead_dist',
    'controller.max_lookahead_dist':         'controller_server.ros__parameters.FollowPath.max_lookahead_dist',
    'controller.lookahead_time':             'controller_server.ros__parameters.FollowPath.lookahead_time',
    'controller.cost_scaling_gain':          'controller_server.ros__parameters.FollowPath.cost_scaling_gain',
    'controller.cost_scaling_dist':          'controller_server.ros__parameters.FollowPath.cost_scaling_dist',
    'controller.min_approach_linear_vel':    'controller_server.ros__parameters.FollowPath.min_approach_linear_velocity',
    'controller.approach_velocity_scaling_dist': 'controller_server.ros__parameters.FollowPath.approach_velocity_scaling_dist',
    'controller.xy_goal_tolerance':          'controller_server.ros__parameters.goal_checker.xy_goal_tolerance',
    'controller.max_linear_vel':             'controller_server.ros__parameters.FollowPath.max_linear_vel',
    'controller.max_angular_vel':            'controller_server.ros__parameters.FollowPath.max_angular_vel',
    'controller.max_linear_accel':           'controller_server.ros__parameters.FollowPath.max_linear_accel',
    'controller.regulated_linear_scaling_min_radius': 'controller_server.ros__parameters.FollowPath.regulated_linear_scaling_min_radius',
    'controller.regulated_linear_scaling_min_speed':  'controller_server.ros__parameters.FollowPath.regulated_linear_scaling_min_speed',
    'planner.inflation_radius.local':        'local_costmap.local_costmap.ros__parameters.inflation_layer.inflation_radius',
    'planner.inflation_radius.global':       'global_costmap.global_costmap.ros__parameters.inflation_layer.inflation_radius',
    'planner.cost_scaling_factor.local':     'local_costmap.local_costmap.ros__parameters.inflation_layer.cost_scaling_factor',
    'planner.cost_scaling_factor.global':    'global_costmap.global_costmap.ros__parameters.inflation_layer.cost_scaling_factor',
    'planner.reverse_penalty':               'planner_server.ros__parameters.GridBased.reverse_penalty',
    'planner.change_penalty':                'planner_server.ros__parameters.GridBased.change_penalty',
    'planner.non_straight_penalty':          'planner_server.ros__parameters.GridBased.non_straight_penalty',
    'planner.analytic_expansion_ratio':      'planner_server.ros__parameters.GridBased.analytic_expansion_ratio',
    'planner.max_iterations':                'planner_server.ros__parameters.GridBased.max_iterations',
    'planner.max_planning_time':             'planner_server.ros__parameters.GridBased.max_planning_time',
    'planner.angle_quantization_bins':       'planner_server.ros__parameters.GridBased.angle_quantization_bins',
    'planner.cost_penalty':                  'planner_server.ros__parameters.GridBased.cost_penalty',
}

# CSV column names (14-column format)
CSV_COLUMNS = [
    'elapsed_s', 'x_m', 'y_m', 'yaw_rad', 'state',
    'cmd_vx', 'cmd_wz', 'plan_pts', 'plan_len_m',
    'plan_end_x', 'plan_end_y', 'cpu_pct', 'mem_pct', 'cpu_temp_c',
]

# Known mission phases
KNOWN_PHASES = ['NAV_TO_QR', 'BACKING_UP', 'CRUISE_CHANNEL', 'RETURN_P']

# ═══════════════════════════════════════════════════════════
# Obstacle / keepout modelling for offline tuning
# ═══════════════════════════════════════════════════════════
OBSTACLE_COUNT = 5                 # number of obstacles placed on the field
N_OBSTACLE_SAMPLES = 5             # Monte-Carlo samples per parameter evaluation
KEEPOUT_COST = 200                 # cost value for traversable keepout cells (< LETHAL)
OBSTACLE_PLACE_RETRIES = 10        # retries if random obstacles make course unreachable
OBSTACLE_SOFT_MARGIN = 0.10        # m — keep obstacles at least this far from walls/keepout
ROBOT_RADIUS = 0.15                # m — circular footprint radius for collision checks

# Metrics tracked for correlation scoring
TRACKED_METRICS = [
    'total_time', 'path_len', 'avg_speed', 'jerk', 'wobble',
    'angular_oscillation', 'dir_switches', 'avg_plan_len', 'plan_changes',
    'cpu_avg', 'cpu_max', 'curvature_mean', 'curvature_variance',
    'planner_frequency', 'goal_reached', 'smoothness',
]
