#!/usr/bin/env python3
"""
competition_master_stage2 — Stage 2 管理层节点
Stage 1: P点→任务发布点(0.41,-3.17) + QR 扫描 → 扫到码后转去通道入口
Stage 2: QR 拦截 → 通道入口(0.38,-1.10) → 到达后停车打印成功

QR 方向获取:
  - 订阅 /sign (qr_decoder 原始解码) → 触发 QR 拦截逻辑
  - 订阅 /qr_event (qr_decision 结构化输出) → 获取通道巡航方向 (CW/CCW)
  - 方向用于后续通道巡航阶段 (NAV_TO_CRUISE, 待实现)
"""

import math
import subprocess
import rclpy
from rclpy.qos import QoSProfile, QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy
from nav2_msgs.msg import CostmapFilterInfo
from rclpy.node import Node
from rclpy.action import ActionClient
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav2_msgs.action import NavigateToPose
from action_msgs.msg import GoalStatus


class CompetitionMasterStage2(Node):
    def __init__(self):
        super().__init__('competition_master_stage2')

        # ── 声明参数 ──────────────────────────────────────────
        self.declare_parameter('nav_timeout', 180.0)
        self.declare_parameter('qr_point_x', 0.41)
        self.declare_parameter('qr_point_y', -3.17)
        self.declare_parameter('qr_point_yaw', 0.0)
        self.declare_parameter('entry_point_x', 0.38)
        self.declare_parameter('entry_point_y', -1.10)
        self.declare_parameter('entry_point_yaw', 0.0)

        # ── 读取参数 ──────────────────────────────────────────
        self.nav_timeout = self.get_parameter('nav_timeout').value
        self.qr_point_x = self.get_parameter('qr_point_x').value
        self.qr_point_y = self.get_parameter('qr_point_y').value
        self.qr_point_yaw = self.get_parameter('qr_point_yaw').value
        self.entry_point_x = self.get_parameter('entry_point_x').value
        self.entry_point_y = self.get_parameter('entry_point_y').value
        self.entry_point_yaw = self.get_parameter('entry_point_yaw').value

        # ── 状态变量 ──────────────────────────────────────────
        self.state = 'INIT'      # INIT → NAV_TO_QR → NAV_TO_ENTRY → DONE
        self.qr_data = None
        self._qr_direction = None      # qr_decision 输出: "顺时针"/"逆时针" (CW/CCW), 用于通道巡航
        self._qr_event_received = False
        self._goal_handle = None
        self._retry_timer = None
        self._nav_start_time = None   # 导航目标发送时间 (用于超时检测)

        # ── QR 拦截取消等待 (防止 Issue 2 竞争条件) ──────────
        self._pending_entry_nav = False            # True=等待BT取消确认, 收到STATUS_CANCELED后再发第二个目标
        self._pending_entry_nav_timeout = None     # 取消确认超时定时器 (3s fallback)

        # ── 后退序列变量 ──────────────────────────────────────
        self._backup_timer = None
        self._backup_keepalive = None          # 10Hz 保活
        self._backup_twist = None

        # ── ROS 接口 ──────────────────────────────────────────
        self.nav_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')
        self.qr_sub = self.create_subscription(String, '/sign', self.qr_callback, 10)
        self.qr_event_sub = self.create_subscription(
            String, '/qr_event', self._on_qr_event, 10)
        self.stop_pub = self.create_publisher(Twist, '/stop_cmd_vel', 10)
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)

        # ── 导航超时检测定时器 (1 Hz) ─────────────────────────
        self._timeout_timer = self.create_timer(1.0, self._check_nav_timeout)

        # ── 禁区初始化 ──────────────────────────────────────
        _fi_qos = QoSProfile(depth=10, reliability=QoSReliabilityPolicy.RELIABLE,
                             durability=QoSDurabilityPolicy.TRANSIENT_LOCAL,
                             history=QoSHistoryPolicy.KEEP_LAST)
        self.keepout_info_pub = self.create_publisher(
            CostmapFilterInfo, '/costmap_ctrl', _fi_qos)
        _reset_msg = CostmapFilterInfo()
        _reset_msg.type = 0
        _reset_msg.filter_mask_topic = "/keepout_mask"
        _reset_msg.base = 0.0; _reset_msg.multiplier = 1.0
        self.keepout_info_pub.publish(_reset_msg)

        self.get_logger().info("=== [Stage 2] 总控节点初始化 ===")
        self.get_logger().info(
            f"  参数: nav_timeout={self.nav_timeout}s, "
            f"qr_point=({self.qr_point_x:.2f}, {self.qr_point_y:.2f}, yaw={self.qr_point_yaw:.2f}), "
            f"entry_point=({self.entry_point_x:.2f}, {self.entry_point_y:.2f}, yaw={self.entry_point_yaw:.2f})"
        )

    # ═══════════════════════════════════════════════════════════

    def _kill_process(self, name):
        """安全终止进程 (subprocess.run 替代 os.system, 带错误检查)"""
        try:
            result = subprocess.run(
                ['pkill', '-f', name],
                capture_output=True, text=True, timeout=5.0
            )
            if result.returncode == 0:
                self.get_logger().info(f"已终止进程: {name}")
            elif result.returncode == 1:
                # pkill exit code 1 = no matching processes (not an error)
                self.get_logger().info(f"没有匹配的进程: {name}")
            else:
                self.get_logger().warn(
                    f"终止进程 {name} 返回码={result.returncode}: {result.stderr.strip()}"
                )
        except subprocess.TimeoutExpired:
            self.get_logger().error(f"终止进程 {name} 超时 (5s)")
        except FileNotFoundError:
            self.get_logger().error(f"命令 pkill 未找到，跳过终止 {name}")
        except Exception as e:
            self.get_logger().error(f"终止进程 {name} 异常: {e}")

    def qr_callback(self, msg):
        if not msg.data or self.state != 'NAV_TO_QR':
            return
        self.qr_data = msg.data
        self.get_logger().info(f"[QR检测] 内容: {msg.data}")
        self._nav_start_time = None   # 第一段导航已由 QR 拦截终止，清除超时计时

        # 关闭 ZBar 解码节点 (CPU密集), 保留 qr_decision 以获取 /qr_event (方向)
        self._kill_process('qr_decoder_zbar')
        # qr_decision 将在收到 /qr_event 后关闭 (见 _on_qr_event)
        # 如果 2s 内未收到 /qr_event, 也强制关闭
        self._qr_kill_timer = self.create_timer(2.0, self._kill_qr_decision_on_timeout)
        self.get_logger().info(">>> QR 解码已关闭, 等待方向判断 (/qr_event)...")

        if self._goal_handle is not None:
            # ★ 关键修复: 取消第一个目标后，必须等待 BT navigator 完成 follow_path halt
            # 否则立即发送第二个目标会导致竞争条件:
            #   BT abort → controller_server 停止发布 cmd_vel → nav 源超时 → IDLE
            self.get_logger().info("[QR检测] 取消当前导航目标, 等待BT完成 cancel/halt 清理...")
            self._goal_handle.cancel_goal_async()
            # 设置等待标志: get_result_callback 收到 STATUS_CANCELED 后再发送第二个目标
            self._pending_entry_nav = True
            self._pending_entry_nav_timeout = self.create_timer(
                3.0, self._entry_nav_on_cancel_timeout)
        else:
            # goal_handle 不存在 (异常/边界情况)，直接发送第二个目标
            self.get_logger().warn("[QR检测] goal_handle 为空，直接发送通道入口目标")
            self._transition_to_entry_nav()

    def _on_qr_event(self, msg):
        """qr_decision 结构化输出: {num},{direction},{x},{y}

        仅在 NAV_TO_ENTRY 阶段接收 (QR 拦截后)，解析方向用于后续通道巡航。
        收到有效方向后立即关闭 qr_decision 释放资源。
        """
        # 仅在 NAV_TO_ENTRY 或等待取消确认期间接收 qr_event
        if (self.state != 'NAV_TO_ENTRY' and not self._pending_entry_nav) or self._qr_event_received:
            return
        parts = msg.data.split(',') if msg.data else []
        if len(parts) < 2:
            return
        self._qr_direction = parts[1]  # "顺时针" 或 "逆时针"
        self._qr_event_received = True
        self.get_logger().info(f"[QR事件] 方向: {self._qr_direction} (通道巡航阶段使用)")
        # 收到方向后立即关闭 qr_decision
        self._kill_process('qr_decision')
        # 取消 2s 超时定时器
        if hasattr(self, '_qr_kill_timer') and self._qr_kill_timer is not None:
            self._qr_kill_timer.cancel()
            self._qr_kill_timer = None

    def _kill_qr_decision_on_timeout(self):
        """如果 2s 内未收到 /qr_event, 强制关闭 qr_decision 防止资源泄漏"""
        if self._qr_event_received:
            return
        self.get_logger().warn("qr_decision 2s 内未返回 /qr_event, 强制关闭")
        self._kill_process('qr_decision')
        if hasattr(self, '_qr_kill_timer') and self._qr_kill_timer is not None:
            self._qr_kill_timer.cancel()
            self._qr_kill_timer = None

    def _transition_to_entry_nav(self):
        """从 NAV_TO_QR 转换到 NAV_TO_ENTRY 状态并发送通道入口导航目标。

        仅当 BT navigator 已完成第一个目标的 cancel/halt 清理后才调用。
        调用时机: get_result_callback 收到 STATUS_CANCELED, 或超时 fallback。

        修复 keepout 边界问题:
          QR 检测后机器人停止在 keepout 边界上，SmacPlannerHybrid 拒绝
          从 lethal cell 规划路径 (报 "Starting point in lethal space!")。
          解决: 先发布后退命令 (-0.15 m/s * 1.5s ≈ 22cm), 远离边界后
          再发送通道入口导航目标。
        """
        self._pending_entry_nav = False
        # 取消 fallback 超时定时器
        if self._pending_entry_nav_timeout is not None:
            self._pending_entry_nav_timeout.cancel()
            self._pending_entry_nav_timeout = None
        # 清理重试定时器 (如果有)
        if self._retry_timer is not None:
            self._retry_timer.cancel()
            self._retry_timer = None
        # 重置 goal_handle，BT 已完成清理
        self._goal_handle = None
        # 切换到后退状态, 远离 keepout 边界后进入 NAV_TO_ENTRY
        self.state = 'BACKING_UP'
        self.get_logger().info(
            ">>> BT取消确认完成, 先后退 22cm 远离 keepout 边界再发送通道入口目标..."
        )
        self._start_backup()

    def _start_backup(self):
        """开始右后后退: 发布负速度 + 正偏航 3.0s, 撤离 keepout 边界 + 摆正车头对准通道。

        """
        self._backup_twist = Twist()
        self._backup_twist.linear.x = -0.15
        self._backup_twist.angular.z = 2.80
        self.cmd_vel_pub.publish(self._backup_twist)
        self._backup_keepalive = self.create_timer(0.1, self._backup_republish)
        self._backup_timer = self.create_timer(6.0, self._backup_stop)
        self.get_logger().info("[BACKUP] 右后退中: vx=-0.15 wz=-2.80, 6.0s")

    def _backup_republish(self):
        if self._backup_twist is not None and self.state == 'BACKING_UP':
            self.cmd_vel_pub.publish(self._backup_twist)

    def _backup_stop(self):
        if self._backup_keepalive is not None:
            self._backup_keepalive.cancel()
            self._backup_keepalive = None
        """后退完成: 发布停止, 进入 NAV_TO_ENTRY, 发送通道入口导航目标。"""
        if self._backup_timer is not None:
            self._backup_timer.cancel()
            self._backup_timer = None
        # 发布停止
        self.cmd_vel_pub.publish(Twist())
        self.stop_pub.publish(Twist())
        # 切换状态
        self.state = 'NAV_TO_ENTRY'
        self.get_logger().info(
            "[BACKUP] 后退完成, 机器人已远离 keepout 边界, 发送通道入口导航目标..."
        )
        self.send_nav_goal(
            self.entry_point_x, self.entry_point_y,
            self.entry_point_yaw, "通道入口"
        )

    def _entry_nav_on_cancel_timeout(self):
        """fallback: 如果 3s 内未收到 STATUS_CANCELED, 直接发送第二个目标。

        可能原因: goal_handle 在 cancel 前已完成 (STATUS_SUCCEEDED), 或 BT 状态异常。
        """
        if not self._pending_entry_nav:
            return
        self.get_logger().warn(
            "[超时] 等待 BT 取消确认超时 (3s), 直接发送通道入口目标 (fallback)"
        )
        self._transition_to_entry_nav()

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
            if self.state in ('NAV_TO_QR', 'NAV_TO_ENTRY'):
                self.get_logger().warn("导航目标被拒绝, 3s 后重试...")
                if self._retry_timer is not None:
                    self._retry_timer.cancel()
                self._retry_timer = self.create_timer(3.0, self._retry_nav)
            return
        if self._retry_timer is not None:
            self._retry_timer.cancel()
            self._retry_timer = None
        self._goal_handle = goal_handle
        self.get_logger().info("导航目标已接受，车辆出发...")
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def _retry_nav(self):
        if self.state == 'NAV_TO_QR':
            self.get_logger().info("重试发送导航目标 (QR点)...")
            self.send_nav_goal(self.qr_point_x, self.qr_point_y, self.qr_point_yaw, "任务发布点")
        elif self.state == 'NAV_TO_ENTRY':
            self.get_logger().info("重试发送导航目标 (通道入口)...")
            self.send_nav_goal(self.entry_point_x, self.entry_point_y, self.entry_point_yaw, "通道入口")

    def get_result_callback(self, future):
        status = future.result().status
        if status == GoalStatus.STATUS_SUCCEEDED:
            if self.state == 'NAV_TO_QR':
                if self._pending_entry_nav:
                    # QR 已检测, 但 goal 在 cancel 前已成功完成 (race)
                    # 直接过渡到通道入口导航
                    self.get_logger().info(
                        "[结果回调] QR导航目标在cancel前已完成, 直接过渡到通道入口"
                    )
                    self._nav_start_time = None
                    self._transition_to_entry_nav()
                else:
                    self.get_logger().warn("已到达任务发布点，但全程未检测到 QR 码！")
                    self._nav_start_time = None
            elif self.state == 'NAV_TO_ENTRY':
                self._nav_start_time = None
                self._finish()
        elif status == GoalStatus.STATUS_CANCELED:
            self._nav_start_time = None
            if self._pending_entry_nav:
                # ★ 关键修复: BT 已确认 cancel/halt 完成, 安全发送第二个目标
                self.get_logger().info(
                    "[结果回调] BT取消确认完成 (STATUS_CANCELED), 准备发送通道入口目标..."
                )
                self._transition_to_entry_nav()
            else:
                self.get_logger().info("导航任务已取消（QR 拦截成功）")

    # ═══════════════════════════════════════════════════════════

    def _check_nav_timeout(self):
        """定时检查导航是否超时 (1Hz 定时器回调)"""
        if self._nav_start_time is None:
            return
        if self.state not in ('NAV_TO_QR', 'NAV_TO_ENTRY'):
            return
        elapsed = (self.get_clock().now() - self._nav_start_time).nanoseconds / 1e9
        if elapsed > self.nav_timeout:
            self.get_logger().error(
                f">>> [TIMEOUT] 导航超时! 已等待 {elapsed:.1f}s > {self.nav_timeout}s, "
                f"当前状态={self.state}"
            )
            self._nav_start_time = None
            if self._goal_handle is not None:
                self._goal_handle.cancel_goal_async()
                self._goal_handle = None
            self.send_stop()
            self.state = 'TIMEOUT'
            self.get_logger().error(">>> [TIMEOUT] Stage 2 导航超时，任务失败！")

    def _start_nav(self):
        if self.state != 'INIT':
            return
        self.get_logger().info(">>> 系统就绪, 开始 Stage 2 导航")
        self.state = 'NAV_TO_QR'
        self.send_nav_goal(self.qr_point_x, self.qr_point_y, self.qr_point_yaw, "任务发布点")

    def _finish(self):
        self.send_stop()
        self.get_logger().info("")
        self.get_logger().info("=" * 60)
        self.get_logger().info(">>> [Stage 2] 任务完成！")
        self.get_logger().info(f">>> QR 原始数据: {self.qr_data}")
        if self._qr_direction:
            self.get_logger().info(f">>> QR 方向: {self._qr_direction} (通道巡航: CW=顺时针 奇数, CCW=逆时针 偶数)")
        else:
            self.get_logger().warn(">>> QR 方向未获取 (qr_decision 未返回 /qr_event)")
        self.get_logger().info(">>> 已抵达通道入口，等待下阶段扩展")
        self.get_logger().info("=" * 60)
        self.state = 'DONE'

    def run(self):
        self._start_timer = self.create_timer(8.0, self._start_nav)  # BT激活约需7.7s
        rclpy.spin(self)


def main(args=None):
    rclpy.init(args=args)
    node = CompetitionMasterStage2()
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
