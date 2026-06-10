#!/usr/bin/env python3
"""
pose_pid_corrector — 位姿环 PID 校正节点
参考 amphibious_analysis.md: §2.2 (全局→本体坐标 PID) + §2.3 (Dead Zone)

激活方式: task_manager 发布 /target_pose → 节点在接近目标 (<activate_range) 时接管控制,
         global→local 坐标变换后在机器人本体系做 PID, 输出校正后的 /pid_cmd_vel.
         无目标时静默 (不发布), 依赖 cmd_vel_mux 的 pid_timeout (0.3s) 自动回退到
         低优先级 Nav2 通道.

BUGFIX (2026-06-10): idle-publish bug
  旧行为: _target_pose is None 时每 30Hz 发布 self._last_rpp_cmd (零 Twist) 到
          /pid_cmd_vel. 该 topic 在 cmd_vel_mux 中 priority=20, 高于 Nav2 的
          /nav_cmd_vel (priority=10), 且从不超时 (持续收到消息), 因此永久阻塞
          所有 Nav2 指令.
  新行为: 无目标时完全不发布. mux pid_timeout (0.3s) 到期后, nav 通道接管.
         有目标时正常发布; 到达目标后停止, 清空目标, 发布单次
         /target_pose_cancel 通知 task_manager.
"""

import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, PoseStamped, PoseWithCovarianceStamped
from nav_msgs.msg import Odometry
from std_msgs.msg import Bool, String, Empty


class DeadZonePID:
    """§2.3: 带死区的增量式 PID 控制器"""

    def __init__(self, kp, ki, kd, dead_zone, max_output, max_i):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.dead_zone = dead_zone
        self.max_output = max_output
        self.max_i = max_i
        self._integral = 0.0
        self._prev_error = 0.0
        self._prev_output = 0.0

    def reset(self):
        self._integral = 0.0
        self._prev_error = 0.0
        self._prev_output = 0.0

    def compute(self, error, dt):
        if dt <= 0.0:
            return self._prev_output

        # §2.3: 死区—清零积分防止 windup, 输出零
        if abs(error) < self.dead_zone:
            self._integral = 0.0
            self._prev_output = 0.0
            self._prev_error = error
            return 0.0

        self._integral += error * dt
        if self._integral > self.max_i:
            self._integral = self.max_i
        elif self._integral < -self.max_i:
            self._integral = -self.max_i

        derivative = (error - self._prev_error) / dt
        output = self.kp * error + self.ki * self._integral + self.kd * derivative

        if output > self.max_output:
            output = self.max_output
        elif output < -self.max_output:
            output = -self.max_output

        self._prev_error = error
        self._prev_output = output
        return output


class PosePIDCorrector(Node):
    def __init__(self):
        super().__init__('pose_pid_corrector')

        # ── 参数 ──────────────────────────────────────────
        # 激活距离: 目标在此范围内才启用 PID 接管
        self.declare_parameter('activate_range', 0.5)
        # 混合过渡下限: activate_range→blend_range 之间线性混合 RPP+PID, blend_range以内纯PID
        self.declare_parameter('blend_range', 0.25)

        # PID: 前进方向 (x_local)
        self.declare_parameter('kp_x', 1.2)
        self.declare_parameter('ki_x', 0.05)
        self.declare_parameter('kd_x', 0.1)
        self.declare_parameter('dead_zone_x', 0.02)       # §2.3: 2cm
        self.declare_parameter('max_vx', 0.40)             # 精确靠近时限速

        # PID: 偏航 (yaw)
        self.declare_parameter('kp_yaw', 1.0)
        self.declare_parameter('ki_yaw', 0.02)
        self.declare_parameter('kd_yaw', 0.05)
        self.declare_parameter('dead_zone_yaw', 0.03)      # §2.3: ~1.7°
        self.declare_parameter('max_vyaw', 0.80)

        # Ackermann
        self.declare_parameter('wheelbase', 0.143)

        # 目标达到后等待确认时间: 误差连续在死区内 settle_time 秒才视为到达
        self.declare_parameter('settle_time', 0.5)

        # ── PID 实例 ──────────────────────────────────────
        self._pid_x = self._make_pid('x')
        self._pid_yaw = self._make_pid('yaw')

        # ── AMCL 定位质量 ──────────────────────────────────
        self.declare_parameter('localization_quality_check', True)
        self.declare_parameter('max_pos_cov', 0.25)   # 位置方差上限 (σ=0.5m)
        self.declare_parameter('max_yaw_cov', 0.09)   # 角度方差上限 (σ=0.3rad)
        self._amcl_cov_xy = 0.0
        self._amcl_cov_yaw = 0.0
        self._localization_ok = True

        # ── 状态 ──────────────────────────────────────────
        self._current_x = 0.0
        self._current_y = 0.0
        self._current_yaw = 0.0
        self._target_pose = None           # [x, y, yaw] | None
        self._last_time = None
        self._active = False
        self._settle_start_time = None     # 误差首次进入死区的时刻 (None = 未进入)

        # ── 订阅 ──────────────────────────────────────────
        self._odom_sub = self.create_subscription(
            Odometry, '/odom', self._on_odom, 10)
        self._target_sub = self.create_subscription(
            PoseStamped, '/target_pose', self._on_target, 10)
        self._rpp_cmd_sub = self.create_subscription(
            Twist, '/rpp_cmd_vel', self._on_rpp_cmd, 10)
        self._amcl_sub = self.create_subscription(
            PoseWithCovarianceStamped, '/amcl_pose', self._on_amcl_pose, 10)
        self._target_cancel_sub = self.create_subscription(
            Empty, '/target_pose_cancel', self._on_target_cancel, 10)

        # ── 发布 ──────────────────────────────────────────
        self._cmd_pub = self.create_publisher(Twist, '/pid_cmd_vel', 10)
        self._active_pub = self.create_publisher(Bool, '/pid_active', 10)
        self._heartbeat_pub = self.create_publisher(String, '/heartbeat/pose_pid_corrector', 10)
        # 到达目标时通知 task_manager (与 cancel 共用话题, 双向信号)
        self._target_cancel_pub = self.create_publisher(Empty, '/target_pose_cancel', 10)

        # ── 控制循环 30Hz ─────────────────────────────────
        self._timer = self.create_timer(1.0 / 30.0, self._control_loop)

        # ── 透传 ──────────────────────────────────────────
        self._last_rpp_cmd = Twist()

        self.get_logger().info("PosePIDCorrector 就绪 (global→local + dead_zone, idle=静默)")

    # ═══════════════════════════════════════════════════════════
    def _make_pid(self, prefix):
        return DeadZonePID(
            kp=self.get_parameter(f'kp_{prefix}').value,
            ki=self.get_parameter(f'ki_{prefix}').value,
            kd=self.get_parameter(f'kd_{prefix}').value,
            dead_zone=self.get_parameter(f'dead_zone_{prefix}').value,
            max_output=self.get_parameter(f'max_v{prefix}').value,
            max_i=self.get_parameter(f'max_v{prefix}').value * 0.5,
        )

    def _reload_pid_params(self):
        for prefix in ['x', 'yaw']:
            self._pid_x.kp = self.get_parameter('kp_x').value
            self._pid_x.ki = self.get_parameter('ki_x').value
            self._pid_x.kd = self.get_parameter('kd_x').value
            self._pid_x.dead_zone = self.get_parameter('dead_zone_x').value
            self._pid_x.max_output = self.get_parameter('max_vx').value
            self._pid_yaw.kp = self.get_parameter('kp_yaw').value
            self._pid_yaw.ki = self.get_parameter('ki_yaw').value
            self._pid_yaw.kd = self.get_parameter('kd_yaw').value
            self._pid_yaw.dead_zone = self.get_parameter('dead_zone_yaw').value
            self._pid_yaw.max_output = self.get_parameter('max_vyaw').value

    # ═══════════════════════════════════════════════════════════
    def _on_odom(self, msg):
        self._current_x = msg.pose.pose.position.x
        self._current_y = msg.pose.pose.position.y
        q = msg.pose.pose.orientation
        siny = 2.0 * (q.w * q.z + q.x * q.y)
        cosy = 1.0 - 2.0 * (q.y * q.y + q.z * q.z)
        self._current_yaw = math.atan2(siny, cosy)
        # §检查点: /odom 数据时效
        stamp = msg.header.stamp
        age = self.get_clock().now().nanoseconds / 1e9 - (stamp.sec + stamp.nanosec * 1e-9)
        if age > 0.5:
            self.get_logger().warn(f"/odom 数据过期 ({age:.2f}s)", throttle_duration_sec=2.0)

    def _on_target(self, msg):
        q = msg.pose.orientation
        siny = 2.0 * (q.w * q.z + q.x * q.y)
        cosy = 1.0 - 2.0 * (q.y * q.y + q.z * q.z)
        yaw = math.atan2(siny, cosy)
        self._target_pose = [msg.pose.position.x, msg.pose.position.y, yaw]
        # 新目标到达, 清除任何进行中的 settle 计时
        self._settle_start_time = None
        self.get_logger().info(
            f"新目标: ({msg.pose.position.x:.2f}, {msg.pose.position.y:.2f}, yaw={yaw:.2f})")

    def _on_rpp_cmd(self, msg):
        self._last_rpp_cmd = msg

    def _on_amcl_pose(self, msg):
        cov = msg.pose.covariance
        self._amcl_cov_xy = max(cov[0], cov[7])
        self._amcl_cov_yaw = cov[35]

    def _on_target_cancel(self, msg):
        """外部取消信号 — 清空目标, 停止发布."""
        if self._target_pose is not None:
            self.get_logger().info("[pose_pid] CANCEL external cancel, clearing target")
            self._target_pose = None
            self._settle_start_time = None
            self._deactivate()

    # ═══════════════════════════════════════════════════════════
    # §2.2: 全局坐标 → 机器人本体坐标
    # ═══════════════════════════════════════════════════════════

    @staticmethod
    def _global_to_local(gx, gy, yaw):
        """将全局误差旋转到机器人本体坐标系"""
        lx = math.cos(yaw) * gx + math.sin(yaw) * gy
        ly = -math.sin(yaw) * gx + math.cos(yaw) * gy
        return lx, ly

    @staticmethod
    def _normalize_angle(a):
        while a > math.pi:
            a -= 2.0 * math.pi
        while a < -math.pi:
            a += 2.0 * math.pi
        return a

    # ═══════════════════════════════════════════════════════════
    # 30Hz 控制循环
    # ═══════════════════════════════════════════════════════════

    def _control_loop(self):
        # 心跳总是发布 (独立 topic, 不影响 mux)
        self._heartbeat_pub.publish(String(data=f"active={self._active}"))

        now = self.get_clock().now().nanoseconds / 1e9
        dt = now - self._last_time if self._last_time else 0.033
        self._last_time = now

        self._reload_pid_params()

        # ══════════════════════════════════════════════════════
        # FIX: 无目标时静默 — 不发布任何内容到 /pid_cmd_vel
        # cmd_vel_mux 的 pid_timeout (0.3s) 到期后, Nav2 /nav_cmd_vel (priority 10) 接管
        # ══════════════════════════════════════════════════════
        if self._target_pose is None:
            if self._active:
                self._deactivate()
            # 不发布 — 让 mux 超时
            return

        tx, ty, tyaw = self._target_pose

        # §2.2 Step 1: 全局坐标系位置误差
        ex_global = tx - self._current_x
        ey_global = ty - self._current_y
        dist = math.sqrt(ex_global ** 2 + ey_global ** 2)

        activate_range = self.get_parameter('activate_range').value
        blend_range = self.get_parameter('blend_range').value

        # ══════════════════════════════════════════════════════
        # FIX: 超出激活范围 — 不发布, 让 mux 超时回退到 Nav2
        # ══════════════════════════════════════════════════════
        if dist > activate_range:
            if self._active:
                self._deactivate()
            # 不发布 — 让 mux 超时
            return

        # 定位质量检查: AMCL 协方差过大 → 拒绝 PID 接管
        if self.get_parameter('localization_quality_check').value:
            max_cov_xy = self.get_parameter('max_pos_cov').value
            max_cov_yaw = self.get_parameter('max_yaw_cov').value
            if self._amcl_cov_xy > max_cov_xy or self._amcl_cov_yaw > max_cov_yaw:
                if self._active:
                    self.get_logger().warn(
                        f"[pose_pid] DEACTIVATED 定位质量差 → 释放控制: "
                        f"σ_xy={math.sqrt(self._amcl_cov_xy):.2f}m "
                        f"σ_yaw={math.sqrt(self._amcl_cov_yaw):.2f}rad",
                        throttle_duration_sec=2.0)
                    self._deactivate()
                # 不发布 — 让 mux 超时
                return

        # ══════════════════════════════════════════════════════
        # 激活 PID 跟踪 (首次进入范围)
        # ══════════════════════════════════════════════════════
        if not self._active:
            self.get_logger().info(
                f"[pose_pid] ACTIVATED dist={dist:.3f}m < {activate_range}m "
                f"→ target=({tx:.2f}, {ty:.2f}, yaw={tyaw:.2f})")
            self._active = True
            self._publish_active(True)
            self._settle_start_time = None

        # §2.2 Step 2: 旋转到机器人本体坐标系
        ex_local, ey_local = self._global_to_local(ex_global, ey_global, self._current_yaw)

        # §2.2 Step 3: 本体坐标系 PID
        vx_pid = self._pid_x.compute(ex_local, dt)

        eyaw = self._normalize_angle(tyaw - self._current_yaw)
        vw_pid = self._pid_yaw.compute(eyaw, dt)

        # §2.2 Step 4: PID 指令 → Ackermann 合成
        pid_cmd = Twist()
        pid_cmd.linear.x = vx_pid
        if abs(vx_pid) > 0.01:
            wheelbase = self.get_parameter('wheelbase').value
            pid_cmd.angular.z = vx_pid * math.tan(
                max(-1.2, min(1.2, vw_pid * wheelbase / vx_pid))) / wheelbase
        else:
            pid_cmd.angular.z = 0.0

        # §2.6: 混合过渡带 — activate_range→blend_range 线性融合 RPP+PID
        if dist > blend_range:
            alpha = (activate_range - dist) / max(activate_range - blend_range, 0.01)
            alpha = max(0.0, min(1.0, alpha))
            rpp = self._last_rpp_cmd
            cmd = Twist()
            cmd.linear.x = (1.0 - alpha) * rpp.linear.x + alpha * pid_cmd.linear.x
            cmd.angular.z = (1.0 - alpha) * rpp.angular.z + alpha * pid_cmd.angular.z
        else:
            cmd = pid_cmd

        self._cmd_pub.publish(cmd)

        # ══════════════════════════════════════════════════════
        # 目标达到检测 — 按 settle_time 确认后停止发布
        # ══════════════════════════════════════════════════════
        settle_time = self.get_parameter('settle_time').value

        if abs(ex_local) < self._pid_x.dead_zone and abs(eyaw) < self._pid_yaw.dead_zone:
            if self._settle_start_time is None:
                self._settle_start_time = now
            elif (now - self._settle_start_time) >= settle_time:
                self.get_logger().info(
                    f"[pose_pid] TARGET_REACHED dist={dist:.3f}m "
                    f"ex_local={ex_local:.3f}m eyaw={eyaw:.3f}rad "
                    f"→ settled {settle_time}s, deactivating")
                self._target_pose = None
                self._settle_start_time = None
                self._deactivate()
                # 通知 task_manager 位姿任务已完成
                self._target_cancel_pub.publish(Empty())
        else:
            # 误差离开死区, 重置 settle 计时
            self._settle_start_time = None

    # ═══════════════════════════════════════════════════════════

    def _deactivate(self):
        """停用 PID: 重置积分器, 标记 inactive, 记录日志."""
        if not self._active:
            return
        self._pid_x.reset()
        self._pid_yaw.reset()
        self._active = False
        self._settle_start_time = None
        self._publish_active(False)
        self.get_logger().info("[pose_pid] DEACTIVATED → mux pid_timeout 后 Nav2 接管")

    def _publish_active(self, active):
        msg = Bool()
        msg.data = active
        self._active_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = PosePIDCorrector()
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
