"""
A* grid planner — Numba-JIT accelerated.

Primary: Numba A* (~0.01ms on 163x141 grid)
Fallback: Pure Python A* (~7ms)
"""
import logging
import time
import heapq
import numpy as np
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

from .costmap_generator import (CostmapData, CostmapGenerator,
                                P_POINT, VLM_CCW, VLM_CW, ENTRY_POINT,
                                RESOLUTION, LETHAL, FREE)

log = logging.getLogger('Nav2Tuner.AStar')

# Try Numba
try:
    from numba import njit
    _HAS_NUMBA = True
except ImportError:
    _HAS_NUMBA = False

MAX_ITERATIONS = 15000
SQRT2 = 1.414

NEIGHBORS = [
    (-1, 0, 1.0), (1, 0, 1.0), (0, -1, 1.0), (0, 1, 1.0),
    (-1, -1, SQRT2), (-1, 1, SQRT2), (1, -1, SQRT2), (1, 1, SQRT2),
]


@dataclass
class PathResult:
    path: List[Tuple[int, int]] = field(default_factory=list)
    world_path: List[Tuple[float, float]] = field(default_factory=list)
    path_len: float = 0.0
    curvature_mean: float = 0.0
    curvature_std: float = 0.0
    clearance_min: float = 999.0
    clearance_mean: float = 0.0
    cusp_count: int = 0
    in_lethal_count: int = 0
    total_cost: float = 0.0
    reachable: bool = False
    planning_time_ms: float = 0.0
    n_expanded: int = 0
    # Keepout behavior fields (Phase 3)
    keepout_incursion_count: int = 0
    keepout_cost: float = 0.0
    in_narrow_corridor_keepout: bool = False


# ═══════════════════════════════════════════════════════════
# Numba-JIT accelerated A* (if available)
# ═══════════════════════════════════════════════════════════

if _HAS_NUMBA:
    @njit
    def _astar_numba(grid, start_r, start_c, goal_r, goal_c):
        """Numba-JIT A* on uint8 2D grid.
        Returns (path_len_m, expanded, reachable, parent_r, parent_c, final_r, final_c,
                 start_r, start_c) for full path reconstruction.
        """
        H, W = grid.shape
        INF = np.int32(1000000000)
        g_cost = np.full((H, W), INF, dtype=np.int32)
        parent_r = np.full((H, W), -1, dtype=np.int32)
        parent_c = np.full((H, W), -1, dtype=np.int32)
        closed = np.zeros((H, W), dtype=np.bool_)
        g_cost[start_r, start_c] = 0

        open_set = np.zeros((MAX_ITERATIONS, 3), dtype=np.int32)
        open_size = 1
        open_set[0, 1] = start_r
        open_set[0, 2] = start_c
        expanded = 0
        final_r, final_c = start_r, start_c

        dr = np.array([-1, 1, 0, 0, -1, -1, 1, 1], dtype=np.int32)
        dc = np.array([0, 0, -1, 1, -1, 1, -1, 1], dtype=np.int32)
        mc = np.array([1.0, 1.0, 1.0, 1.0, SQRT2, SQRT2, SQRT2, SQRT2], dtype=np.float32)

        while open_size > 0 and expanded < MAX_ITERATIONS:
            bi, bf = 0, open_set[0, 0]
            for i in range(1, open_size):
                if open_set[i, 0] < bf:
                    bi, bf = i, open_set[i, 0]
            cr, cc = open_set[bi, 1], open_set[bi, 2]
            open_set[bi] = open_set[open_size - 1]
            open_size -= 1
            expanded += 1
            if closed[cr, cc]:
                continue
            closed[cr, cc] = True
            final_r, final_c = cr, cc

            if max(abs(cr - goal_r), abs(cc - goal_c)) <= 3:
                pl = 0.0
                r, c = cr, cc
                while r != start_r or c != start_c:
                    pr, pc = parent_r[r, c], parent_c[r, c]
                    if pr < 0:
                        break
                    step = abs(r - pr) + abs(c - pc)
                    pl += (1.0 if step == 1 else SQRT2) * RESOLUTION
                    r, c = pr, pc
                return (np.float32(pl), np.int32(expanded), np.bool_(True),
                        parent_r, parent_c, np.int32(final_r), np.int32(final_c),
                        np.int32(start_r), np.int32(start_c))

            cg = g_cost[cr, cc]
            for i in range(8):
                nr, nc = cr + dr[i], cc + dc[i]
                if nr < 0 or nr >= H or nc < 0 or nc >= W or closed[nr, nc]:
                    continue
                cc_val = grid[nr, nc]
                if cc_val >= 250:
                    continue
                ng = cg + mc[i] * (1.0 + 0.08 * cc_val / 254.0)
                if ng < g_cost[nr, nc]:
                    g_cost[nr, nc] = ng
                    parent_r[nr, nc] = cr
                    parent_c[nr, nc] = cc
                    h = (abs(nr - goal_r) + abs(nc - goal_c) +
                         (SQRT2 - 1.0) * min(abs(nr - goal_r), abs(nc - goal_c)))
                    open_set[open_size, 0] = np.int32(ng * 1000 + h * 1000)
                    open_set[open_size, 1] = nr
                    open_set[open_size, 2] = nc
                    open_size += 1

        return (np.float32(0.0), np.int32(expanded), np.bool_(False),
                parent_r, parent_c, np.int32(final_r), np.int32(final_c),
                np.int32(start_r), np.int32(start_c))


class AstarPlanner:
    """A* grid planner with Numba acceleration if available."""

    def __init__(self):
        self._grid = None
        self._dist_to_obstacle = None
        self._n_expanded = 0
        self._use_numba = _HAS_NUMBA

    def plan_path(self, costmap, waypoints):
        """Plan multi-segment path through competition waypoints.

        Args:
            costmap: CostmapData for A* search.
            waypoints: List of (x, y) world coordinates.

        Returns:
            PathResult with concatenated path through all waypoints.
        """
        import numpy as np

        all_pixels = []
        total_len = 0.0
        total_time = 0.0
        all_reachable = True
        min_clearance = float('inf')
        curvatures = []
        total_cusp = 0
        total_lethal = 0
        total_cost = 0.0
        all_expanded = 0

        for i in range(len(waypoints) - 1):
            start_wp = waypoints[i]
            goal_wp = waypoints[i + 1]

            result = self.plan(costmap, start_world=start_wp, goal_world=goal_wp)
            total_time += result.planning_time_ms
            all_expanded += result.n_expanded

            if not result.reachable:
                all_reachable = False
                break

            if result.path:
                # Skip duplicate first pixel of each segment (except first segment)
                if all_pixels:
                    result.path = result.path[1:]
                all_pixels.extend(result.path)

            total_len += result.path_len
            min_clearance = min(min_clearance, result.clearance_min)
            curvatures.append(result.curvature_mean)
            total_cusp += result.cusp_count
            total_lethal += result.in_lethal_count
            total_cost += result.total_cost

        if not all_reachable:
            return PathResult(reachable=False, planning_time_ms=total_time)

        avg_curvature = float(np.mean(curvatures)) if curvatures else 0.0
        return PathResult(
            reachable=True,
            path=all_pixels,
            path_len=total_len,
            curvature_mean=avg_curvature,
            clearance_min=min_clearance if min_clearance != float('inf') else 0.5,
            cusp_count=total_cusp,
            in_lethal_count=total_lethal,
            total_cost=total_cost,
            planning_time_ms=total_time,
            n_expanded=all_expanded,
        )

    def plan(self, costmap, start_world=P_POINT, goal_world=VLM_CCW):
        """Plan path and extract features. Uses Numba A* if available."""
        t0 = time.perf_counter()
        self._grid = costmap.grid

        sr, sc = self._world_to_pixel(*start_world)
        gr, gc = self._world_to_pixel(*goal_world)

        # Find nearest free
        sr, sc = self._nearest_free(sr, sc) or (sr, sc)
        gr, gc = self._nearest_free(gr, gc) or (gr, gc)

        if self._use_numba:
            result = _astar_numba(
                self._grid, int(sr), int(sc), int(gr), int(gc))
            # Unpack: 10 values returned
            path_len, expanded = result[0], result[1]
            reachable = result[2]
            self._n_expanded = int(expanded)
            dt_ms = (time.perf_counter() - t0) * 1000

            if not reachable:
                return PathResult(reachable=False, planning_time_ms=dt_ms)

            # Reconstruct full pixel path from parent arrays
            parent_r, parent_c = result[3], result[4]
            final_r, final_c = int(result[5]), int(result[6])
            start_r_i, start_c_i = int(result[7]), int(result[8])
            path_px = self._reconstruct_path_numba(
                parent_r, parent_c, final_r, final_c, start_r_i, start_c_i)
            return self._extract_features_py(path_px, dt_ms, keepout_data=costmap)
        else:
            # Python fallback
            path_px = self._astar_search((int(sr), int(sc)), (int(gr), int(gc)))
            dt_ms = (time.perf_counter() - t0) * 1000
            if path_px is None:
                return PathResult(reachable=False, planning_time_ms=dt_ms)
            return self._extract_features_py(path_px, dt_ms, keepout_data=costmap)

    @staticmethod
    def _reconstruct_path_numba(parent_r, parent_c, final_r, final_c,
                                start_r, start_c):
        """Reconstruct pixel path from Numba A* parent arrays.
        Returns list of (row, col) tuples from start to goal.
        """
        path = []
        r, c = final_r, final_c
        max_steps = parent_r.shape[0] * parent_r.shape[1]  # safety limit
        steps = 0
        while (r != start_r or c != start_c) and steps < max_steps:
            path.append((int(r), int(c)))
            pr, pc = int(parent_r[r, c]), int(parent_c[r, c])
            if pr < 0 or pc < 0:
                break
            r, c = pr, pc
            steps += 1
        path.append((int(start_r), int(start_c)))
        path.reverse()
        return path

    # ══════════════════════════════════════════════════════
    # Python A* (fallback)
    # ══════════════════════════════════════════════════════

    def _astar_search(self, start, goal):
        H, W = self._grid.shape
        sr, sc = start; gr, gc = goal
        g_cost = {(sr, sc): 0.0}
        parent = {(sr, sc): None}
        closed = set()
        n_expanded = 0; tiebreaker = 1
        h0 = max(abs(sr-gr), abs(sc-gc)) + (SQRT2-1.0)*min(abs(sr-gr), abs(sc-gc))
        open_set = [(h0, 0, (sr, sc))]
        while open_set and n_expanded < MAX_ITERATIONS:
            _, _, cur = heapq.heappop(open_set)
            cr, cc = cur; n_expanded += 1
            if max(abs(cr-gr), abs(cc-gc)) <= 3:
                self._n_expanded = n_expanded
                return self._reconstruct_path(parent, cur)
            if cur in closed: continue
            closed.add(cur)
            cg = g_cost.get(cur, float('inf'))
            for dr, dc, mc in NEIGHBORS:
                nr, nc = cr+dr, cc+dc
                nb = (nr, nc)
                if nb in closed or nr<0 or nr>=H or nc<0 or nc>=W: continue
                cv = float(self._grid[nr, nc])
                if cv >= 250: continue
                ng = cg + mc * (1.0 + 0.08*cv/254.0)
                if ng < g_cost.get(nb, float('inf')):
                    g_cost[nb] = ng; parent[nb] = cur
                    h = max(abs(nr-gr), abs(nc-gc)) + (SQRT2-1.0)*min(abs(nr-gr), abs(nc-gc))
                    heapq.heappush(open_set, (ng+h, tiebreaker, nb)); tiebreaker += 1
        self._n_expanded = n_expanded
        return None

    @staticmethod
    def _reconstruct_path(parent, node):
        path = []
        while node is not None:
            path.append(node); node = parent.get(node)
        path.reverse()
        return path

    def _extract_features_py(self, path_px, dt_ms, keepout_data=None):
        result = PathResult(path=path_px, planning_time_ms=dt_ms,
                            n_expanded=self._n_expanded, reachable=True)
        if len(path_px) < 2: return result
        world = [self._pixel_to_world(r,c) for r,c in path_px]
        result.world_path = world
        xs=np.array([w[0] for w in world]); ys=np.array([w[1] for w in world])
        seg=np.hypot(np.diff(xs), np.diff(ys)); result.path_len=float(np.sum(seg))
        yaws=np.arctan2(np.diff(ys), np.diff(xs))
        if len(yaws)>=2:
            dyaw=np.abs(np.diff(yaws)); dyaw=np.minimum(dyaw, 2*np.pi-dyaw)
            result.curvature_mean=float(np.mean(dyaw/(seg[1:]+0.001)))
            result.curvature_std=float(np.std(dyaw/(seg[1:]+0.001)))
        if len(path_px)>=3:
            dx=np.diff(xs); result.cusp_count=int(np.sum((dx[:-1]*dx[1:])<-0.001))
        self._precompute_clearance()
        clearances=[]; lc=0; tc=0.0; kc=0; kcost=0.0
        for r,c in path_px:
            cv=float(self._grid[r,c]); tc+=cv
            if cv>=254: lc+=1
            # Keepout incursion: check if this cell is keepout (not just wall)
            if keepout_data is not None and hasattr(keepout_data, 'keepout_mask'):
                km = keepout_data.keepout_mask
                if km is not None and 0 <= r < km.shape[0] and 0 <= c < km.shape[1]:
                    if km[r, c] >= 250:
                        kc += 1
                        kcost += cv
            if self._dist_to_obstacle is not None: clearances.append(self._dist_to_obstacle[r,c]*RESOLUTION)
        result.in_lethal_count=lc; result.total_cost=tc/max(len(path_px),1)
        result.keepout_incursion_count = kc
        result.keepout_cost = kcost / max(len(path_px), 1)
        if clearances: result.clearance_min=float(np.min(clearances)); result.clearance_mean=float(np.mean(clearances))
        return result

    def _nearest_free(self, sr, sc, max_radius=25):
        H, W = self._grid.shape
        if 0<=sr<H and 0<=sc<W and self._grid[sr,sc]<200: return (int(sr), int(sc))
        for r in range(1, max_radius+1):
            for dr in range(-r, r+1):
                for dc in range(-r, r+1):
                    if max(abs(dr),abs(dc))!=r: continue
                    nr,nc=sr+dr,sc+dc
                    if 0<=nr<H and 0<=nc<W and self._grid[nr,nc]<200: return (int(nr), int(nc))
        return None

    def _precompute_clearance(self):
        try:
            from scipy.ndimage import distance_transform_edt
            lm = (self._grid >= 250)
            self._dist_to_obstacle = distance_transform_edt(~lm) if lm.any() else np.full(self._grid.shape, 999.0)
        except ImportError:
            self._dist_to_obstacle = None

    def _pixel_to_world(self, row, col):
        return CostmapGenerator.pixel_to_world(col, row)

    def _world_to_pixel(self, wx, wy):
        col, row = CostmapGenerator.world_to_pixel(wx, wy)
        return int(row), int(col)

    @staticmethod
    def render_path(costmap_data, path_result, output_path, title="Best Path"):
        """Render A* path on room map + keepout — same style as plot_trajectory.py.

        Uses real PGM map files as background, keepout overlay in red,
        path in green, with world coordinates on axes.
        """
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        from pathlib import Path
        import yaml

        # Map paths
        map_dir = Path(__file__).parent.parent / "originbot_navigation" / "maps"
        room_pgm = map_dir / "room.pgm"
        keepout_pgm = map_dir / "keepout_mask.pgm"
        room_yaml = map_dir / "room.yaml"

        # Load maps
        try:
            room_img = AstarPlanner._read_pgm(str(room_pgm)).astype(float)
            kp_img = AstarPlanner._read_pgm(str(keepout_pgm)).astype(float)
            with open(room_yaml) as f:
                yd = yaml.safe_load(f)
            res = float(yd['resolution'])
            ox = float(yd['origin'][0])
            oy = float(yd['origin'][1])
            h, w = room_img.shape
        except Exception:
            # Fallback: use costmap grid directly
            room_img = costmap_data.grid.astype(float)
            kp_img = None
            h, w = room_img.shape
            res = costmap_data.resolution
            ox = costmap_data.origin_x
            oy = costmap_data.origin_y

        extent = [ox, ox + w * res, oy, oy + h * res]

        fig, ax = plt.subplots(figsize=(12, 10))

        # Room background: same thresholding as plot_trajectory.py
        room_viz = np.where(room_img <= 25, 1.0,
                   np.where(room_img >= 65, 0.0, 0.5))
        ax.imshow(np.flipud(room_viz), extent=extent, cmap='gray', origin='lower',
                  alpha=0.45, vmin=0, vmax=1)

        # Keepout overlay in red
        if kp_img is not None:
            kp_viz = np.where(kp_img >= 128, 1.0, np.nan)
            ax.imshow(np.flipud(kp_viz), extent=extent, cmap='Reds', origin='lower',
                      alpha=0.35, vmin=0, vmax=1)

        # Path in green
        if path_result.world_path:
            xs = [p[0] for p in path_result.world_path]
            ys = [p[1] for p in path_result.world_path]
            if len(xs) > 1:
                ax.plot(xs, ys, '-', color='#00ff00', linewidth=2.5, zorder=5,
                        label='Planned path')

        # Start / Goal markers
        if path_result.world_path:
            sx, sy = path_result.world_path[0]
            ax.plot(sx, sy, 'o', color='lime', markersize=10,
                    markeredgecolor='black', zorder=6, label=f'Start ({sx:.2f},{sy:.2f})')
            gx, gy = path_result.world_path[-1]
            ax.plot(gx, gy, 's', color='red', markersize=10,
                    markeredgecolor='black', zorder=6, label=f'Goal ({gx:.2f},{gy:.2f})')

        # Waypoints
        for name, kx, ky in [('QR', 0.41, -3.17), ('Entry', 0.38, -1.10),
                              ('P', -1.99, -0.01)]:
            ax.plot(kx, ky, '*', markersize=14, markeredgecolor='black',
                    markerfacecolor='yellow', zorder=7)
            ax.annotate(name, (kx, ky), textcoords="offset points",
                        xytext=(8, -12), fontsize=10, weight='bold')

        ax.set_xlabel('X (m)')
        ax.set_ylabel('Y (m)')
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.25)
        ax.set_xlim(ox, ox + w * res)
        ax.set_ylim(oy, oy + h * res)
        ax.set_title(title, fontsize=10)
        ax.legend(loc='lower left', fontsize=7)

        fig.tight_layout()
        fig.savefig(str(output_path), dpi=150)
        plt.close(fig)

    @staticmethod
    def render_csv_trajectory(csv_path, output_path, title="Best Run",
                              obstacle_pixels=None):
        """Render actual robot trajectory from CSV on the map — same style as plot_trajectory.py.

        Args:
          csv_path: path to trajectory CSV
          output_path: where to save PNG
          title: plot title
          obstacle_pixels: optional list of (col, row) obstacle positions to highlight
        """
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        from pathlib import Path
        import csv, yaml

        map_dir = Path(__file__).parent.parent / "originbot_navigation" / "maps"
        room_img = AstarPlanner._read_pgm(str(map_dir / "room.pgm")).astype(float)
        kp_img = AstarPlanner._read_pgm(str(map_dir / "keepout_mask.pgm")).astype(float)
        with open(map_dir / "room.yaml") as f:
            yd = yaml.safe_load(f)
        res = float(yd['resolution']); ox = float(yd['origin'][0]); oy = float(yd['origin'][1])
        h, w = room_img.shape
        extent = [ox, ox + w * res, oy, oy + h * res]

        # Parse CSV
        xs, ys = [], []
        with open(csv_path, newline='') as f:
            for row in csv.DictReader(f):
                xs.append(float(row['x_m']))
                ys.append(float(row['y_m']))

        fig, ax = plt.subplots(figsize=(12, 10))

        # Room background
        room_viz = np.where(room_img <= 25, 1.0, np.where(room_img >= 65, 0.0, 0.5))
        ax.imshow(np.flipud(room_viz), extent=extent, cmap='gray', origin='lower', alpha=0.45)
        # Keepout
        kp_viz = np.where(kp_img >= 128, 1.0, np.nan)
        ax.imshow(np.flipud(kp_viz), extent=extent, cmap='Reds', origin='lower', alpha=0.35)

        # ★ Synthetic obstacles (if provided)
        if obstacle_pixels:
            obs_xs, obs_ys = [], []
            for col, row in obstacle_pixels:
                wx, wy = CostmapGenerator.pixel_to_world(col, row)
                obs_xs.append(wx); obs_ys.append(wy)
            ax.scatter(obs_xs, obs_ys, marker='s', s=80, color='orange',
                      edgecolor='black', linewidth=1.5, zorder=8, label='Obstacles')

        # Trajectory
        if len(xs) > 1:
            ax.plot(xs, ys, '-', color='#00ff00', linewidth=2.5, zorder=5)
            ax.plot(xs[0], ys[0], 'o', color='lime', markersize=10, markeredgecolor='black', zorder=6)
            ax.plot(xs[-1], ys[-1], 's', color='red', markersize=10, markeredgecolor='black', zorder=6)

        # Waypoints
        for name, kx, ky in [('QR',0.41,-3.17),('Entry',0.38,-1.10),('P',-1.99,-0.01)]:
            ax.plot(kx, ky, '*', markersize=14, markeredgecolor='black', markerfacecolor='yellow', zorder=7)
            ax.annotate(name, (kx, ky), textcoords="offset points", xytext=(8,-12), fontsize=10, weight='bold')

        ax.set_xlabel('X (m)'); ax.set_ylabel('Y (m)')
        ax.set_aspect('equal'); ax.grid(True, alpha=0.25)
        ax.set_xlim(ox, ox + w * res); ax.set_ylim(oy, oy + h * res)
        ax.set_title(f"{title} — {Path(csv_path).name} ({len(xs)} pts)", fontsize=10)
        if obstacle_pixels:
            ax.legend(loc='lower left', fontsize=7)

        fig.tight_layout()
        fig.savefig(str(output_path), dpi=150)
        plt.close(fig)

    @staticmethod
    def render_multi_path(costmap_data, path_results, output_path,
                          labels=None, title="Top Parameter Paths"):
        """Render multiple A* paths on the same costmap for comparison.

        Args:
          costmap_data: CostmapData with grid metadata.
          path_results: List of (PathResult, label, color) tuples.
          output_path: Where to save PNG.
          labels: Optional list of labels.
          title: Plot title.
        """
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        from pathlib import Path
        import yaml

        map_dir = Path(__file__).parent.parent / "originbot_navigation" / "maps"
        room_pgm = map_dir / "room.pgm"
        keepout_pgm = map_dir / "keepout_mask.pgm"
        room_yaml = map_dir / "room.yaml"

        try:
            room_img = AstarPlanner._read_pgm(str(room_pgm)).astype(float)
            kp_img = AstarPlanner._read_pgm(str(keepout_pgm)).astype(float)
            with open(room_yaml) as f:
                yd = yaml.safe_load(f)
            res = float(yd['resolution'])
            ox = float(yd['origin'][0])
            oy = float(yd['origin'][1])
            h, w = room_img.shape
        except Exception:
            room_img = costmap_data.grid.astype(float)
            kp_img = None
            h, w = room_img.shape
            res = costmap_data.resolution
            ox = costmap_data.origin_x
            oy = costmap_data.origin_y

        extent = [ox, ox + w * res, oy, oy + h * res]

        fig, ax = plt.subplots(figsize=(14, 11))

        # Room background
        room_viz = np.where(room_img <= 25, 1.0,
                   np.where(room_img >= 65, 0.0, 0.5))
        ax.imshow(np.flipud(room_viz), extent=extent, cmap='gray', origin='lower',
                  alpha=0.45, vmin=0, vmax=1)

        # Keepout overlay in red
        if kp_img is not None:
            kp_viz = np.where(kp_img >= 128, 1.0, np.nan)
            ax.imshow(np.flipud(kp_viz), extent=extent, cmap='Reds', origin='lower',
                      alpha=0.35, vmin=0, vmax=1)

        # Paths in different colors
        colors = ['#00ff00', '#00aaff', '#ff8800', '#ff00ff', '#ffff00']
        if labels is None:
            labels = [f"Path {i+1}" for i in range(len(path_results))]

        for i, item in enumerate(path_results):
            if len(item) == 3:
                result, label, color = item
            else:
                result, label = item
                color = colors[i % len(colors)]

            if not result.world_path or len(result.world_path) < 2:
                continue
            xs = [p[0] for p in result.world_path]
            ys = [p[1] for p in result.world_path]
            ax.plot(xs, ys, '-', color=color, linewidth=2.0, zorder=5,
                    label=f"{label} (len={result.path_len:.1f}m)")

            # Start/Goal markers
            ax.plot(xs[0], ys[0], 'o', color=color, markersize=8,
                    markeredgecolor='black', zorder=6)
            ax.plot(xs[-1], ys[-1], 's', color=color, markersize=8,
                    markeredgecolor='black', zorder=6)

        # Waypoints
        for name, kx, ky in [('QR',0.41,-3.17),('Entry',0.38,-1.10),('P',-1.99,-0.01)]:
            ax.plot(kx, ky, '*', markersize=14, markeredgecolor='black',
                    markerfacecolor='yellow', zorder=7)
            ax.annotate(name, (kx, ky), textcoords="offset points",
                        xytext=(8,-12), fontsize=10, weight='bold')

        ax.set_xlabel('X (m)')
        ax.set_ylabel('Y (m)')
        ax.set_aspect('equal')
        ax.grid(True, alpha=0.25)
        ax.set_xlim(ox, ox + w * res)
        ax.set_ylim(oy, oy + h * res)
        ax.set_title(title, fontsize=12)
        ax.legend(loc='lower left', fontsize=8)

        fig.tight_layout()
        fig.savefig(str(output_path), dpi=150)
        plt.close(fig)

    @staticmethod
    def _read_pgm(path):
        """Read PGM P5 binary file. Returns numpy array."""
        with open(path, 'rb') as f:
            assert f.readline().strip() == b'P5'
            w, h = map(int, f.readline().split())
            maxval = int(f.readline().strip())
            data = np.frombuffer(f.read(), dtype=np.uint8 if maxval < 256 else np.uint16)
            return data.reshape(h, w)
