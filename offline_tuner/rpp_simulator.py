"""
RPP Simulator — Python clone of Nav2's Regulated Pure Pursuit controller.

Algorithm from Nav2 Humble source:
  nav2_regulated_pure_pursuit_controller/src/regulated_pure_pursuit_controller.cpp
  include/nav2_regulated_pure_pursuit_controller/regulation_functions.hpp

Simulates the RPP control loop on a given path + costmap at 10Hz,
producing estimated time-to-goal and tracking quality metrics.

Usage:
  sim = RPPSimulator(costmap, global_path_pixels)
  metrics = sim.run(params_dict)
  print(f"Estimated time: {metrics.ttg:.1f}s, score: {metrics.composite_score():.3f}")
"""

import math
import time
import numpy as np
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, field


@dataclass
class RPPMetrics:
    """Output of a single RPP simulation run."""
    ttg: float = 0.0               # time-to-goal (seconds)
    path_len: float = 0.0           # total path length (meters)
    traversed_len: float = 0.0      # actual distance traversed
    mean_speed: float = 0.0         # average linear velocity
    max_speed: float = 0.0          # peak velocity
    stop_time: float = 0.0          # total time spent stopped (<0.01 m/s)
    mean_track_error: float = 0.0   # mean cross-track error (meters)
    max_track_error: float = 0.0    # max cross-track error
    jerk_lin: float = 0.0           # integrated linear jerk (m/s³)
    jerk_ang: float = 0.0           # integrated angular jerk (rad/s³)
    n_cusps: int = 0                # direction reversals
    n_lethal_cross: int = 0         # times robot entered lethal zone
    reached_goal: bool = False      # did the simulation finish?
    velocity_profile: List[float] = field(default_factory=list)
    pose_trace: List[Tuple[float, float, float]] = field(default_factory=list)

    def composite_score(self) -> float:
        """Normalized quality score (lower=better, 0-1 range)."""
        if self.ttg <= 0:
            return 1.0
        return (
            0.35 * min(self.ttg / 100.0, 1.0) +
            0.20 * min(self.stop_time / max(self.ttg, 0.1), 1.0) +
            0.15 * min(self.mean_track_error / 0.5, 1.0) +
            0.10 * min(self.jerk_lin / 5.0, 1.0) +
            0.10 * min(self.jerk_ang / 10.0, 1.0) +
            0.05 * min(self.n_lethal_cross / 5.0, 1.0) +
            0.05 * min(self.n_cusps / 10.0, 1.0)
        )


class RPPSimulator:
    """Offline RPP controller simulator for parameter evaluation.

    Replicates the Nav2 RPP algorithm without ROS2 runtime.
    Assumes Ackermann steering with allow_reversing=true.
    """

    def __init__(self, costmap: np.ndarray, path_pixels: List[Tuple[int, int]],
                 resolution: float = 0.05, origin: Tuple[float, float] = (-2.65, -4.5),
                 controller_frequency: float = 10.0, max_time: float = 180.0):
        """
        Args:
            costmap: HxW uint8 Nav2 costmap (0=free, 254=lethal, 255=unknown).
            path_pixels: Global path as [(r, c), ...] pixel coordinates.
            resolution: Meters per pixel.
            origin: World (x, y) at pixel (0, 0).
            controller_frequency: RPP update rate in Hz.
            max_time: Simulation timeout in seconds.
        """
        self.costmap = costmap
        self.H, self.W = costmap.shape
        self.resolution = resolution
        self.origin_x, self.origin_y = origin
        self.dt = 1.0 / controller_frequency
        self.max_time = min(max_time, 30.0)  # cap sim time for tuner performance

        # Convert pixel path to world coordinates [(x, y), ...]
        self.world_path = [(c * resolution + origin[0],
                            (self.H - 1 - r) * resolution + origin[1])
                           for r, c in path_pixels]
        self.n_pts = len(self.world_path)

        # Precompute path arc-lengths from start
        self._path_dists = [0.0]
        for i in range(1, self.n_pts):
            dx = self.world_path[i][0] - self.world_path[i-1][0]
            dy = self.world_path[i][1] - self.world_path[i-1][1]
            self._path_dists.append(self._path_dists[-1] + math.hypot(dx, dy))
        self.total_path_len = self._path_dists[-1]

    # ═══════════════════════════════════════════════════════════════
    # Public API
    # ═══════════════════════════════════════════════════════════════

    def run(self, params: Dict[str, float]) -> RPPMetrics:
        """Run RPP simulation with given controller parameters.

        Args:
            params: Flat dict with keys like 'controller.desired_linear_vel'.

        Returns:
            RPPMetrics with TTG, tracking error, etc.
        """
        p = self._resolve_params(params)
        metrics = RPPMetrics(path_len=self.total_path_len)

        # Start at first path point
        px, py = self.world_path[0]
        # Heading towards second point
        if self.n_pts > 1:
            pyaw = math.atan2(self.world_path[1][1] - py,
                              self.world_path[1][0] - px)
        else:
            pyaw = 0.0

        vx, wz = 0.0, 0.0  # current velocity
        closest_idx = 0
        t = 0.0
        prev_vx, prev_wz = 0.0, 0.0

        while t < self.max_time:
            # ── Find closest point on path ──
            closest_idx = self._closest_index(px, py, max(closest_idx - 3, 0))

            # ── Check goal reached ──
            remaining = self._remaining_distance(closest_idx, px, py)
            if remaining < p['xy_goal_tolerance']:
                metrics.reached_goal = True
                break

            # ── Compute RPP velocity command ──
            vx_cmd, wz_cmd = self._compute_rpp_command(
                px, py, pyaw, vx, wz, closest_idx, remaining, p)

            # ── Apply acceleration constraints ──
            vx = self._apply_accel_limit(vx, vx_cmd, p['max_linear_accel'],
                                         p['max_linear_decel'], self.dt)
            wz = self._apply_accel_limit(wz, wz_cmd, p['max_angular_accel'],
                                         p['max_angular_decel'], self.dt)

            # ── Check lethal zone ──
            if self._is_lethal(px, py):
                metrics.n_lethal_cross += 1

            # ── Move robot (Ackermann: simpler bicycle model) ──
            px += vx * math.cos(pyaw) * self.dt
            py += vx * math.sin(pyaw) * self.dt
            pyaw += wz * self.dt
            pyaw = math.atan2(math.sin(pyaw), math.cos(pyaw))  # normalize

            # ── Track cusp (sign change of vx) ──
            if prev_vx * vx < 0 and abs(vx) > 0.01:
                metrics.n_cusps += 1

            # ── Record metrics ──
            if abs(vx) < 0.01:
                metrics.stop_time += self.dt
            metrics.mean_speed += abs(vx) * self.dt
            metrics.max_speed = max(metrics.max_speed, abs(vx))
            metrics.traversed_len += abs(vx) * self.dt
            metrics.velocity_profile.append(vx)
            metrics.pose_trace.append((px, py, pyaw))

            # ── Track error ──
            track_err = self._cross_track_error(px, py, closest_idx)
            metrics.mean_track_error += track_err * self.dt
            metrics.max_track_error = max(metrics.max_track_error, track_err)

            # ── Jerk ──
            metrics.jerk_lin += abs(vx - prev_vx) / self.dt * self.dt
            metrics.jerk_ang += abs(wz - prev_wz) / self.dt * self.dt

            prev_vx, prev_wz = vx, wz
            t += self.dt

        metrics.ttg = t
        if metrics.ttg > 0:
            metrics.mean_speed /= metrics.ttg
            metrics.mean_track_error /= metrics.ttg

        return metrics

    # ═══════════════════════════════════════════════════════════════
    # RPP Core Algorithm (from Nav2 regulated_pure_pursuit_controller.cpp)
    # ═══════════════════════════════════════════════════════════════

    def _compute_rpp_command(self, px, py, pyaw, vx, wz, closest_idx,
                              remaining, p) -> Tuple[float, float]:
        """Compute RPP velocity command for one timestep."""

        # 1. Lookahead distance
        if p['use_velocity_scaled_lookahead']:
            la = abs(vx) * p['lookahead_time']
            la = max(p['min_lookahead_dist'], min(p['max_lookahead_dist'], la))
        else:
            la = p['lookahead_dist']

        # 2. Cusp detection (allow_reversing)
        if p['allow_reversing']:
            dist_to_cusp = self._find_velocity_sign_change(closest_idx)
            if dist_to_cusp < la:
                la = dist_to_cusp

        # 3. Lookahead point (carrot)
        carrot_x, carrot_y = self._get_lookahead_point(closest_idx, px, py, la)
        if carrot_x is None:
            return 0.0, 0.0

        # 4. Transform carrot to robot frame
        dx = carrot_x - px
        dy = carrot_y - py
        rx = dx * math.cos(-pyaw) - dy * math.sin(-pyaw)
        ry = dx * math.sin(-pyaw) + dy * math.cos(-pyaw)

        # 5. Curvature: k = 2y / (x² + y²)
        d2 = rx * rx + ry * ry
        if d2 < 0.001:
            return 0.0, 0.0
        curvature = 2.0 * ry / d2

        # 6. Velocity sign (allow_reversing)
        sign = 1.0 if rx >= 0.0 or not p['allow_reversing'] else -1.0

        # 7. Base velocity
        v = p['desired_linear_vel']

        # 8. Curvature regulation
        if p['use_regulated_linear_velocity_scaling']:
            v = self._curvature_constraint(v, curvature, p['regulated_linear_scaling_min_radius'])

        # 9. Cost regulation
        if p['use_cost_regulated_linear_velocity_scaling']:
            v = self._cost_constraint(v, px, py, p)

        # 10. Use minimum of constraints, but above min speed
        v = max(v, p['regulated_linear_scaling_min_speed'])

        # 11. Approach velocity scaling
        v = self._approach_constraint(v, remaining, p)

        # 12. Final clamp
        v = max(0.0, min(v, p['desired_linear_vel']))

        # 13. Angular velocity from curvature
        w = curvature * v * sign

        # 14. Clamp angular velocity
        w = max(-p['max_angular_vel'], min(p['max_angular_vel'], w))

        return v * sign, w

    # ═══════════════════════════════════════════════════════════════
    # Regulation Functions (from regulation_functions.hpp)
    # ═══════════════════════════════════════════════════════════════

    @staticmethod
    def _curvature_constraint(v: float, curvature: float, min_radius: float) -> float:
        """Slow down for tight turns."""
        if abs(curvature) < 1e-6:
            return v
        radius = 1.0 / abs(curvature)
        if radius < min_radius:
            return v * (1.0 - abs(radius - min_radius) / min_radius)
        return v

    def _cost_constraint(self, v: float, px: float, py: float, p) -> float:
        """Slow down near obstacles based on costmap cost value."""
        cost = self._cost_at(px, py)
        if cost <= 0:  # FREE_SPACE or unknown
            return v

        # Nav2: cost_to_distance via inflation formula inverse
        # distance = (inflation_csf * inscribed - log(cost) + log(253)) / inflation_csf
        insc = 0.05  # inscribed radius (meters)
        csf = p.get('inflation_cost_scaling_factor', 5.0)
        if cost >= 253:
            dist = 0.0
        else:
            try:
                dist = (csf * insc - math.log(cost) + math.log(253.0)) / csf
            except ValueError:
                return v

        if dist < p['cost_scaling_dist']:
            return v * (p['cost_scaling_gain'] * dist / p['cost_scaling_dist'])
        return v

    @staticmethod
    def _approach_constraint(v: float, remaining: float, p) -> float:
        """Slow down when approaching goal."""
        if remaining < p['approach_velocity_scaling_dist']:
            factor = remaining / p['approach_velocity_scaling_dist']
            v *= factor
            if v < p['min_approach_linear_velocity']:
                v = p['min_approach_linear_velocity']
        return v

    @staticmethod
    def _apply_accel_limit(current: float, target: float,
                           max_accel: float, max_decel: float,
                           dt: float) -> float:
        """Apply acceleration/deceleration limits (DWPP)."""
        diff = target - current
        if diff > 0:
            diff = min(diff, max_accel * dt)
        else:
            diff = max(diff, -max_decel * dt)
        return current + diff

    # ═══════════════════════════════════════════════════════════════
    # Path Helpers
    # ═══════════════════════════════════════════════════════════════

    def _closest_index(self, px: float, py: float, search_start: int = 0) -> int:
        """Find index of path point closest to robot."""
        best_i = search_start
        best_d2 = float('inf')
        end = min(search_start + 30, self.n_pts)
        for i in range(search_start, end):
            wx, wy = self.world_path[i]
            d2 = (wx - px) ** 2 + (wy - py) ** 2
            if d2 < best_d2:
                best_d2 = d2
                best_i = i
        return best_i

    def _get_lookahead_point(self, from_idx: int, px: float, py: float,
                              lookahead: float) -> Optional[Tuple[float, float]]:
        """Find point on path at arc-length `lookahead` ahead of robot."""
        # Start from the closest point, advance along path
        cum_dist = 0.0
        prev = self.world_path[from_idx]

        for i in range(from_idx + 1, self.n_pts):
            curr = self.world_path[i]
            seg_len = math.hypot(curr[0] - prev[0], curr[1] - prev[1])
            if cum_dist + seg_len >= lookahead:
                # Interpolate on this segment
                frac = (lookahead - cum_dist) / seg_len if seg_len > 0 else 0.0
                return (prev[0] + frac * (curr[0] - prev[0]),
                        prev[1] + frac * (curr[1] - prev[1]))
            cum_dist += seg_len
            prev = curr

        # Lookahead beyond path end — return goal
        return self.world_path[-1]

    def _remaining_distance(self, from_idx: int, px: float, py: float) -> float:
        """Distance from robot to end of path along the path."""
        if from_idx >= self.n_pts:
            return 0.0
        # Distance from robot to closest path point
        wx, wy = self.world_path[from_idx]
        dist_to_path = math.hypot(wx - px, wy - py)
        # Plus remaining arc length
        return dist_to_path + (self._path_dists[-1] - self._path_dists[from_idx])

    def _cross_track_error(self, px: float, py: float, closest_idx: int) -> float:
        """Perpendicular distance from robot to path segment."""
        if closest_idx >= self.n_pts - 1:
            return 0.0
        p0 = self.world_path[closest_idx]
        p1 = self.world_path[min(closest_idx + 1, self.n_pts - 1)]
        dx = p1[0] - p0[0]
        dy = p1[1] - p0[1]
        seg_len2 = dx * dx + dy * dy
        if seg_len2 < 1e-9:
            return math.hypot(px - p0[0], py - p0[1])
        t = max(0.0, min(1.0, ((px - p0[0]) * dx + (py - p0[1]) * dy) / seg_len2))
        proj_x = p0[0] + t * dx
        proj_y = p0[1] + t * dy
        return math.hypot(px - proj_x, py - proj_y)

    def _find_velocity_sign_change(self, from_idx: int) -> float:
        """Find distance to next cusp (direction reversal) point on path.
        Uses dot product of consecutive segments (Nav2 findVelocitySignChange)."""
        if from_idx >= self.n_pts - 2:
            return float('inf')

        for i in range(from_idx, min(from_idx + 50, self.n_pts - 2)):
            # Vector OA: from i to i+1
            oa_x = self.world_path[i+1][0] - self.world_path[i][0]
            oa_y = self.world_path[i+1][1] - self.world_path[i][1]
            # Vector AB: from i+1 to i+2
            ab_x = self.world_path[i+2][0] - self.world_path[i+1][0]
            ab_y = self.world_path[i+2][1] - self.world_path[i+1][1]
            # Dot product < 0 → direction reversal
            if (oa_x * ab_x + oa_y * ab_y) < 0.0:
                return self._path_dists[i] - self._path_dists[from_idx]
        return float('inf')

    # ═══════════════════════════════════════════════════════════════
    # Costmap Access
    # ═══════════════════════════════════════════════════════════════

    def _cost_at(self, wx: float, wy: float) -> int:
        """Get Nav2 costmap value at world coordinate."""
        c = int((wx - self.origin_x) / self.resolution)
        r = self.H - 1 - int((wy - self.origin_y) / self.resolution)
        r = max(0, min(self.H - 1, r))
        c = max(0, min(self.W - 1, c))
        return int(self.costmap[r, c])

    def _is_lethal(self, wx: float, wy: float) -> bool:
        """Check if position is in lethal cost zone."""
        return self._cost_at(wx, wy) >= 253

    # ═══════════════════════════════════════════════════════════════
    # Parameter Resolution
    # ═══════════════════════════════════════════════════════════════

    @staticmethod
    def _resolve_params(params: Dict[str, float]) -> dict:
        """Resolve flat param dict to RPP-usable values with defaults."""
        def g(k, default):
            # Try both 'controller.k' and 'k' keys
            for prefix in ('controller.', 'planner.', ''):
                if prefix + k in params:
                    return float(params[prefix + k])
            return float(default)

        return {
            # Lookahead
            'lookahead_dist': g('lookahead_dist', 0.65),
            'min_lookahead_dist': g('min_lookahead_dist', 0.30),
            'max_lookahead_dist': g('max_lookahead_dist', 0.90),
            'lookahead_time': g('lookahead_time', 1.2),
            'use_velocity_scaled_lookahead': g('use_velocity_scaled_lookahead_dist', 1.0) > 0.5,

            # Velocity
            'desired_linear_vel': g('desired_linear_vel', 0.50),
            'max_linear_vel': g('max_linear_vel', 0.60),
            'max_angular_vel': g('max_angular_vel', 2.0),
            'max_linear_accel': g('max_linear_accel', 1.2),
            'max_linear_decel': abs(g('max_linear_decel', 1.5)),
            'max_angular_accel': g('max_angular_accel', 2.0),
            'max_angular_decel': abs(g('max_angular_decel', 2.0)),

            # Regulation
            'use_regulated_linear_velocity_scaling': True,
            'regulated_linear_scaling_min_radius': g('regulated_linear_scaling_min_radius', 0.30),
            'regulated_linear_scaling_min_speed': g('regulated_linear_scaling_min_speed', 0.18),
            'use_cost_regulated_linear_velocity_scaling': True,
            'cost_scaling_dist': g('cost_scaling_dist', 0.12),
            'cost_scaling_gain': g('cost_scaling_gain', 1.0),
            'inflation_cost_scaling_factor': g('inflation_cost_scaling_factor', 5.0),

            # Approach
            'min_approach_linear_velocity': g('min_approach_linear_vel', 0.22),
            'approach_velocity_scaling_dist': g('approach_velocity_scaling_dist', 0.50),
            'xy_goal_tolerance': g('xy_goal_tolerance', 0.40),

            # Ackermann
            'allow_reversing': True,
            'use_rotate_to_heading': False,
        }
