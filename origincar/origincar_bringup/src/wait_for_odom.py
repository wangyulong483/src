#!/usr/bin/env python3
"""
wait_for_odom — 启动屏障: 等待 /odom 话题有数据后退出
用于 launch 文件中作为依赖检查: 确保底盘已启动后再启 Nav2
用法: ros2 run origincar_bringup wait_for_odom.py --timeout 15
"""

import sys
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry


class WaitForOdom(Node):
    def __init__(self, timeout_sec):
        super().__init__('wait_for_odom')
        self._timeout = timeout_sec
        self._start = self.get_clock().now()
        self._received = False
        self._sub = self.create_subscription(Odometry, '/odom', self._cb, 10)
        self._timer = self.create_timer(0.1, self._check)

    def _cb(self, _msg):
        self._received = True

    def _check(self):
        if self._received:
            self.get_logger().info("/odom 数据已到达, 启动屏障通过")
            raise SystemExit(0)
        elapsed = (self.get_clock().now() - self._start).nanoseconds / 1e9
        if elapsed > self._timeout:
            self.get_logger().error(f"/odom 等待超时 ({self._timeout}s), 强制继续")
            raise SystemExit(1)


def main():
    rclpy.init(args=sys.argv)
    timeout = 15.0
    for i, arg in enumerate(sys.argv):
        if arg == '--timeout' and i + 1 < len(sys.argv):
            timeout = float(sys.argv[i + 1])
    node = WaitForOdom(timeout)
    try:
        rclpy.spin(node)
    except SystemExit:
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
