"""
Keepout Behavior Model — Soft-keepout incursion modeling for narrow corridors.

Models the robot's actual behavior: when forced into keepout zones in narrow
corridors (override_lethal_cost=True), the penalty should be mild. In open
spaces, keepout entry is avoidable and should be heavily penalized.

Used by A* planner (PathResult.keepout_*) and score model (keepout penalty term).
"""
import logging
import numpy as np
from typing import Dict, List, Optional, Tuple

log = logging.getLogger('Nav2Tuner.Keepout')


class KeepoutBehaviorModel:
    """Models keepout zone navigation behavior for Ackermann robot.

    The robot uses ``override_lethal_cost=True`` in Nav2, which allows it
    to enter keepout zones in emergencies (e.g., narrow corridors where the
    keepout mask leaves insufficient clearance). This model differentiates:
      - Narrow corridor keepout entry: mild penalty (physically forced)
      - Open space keepout entry: heavy penalty (avoidable violation)

    Usage:
      model = KeepoutBehaviorModel()
      model.fit(costmap_data)
      cost = model.compute_keepout_cost(path_pixels, costmap)
    """

    def __init__(self,
                 corridor_width_threshold: float = 0.6,
                 narrow_penalty: float = 0.05,
                 open_penalty: float = 0.30):
        """
        Args:
          corridor_width_threshold: Max free-space width (m) to be "narrow corridor".
          narrow_penalty: Per-point penalty for keepout incursion in narrow corridors.
          open_penalty: Per-point penalty for keepout incursion in open spaces.
        """
        self.corridor_width_threshold = corridor_width_threshold
        self.narrow_penalty = narrow_penalty
        self.open_penalty = open_penalty
        self._corridor_mask: Optional[np.ndarray] = None
        self._keepout_mask: Optional[np.ndarray] = None

    # ═══════════════════════════════════════════════════════════
    # Corridor Detection
    # ═══════════════════════════════════════════════════════════

    def detect_narrow_corridors(self, costmap_grid: np.ndarray,
                                resolution: float = 0.05) -> np.ndarray:
        """Detect narrow corridors via EDT-based width estimation.

        For each free cell, corridor width ≈ 2 * distance_to_nearest_obstacle.
        Cells where width < corridor_width_threshold are marked as narrow.

        Returns bool array (same shape as costmap_grid).
        """
        try:
            from scipy.ndimage import distance_transform_edt
        except ImportError:
            log.warning("scipy not available — corridor detection disabled")
            return np.zeros(costmap_grid.shape, dtype=bool)

        # Obstacle mask: cells with cost >= 250 (lethal)
        lethal = (costmap_grid >= 250)
        if not lethal.any():
            return np.zeros(costmap_grid.shape, dtype=bool)

        # Distance from each cell to nearest obstacle (in pixels)
        dist_px = distance_transform_edt(~lethal)
        # Corridor width ≈ 2 * distance (walls on both sides)
        width_m = 2.0 * dist_px * resolution

        return width_m < self.corridor_width_threshold

    def fit(self, costmap_data) -> None:
        """Pre-compute corridor mask and keepout mask for a costmap.

        Args:
          costmap_data: CostmapData with grid, resolution, and optional keepout_mask.
        """
        self._keepout_mask = (costmap_data.keepout_mask
                             if costmap_data.keepout_mask is not None
                             else np.zeros(costmap_data.grid.shape, dtype=bool))

        self._corridor_mask = self.detect_narrow_corridors(
            costmap_data.grid, costmap_data.resolution
        )

    # ═══════════════════════════════════════════════════════════
    # Keepout Cost Computation
    # ═══════════════════════════════════════════════════════════

    def compute_keepout_cost(self,
                             path_px: List[Tuple[int, int]],
                             costmap_grid: np.ndarray) -> Dict[str, float]:
        """Compute keepout incursion metrics for an A* path.

        Args:
          path_px: List of (row, col) pixel coordinates.
          costmap_grid: HxW uint8 costmap array.

        Returns dict with:
          keepout_incursion_count: number of path points inside keepout
          keepout_cost: mean cost of keepout incursions
          narrow_incursions: count of incursions in narrow corridors
          open_incursions: count of incursions in open spaces
          total_penalty: weighted penalty score
        """
        if self._keepout_mask is None or not path_px:
            return {
                'keepout_incursion_count': 0,
                'keepout_cost': 0.0,
                'narrow_incursions': 0,
                'open_incursions': 0,
                'total_penalty': 0.0,
            }

        H, W = costmap_grid.shape
        kc, kcost = 0, 0.0
        narrow_count, open_count = 0, 0

        for r, c in path_px:
            if not (0 <= r < H and 0 <= c < W):
                continue
            # Check if this cell is keepout
            if not self._keepout_mask[r, c]:
                continue
            kc += 1
            kcost += float(costmap_grid[r, c])

            # Corridor context
            if (self._corridor_mask is not None and
                0 <= r < self._corridor_mask.shape[0] and
                0 <= c < self._corridor_mask.shape[1]):
                if self._corridor_mask[r, c]:
                    narrow_count += 1
                else:
                    open_count += 1
            else:
                open_count += 1  # default to open-space penalty when no corridor info

        total_penalty = (narrow_count * self.narrow_penalty +
                        open_count * self.open_penalty)

        return {
            'keepout_incursion_count': kc,
            'keepout_cost': kcost / max(len(path_px), 1),
            'narrow_incursions': narrow_count,
            'open_incursions': open_count,
            'total_penalty': total_penalty / max(len(path_px), 1),
        }

    # ═══════════════════════════════════════════════════════════
    # Scenario-specific keepout analysis
    # ═══════════════════════════════════════════════════════════

    @staticmethod
    def estimate_corridor_width_at_point(row: int, col: int,
                                         costmap_grid: np.ndarray,
                                         resolution: float = 0.05) -> float:
        """Estimate corridor width at a specific pixel.

        Uses ray-casting: shoots rays in 8 directions to find nearest obstacles
        and computes the narrowest passage width.
        """
        H, W = costmap_grid.shape
        if not (0 <= row < H and 0 <= col < W):
            return 999.0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                      (1, 1), (-1, -1), (1, -1), (-1, 1)]
        widths = []

        for dr, dc in directions:
            r, c = row, col
            steps = 0
            while (0 <= r < H and 0 <= c < W and
                   costmap_grid[r, c] < 250 and steps < 100):
                r += dr
                c += dc
                steps += 1
            widths.append(steps * resolution * 2)  # ×2 for both sides

        return min(widths) if widths else 999.0
