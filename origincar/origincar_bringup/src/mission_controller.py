#!/usr/bin/env python3
"""
mission_controller — 任务指令执行器 (控制节点)
职责: 消费 /mission_cmd (编排指令) → 执行 Nav2 goal / STOP / VLM 触发
与 task_manager 分工: task_manager=状态机+编排, mission_controller=执行
"""

import math
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from std_msgs.msg import String, Int32
from geometry_msgs.msg import Twist, PoseStamped
from nav2_msgs.action import NavigateToPose, NavigateThroughPoses


def _flat_to_waypoints(arr, stride=3):
    """将 flat double array 转为 [[x,y,yaw], ...]"""
    return [arr[i:i+stride] for i in range(0, len(arr), stride)]


class MissionController(Node):
    def __init__(self):
        super().__init__('mission_controller')

        # ── 路点参数 (与 task_manager 共享) ────────────────
        # rclpy 不支持嵌套 list, 使用 flat double_array
        self.declare_parameter('p_point', [0.0, 0.0, 0.0])
        self.declare_parameter('qr_publish_point', [0.41, -3.17, 0.0])
        self.declare_parameter('channel_entry', [0.38, -1.10, 0.0])
        self.declare_parameter('cruise_cw', [
            3.0, 2.0, 0.0,  3.0, 0.5, 0.0,
            1.0, 0.5, 0.0,  1.0, 2.0, 0.0,
        ])
        self.declare_parameter('cruise_ccw', [
            1.0, 2.0, 0.0,  1.0, 0.5, 0.0,
            3.0, 0.5, 0.0,  3.0, 2.0, 0.0,
        ])

        # ── 订阅 ──────────────────────────────────────────
        self._cmd_sub = self.create_subscription(
            String, '/mission_cmd', self._on_cmd, 10)

        # ── 发布 ──────────────────────────────────────────
        self._stop_pub = self.create_publisher(Twist, '/stop_cmd_vel', 10)
        self._sign4return_pub = self.create_publisher(Int32, '/sign4return', 10)
        self._status_pub = self.create_publisher(String, '/mission_status', 10)

        # ── Action Clients ────────────────────────────────
        self._nav_pose_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')
        self._nav_through_client = ActionClient(
            self, NavigateThroughPoses, 'navigate_through_poses')

        self.get_logger().info("MissionController 就绪: ← /mission_cmd")

    # ═══════════════════════════════════════════════════════════

    def _on_cmd(self, msg):
        cmd = msg.data.strip()
        self.get_logger().info(f"[mission] 收到指令: {cmd}")

        if cmd == 'stop':
            self._stop_robot()
            self._status_pub.publish(String(data='stopped'))
        elif cmd == 'trigger_vlm':
            self._trigger_vlm()
            self._status_pub.publish(String(data='vlm_triggered'))
        elif cmd.startswith('goto:'):
            # 格式: goto:x,y,yaw
            parts = cmd[5:].split(',')
            if len(parts) == 3:
                x, y, yaw = float(parts[0]), float(parts[1]), float(parts[2])
                self._send_pose_goal(x, y, yaw)
                self._status_pub.publish(String(data=f'navigating_to_pose'))
        elif cmd.startswith('through:'):
            # 格式: through:cw 或 through:ccw
            direction = cmd[8:]
            if direction == 'cw':
                wps = _flat_to_waypoints(self.get_parameter('cruise_cw').value)
            else:
                wps = _flat_to_waypoints(self.get_parameter('cruise_ccw').value)
            self._send_through_poses_goal(wps)
            self._status_pub.publish(String(data='navigating_through_poses'))
        elif cmd.startswith('goto_param:'):
            # 格式: goto_param:param_name
            param_name = cmd[10:]
            pt = self.get_parameter(param_name).value
            if pt and len(pt) >= 2:
                yaw = pt[2] if len(pt) >= 3 else 0.0
                self._send_pose_goal(pt[0], pt[1], yaw)
                self._status_pub.publish(String(data='navigating'))
        else:
            self.get_logger().warn(f"[mission] 未知指令: {cmd}")

    # ═══════════════════════════════════════════════════════════

    def _stop_robot(self):
        self.get_logger().warn("[mission] → STOP")
        self._stop_pub.publish(Twist())

    def _trigger_vlm(self):
        self.get_logger().info("[mission] → sign4return=100 (VLM)")
        self._sign4return_pub.publish(Int32(data=100))

    def _send_pose_goal(self, x, y, yaw):
        if not self._nav_pose_client.wait_for_server(timeout_sec=3.0):
            self.get_logger().error("navigate_to_pose action server 未就绪")
            self._status_pub.publish(String(data='server_not_ready'))
            return
        goal = NavigateToPose.Goal()
        goal.pose.header.frame_id = 'map'
        goal.pose.header.stamp = self.get_clock().now().to_msg()
        goal.pose.pose.position.x = x
        goal.pose.pose.position.y = y
        goal.pose.pose.orientation.z = math.sin(yaw / 2.0)
        goal.pose.pose.orientation.w = math.cos(yaw / 2.0)
        self._nav_pose_client.send_goal_async(goal)
        self.get_logger().info(f"[mission] → navigate_to_pose: ({x:.2f}, {y:.2f}, yaw={yaw:.2f})")

    def _send_through_poses_goal(self, waypoints):
        if not self._nav_through_client.wait_for_server(timeout_sec=3.0):
            self.get_logger().error("navigate_through_poses action server 未就绪")
            return
        goal = NavigateThroughPoses.Goal()
        for wp in waypoints:
            ps = PoseStamped()
            ps.header.frame_id = 'map'
            ps.pose.position.x = wp[0]
            ps.pose.position.y = wp[1]
            ps.pose.orientation.z = math.sin(wp[2] / 2.0)
            ps.pose.orientation.w = math.cos(wp[2] / 2.0)
            goal.poses.append(ps)
        self._nav_through_client.send_goal_async(goal)
        self.get_logger().info(f"[mission] → navigate_through_poses: {len(waypoints)} waypoints")


def main(args=None):
    rclpy.init(args=args)
    node = MissionController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        try:
            node.destroy_node()
        except Exception:
            pass
        try:
            rclpy.shutdown()
        except RuntimeError:
            pass


if __name__ == '__main__':
    main()
