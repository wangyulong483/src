"""
Offline Nav2 Auto Tuner — Data-driven parameter optimization for Ackermann robots.

Usage:
  from offline_tuner import ScoreModel, OptunaTieredSearch, YamlPatchGenerator

Strategy:
  0 CSV    → Heuristic (preserved from original)
  1-29 CSV → Correlation-based weights (corr(metric, total_time))
  30+ CSV  → ML prediction (LightGBM > XGBoost > RandomForest)
  +rosbag  → Same tier, richer feature set
"""

__version__ = "3.0.0"

from .config import PARAM_SPACE, DEFAULTS, TIERS, PARAM_TO_YAML_PATH
from .feature_extractor import FeatureExtractor, PhaseMetrics, RunMetrics
from .phase_metrics import PhaseMetricsDB, PhaseStats
from .score_model import ScoreModel
from .costmap_generator import CostmapGenerator, CostmapData
from .astar_planner import AstarPlanner, PathResult

# Lazy imports for modules built in later phases
try:
    from .optuna_search import OptunaTieredSearch
except ImportError:
    OptunaTieredSearch = None

try:
    from .yaml_patch import YamlPatchGenerator
except ImportError:
    YamlPatchGenerator = None

try:
    from .compare import RunComparer
except ImportError:
    RunComparer = None

try:
    from .visualizer import Visualizer
except ImportError:
    Visualizer = None

try:
    from .evolution_engine import EvolutionEngine
except ImportError:
    EvolutionEngine = None

try:
    from .keepout_behavior import KeepoutBehaviorModel
except ImportError:
    KeepoutBehaviorModel = None
