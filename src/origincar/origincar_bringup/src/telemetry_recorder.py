#!/usr/bin/env python3
"""telemetry_recorder — 5Hz记录 位姿/cmd_vel/规划/目标/里程计 到CSV."""

import csv, math, rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, PoseStamped
from nav_msgs.msg import Odometry, Path
from tf2_ros import Buffer, TransformListener

OUT = "/tmp/telemetry.csv"

class TelemetryRecorder(Node):
    def __init__(self):
        super().__init__("telemetry_recorder")
        self._tf = Buffer()
        self._tf_listener = TransformListener(self._tf, self)

        self._latest_cmd = Twist()
        self._latest_odom = Odometry()
        self._latest_plan = Path()
        self._latest_goal = PoseStamped()

        self.create_subscription(Twist, "/cmd_vel", self._cb_cmd, 10)
        self.create_subscription(Odometry, "/odom", self._cb_odom, 10)
        self.create_subscription(Path, "/plan", self._cb_plan, 10)
        self.create_subscription(PoseStamped, "/goal_pose", self._cb_goal, 10)

        self._file = open(OUT, "w", newline="")
        self._w = csv.writer(self._file)
        self._w.writerow([
            "t", "x", "y", "yaw_deg",
            "cmd_vx", "cmd_wz",
            "odom_vx", "odom_wz",
            "goal_x", "goal_y", "dist_goal",
            "plan_len", "plan_x0", "plan_y0", "plan_x1", "plan_y1",
        ])
        self.create_timer(0.2, self._tick)
        self.get_logger().info(f"Telemetry → {OUT}")

    def _cb_cmd(self, m): self._latest_cmd = m
    def _cb_odom(self, m): self._latest_odom = m
    def _cb_plan(self, m): self._latest_plan = m
    def _cb_goal(self, m): self._latest_goal = m

    def _tick(self):
        # Pose from TF
        try:
            t = self._tf.lookup_transform("map", "base_footprint", rclpy.time.Time())
            px, py = t.transform.translation.x, t.transform.translation.y
            q = t.transform.rotation
            siny = 2.0*(q.w*q.z + q.x*q.y)
            cosy = 1.0 - 2.0*(q.y*q.y + q.z*q.z)
            yaw = math.degrees(math.atan2(siny, cosy))
        except Exception:
            px = py = yaw = 0.0

        # Plan waypoints
        plan = self._latest_plan
        plen = len(plan.poses)
        px0 = plan.poses[0].pose.position.x if plen > 0 else 0.0
        py0 = plan.poses[0].pose.position.y if plen > 0 else 0.0
        px1 = plan.poses[1].pose.position.x if plen > 1 else 0.0
        py1 = plan.poses[1].pose.position.y if plen > 1 else 0.0

        # Goal & distance
        gx = self._latest_goal.pose.position.x
        gy = self._latest_goal.pose.position.y
        dist = math.hypot(px - gx, py - gy) if (gx or gy) else 0.0

        now_s = self.get_clock().now().nanoseconds / 1e9
        self._w.writerow([
            f"{now_s:.3f}",
            f"{px:.3f}", f"{py:.3f}", f"{yaw:.1f}",
            f"{self._latest_cmd.linear.x:.3f}", f"{self._latest_cmd.angular.z:.3f}",
            f"{self._latest_odom.twist.twist.linear.x:.3f}", f"{self._latest_odom.twist.twist.angular.z:.3f}",
            f"{gx:.3f}", f"{gy:.3f}", f"{dist:.3f}",
            plen, f"{px0:.3f}", f"{py0:.3f}", f"{px1:.3f}", f"{py1:.3f}",
        ])

    def destroy_node(self):
        self._file.close()
        super().destroy_node()


def main():
    rclpy.init()
    rclpy.spin(TelemetryRecorder())

if __name__ == "__main__":
    main()
