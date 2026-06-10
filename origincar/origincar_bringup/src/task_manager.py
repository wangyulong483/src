#!/usr/bin/env python3
"""
task_manager — 竞赛编排节点 (管理节点)
职责: 状态机编排 + 事件处理 + 到达判断
控制执行交由 mission_controller, 本节点只发 /mission_cmd 指令
"""

import math
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int32
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseWithCovarianceStamped
from tf2_ros import Buffer, TransformListener


class Step:
    WAIT_START = 0
    TASK1_GOTO_QR = 1
    TASK2_GOTO_ENTRY = 2
    TASK2_CRUISE = 3
    TASK3_RETURN = 4
    DONE = 5

    NAMES = {
        0: "WAIT_START", 1: "TASK1_GOTO_QR", 2: "TASK2_GOTO_ENTRY",
        3: "TASK2_CRUISE", 4: "TASK3_RETURN", 5: "DONE",
    }


class TaskManager(Node):
    def __init__(self):
        super().__init__('task_manager')

        # ── 路点参数 (只读, 构造指令用) ────────────────────
        self.declare_parameter('qr_publish_point', [0.41, -3.17, 0.0])
        self.declare_parameter('channel_entry', [0.38, -1.10, 0.0])
        self.declare_parameter('channel_exit', [2.0, 2.0, 0.0])
        self.declare_parameter('p_point', [0.0, 0.0, 0.0])

        # ── 容差 & 计时 ────────────────────────────────────
        self.declare_parameter('position_tolerance', 0.15)
        self.declare_parameter('angle_tolerance', 0.30)
        self.declare_parameter('dwell_threshold_sec', 2.0)
        self.declare_parameter('task1_timeout', 90.0)
        self.declare_parameter('task2_timeout', 90.0)
        self.declare_parameter('task3_timeout', 60.0)
        self.declare_parameter('total_timeout', 180.0)

        # ── TF ────────────────────────────────────────────
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)

        # ── 订阅 ──────────────────────────────────────────
        self.sign_sub = self.create_subscription(String, '/sign', self._on_sign, 10)
        self.qr_event_sub = self.create_subscription(
            String, 'qr_event', self._on_qr_event, 10)
        self.odom_sub = self.create_subscription(Odometry, '/odom', self._on_odom, 10)
        self.amcl_sub = self.create_subscription(
            PoseWithCovarianceStamped, '/amcl_pose', self._on_amcl_pose, 10)
        self.status_sub = self.create_subscription(
            String, '/mission_status', self._on_status, 10)

        # ── 发布 (仅编排指令，不直接控制) ──────────────────
        self._mission_pub = self.create_publisher(String, '/mission_cmd', 10)
        self._heartbeat_pub = self.create_publisher(String, '/heartbeat/task_manager', 10)

        # ── 状态机 ────────────────────────────────────────
        self._step = Step.WAIT_START
        self._cmd_sent = False
        self._target_reached = False
        self._target_reached_time = 0.0

        # ── 传感器缓存 ────────────────────────────────────
        self._current_x = 0.0
        self._current_y = 0.0
        self._current_yaw = 0.0
        self._amcl_stale = True

        # ── QR 状态 ───────────────────────────────────────
        self._qr_text = None
        self._qr_number = None
        self._qr_direction = None

        # ── 计时 ──────────────────────────────────────────
        self._clock_start = None
        self._step_start_time = None
        self._penalty_sec = 0

        # ── 100ms 主循环 ──────────────────────────────────
        self._timer = self.create_timer(0.1, self._tick)

        self.get_logger().info("TaskManager 就绪 (编排模式): → /mission_cmd")

    # ═══════════════════════════════════════════════════════════
    # 回调
    # ═══════════════════════════════════════════════════════════

    def _now(self):
        return self.get_clock().now().nanoseconds / 1e9

    def _on_sign(self, msg):
        text = msg.data.strip() if msg.data else ''
        if not text or text == getattr(self, '_last_sign_text', None):
            return
        self._last_sign_text = text
        self._qr_text = text
        self.get_logger().info(f"[QR] 解码: {text}")

    def _on_qr_event(self, msg):
        """qr_decision 结构化输出: {num},{direction},{x},{y}"""
        parts = msg.data.split(',') if msg.data else []
        if len(parts) >= 2:
            self._qr_number = parts[0]
            self._qr_direction = parts[1]
            pos = f"@({parts[2]},{parts[3]})" if len(parts) >= 4 else ""
            self.get_logger().info(f"[QR事件] {self._qr_number}, {self._qr_direction} {pos}")

    def _on_odom(self, msg):
        self._current_x = msg.pose.pose.position.x
        self._current_y = msg.pose.pose.position.y
        q = msg.pose.pose.orientation
        siny = 2.0 * (q.w * q.z + q.x * q.y)
        cosy = 1.0 - 2.0 * (q.y * q.y + q.z * q.z)
        self._current_yaw = math.atan2(siny, cosy)
        stamp = msg.header.stamp
        age = self._now() - (stamp.sec + stamp.nanosec * 1e-9)
        if age > 0.5:
            self.get_logger().warn(f"/odom 数据过期 ({age:.2f}s)", throttle_duration_sec=2.0)

    def _on_amcl_pose(self, msg):
        cov = msg.pose.covariance
        self._amcl_stale = False
        self._amcl_cov_xy = max(cov[0], cov[7])
        self._amcl_cov_yaw = cov[35]

    def _on_status(self, msg):
        if 'server_not_ready' in msg.data:
            self._cmd_sent = False  # 允许重试, 下个 tick 重新发送 /mission_cmd

    # ═══════════════════════════════════════════════════════════
    # 编排指令 (每个状态只发一次)
    # ═══════════════════════════════════════════════════════════

    def _send_mission_cmd(self, cmd):
        if self._cmd_sent:
            return
        self._mission_pub.publish(String(data=cmd))
        self._cmd_sent = True
        self.get_logger().info(f"[编排] → mission_cmd: {cmd}")

    # ═══════════════════════════════════════════════════════════
    # 主循环
    # ═══════════════════════════════════════════════════════════

    def _tick(self):
        self._heartbeat_pub.publish(String(data=f"step={Step.NAMES.get(self._step,'?')}"))
        self._check_total_timeout()
        if self._step == Step.WAIT_START:
            self._tick_wait_start()
        elif self._step == Step.TASK1_GOTO_QR:
            self._tick_task1()
        elif self._step == Step.TASK2_GOTO_ENTRY:
            self._tick_task2_entry()
        elif self._step == Step.TASK2_CRUISE:
            self._tick_task2_cruise()
        elif self._step == Step.TASK3_RETURN:
            self._tick_task3()

    # ═══════════════════════════════════════════════════════════
    # 到达确认
    # ═══════════════════════════════════════════════════════════

    def _check_arrival(self, target_x, target_y, target_yaw=None):
        pos_tol = self.get_parameter('position_tolerance').value
        ang_tol = self.get_parameter('angle_tolerance').value
        dwell_th = self.get_parameter('dwell_threshold_sec').value

        px, py, pyaw = self._current_x, self._current_y, self._current_yaw

        dx = px - target_x
        dy = py - target_y
        dist = math.sqrt(dx * dx + dy * dy)

        pos_ok = dist <= pos_tol
        ang_ok = True
        if target_yaw is not None:
            diff = abs(self._normalize_angle(pyaw - target_yaw))
            ang_ok = diff <= ang_tol

        if pos_ok and ang_ok:
            if not self._target_reached:
                self._target_reached = True
                self._target_reached_time = self._now()
                self.get_logger().info(f"到达目标附近 (dist={dist:.3f}), 开始驻留计时...")
        else:
            self._target_reached = False

        if self._target_reached:
            elapsed = self._now() - self._target_reached_time
            if elapsed >= dwell_th:
                self.get_logger().info(f"驻留确认 ({elapsed:.1f}s >= {dwell_th}s)")
                return True
        return False

    @staticmethod
    def _normalize_angle(a):
        while a > math.pi:
            a -= 2.0 * math.pi
        while a < -math.pi:
            a += 2.0 * math.pi
        return a

    # ═══════════════════════════════════════════════════════════
    # 状态切换
    # ═══════════════════════════════════════════════════════════

    def _goto_step(self, new_step):
        old = Step.NAMES.get(self._step, '?')
        new = Step.NAMES.get(new_step, '?')
        self.get_logger().info(f"[状态机] {old} → {new}")
        self._step = new_step
        self._cmd_sent = False
        self._target_reached = False
        self._target_reached_time = 0.0
        self._step_start_time = self._now()

    # ═══════════════════════════════════════════════════════════
    # WAIT_START
    # ═══════════════════════════════════════════════════════════

    def _check_map_odom_available(self):
        try:
            self.tf_buffer.lookup_transform('map', 'odom', rclpy.time.Time())
        except Exception:
            return False
        if not self._amcl_stale:
            if getattr(self, '_amcl_cov_xy', 999.0) > 0.25 or \
               getattr(self, '_amcl_cov_yaw', 999.0) > 0.09:
                self.get_logger().warn(
                    f"AMCL 未收敛", throttle_duration_sec=3.0)
                return False
        return True

    def _tick_wait_start(self):
        if not self._check_map_odom_available():
            self.get_logger().info("等待定位就绪...", throttle_duration_sec=2.0)
            return
        self.get_logger().info("定位就绪, 比赛开始!")
        self._clock_start = self._now()
        self._goto_step(Step.TASK1_GOTO_QR)

    # ═══════════════════════════════════════════════════════════
    # TASK1: 前往QR发布点
    # ═══════════════════════════════════════════════════════════

    def _tick_task1(self):
        if self._qr_text is not None:
            self.get_logger().info("途中扫到QR, 提前结束任务1")
            self._goto_step(Step.TASK2_GOTO_ENTRY)
            return

        qr_pt = self.get_parameter('qr_publish_point').value
        self._send_mission_cmd(f"goto:{qr_pt[0]},{qr_pt[1]},{qr_pt[2]}")

        if self._check_arrival(qr_pt[0], qr_pt[1], qr_pt[2]):
            self.get_logger().warn("到达QR发布点但未扫到码, 继续等待...")
        self._check_step_timeout(Step.TASK1_GOTO_QR)

    # ═══════════════════════════════════════════════════════════
    # TASK2_ENTRY
    # ═══════════════════════════════════════════════════════════

    def _tick_task2_entry(self):
        entry = self.get_parameter('channel_entry').value
        self._send_mission_cmd(f"goto:{entry[0]},{entry[1]},{entry[2]}")
        if self._check_arrival(entry[0], entry[1], entry[2]):
            self._goto_step(Step.TASK2_CRUISE)
        self._check_step_timeout(Step.TASK2_GOTO_ENTRY)

    # ═══════════════════════════════════════════════════════════
    # TASK2_CRUISE
    # ═══════════════════════════════════════════════════════════

    def _tick_task2_cruise(self):
        if self._qr_direction is None:
            return

        if "逆时针" in self._qr_direction:
            self._send_mission_cmd("through:ccw")
        else:
            self._send_mission_cmd("through:cw")

        exit_pt = self.get_parameter('channel_exit').value
        if self._check_arrival(exit_pt[0], exit_pt[1], exit_pt[2]):
            self._goto_step(Step.TASK3_RETURN)
        self._check_step_timeout(Step.TASK2_CRUISE)

    # ═══════════════════════════════════════════════════════════
    # TASK3: 返航
    # ═══════════════════════════════════════════════════════════

    def _tick_task3(self):
        p_pt = self.get_parameter('p_point').value
        self._send_mission_cmd(f"goto:{p_pt[0]},{p_pt[1]},{p_pt[2]}")
        if self._check_arrival(p_pt[0], p_pt[1], p_pt[2]):
            self._send_mission_cmd("stop")
            self.get_logger().info("到达P点, 精准停车完成!")
            self._goto_step(Step.DONE)
            self._print_summary()
        self._check_step_timeout(Step.TASK3_RETURN)

    # ═══════════════════════════════════════════════════════════
    # 超时
    # ═══════════════════════════════════════════════════════════

    def _check_step_timeout(self, step):
        if self._step_start_time is None:
            return
        elapsed = self._now() - self._step_start_time
        limits = {
            Step.TASK1_GOTO_QR: self.get_parameter('task1_timeout').value,
            Step.TASK2_GOTO_ENTRY: self.get_parameter('task2_timeout').value,
            Step.TASK2_CRUISE: self.get_parameter('task2_timeout').value,
            Step.TASK3_RETURN: self.get_parameter('task3_timeout').value,
        }
        limit = limits.get(step, 999.0)
        if elapsed > limit:
            self.get_logger().error(f"{Step.NAMES.get(step, '?')} 超时 +50s罚时")
            self._penalty_sec += 50
            next_step = {
                Step.TASK1_GOTO_QR: Step.TASK2_GOTO_ENTRY,
                Step.TASK2_GOTO_ENTRY: Step.TASK2_CRUISE,
                Step.TASK2_CRUISE: Step.TASK3_RETURN,
                Step.TASK3_RETURN: Step.DONE,
            }
            self._goto_step(next_step.get(step, Step.DONE))

    def _check_total_timeout(self):
        if self._clock_start is None:
            return
        elapsed = self._now() - self._clock_start
        if elapsed > self.get_parameter('total_timeout').value:
            self.get_logger().error(f"全局超时 ({elapsed:.1f}s > 180s), 比赛结束")
            self._send_mission_cmd("stop")
            self._goto_step(Step.DONE)
            self._print_summary()

    def _print_summary(self):
        elapsed = self._now() - (self._clock_start or self._now())
        self.get_logger().info(f"===== 比赛结束 =====")
        self.get_logger().info(f"总用时: {elapsed:.1f}s | 罚时: {self._penalty_sec}s")
        self.get_logger().info(f"最终成绩: {elapsed + self._penalty_sec:.1f}s")


def main(args=None):
    rclpy.init(args=args)
    node = TaskManager()
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
