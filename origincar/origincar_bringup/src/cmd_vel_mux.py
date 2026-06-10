#!/usr/bin/env python3
"""
cmd_vel_mux — /cmd_vel 优先级多路复用器
参考 twist_mux (ROS wiki) 设计, 解决多个节点同时发布 /cmd_vel 时的控制权冲突。

工作原理:
  - 多个输入话题 (nav/pid/stop) 各有优先级 (0~255, 越大越优先)
  - 每个输入有 timeout: 超时未收到消息 → 视为非活跃, 降级到下一优先级
  - 选择当前活跃输入中优先级最高的 → 发布到输出 (/cmd_vel)
  - STOP 类输入优先级最高 (255), 确保紧急停车不被覆盖

输入话题    | 默认优先级 | 默认超时 | 来源
/nav_cmd_vel   | 10         | 0.5s     | velocity_smoother (RPP), remap自 /cmd_vel
/pid_cmd_vel   | 20         | 0.3s     | pose_pid_corrector (外环位置校正，暂未启用)
/stop_cmd_vel  | 255        | 0.5s     | qr_decision + competition_master

输出: /cmd_vel_muxed (Twist, 仲裁后的速度指令 → velocity_pid → /cmd_vel_corrected → STM32)

注意: /pid_cmd_vel 是给 pose_pid_corrector (位置环) 的，与 velocity_pid (速度环)
是不同的控制层级。velocity_pid 位于 mux 下游，不作为 mux 的输入通道。
"""

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String


class PriorityInput:
    def __init__(self, name, priority, timeout):
        self.name = name
        self.priority = priority
        self.timeout = timeout
        self.last_msg = Twist()
        self.last_time = None
        self.active = False


class CmdVelMux(Node):
    def __init__(self):
        super().__init__('cmd_vel_mux')

        self.declare_parameter('output_topic', '/cmd_vel')
        self.declare_parameter('rate', 30.0)

        # ── 输入配置: (名称, 默认优先级, 默认超时) ──
        inputs_cfg = [
            ('nav',   10, 0.5),
            ('pid',   20, 0.3),
            ('stop', 255, 0.5),
        ]

        self._inputs = {}
        self._last_active = ''
        self._last_vx = 0.0
        self._was_active = {}  # track previous active state per input for timeout logging
        for name, prio, to in inputs_cfg:
            self.declare_parameter(f'{name}_priority', prio)
            self.declare_parameter(f'{name}_timeout', to)
            inp = PriorityInput(
                name,
                self.get_parameter(f'{name}_priority').value,
                self.get_parameter(f'{name}_timeout').value,
            )
            self._inputs[name] = inp
            self._was_active[name] = False
            self.create_subscription(
                Twist, f'/{name}_cmd_vel',
                lambda msg, n=name: self._on_input(n, msg), 10)
            self.get_logger().info(
                f"  {name}: /{name}_cmd_vel priority={inp.priority} timeout={inp.timeout}s")

        self._pub = self.create_publisher(Twist, '/cmd_vel_muxed', 10)
        self._state_pub = self.create_publisher(String, '/cmd_vel_mux_state', 10)
        self._timer = self.create_timer(1.0 / 30.0, self._tick)

        self.get_logger().info("cmd_vel_mux 就绪: 输出 → /cmd_vel_muxed")

    def _on_input(self, name, msg):
        inp = self._inputs[name]
        inp.last_msg = msg
        inp.last_time = self.get_clock().now()
        inp.active = True

    def _tick(self):
        now = self.get_clock().now()

        # 重载参数
        for inp in self._inputs.values():
            inp.priority = self.get_parameter(f'{inp.name}_priority').value
            inp.timeout = self.get_parameter(f'{inp.name}_timeout').value

        # 超时检查
        for inp in self._inputs.values():
            if inp.last_time is not None:
                age = (now - inp.last_time).nanoseconds / 1e9
                if age > max(inp.timeout, 0.01):
                    was = inp.active
                    inp.active = False
                    if was and not inp.active:
                        self.get_logger().info(
                            f"[mux] TIMEOUT src={inp.name} age={age:.2f}s > {inp.timeout}s, marked inactive",
                            throttle_duration_sec=1.0)
            self._was_active[inp.name] = inp.active

        # 选择最高优先级活跃输入
        best = None
        for inp in self._inputs.values():
            if inp.active:
                if best is None or inp.priority > best.priority:
                    best = inp

        if best is not None:
            v = best.last_msg.linear.x
            self._pub.publish(best.last_msg)
            state = f"active={best.name}(p={best.priority})"
            # §检查点: 源切换或速度显著变化时记录
            if best.name != self._last_active or abs(v - self._last_vx) > 0.1:
                self.get_logger().info(
                    f"[mux→] src={best.name} vx={v:.2f} wz={best.last_msg.angular.z:.2f}",
                    throttle_duration_sec=0.5)
                self._last_active = best.name
                self._last_vx = v
        else:
            self._pub.publish(Twist())
            state = "idle (all inactive)"
            if self._last_active != 'idle':
                self.get_logger().info(
                    "[mux] IDLE all sources inactive, publishing zero Twist",
                    throttle_duration_sec=2.0)
                self._last_active = 'idle'

        self._state_pub.publish(String(data=state))


def main(args=None):
    rclpy.init(args=args)
    node = CmdVelMux()
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
