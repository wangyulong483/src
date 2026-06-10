#!/usr/bin/env python3
"""
competition_master_stage1 — Stage 1 管理层节点
单模块联调：P点→任务发布点导航 + QR 扫描监听 → 扫到码后停车打印成功

绕过 task_manager/mission_controller，直接操控 Nav2 Action + /stop_cmd_vel。
Stage 2~4 逐步迁移到标准 task_manager 架构。
"""

import math
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav2_msgs.action import NavigateToPose
from action_msgs.msg import GoalStatus


class CompetitionMasterStage1(Node):
    def __init__(self):
        super().__init__('competition_master_stage1')

        # ── 声明参数 ──────────────────────────────────────────
        self.declare_parameter('nav_timeout', 120.0)
        self.declare_parameter('qr_point_x', 0.41)
        self.declare_parameter('qr_point_y', -3.17)
        self.declare_parameter('qr_point_yaw', 0.0)

        # ── 读取参数 ──────────────────────────────────────────
        self.nav_timeout = self.get_parameter('nav_timeout').value
        self.qr_point_x = self.get_parameter('qr_point_x').value
        self.qr_point_y = self.get_parameter('qr_point_y').value
        self.qr_point_yaw = self.get_parameter('qr_point_yaw').value

        # ── 状态变量 ──────────────────────────────────────────
        self.state = 'INIT'
        self.qr_data = None
        self._goal_handle = None
        self._retry_timer = None
        self._nav_start_time = None   # 导航目标发送时间 (用于超时检测)

        # ── ROS 接口 ──────────────────────────────────────────
        self.nav_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')
        self.qr_sub = self.create_subscription(String, '/sign', self.qr_callback, 10)
        self.stop_pub = self.create_publisher(Twist, '/stop_cmd_vel', 10)

        # ── 导航超时检测定时器 (1 Hz) ─────────────────────────
        self._timeout_timer = self.create_timer(1.0, self._check_nav_timeout)

        self.get_logger().info("=== [Stage 1] 总控节点初始化 ===")
        self.get_logger().info(
            f"  参数: nav_timeout={self.nav_timeout}s, "
            f"qr_point=({self.qr_point_x:.2f}, {self.qr_point_y:.2f}, yaw={self.qr_point_yaw:.2f})"
        )

    # ═══════════════════════════════════════════════════════════

    def qr_callback(self, msg):
        if not msg.data or self.state != 'NAV_TO_QR':
            return
        self.qr_data = msg.data
        self.get_logger().info(f"[QR检测] 内容: {msg.data}")
        self._nav_start_time = None   # 导航已由 QR 拦截终止，清除超时计时
        if self._goal_handle is not None:
            self.get_logger().info("取消当前导航目标...")
            self._goal_handle.cancel_goal_async()
        self._finish()

    def send_stop(self):
        self.stop_pub.publish(Twist())

    # ═══════════════════════════════════════════════════════════

    def send_nav_goal(self, x, y, yaw, description):
        # 生命周期检查: 确保 navigate_to_pose action server 可用 (3s 超时)
        if not self.nav_client.wait_for_server(timeout_sec=3.0):
            self.get_logger().warn(
                f"navigate_to_pose action server 未就绪 (3s 超时), "
                f"跳过导航目标 [{description}]. 3s 后重试."
            )
            if self._retry_timer is not None:
                self._retry_timer.cancel()
            self._retry_timer = self.create_timer(3.0, self._retry_nav)
            return

        goal_msg = NavigateToPose.Goal()
        goal_msg.pose.header.frame_id = 'map'
        goal_msg.pose.header.stamp = self.get_clock().now().to_msg()
        goal_msg.pose.pose.position.x = x
        goal_msg.pose.pose.position.y = y
        goal_msg.pose.pose.orientation.x = 0.0
        goal_msg.pose.pose.orientation.y = 0.0
        goal_msg.pose.pose.orientation.z = math.sin(yaw / 2.0)
        goal_msg.pose.pose.orientation.w = math.cos(yaw / 2.0)

        self.get_logger().info(f">>> 发送导航目标 [{description}]: ({x:.2f}, {y:.2f}, yaw={yaw:.2f})")
        self._nav_start_time = self.get_clock().now()   # 记录发送时间，启动超时计时
        self._send_goal_future = self.nav_client.send_goal_async(goal_msg)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            if self.state == 'NAV_TO_QR':
                self.get_logger().warn("导航目标被拒绝, 3s 后重试...")
                if self._retry_timer is not None:
                    self._retry_timer.cancel()
                self._retry_timer = self.create_timer(3.0, self._retry_nav)
            return
        # goal 被接受, 取消所有重试
        if self._retry_timer is not None:
            self._retry_timer.cancel()
            self._retry_timer = None
        self._goal_handle = goal_handle
        self.get_logger().info("[stage_master] nav goal ACCEPTED, robot departing...")
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def _retry_nav(self):
        """目标被拒绝后的重试回调"""
        if self.state != 'NAV_TO_QR':
            return
        self.get_logger().info("重试发送导航目标...")
        self.send_nav_goal(self.qr_point_x, self.qr_point_y, self.qr_point_yaw, "任务发布点")

    def get_result_callback(self, future):
        status = future.result().status
        if status == GoalStatus.STATUS_SUCCEEDED and self.state == 'NAV_TO_QR':
            self.get_logger().warn("已到达任务发布点，但全程未检测到 QR 码！")
            self._nav_start_time = None
        elif status == GoalStatus.STATUS_CANCELED:
            self.get_logger().info("导航任务已取消（QR 拦截成功）")
            self._nav_start_time = None

    # ═══════════════════════════════════════════════════════════

    def _check_nav_timeout(self):
        """定时检查导航是否超时 (1Hz 定时器回调)"""
        if self._nav_start_time is None:
            return
        if self.state not in ('NAV_TO_QR',):
            return
        elapsed = (self.get_clock().now() - self._nav_start_time).nanoseconds / 1e9
        if elapsed > self.nav_timeout:
            self.get_logger().error(
                f"[stage_master] STATE NAV_TO_QR -> TIMEOUT (elapsed={elapsed:.1f}s > {self.nav_timeout}s)"
            )
            self._nav_start_time = None
            if self._goal_handle is not None:
                self._goal_handle.cancel_goal_async()
                self._goal_handle = None
            self.send_stop()
            self.state = 'TIMEOUT'

    def _start_nav(self):
        """延迟回调: 发送导航目标 (timer 触发, 避开 spin_once 死锁)"""
        if self.state != 'INIT':
            return
        self.get_logger().info("[stage_master] STATE INIT -> NAV_TO_QR")
        self.state = 'NAV_TO_QR'
        self.send_nav_goal(self.qr_point_x, self.qr_point_y, self.qr_point_yaw, "任务发布点")

    def _finish(self):
        """QR 检测到后打印完成信息"""
        self.send_stop()
        self.get_logger().info("[stage_master] STATE NAV_TO_QR -> DONE")
        self.get_logger().info(f"[stage_master] QR_DATA: {self.qr_data}")
        self.state = 'DONE'

    def run(self):
        self._start_timer = self.create_timer(8.0, self._start_nav)  # BT激活约需7.7s
        rclpy.spin(self)


def main(args=None):
    rclpy.init(args=args)
    node = CompetitionMasterStage1()
    try:
        node.run()
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
