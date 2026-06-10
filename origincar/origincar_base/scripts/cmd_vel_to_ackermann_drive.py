#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@file cmd_vel_to_ackermann_drive.py
@brief 将标准速度指令 (cmd_vel) 转换为阿克曼转向模型指令
@details 该节点订阅 /cmd_vel_corrected (经 velocity_pid 校正),
         将其转换为 ackermann_msgs/msg/AckermannDriveStamped 类型发布

工作原理：
    - 根据线速度和角速度计算转向角
    - steering_angle = steering_sign * arctan(wheelbase / turning_radius) + steering_offset
    - turning_radius = linear_velocity / angular_velocity
    - steering_sign: +1=ROS规范(正=左转/CCW), -1=STM32规范(正=右转)
"""

import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from ackermann_msgs.msg import AckermannDriveStamped
from rclpy.qos import QoSProfile

class CmdVel2AckermannDriveNode(Node):
    """
    @brief cmd_vel 到 Ackermann 驱动转换节点
    """
    def __init__(self):
        super().__init__('cmd_vel_to_ackermann_drive')

        self.declare_parameter('wheelbase', 0.143)
        self.declare_parameter('steering_sign', -1.0)
        self.declare_parameter('steering_offset', 0.0)
        self.declare_parameter('cmd_angle_instead_rotvel', False)

        self.publisher = self.create_publisher(
            AckermannDriveStamped, '/ackermann_cmd', QoSProfile(depth=10))
        self.subscription = self.create_subscription(
            Twist, 'cmd_vel_corrected', self.cmd_callback, QoSProfile(depth=10))
        self.frame_id = 'odom_combined'

        self.get_logger().info(
            f"Ackermann: wheelbase={self.get_parameter('wheelbase').value:.3f}m"
            f", sign={self.get_parameter('steering_sign').value:+.0f}"
            f", offset={self.get_parameter('steering_offset').value:+.3f}rad")

    def convert_trans_rot_vel_to_steering_angle(self, vel, omega):
        if omega == 0 or vel == 0:
            return 0
        radius = vel / omega
        return math.atan(self.get_parameter('wheelbase').value / radius)

    def cmd_callback(self, data):
        vel = data.linear.x

        if self.get_parameter('cmd_angle_instead_rotvel').value:
            steering = data.angular.z
        else:
            steering = self.convert_trans_rot_vel_to_steering_angle(vel, data.angular.z)

        sign = self.get_parameter('steering_sign').value
        offset = self.get_parameter('steering_offset').value

        msg = AckermannDriveStamped()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = self.frame_id
        msg.drive.steering_angle = sign * steering + offset
        msg.drive.speed = vel

        self.publisher.publish(msg)


def main():
    rclpy.init()
    node = CmdVel2AckermannDriveNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
