"""Basic smoke tests for offline_tuner core components.

Run: python -m pytest tests/ -v  (or just: python tests/test_core.py)
"""

import sys
import os
import unittest
import numpy as np

# Ensure project root is in path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from offline_tuner.config import DEFAULTS, PARAM_SPACE, TIERS
from offline_tuner.feature_extractor import FeatureExtractor
from offline_tuner.costmap_generator import (CostmapGenerator, ORIGIN_X, ORIGIN_Y,
                                              MAP_WIDTH, MAP_HEIGHT)
from offline_tuner.astar_planner import AstarPlanner
from offline_tuner.score_model import ScoreModel
from offline_tuner.phase_metrics import PhaseMetricsDB


class TestFeatureExtractor(unittest.TestCase):
    """CSV → RunMetrics parsing."""

    def setUp(self):
        self.extractor = FeatureExtractor()

    def test_parse_trajectory_csv(self):
        """Parse a real trajectory CSV."""
        csv_dir = os.path.join(os.path.dirname(__file__), '..', 'data', 'trajectories')
        if not os.path.isdir(csv_dir):
            self.skipTest("No trajectory data directory")
        csvs = [f for f in os.listdir(csv_dir) if f.endswith('.csv') and '_plans' not in f]
        if not csvs:
            self.skipTest("No CSV files found")
        run = self.extractor.analyze_run(os.path.join(csv_dir, csvs[0]))
        self.assertIsNotNone(run)
        self.assertGreater(run.total_time, 0)
        self.assertTrue(hasattr(run, 'phases'))


class TestCostmapGenerator(unittest.TestCase):
    """Costmap generation from competition maps."""

    def setUp(self):
        self.gen = CostmapGenerator()

    def test_load_maps(self):
        """Load static map and optionally keepout."""
        self.gen.load_maps()
        self.assertIsNotNone(self.gen.static_map)
        self.assertGreater(self.gen.static_map.sum(), 0)

    def test_generate_default_costmap(self):
        """Generate costmap with default params."""
        self.gen.load_maps()
        costmap = self.gen.generate(DEFAULTS, with_keepout=False)
        self.assertIsNotNone(costmap.grid)
        self.assertEqual(costmap.grid.shape, (MAP_HEIGHT, MAP_WIDTH))


class TestAstarPlanner(unittest.TestCase):
    """A* path planning on costmap."""

    def setUp(self):
        self.gen = CostmapGenerator()
        self.gen.load_maps()
        self.planner = AstarPlanner()

    def test_plan_reachable(self):
        """P→VLM should always be reachable."""
        from offline_tuner.costmap_generator import P_POINT, VLM_CCW
        costmap = self.gen.generate(DEFAULTS, with_keepout=False)
        result = self.planner.plan(costmap, start_world=P_POINT, goal_world=VLM_CCW)
        self.assertTrue(result.reachable)
        self.assertGreater(result.path_len, 2.0)

    def test_plan_unreachable(self):
        """Goal isolated by walls should be unreachable."""
        # Create a costmap with a fully enclosed lethal box
        grid = np.full((50, 50), 0, dtype=np.uint8)
        grid[10:40, 10:40] = 254  # lethal box
        grid[20, 20] = 0  # goal inside box
        from offline_tuner.costmap_generator import CostmapData
        cm = CostmapData(grid=grid, width=50, height=50, resolution=0.05,
                         origin_x=0, origin_y=0, inflation_radius=0.1, cost_scaling_factor=3.0)
        # Start outside box (goal inside)
        result = self.planner.plan(cm, start_world=(0.1, 0.1), goal_world=(1.0, 1.0))
        self.assertFalse(result.reachable)


class TestScoreModel(unittest.TestCase):
    """Scoring pipeline integration."""

    def setUp(self):
        self.db = PhaseMetricsDB()
        self.model = ScoreModel(self.db)

    def test_compute_score_defaults(self):
        """Score default params. Should return 0-1 range."""
        score = self.model.compute_score(DEFAULTS)
        self.assertGreater(score, 0.0)
        self.assertLess(score, 2.0)

    def test_strategy_selection(self):
        """Strategy should be heuristic with 0 runs, path_based with map."""
        empty_db = PhaseMetricsDB()
        empty_model = ScoreModel(empty_db)
        self.assertIn(empty_model.strategy, ('heuristic', 'path_based'))


class TestParameterSpace(unittest.TestCase):
    """Parameter configuration integrity."""

    def test_tier_sizes(self):
        """Verify tier parameter counts."""
        self.assertEqual(len(TIERS['tier1']), 7)
        self.assertGreater(len(TIERS['default']), 15)
        self.assertGreater(len(TIERS['full']), len(TIERS['default']))

    def test_defaults_in_param_space(self):
        """All DEFAULTS must be in PARAM_SPACE."""
        for key in DEFAULTS:
            self.assertIn(key, PARAM_SPACE, f"{key} not in PARAM_SPACE")


if __name__ == '__main__':
    unittest.main(verbosity=2)
