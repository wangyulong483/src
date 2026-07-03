"""
Costmap generator — load real competition map and generate Nav2-style costmaps.
Supports inflation, keepout zones, and obstacle layers from PGM files.

Used by offline_tuner for path planning evaluation against the real track geometry.
Falls back gracefully to heuristic scoring when map files are unavailable.
"""
import logging
import time
from collections import deque
import numpy as np
from pathlib import Path
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

from .config import KEEPOUT_COST, OBSTACLE_COUNT, OBSTACLE_PLACE_RETRIES, OBSTACLE_SOFT_MARGIN

log = logging.getLogger('Nav2Tuner.Costmap')

# ---------------------------------------------------------------------------
# Map paths (relative to project root)
# ---------------------------------------------------------------------------
MAP_DIR = Path(__file__).parent.parent / "originbot_navigation" / "maps"
ROOM_PGM = MAP_DIR / "room.pgm"
ROOM_YAML = MAP_DIR / "room.yaml"
KEEPOUT_PGM = MAP_DIR / "keepout_mask.pgm"

# ---------------------------------------------------------------------------
# Map parameters (from room.yaml / keepout_mask.yaml)
# ---------------------------------------------------------------------------
RESOLUTION = 0.05   # m/pixel
ORIGIN_X = -2.65    # world x at pixel col=0
ORIGIN_Y = -4.5     # world y at pixel row=0
MAP_WIDTH = 163     # columns (pixels)
MAP_HEIGHT = 141    # rows (pixels)

# ---------------------------------------------------------------------------
# Key waypoints — world coordinates (from competition_master_stage3.py)
# ---------------------------------------------------------------------------
P_POINT = (-1.985, -0.014)      # yaw=0.262
QR_POINT = (0.41, -3.17)        # QR task point
ENTRY_POINT = (0.38, -1.10)     # channel entry
VLM_CCW = (2.17, 0.69)          # CCW VLM stop (yaw=0.80)
VLM_CW = (3.01, -1.16)          # CW VLM stop (2026-06-28 recalibrated)

# Full competition paths — each is [start, waypoint1, waypoint2, ..., goal]
# CCW (逆时针, even QR): P→QR→entry→ccw_wps→VLM→return_wp→P
CCW_PATH = [
    P_POINT, QR_POINT, ENTRY_POINT,
    (0.25, -1.17), (1.66, -1.50), (2.90, -0.90), VLM_CCW,
    (1.07, -0.73), P_POINT,
]
# CW (顺时针, odd QR): P→QR→entry→cw_wps→VLM→return_wp→P
CW_PATH = [
    P_POINT, QR_POINT, ENTRY_POINT,
    (0.93, 0.11), (2.17, 0.69), VLM_CW,
    (1.07, -0.73), P_POINT,
]

# ---------------------------------------------------------------------------
# Costmap constants
# ---------------------------------------------------------------------------
LETHAL = 254
FREE = 0
UNKNOWN = 205
INSCRIBED_RADIUS = 0.05  # m — simplified: use 1px as inscribed radius


@dataclass
class CostmapData:
    """Generated costmap with metadata.

    Attributes
    ----------
    grid : np.ndarray
        HxW uint8 array. 0 = free space, 254 = lethal obstacle.
    width : int
        Columns (pixels).
    height : int
        Rows (pixels).
    resolution : float
        Meters per pixel.
    origin_x : float
        World x coordinate at pixel (0, 0).
    origin_y : float
        World y coordinate at pixel (0, 0).
    inflation_radius : float
        Inflation radius used to generate this costmap (meters).
    cost_scaling_factor : float
        Cost scaling factor used to generate this costmap.
    keepout_mask : np.ndarray or None
        Separate keepout mask (HxW bool or uint8). Cells >= 250 are keepout zones.
        Used by A* planner to track keepout incursions vs wall collisions.
    """
    grid: np.ndarray
    width: int
    height: int
    resolution: float
    origin_x: float
    origin_y: float
    inflation_radius: float
    cost_scaling_factor: float
    keepout_mask: np.ndarray = None  # Phase 3: keepout behavior tracking
    obstacle_pixels: List[Tuple[int, int]] = field(default_factory=list)  # (col,row) of synthetic obstacles


class CostmapGenerator:
    """Load PGM maps and generate Nav2-style costmaps with inflation.

    Usage
    -----
    >>> gen = CostmapGenerator()
    >>> gen.load_maps()
    >>> costmap = gen.generate({
    ...     'planner.inflation_radius.local': 0.60,
    ...     'planner.cost_scaling_factor.local': 5.0,
    ... })

    Falls back gracefully: if maps are unavailable, ``maps_available``
    returns False and the caller should use heuristic scoring instead.
    """

    def __init__(self) -> None:
        self.static_map: Optional[np.ndarray] = None
        self.keepout_map: Optional[np.ndarray] = None
        self._loaded: bool = False

    # ------------------------------------------------------------------
    # Map loading
    # ------------------------------------------------------------------

    def load_maps(self) -> bool:
        """Load static map and keepout mask from PGM files.

        Returns True if at least the static map was loaded successfully.
        The keepout mask is optional — missing it is only a warning.
        """
        self.static_map = self._load_pgm(ROOM_PGM)
        if self.static_map is not None:
            log.info("Static map loaded: %s", self.static_map.shape)
        else:
            log.warning("Static map not found at %s", ROOM_PGM)
            return False

        self.keepout_map = self._load_pgm(KEEPOUT_PGM)
        if self.keepout_map is not None:
            log.info("Keepout mask loaded: %s", self.keepout_map.shape)
        else:
            log.warning("Keepout mask not found at %s", KEEPOUT_PGM)

        self._loaded = True
        return True

    @staticmethod
    def _load_pgm(path: Path) -> Optional[np.ndarray]:
        """Load a PGM P5 (raw/binary) file.

        Returns a numpy uint8 array (HxW) or None if the file cannot be read.

        Handles comments (lines starting with ``#``) and the optional
        fourth header token (maxval) per the PGM spec.
        """
        if not path.is_file():
            log.warning("PGM file not found: %s", path)
            return None

        try:
            with open(path, 'rb') as fh:
                # --- read header tokens (handling comments) ---
                tokens: list = []
                while len(tokens) < 4:
                    raw_line: bytes = fh.readline()
                    if raw_line == b'':
                        raise ValueError("Unexpected EOF in PGM header")
                    line: str = raw_line.decode('ascii').strip()
                    if line == '' or line.startswith('#'):
                        continue
                    tokens.extend(line.split())
                    if len(tokens) >= 4:
                        break

                magic = tokens[0]
                width = int(tokens[1])
                height = int(tokens[2])
                maxval = int(tokens[3])

                if magic not in ('P5', 'P2'):
                    raise ValueError(
                        f"Unsupported PGM magic: {magic} (expected P5 or P2)")

                # --- read binary raster ---
                n_pixels = width * height
                if magic == 'P5':
                    payload = fh.read(n_pixels)
                    if len(payload) < n_pixels:
                        raise ValueError(
                            f"Truncated PGM data: expected {n_pixels} bytes, "
                            f"got {len(payload)}")
                    data = np.frombuffer(payload[:n_pixels], dtype=np.uint8)
                else:
                    # P2 (ASCII) — robust fallback
                    rest = fh.read().decode('ascii')
                    vals = rest.split()
                    vals = [v for v in vals if v.strip() != '']
                    if len(vals) < n_pixels:
                        raise ValueError(
                            f"Truncated PGM ASCII data: expected {n_pixels} "
                            f"values, got {len(vals)}")
                    data = np.array(vals[:n_pixels], dtype=np.uint8)

                # Handle 16-bit (maxval > 255) by scaling down
                if maxval > 255:
                    data = (data.astype(np.float32) * 255.0 / maxval).astype(np.uint8)

                return data.reshape((height, width))

        except Exception:
            log.exception("Failed to load PGM: %s", path)
            return None

    # ------------------------------------------------------------------
    # Costmap generation
    # ------------------------------------------------------------------

    def generate(self, params: Dict[str, float], with_keepout: bool = False) -> CostmapData:
        """Generate an inflated costmap from the given Nav2 parameters.

        Parameters
        ----------
        params : dict
        with_keepout : bool
            If True, overlay keepout zones (default False — competition disables
            keepout during cruise/return, so evaluating without is more realistic).

        Pipeline
        --------
        1. Start with static map (room walls = 254).
        2. (Optional) Overlay keepout zones.
        3. Apply Nav2-compatible inflation.

        Returns
        -------
        CostmapData
        """
        if not self._loaded or self.static_map is None:
            raise RuntimeError(
                "Maps not loaded. Call load_maps() before generate().")

        # 1. Start from the static (wall) map
        costmap = self.static_map.copy()

        # 2. Overlay keepout zones (only if explicitly requested) as soft,
        #    traversable high-cost cells. Walls in static_map remain lethal.
        if with_keepout and self.keepout_map is not None:
            keepout_mask = (self.keepout_map == LETHAL)
            costmap[keepout_mask] = KEEPOUT_COST

        # 3. Resolve parameters — try local first, fall back to global
        infl_radius = params.get('planner.inflation_radius.local')
        if infl_radius is None:
            infl_radius = params.get('planner.inflation_radius.global', 0.55)

        cost_factor = params.get('planner.cost_scaling_factor.local')
        if cost_factor is None:
            cost_factor = params.get('planner.cost_scaling_factor.global', 5.0)

        # 4. Inflate
        inflated = self._inflate(costmap, infl_radius, cost_factor)

        # Preserve keepout-only mask for A* incursion tracking
        # Cells that are keepout (in keepout_map) but NOT walls (in static_map)
        keepout_bool = None
        if self.keepout_map is not None:
            keepout_bool = (self.keepout_map == LETHAL) & (self.static_map < 250)

        return CostmapData(
            grid=inflated,
            width=costmap.shape[1],
            height=costmap.shape[0],
            resolution=RESOLUTION,
            origin_x=ORIGIN_X,
            origin_y=ORIGIN_Y,
            inflation_radius=infl_radius,
            cost_scaling_factor=cost_factor,
            keepout_mask=keepout_bool,
        )

    def generate_with_obstacles(
        self, params: Dict[str, float], n_obstacles: int = None,
        seed: Optional[int] = None, scenario: str = 'scatter',
        obstacle_density: float = 0.05,
        max_retries: int = None,
    ) -> CostmapData:
        """Generate costmap with random synthetic obstacles.

        Obstacles are placed only in physical free space (not walls, not
        keepout zones) and the resulting map is checked for reachability
        along the competition course. If a random layout blocks the course,
        it is regenerated up to ``max_retries`` times.

        Parameters
        ----------
        params : dict
            Inflation parameters (inflation_radius + cost_scaling_factor).
        n_obstacles : int
            Number of obstacle blocks. Defaults to ``OBSTACLE_COUNT`` (5).
        seed : int or None
            Random seed. ``None`` uses a fresh random layout.
        scenario : str
            Currently only 'scatter' (truly random) and 'empty' are used.
        obstacle_density : float
            Ignored — kept for API compatibility.
        max_retries : int
            Defaults to ``OBSTACLE_PLACE_RETRIES``.

        Returns
        -------
        CostmapData
            Inflated costmap with synthetic obstacles.
        """
        from scipy.ndimage import distance_transform_edt

        if n_obstacles is None:
            n_obstacles = OBSTACLE_COUNT
        if max_retries is None:
            max_retries = OBSTACLE_PLACE_RETRIES

        if not self._loaded or self.static_map is None:
            raise RuntimeError(
                "Maps not loaded. Call load_maps() before generate_with_obstacles().")

        # Resolve inflation parameters once
        infl_radius = params.get('planner.inflation_radius.local')
        if infl_radius is None:
            infl_radius = params.get('planner.inflation_radius.global', 0.55)
        cost_factor = params.get('planner.cost_scaling_factor.local')
        if cost_factor is None:
            cost_factor = params.get('planner.cost_scaling_factor.global', 5.0)

        # Base masks
        wall_mask = (self.static_map == LETHAL)
        keepout_bool = None
        if self.keepout_map is not None:
            keepout_bool = (self.keepout_map == LETHAL) & (~wall_mask)

        # Distance from walls only (keepout is traversable)
        dist_to_wall = distance_transform_edt(~wall_mask)
        margin_px = max(1, int(round(OBSTACLE_SOFT_MARGIN / RESOLUTION)))

        # Candidate cells: free of walls, outside keepout, away from walls
        base_candidate = (~wall_mask) & (dist_to_wall >= margin_px)
        if keepout_bool is not None:
            base_candidate &= ~keepout_bool

        obstacle_sizes = [
            (1, 1, 0.40),
            (2, 2, 0.25),
            (1, 3, 0.20),
            (3, 1, 0.15),
        ]

        base_seed = seed
        if base_seed is None:
            base_seed = int((time.time() * 1000) % (2**31))

        best_costmap = None
        best_obstacle_pixels = []
        best_reachable = False

        for attempt in range(max_retries):
            current_seed = base_seed + attempt * 7919
            rng = np.random.RandomState(current_seed)

            costmap = self.static_map.copy()
            if keepout_bool is not None:
                costmap[keepout_bool] = KEEPOUT_COST

            obstacle_pixels = []
            if scenario != 'empty':
                self._place_random_obstacles(
                    costmap, base_candidate, rng, n_obstacles,
                    obstacle_sizes, obstacle_pixels
                )

            inflated = self._inflate(costmap, infl_radius, cost_factor)

            if self._course_reachable(inflated):
                best_costmap = costmap
                best_obstacle_pixels = obstacle_pixels
                best_reachable = True
                break

            # Keep the last attempt as fallback (will be penalised by scoring)
            best_costmap = costmap
            best_obstacle_pixels = obstacle_pixels

        if not best_reachable:
            log.warning(
                "Could not place a reachable obstacle layout after %d retries (seed=%s)",
                max_retries, base_seed)

        log.info("Obstacles: placed %d, reachable=%s (seed=%s, attempt=%d/%d)",
                 len(best_obstacle_pixels), best_reachable, base_seed,
                 attempt + 1, max_retries)

        # Final inflation on the chosen layout
        inflated = self._inflate(best_costmap, infl_radius, cost_factor)

        return CostmapData(
            grid=inflated,
            width=best_costmap.shape[1],
            height=best_costmap.shape[0],
            resolution=RESOLUTION,
            origin_x=ORIGIN_X,
            origin_y=ORIGIN_Y,
            inflation_radius=infl_radius,
            cost_scaling_factor=cost_factor,
            keepout_mask=keepout_bool,
            obstacle_pixels=best_obstacle_pixels,
        )

    # ═══════════════════════════════════════════════════════════
    # Obstacle Placement Strategies
    # ═══════════════════════════════════════════════════════════

    @staticmethod
    def _paint_obstacle(costmap, r, c, size_h, size_w, obstacle_pixels=None):
        """Paint an obstacle of given size at (r,c). Truncates at map edges.

        If ``obstacle_pixels`` is given, append every occupied cell as
        (col, row) for downstream visualisation.
        """
        H, W = costmap.shape
        for dr in range(size_h):
            for dc in range(size_w):
                rr, cc = r + dr, c + dc
                if 0 <= rr < H and 0 <= cc < W:
                    costmap[rr, cc] = LETHAL
                    if obstacle_pixels is not None:
                        obstacle_pixels.append((cc, rr))

    @staticmethod
    def _place_random_obstacles(costmap, candidate_mask, rng, n_obstacles,
                                obstacle_sizes, obstacle_pixels=None):
        """Place obstacles uniformly at random over the candidate mask."""
        rows, cols = np.where(candidate_mask)
        if len(rows) == 0:
            return 0

        sizes_list, probs = zip(*[(s[:2], s[2]) for s in obstacle_sizes])
        probs = np.array(probs) / sum(probs)

        n_place = 0
        for _ in range(n_obstacles):
            idx = rng.choice(len(rows))
            r, c = rows[idx], cols[idx]
            size_idx = rng.choice(len(sizes_list), p=probs)
            sh, sw = sizes_list[size_idx]
            CostmapGenerator._paint_obstacle(
                costmap, r, c, sh, sw, obstacle_pixels)
            n_place += 1
        return n_place

    def _course_reachable(self, grid: np.ndarray) -> bool:
        """Check that the competition waypoints are still connected.

        Uses BFS on the inflated grid with the same rule as the A* planner:
        cells with cost >= 250 are lethal, everything else is traversable.
        """
        waypoints = [P_POINT, QR_POINT, ENTRY_POINT, VLM_CCW, VLM_CW]
        for i in range(len(waypoints) - 1):
            if not self._bfs_reachable(grid, waypoints[i], waypoints[i + 1]):
                return False
        return True

    @staticmethod
    def _bfs_reachable(grid: np.ndarray, start_world, goal_world) -> bool:
        """8-connected BFS reachability on a uint8 grid (lethal >= 250)."""
        H, W = grid.shape
        sc, sr = CostmapGenerator.world_to_pixel(*start_world)
        gc, gr = CostmapGenerator.world_to_pixel(*goal_world)

        def clamp(r, c):
            return max(0, min(H - 1, r)), max(0, min(W - 1, c))

        sr, sc = clamp(sr, sc)
        gr, gc = clamp(gr, gc)

        if grid[sr, sc] >= 250 or grid[gr, gc] >= 250:
            return False

        if (sr, sc) == (gr, gc):
            return True

        visited = np.zeros((H, W), dtype=bool)
        visited[sr, sc] = True
        queue = deque([(sr, sc)])
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1),
                     (-1, -1), (-1, 1), (1, -1), (1, 1)]

        while queue:
            r, c = queue.popleft()
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                if 0 <= nr < H and 0 <= nc < W:
                    if not visited[nr, nc] and grid[nr, nc] < 250:
                        if nr == gr and nc == gc:
                            return True
                        visited[nr, nc] = True
                        queue.append((nr, nc))
        return False

    # ═══════════════════════════════════════════════════════════
    # Multi-scenario generation
    # ═══════════════════════════════════════════════════════════

    def generate_scenarios(self, params: Dict[str, float],
                           n_scenarios: int = 3,
                           base_seed: int = 42) -> List[CostmapData]:
        """Generate N diverse obstacle scenarios for multi-scenario scoring.

        Args:
          params: Inflation parameters.
          n_scenarios: Number of scenarios to generate.
          base_seed: Base seed (incremented per scenario).

        Returns list of CostmapData, one per scenario.
        """
        scenario_types = ['scatter', 'corridor_block', 'entry_clutter', 'empty']
        costmaps = []

        for i in range(n_scenarios):
            stype = scenario_types[i % len(scenario_types)]
            cm = self.generate_with_obstacles(
                params,
                n_obstacles=5,
                seed=base_seed + i * 100,
                scenario=stype,
            )
            costmaps.append(cm)

        log.info("Generated %d scenarios: %s",
                 n_scenarios,
                 ', '.join(scenario_types[:n_scenarios]))
        return costmaps

    @staticmethod
    def _inflate(
        costmap: np.ndarray,
        inflation_radius: float,
        cost_scaling_factor: float,
    ) -> np.ndarray:
        """Apply Nav2-compatible cost inflation to a costmap.

        Algorithm
        ---------
        1. Compute Euclidean distance transform from every lethal cell.
        2. Apply the Nav2 exponential decay formula::

               cost = LETHAL * exp(-cost_scaling_factor * (dist - inscribed) / inflation_radius)

        3. Cells within ``inscribed_radius`` of an obstacle are forced lethal.
        4. Costs are clamped to [0, 254] and cast to uint8.

        Uses ``scipy.ndimage.distance_transform_edt`` for the distance field.
        """
        lethal_mask = (costmap == LETHAL)

        # If nothing is lethal, return a free map
        if not lethal_mask.any():
            return np.zeros_like(costmap, dtype=np.uint8)

        # Euclidean distance from every pixel to the nearest non-lethal cell
        from scipy.ndimage import distance_transform_edt
        dist_px = distance_transform_edt(~lethal_mask)
        dist_m = dist_px * RESOLUTION  # px → meters

        # Nav2 inflation formula
        cost = LETHAL * np.exp(
            -1.0 * cost_scaling_factor * (dist_m - INSCRIBED_RADIUS) / inflation_radius
        )
        cost = np.clip(cost, 0, LETHAL).astype(np.uint8)

        # Lethal cells stay lethal (distance=0 gives cost=254*exp(positive) ≤ 254,
        # but clamp to be explicit)
        cost[lethal_mask] = LETHAL

        return cost

    # ------------------------------------------------------------------
    # Coordinate conversion
    # ------------------------------------------------------------------

    @staticmethod
    def world_to_pixel(wx: float, wy: float) -> Tuple[int, int]:
        """Convert world coordinates to pixel indices (col, row).

        Notes
        -----
        - PGM y axis increases downward (row 0 = top of image).
        - World y is negative for the upper part of the map.
        """
        col = int((wx - ORIGIN_X) / RESOLUTION)
        row = int((wy - ORIGIN_Y) / RESOLUTION)
        return col, row

    @staticmethod
    def pixel_to_world(col: int, row: int) -> Tuple[float, float]:
        """Convert pixel indices to world coordinates (x, y)."""
        wx = ORIGIN_X + col * RESOLUTION
        wy = ORIGIN_Y + row * RESOLUTION
        return wx, wy

    # ------------------------------------------------------------------
    # Convenience
    # ------------------------------------------------------------------

    @property
    def maps_available(self) -> bool:
        """True if the static map is loaded and ready for generation."""
        return self._loaded and self.static_map is not None
