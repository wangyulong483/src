#!/usr/bin/env python3
"""
velocity_pid — 速度环 PID 校正节点 (POST-mux 编码器反馈闭环)
订阅期望速度 (/cmd_vel_muxed, 来自 cmd_vel_mux 仲裁器) 和编码器反馈 (/robotvel)，
通过增量式 PID 校正后发布 /cmd_vel_corrected，形成轮速反馈闭环。

架构位置 (POST-mux, 非 mux 输入):
  Nav2 /cmd_vel ─┐
                 ├─► cmd_vel_mux ─► /cmd_vel_muxed ─► velocity_pid ─► /cmd_vel_corrected ─► STM32
  /stop_cmd_vel ─┘    (仲裁器)                        (编码器反馈闭环)     (最终底盘指令)
          /pid_cmd_vel (pose_pid_corrector, 未启用)

注意: cmd_vel_mux 的 "pid" 通道 (priority 20, /pid_cmd_vel) 是给 pose_pid_corrector
(外环位置校正) 的，与本节点 velocity_pid (内环速度校正) 是不同的控制层级。
velocity_pid 位于 mux 下游，对所有通过仲裁的速度指令做统一的编码器反馈补偿。
"""

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool
from origincar_msg.msg import Data


class IncrementalPID:
    """增量式 (velocity form) PID 控制器，带独立积分限幅.

    数学等价形式 (位置式分解):
        u(k) = Kp * e(k) + I(k) + Kd * [e(k) - e(k-1)] / dt

        其中 I(k) = clamp( I(k-1) + Ki * e(k) * dt,  -max_i, max_i )

    此形式与经典增量式 (Δu = Kp*Δe + Ki*e*dt + Kd*Δ²e/dt, u += Δu)
    在无积分限幅时数值等价，但允许通过 max_i 对积分项独立限幅，
    防止机器人被卡住时积分饱和 (integral windup)。
    """

    def __init__(self, kp, ki, kd, max_out, max_i):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.max_out = max_out
        self._max_i = max_i
        self._e = [0.0, 0.0, 0.0]        # e(k), e(k-1), e(k-2)
        self._out = 0.0
        self._integral = 0.0              # 独立积分累加器 (受 max_i 限幅)

    def reset(self):
        self._e = [0.0, 0.0, 0.0]
        self._out = 0.0
        self._integral = 0.0

    def compute(self, target, actual, dt):
        if dt <= 0.0:
            return self._out

        # 移位误差历史
        self._e[2] = self._e[1]
        self._e[1] = self._e[0]
        self._e[0] = target - actual

        # ── 位置式分解 (与增量式数值等价) ─────────────────
        p_out = self.kp * self._e[0]
        d_out = self.kd * (self._e[0] - self._e[1]) / dt

        # 积分累加 + 独立限幅 (抗积分饱和)
        self._integral += self.ki * self._e[0] * dt
        if self._integral > self._max_i:
            self._integral = self._max_i
        elif self._integral < -self._max_i:
            self._integral = -self._max_i

        self._out = p_out + self._integral + d_out

        # 输出限幅 (belt-and-suspenders: max_i 限积分 + max_out 限总和)
        if self._out > self.max_out:
            self._out = self.max_out
        elif self._out < -self.max_out:
            self._out = -self.max_out

        return self._out


class VelocityPID(Node):
    def __init__(self):
        super().__init__('velocity_pid')

        # ── 参数 ──────────────────────────────────────────
        self.declare_parameter('kp_vx', 0.8)
        self.declare_parameter('ki_vx', 0.6)
        self.declare_parameter('kd_vx', 0.05)
        self.declare_parameter('max_vx', 0.85)
        self.declare_parameter('kp_wz', 1.0)
        self.declare_parameter('ki_wz', 0.4)
        self.declare_parameter('kd_wz', 0.02)
        self.declare_parameter('max_wz', 2.8)
        self.declare_parameter('max_i_fraction', 0.8)
        self.declare_parameter('feedback_timeout', 0.5)
        self.declare_parameter('enable_pid', True)

        max_i_vx = self.get_parameter('max_vx').value * self.get_parameter('max_i_fraction').value
        max_i_wz = self.get_parameter('max_wz').value * self.get_parameter('max_i_fraction').value

        self._pid_vx = IncrementalPID(
            kp=self.get_parameter('kp_vx').value,
            ki=self.get_parameter('ki_vx').value,
            kd=self.get_parameter('kd_vx').value,
            max_out=self.get_parameter('max_vx').value,
            max_i=max_i_vx,
        )
        self._pid_wz = IncrementalPID(
            kp=self.get_parameter('kp_wz').value,
            ki=self.get_parameter('ki_wz').value,
            kd=self.get_parameter('kd_wz').value,
            max_out=self.get_parameter('max_wz').value,
            max_i=max_i_wz,
        )

        # ── 状态 ──────────────────────────────────────────
        self._actual_vx = 0.0
        self._actual_wz = 0.0
        self._feedback_stale = True
        self._last_feedback_time = self.get_clock().now()
        self._last_cmd_time = self.get_clock().now()
        self._last_control_time = self.get_clock().now()
        self._last_desired_vx = 0.0
        self._last_desired_wz = 0.0
        self._prev_desired_vx = 0.0       # 上一控制周期的期望值 (用于方向切换检测)
        self._prev_desired_wz = 0.0
        self._last_dir_switch_time_vx = self.get_clock().now()
        self._last_dir_switch_time_wz = self.get_clock().now()
        self._active = False
        self._pid_out_vx = 0.0
        self._pid_out_wz = 0.0

        # ── 订阅 ──────────────────────────────────────────
        self._cmd_sub = self.create_subscription(
            Twist, '/cmd_vel_muxed', self._on_cmd_vel, 10)
        self._robotvel_sub = self.create_subscription(
            Data, '/robotvel', self._on_robotvel, 10)

        # ── 发布 ──────────────────────────────────────────
        self._cmd_pub = self.create_publisher(Twist, '/cmd_vel_corrected', 10)
        self._active_pub = self.create_publisher(Bool, '/velocity_pid_active', 10)

        # ── 30Hz 控制循环 ─────────────────────────────────
        self._timer = self.create_timer(1.0 / 30.0, self._control_loop)

        self.get_logger().info(
            f"VelocityPID 就绪: vx(Kp={self._pid_vx.kp:.1f}, Ki={self._pid_vx.ki:.2f}, Kd={self._pid_vx.kd:.2f}, max_i={max_i_vx:.2f}) "
            f"wz(Kp={self._pid_wz.kp:.1f}, Ki={self._pid_wz.ki:.2f}, Kd={self._pid_wz.kd:.2f}, max_i={max_i_wz:.2f}) "
            f"| feedback_timeout={self.get_parameter('feedback_timeout').value}s"
        )

    # ═══════════════════════════════════════════════════════════

    def _on_cmd_vel(self, msg):
        was_inactive = not self._active
        self._last_desired_vx = msg.linear.x
        self._last_desired_wz = msg.angular.z
        self._last_cmd_time = self.get_clock().now()
        self._active = True
        if was_inactive:
            self.get_logger().info(
                f"[vel_pid] ACTIVATED vx={msg.linear.x:.2f} wz={msg.angular.z:.2f}")

    def _on_robotvel(self, msg):
        self._actual_vx = msg.x   # Robot_Vel.X (forward speed, m/s)
        self._actual_wz = msg.z   # Robot_Vel.Z (angular speed, rad/s)
        self._last_feedback_time = self.get_clock().now()
        self._feedback_stale = False

    # ═══════════════════════════════════════════════════════════

    def _control_loop(self):
        now = self.get_clock().now()

        # 使用实际经过时间，而非假定定时器精确 30Hz
        dt = (now - self._last_control_time).nanoseconds / 1e9
        if dt <= 0.0 or dt > 1.0:
            dt = 1.0 / 30.0
        self._last_control_time = now

        # 重载 PID 参数
        self._pid_vx.kp = self.get_parameter('kp_vx').value
        self._pid_vx.ki = self.get_parameter('ki_vx').value
        self._pid_vx.kd = self.get_parameter('kd_vx').value
        self._pid_wz.kp = self.get_parameter('kp_wz').value
        self._pid_wz.ki = self.get_parameter('ki_wz').value
        self._pid_wz.kd = self.get_parameter('kd_wz').value
        # max_i 依赖 max_out 和 max_i_fraction，运行时可变
        max_i_frac = self.get_parameter('max_i_fraction').value
        self._pid_vx._max_i = self.get_parameter('max_vx').value * max_i_frac
        self._pid_wz._max_i = self.get_parameter('max_wz').value * max_i_frac
        enable = self.get_parameter('enable_pid').value

        # 超时检查: cmd_vel 超过 0.3s 未更新 → 停止
        cmd_age = (now - self._last_cmd_time).nanoseconds / 1e9
        if cmd_age > 0.3:
            if self._active:
                self.get_logger().info(
                    f"[vel_pid] CMD_TIMEOUT cmd_vel age={cmd_age:.2f}s > 0.3s, stopping")
                self._pid_vx.reset()
                self._pid_wz.reset()
                self._active = False
                self._publish_active(False)
            self._cmd_pub.publish(Twist())
            return

        # 反馈超时 → 退化为开环直通
        feedback_timeout = self.get_parameter('feedback_timeout').value
        feedback_age = (now - self._last_feedback_time).nanoseconds / 1e9
        self._feedback_stale = feedback_age > feedback_timeout

        if not enable or self._feedback_stale:
            if self._feedback_stale and self._active:
                self.get_logger().warn(
                    f"/robotvel 反馈超时 ({feedback_age:.2f}s > {feedback_timeout}s), 退化为直通",
                    throttle_duration_sec=3.0)
            cmd = Twist()
            cmd.linear.x = self._last_desired_vx
            cmd.angular.z = self._last_desired_wz
            self._cmd_pub.publish(cmd)
            return

        # 方向切换检测: 比较当前期望符号与前一周期期望符号 (而非PID输出符号)
        # BUGFIX: OLD checked sign(desired) != sign(pid_out) — PID输出物理上跟不上
        #   RPP 10Hz快速变化, 在积分项还没积累时就触发重置, 导致每周期都重置 (50次/3秒)
        # NEW: sign(current_desired) != sign(previous_desired) — 真正的指令方向变化
        # 双重保护: (1) dt < 15ms ( >66Hz ) 跳过检测 (2) 两次重置间隔 >= 250ms (防抖)
        desired_vx = self._last_desired_vx
        desired_wz = self._last_desired_wz
        MIN_DIR_SWITCH_DT = 0.015       # dt过短 → 高频噪声, 抑制
        MIN_RESET_INTERVAL = 0.25        # 两次重置最小间隔, 防高频振荡

        if dt >= MIN_DIR_SWITCH_DT:
            # ── vx channel ──
            dir_switch_vx = (self._prev_desired_vx != 0.0 and desired_vx != 0.0 and
                             (desired_vx * self._prev_desired_vx) < 0.0)
            if dir_switch_vx:
                since_last = (now - self._last_dir_switch_time_vx).nanoseconds / 1e9
                if since_last >= MIN_RESET_INTERVAL:
                    self.get_logger().info(
                        f"[vel_pid] DIR_SWITCH vx prev_desired={self._prev_desired_vx:.2f} -> "
                        f"current={desired_vx:.2f} dt={dt:.4f}s, resetting")
                    self._pid_vx.reset()
                    self._last_dir_switch_time_vx = now

            # ── wz channel ──
            dir_switch_wz = (self._prev_desired_wz != 0.0 and desired_wz != 0.0 and
                             (desired_wz * self._prev_desired_wz) < 0.0)
            if dir_switch_wz:
                since_last = (now - self._last_dir_switch_time_wz).nanoseconds / 1e9
                if since_last >= MIN_RESET_INTERVAL:
                    self.get_logger().info(
                        f"[vel_pid] DIR_SWITCH wz prev_desired={self._prev_desired_wz:.2f} -> "
                        f"current={desired_wz:.2f} dt={dt:.4f}s, resetting")
                    self._pid_wz.reset()
                    self._last_dir_switch_time_wz = now

        # 保存本周期期望值供下周期方向比较
        self._prev_desired_vx = desired_vx
        self._prev_desired_wz = desired_wz

        # PID 计算
        self._pid_out_vx = self._pid_vx.compute(
            desired_vx, self._actual_vx, dt)
        self._pid_out_wz = self._pid_wz.compute(
            self._last_desired_wz, self._actual_wz, dt)

        cmd = Twist()
        cmd.linear.x = self._pid_out_vx
        cmd.angular.z = self._pid_out_wz
        self._cmd_pub.publish(cmd)

        # 检查点: 速度校正偏差超过20%时记录
        if abs(self._last_desired_vx) > 0.05:
            err_ratio = abs(self._last_desired_vx - self._actual_vx) / abs(self._last_desired_vx)
            if err_ratio > 0.2:
                self.get_logger().info(
                    f"[vel_pid→] desired={self._last_desired_vx:.2f} actual={self._actual_vx:.2f} "
                    f"corrected={cmd.linear.x:.2f} err={err_ratio:.1%}",
                    throttle_duration_sec=1.0)

        self._publish_active(True)

    def _publish_active(self, active):
        msg = Bool()
        msg.data = active
        self._active_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = VelocityPID()
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
