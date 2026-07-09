#!/usr/bin/env python3
"""
speed_profile_node.py — Path curvature to velocity profile generator for Nav2 RPP.

Generates pre-planned speed profiles from global path curvature,
publishing speed limits that the RPP controller uses to adjust velocity.

Algorithm:
  1. Subscribe to /plan (global path) and /odom (robot pose).
  2. Compute Menger curvature at each waypoint (3-point method).
  3. Apply moving-average smoothing to the curvature array.
  4. Map curvature to raw velocity: v(κ) = v_max / (1 + β * |κ|^λ).
  5. Forward-backward acceleration smoothing constrained by max_accel/max_decel.
  6. Find robot position on path, look ahead N waypoints, publish speed limit.

Publishers:
  /speed_limit         — nav2_msgs/SpeedLimit  (recommended max linear velocity, m/s, percentage=false)
  /speed_profile_debug — nav_msgs/Path      (poses with velocity in z for RViz)

Subscribers:
  /plan  — nav_msgs/Path
  /odom  — nav_msgs/Odometry
"""

import math
from typing import Optional, Tuple

import numpy as np
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry, Path
from nav2_msgs.msg import SpeedLimit


class SpeedProfileNode(Node):
    """ROS2 node that computes curvature-based speed profiles for path following."""

    def __init__(self) -> None:
        super().__init__("speed_profile_node")

        # ---- Parameters --------------------------------------------------------
        self.declare_parameter("v_max", 0.50)
        self.declare_parameter("v_min", 0.20)    # 2026-07-08: 0.10→0.20, 匹配RPP min_speed
        self.declare_parameter("beta", 0.25)     # 2026-07-08: 0.5→0.25, 降低弯道敏感度
        self.declare_parameter("lambda", 1.2)    # 2026-07-08: 1.5→1.2, 减速曲线更平缓
        self.declare_parameter("max_accel", 0.8)
        self.declare_parameter("max_decel", -1.2)
        self.declare_parameter("smoothing_window", 5)
        self.declare_parameter("lookahead_idx", 10)

        self._v_max: float = self.get_parameter("v_max").value
        self._v_min: float = self.get_parameter("v_min").value
        self._beta: float = self.get_parameter("beta").value
        self._lam: float = self.get_parameter("lambda").value
        self._max_accel: float = self.get_parameter("max_accel").value
        self._max_decel: float = self.get_parameter("max_decel").value
        self._smoothing_window: int = self.get_parameter("smoothing_window").value
        self._lookahead_idx: int = self.get_parameter("lookahead_idx").value

        # ---- State -------------------------------------------------------------
        self._last_path_xs: Optional[np.ndarray] = None
        self._last_path_ys: Optional[np.ndarray] = None
        self._velocity_profile: Optional[np.ndarray] = None
        self._robot_x: Optional[float] = None
        self._robot_y: Optional[float] = None
        self._path_received: bool = False

        # ---- Publishers --------------------------------------------------------
        self._pub_speed_limit = self.create_publisher(SpeedLimit, "/speed_limit", 10)
        self._pub_debug = self.create_publisher(Path, "/speed_profile_debug", 10)

        # ---- Subscribers -------------------------------------------------------
        self._sub_plan = self.create_subscription(
            Path, "/plan", self._on_plan, 10
        )
        self._sub_odom = self.create_subscription(
            Odometry, "/odom", self._on_odom, 10
        )

        # ---- Timer: periodic speed-limit publish (20 Hz) -----------------------
        self._timer = self.create_timer(0.05, self._publish_speed_limit)

        self.get_logger().info(
            "speed_profile_node started — "
            f"v_max={self._v_max:.2f} v_min={self._v_min:.2f} "
            f"beta={self._beta:.2f} lambda={self._lam:.2f} "
            f"max_accel={self._max_accel:.2f} max_decel={self._max_decel:.2f}"
        )

    # ------------------------------------------------------------------
    # Subscriber callbacks
    # ------------------------------------------------------------------

    def _on_odom(self, msg: Odometry) -> None:
        """Store the latest robot pose."""
        self._robot_x = msg.pose.pose.position.x
        self._robot_y = msg.pose.pose.position.y

    def _on_plan(self, msg: Path) -> None:
        """Process a new global plan: compute curvature and velocity profile."""
        n = len(msg.poses)
        if n < 3:
            self.get_logger().warning(
                f"Path has only {n} poses (< 3), skipping curvature computation."
            )
            return

        xs = np.array([p.pose.position.x for p in msg.poses], dtype=np.float64)
        ys = np.array([p.pose.position.y for p in msg.poses], dtype=np.float64)

        # Skip recomputation if path is effectively unchanged
        if self._path_changed(xs, ys):
            self._last_path_xs = xs
            self._last_path_ys = ys
        else:
            return  # reuse existing profile

        # 1. Curvature
        kappa = self._compute_curvature(xs, ys)

        # 2. Raw velocity profile
        v_raw = self._generate_velocity_profile(kappa)

        # 3. Forward-backward acceleration smoothing
        v_smooth = self._forward_backward_smooth(v_raw, xs, ys)

        self._velocity_profile = v_smooth
        self._path_received = True

        # Log statistics
        self.get_logger().info(
            f"Plan received: {n} poses, "
            f"mean|κ|={np.mean(np.abs(kappa)):.4f} m⁻¹, "
            f"max|κ|={np.max(np.abs(kappa)):.4f} m⁻¹, "
            f"mean_v={np.mean(v_smooth):.3f} m/s, "
            f"min_v={np.min(v_smooth):.3f} m/s, "
            f"max_v={np.max(v_smooth):.3f} m/s"
        )

        # Publish debug path (encode velocity in pose.position.z)
        self._publish_debug_path(v_smooth, msg)

    # ------------------------------------------------------------------
    # Core algorithms
    # ------------------------------------------------------------------

    def _compute_curvature(self, xs: np.ndarray, ys: np.ndarray) -> np.ndarray:
        """
        Compute Menger curvature at each waypoint using the 3-point method.

        For consecutive points A, B, C:
            a = |BC|,  b = |AB|,  c = |AC|
            area = 0.5 * |cross(B-A, C-A)|
            κ = 4 * area / (a * b * c)

        Boundary points (first and last) copy the nearest computed value.
        A moving-average filter of width `smoothing_window` is applied.

        Args:
            xs: x-coordinates of path waypoints.
            ys: y-coordinates of path waypoints.

        Returns:
            Array of curvature values (m⁻¹), same length as input.
        """
        n = len(xs)
        kappa = np.zeros(n, dtype=np.float64)

        # Interior points: i from 1 to n-2 (inclusive), using (i-1, i, i+1)
        for i in range(1, n - 1):
            ax, ay = xs[i - 1], ys[i - 1]
            bx, by = xs[i], ys[i]
            cx, cy = xs[i + 1], ys[i + 1]

            # Side lengths
            ab = math.hypot(bx - ax, by - ay)
            bc = math.hypot(cx - bx, cy - by)
            ac = math.hypot(cx - ax, cy - ay)

            # Cross product magnitude |(B-A) × (C-A)|
            cross = abs((bx - ax) * (cy - ay) - (by - ay) * (cx - ax))
            area = 0.5 * cross

            denom = ab * bc * ac
            if denom < 1e-12:
                kappa[i] = 0.0
            else:
                kappa[i] = 4.0 * area / denom

        # Boundary points: copy nearest neighbor
        if n >= 1:
            kappa[0] = kappa[1] if n > 1 else 0.0
        if n >= 2:
            kappa[n - 1] = kappa[n - 2]

        # Moving-average smoothing
        if self._smoothing_window > 1 and n >= self._smoothing_window:
            kernel = np.ones(self._smoothing_window, dtype=np.float64) / self._smoothing_window
            kappa = np.convolve(kappa, kernel, mode="same")

        return kappa

    def _generate_velocity_profile(self, kappa: np.ndarray) -> np.ndarray:
        """
        Map curvature to raw velocity using the graceful formula.

            v(κ) = v_max / (1 + β * |κ|^λ)

        Results are clamped to [v_min, v_max].

        Args:
            kappa: Curvature array (m⁻¹).

        Returns:
            Raw velocity array (m/s), same length as kappa.
        """
        abs_kappa = np.abs(kappa)
        denominator = 1.0 + self._beta * np.power(abs_kappa, self._lam)
        v_raw = self._v_max / denominator
        v_raw = np.clip(v_raw, self._v_min, self._v_max)
        return v_raw

    def _forward_backward_smooth(
        self, velocities: np.ndarray, xs: np.ndarray, ys: np.ndarray
    ) -> np.ndarray:
        """
        Apply forward (acceleration-limited) then backward (deceleration-limited)
        smoothing to the velocity profile.

        Segment lengths ds[i] are computed between consecutive waypoints.

        Forward pass (i = 1 .. n-1):
            dt = ds[i] / max(v_fwd[i-1], 0.01)
            max_dv = max_accel * dt
            v_fwd[i] = min(v_fwd[i], v_fwd[i-1] + max_dv)

        Backward pass (i = n-2 .. 0):
            dt = ds[i] / max(v_smooth[i+1], 0.01)
            max_dv = abs(max_decel) * dt
            v_smooth[i] = min(v_smooth[i], v_smooth[i+1] + max_dv)

        Args:
            velocities: Raw velocity array (m/s).
            xs: x-coordinates of path waypoints.
            ys: y-coordinates of path waypoints.

        Returns:
            Acceleration-constrained velocity array (m/s).
        """
        n = len(velocities)
        if n < 2:
            return velocities.copy()

        # Segment lengths (Euclidean distance between consecutive points)
        ds = np.empty(n - 1, dtype=np.float64)
        for i in range(n - 1):
            ds[i] = math.hypot(xs[i + 1] - xs[i], ys[i + 1] - ys[i])

        v_smooth = velocities.copy()

        # ---- Forward pass (acceleration limit) ----
        for i in range(1, n):
            dt = ds[i - 1] / max(v_smooth[i - 1], 0.01)
            max_dv = self._max_accel * dt
            v_smooth[i] = min(v_smooth[i], v_smooth[i - 1] + max_dv)

        # ---- Backward pass (deceleration limit) ----
        abs_decel = abs(self._max_decel)
        for i in range(n - 2, -1, -1):
            dt = ds[i] / max(v_smooth[i + 1], 0.01)
            max_dv = abs_decel * dt
            v_smooth[i] = min(v_smooth[i], v_smooth[i + 1] + max_dv)

        return v_smooth

    # ------------------------------------------------------------------
    # Robot tracking & lookahead
    # ------------------------------------------------------------------

    def _find_robot_index(self) -> Optional[int]:
        """
        Find the index of the path point closest to the robot's current position.

        Returns:
            Index into the stored path arrays, or None if no odom/path available.
        """
        if (
            self._last_path_xs is None
            or self._last_path_ys is None
            or self._robot_x is None
            or self._robot_y is None
        ):
            return None

        dx = self._last_path_xs - self._robot_x
        dy = self._last_path_ys - self._robot_y
        distances = np.hypot(dx, dy)
        return int(np.argmin(distances))

    def _path_changed(self, new_xs: np.ndarray, new_ys: np.ndarray) -> bool:
        """
        Check whether the new path differs significantly from the last one.

        A path is considered changed if any corresponding point has moved
        more than 0.1 m, or if the number of points differs.

        Args:
            new_xs: x-coordinates of the incoming path.
            new_ys: y-coordinates of the incoming path.

        Returns:
            True if the path has changed or no previous path exists.
        """
        if self._last_path_xs is None or self._last_path_ys is None:
            return True
        if len(new_xs) != len(self._last_path_xs):
            return True

        dx = np.abs(new_xs - self._last_path_xs)
        dy = np.abs(new_ys - self._last_path_ys)
        return bool(np.any(dx > 0.1) or np.any(dy > 0.1))

    # ------------------------------------------------------------------
    # Publishers
    # ------------------------------------------------------------------

    def _publish_speed_limit(self) -> None:
        """
        Timer callback (20 Hz): look ahead from the robot's current position
        and publish the recommended maximum velocity.

        Publishes nav2_msgs/SpeedLimit (not std_msgs/Float32) because
        Nav2 controller_server subscribes to nav2_msgs::msg::SpeedLimit.
        percentage=false means absolute m/s mode.
        """
        msg = SpeedLimit()
        msg.percentage = False

        if not self._path_received or self._velocity_profile is None:
            # No path yet — publish v_max as safe default
            msg.speed_limit = float(self._v_max)
            self._pub_speed_limit.publish(msg)
            return

        idx = self._find_robot_index()
        if idx is None:
            msg.speed_limit = float(self._v_max)
            self._pub_speed_limit.publish(msg)
            return

        # Look ahead
        lookahead = min(idx + self._lookahead_idx, len(self._velocity_profile) - 1)
        speed = self._velocity_profile[lookahead]
        msg.speed_limit = float(speed)
        self._pub_speed_limit.publish(msg)

    def _publish_debug_path(
        self, velocities: np.ndarray, original_path: Path
    ) -> None:
        """
        Publish a nav_msgs/Path for RViz visualization with velocity encoded
        in the z-coordinate of each pose position (for color-mapped display).

        Args:
            velocities: Smoothed velocity profile (m/s).
            original_path: The original nav_msgs/Path message (for header/frame).
        """
        debug = Path()
        debug.header = original_path.header
        debug.header.stamp = self.get_clock().now().to_msg()
        debug.poses = []

        for i, pose_stamped in enumerate(original_path.poses):
            new_pose = type(pose_stamped)()
            new_pose.header = pose_stamped.header
            new_pose.pose.position.x = pose_stamped.pose.position.x
            new_pose.pose.position.y = pose_stamped.pose.position.y
            new_pose.pose.position.z = float(velocities[i])
            # Copy orientation unchanged
            new_pose.pose.orientation = pose_stamped.pose.orientation
            debug.poses.append(new_pose)

        self._pub_debug.publish(debug)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = SpeedProfileNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
