#!/usr/bin/env python3
"""
qr_decision — 轻量 QR 决策节点

仅订阅 C++ qr_decoder 的 /sign 解码结果和 /odom 位姿，执行方向判断。
不做重复解码——每条图像由 C++ 端 ZBar 解码一次，此节点只做纯逻辑。
方向判断结果以 /qr_event 发布，由 task_manager 做后续编排决策。
"""

import math
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int32
from nav_msgs.msg import Odometry


class QrDecisionNode(Node):
    def __init__(self):
        super().__init__("qr_decision")

        self.declare_parameter("cooldown_sec", 3.0)
        self.cooldown_sec = self.get_parameter("cooldown_sec").get_parameter_value().double_value

        self._last_qr_num = None
        self._last_trigger_time = self.get_clock().now()
        self._odom_x = 0.0
        self._odom_y = 0.0
        self._odom_yaw = 0.0

        self.pub_qr_event = self.create_publisher(String, "qr_event", 10)
        self.pub_qr_result = self.create_publisher(String, "qr_result", 10)
        self.pub_sign_data = self.create_publisher(Int32, "/sign_switch_sign_data", 10)

        self.sub_sign = self.create_subscription(String, "/sign", self.sign_callback, 10)
        self.sub_odom = self.create_subscription(Odometry, "/odom", self.odom_callback, 10)

        self.get_logger().info(f"qr_decision started: cooldown={self.cooldown_sec}s, awaiting /sign from qr_decoder")

    def odom_callback(self, msg):
        self._odom_x = msg.pose.pose.position.x
        self._odom_y = msg.pose.pose.position.y
        q = msg.pose.pose.orientation
        siny = 2.0 * (q.w * q.z + q.x * q.y)
        cosy = 1.0 - 2.0 * (q.y * q.y + q.z * q.z)
        self._odom_yaw = math.atan2(siny, cosy)

    def sign_callback(self, msg):
        text = msg.data.strip()
        if not text:
            return

        # ── 格式验证: 仅接受 1~4 位纯数字 (范围 1~9999) ──
        if not text.isdigit() or len(text) < 1 or len(text) > 4:
            self.get_logger().info(
                f"[qr_decision] REJECT non-4-digit QR: '{text}' "
                f"(len={len(text)}, digit={text.isdigit()})",
                throttle_duration_sec=2.0)
            return

        num = int(text)
        if not (1 <= num <= 9999):
            self.get_logger().debug(f"QR number out of valid range [1,9999]: {num}")
            return

        now = self.get_clock().now()
        if num == self._last_qr_num:
            elapsed = (now - self._last_trigger_time).nanoseconds / 1e9
            if elapsed < self.cooldown_sec:
                self.get_logger().info(
                    f"[qr_decision] COOLDOWN blocked qr={num} elapsed={elapsed:.1f}s < {self.cooldown_sec}s",
                    throttle_duration_sec=2.0)
                return

        self._last_qr_num = num
        self._last_trigger_time = now

        direction = "顺时针" if num % 2 == 1 else "逆时针"
        dir_short = "CW" if num % 2 == 1 else "CCW"

        self.get_logger().info(
            f"[QR] {num} {dir_short} @ (x={self._odom_x:.2f}, y={self._odom_y:.2f}, yaw={self._odom_yaw:.2f}) → /qr_event")
        self.get_logger().info("[检查点] qr_decision 发布 /qr_event (由 task_manager 决定停车)")

        self.pub_qr_result.publish(
            String(data=f"{num},{direction},{self._odom_x:.2f},{self._odom_y:.2f}"))
        # qr_event: 结构化事件，可由 task_manager 订阅做编排决策
        self.pub_qr_event.publish(
            String(data=f"{num},{direction},{self._odom_x:.2f},{self._odom_y:.2f}"))
        value = 3 if direction == "顺时针" else 4
        self.pub_sign_data.publish(Int32(data=value))


def main(args=None):
    rclpy.init(args=args)
    node = QrDecisionNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    try:
        rclpy.shutdown()
    except RuntimeError:
        pass


if __name__ == "__main__":
    main()
