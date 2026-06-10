#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
imu_madgwick_filter — Madgwick AHRS 姿态解算节点

对 STM32 MPU6050 (Mahony Ki=0) 的 /imu/data_raw 做二阶 Madgwick 滤波,
输出更稳定的姿态四元数, 补偿 Mahony 无法消除的陀螺仪零偏漂移。

算法: Sebastian Madgwick 6-DOF IMU AHRS (无磁力计)
参考: "An efficient orientation filter for inertial and inertial/magnetic sensor arrays" (2010)

架构位置: origincar_base → /imu/data_raw → imu_madgwick_filter → /imu/data/madgwick → EKF
配合: ekf_filter_node (robot_localization), yaw process_noise_covariance 降至 0.005

输入:
  - /imu/data_raw (sensor_msgs/Imu, frame_id=gyro_link)
    只用 angular_velocity + linear_acceleration, 丢弃 STM32 Mahony 四元数

输出:
  - /imu/data/madgwick (sensor_msgs/Imu, frame_id=gyro_link)
    Madgwick 四元数 + 透传原始 gyro + 透传原始 accel

参数:
  - gain (double, 默认 0.033): Madgwick beta, 越低 = 更信任加速度计
  - frequency (double, 默认 100.0): 滤波器设计频率, 用于协方差缩放
  - gyro_noise (double, 默认 0.001): 陀螺仪噪声 rad/s
  - accel_noise (double, 默认 0.05): 加速度计噪声 m/s^2
"""

import math
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from std_msgs.msg import Float64


class MadgwickAHRS:
    """Pure Python Madgwick 6-DOF AHRS (无磁力计)."""

    def __init__(self, beta: float = 0.033):
        self.beta = beta
        self.q = [1.0, 0.0, 0.0, 0.0]  # w, x, y, z (Hamilton convention)

    def update(self, gx: float, gy: float, gz: float,
               ax: float, ay: float, az: float, dt: float) -> None:
        """
        单步 Madgwick 更新。
        gx, gy, gz: 陀螺仪 rad/s
        ax, ay, az: 加速度计 m/s^2
        dt: 时间步长 (s)
        """
        q0, q1, q2, q3 = self.q

        # 归一化加速度计 (防止 NaN)
        norm = math.sqrt(ax * ax + ay * ay + az * az)
        if norm < 1e-6:
            # 自由落体 / 无有效加速度: 仅积分陀螺仪
            _integrate_gyro_only(self, gx, gy, gz, dt)
            return
        ax /= norm
        ay /= norm
        az /= norm

        # 梯度下降步: 从加速度计推算重力方向误差
        # F_g = [2(q1*q3 - q0*q2) - ax, 2(q0*q1 + q2*q3) - ay, 2(0.5 - q1^2 - q2^2) - az]
        _2q0 = 2.0 * q0
        _2q1 = 2.0 * q1
        _2q2 = 2.0 * q2
        _2q3 = 2.0 * q3

        # 目标函数的雅可比转置 × 目标函数值 = 梯度
        # F1 = 2(q1*q3 - q0*q2) - ax
        f1 = _2q1 * q3 - _2q0 * q2 - ax
        # F2 = 2(q0*q1 + q2*q3) - ay
        f2 = _2q0 * q1 + _2q2 * q3 - ay
        # F3 = 2(0.5 - q1^2 - q2^2) - az = 1 - 2q1^2 - 2q2^2 - az
        f3 = 1.0 - _2q1 * q1 - _2q2 * q2 - az

        # J^T * F
        # s0 = -2*q2*f1 + 2*q1*f2
        s0 = -_2q2 * f1 + _2q1 * f2
        # s1 = 2*q3*f1 + 2*q0*f2 - 4*q1*f3
        s1 = _2q3 * f1 + _2q0 * f2 - 4.0 * q1 * f3
        # s2 = -2*q0*f1 + 2*q3*f2 - 4*q2*f3
        s2 = -_2q0 * f1 + _2q3 * f2 - 4.0 * q2 * f3
        # s3 = 2*q1*f1 + 2*q2*f2
        s3 = _2q1 * f1 + _2q2 * f2

        # 归一化梯度
        norm = math.sqrt(s0 * s0 + s1 * s1 + s2 * s2 + s3 * s3)
        if norm > 1e-9:
            s0 /= norm
            s1 /= norm
            s2 /= norm
            s3 /= norm

        # 陀螺仪积分 (q_dot = 0.5 * q ⊗ omega)
        q_dot0 = 0.5 * (-q1 * gx - q2 * gy - q3 * gz)
        q_dot1 = 0.5 * (q0 * gx + q2 * gz - q3 * gy)
        q_dot2 = 0.5 * (q0 * gy - q1 * gz + q3 * gx)
        q_dot3 = 0.5 * (q0 * gz + q1 * gy - q2 * gx)

        # 融合: q_dot = q_dot_gyro - beta * gradient
        q0 += (q_dot0 - self.beta * s0) * dt
        q1 += (q_dot1 - self.beta * s1) * dt
        q2 += (q_dot2 - self.beta * s2) * dt
        q3 += (q_dot3 - self.beta * s3) * dt

        # 归一化四元数
        norm = math.sqrt(q0 * q0 + q1 * q1 + q2 * q2 + q3 * q3)
        if norm > 1e-9:
            self.q = [q0 / norm, q1 / norm, q2 / norm, q3 / norm]

    def reset(self) -> None:
        self.q = [1.0, 0.0, 0.0, 0.0]


def _integrate_gyro_only(self, gx, gy, gz, dt):
    """纯陀螺仪积分 (加速度计不可用时的降级路径)."""
    q0, q1, q2, q3 = self.q
    q0 += 0.5 * (-q1 * gx - q2 * gy - q3 * gz) * dt
    q1 += 0.5 * (q0 * gx + q2 * gz - q3 * gy) * dt
    q2 += 0.5 * (q0 * gy - q1 * gz + q3 * gx) * dt
    q3 += 0.5 * (q0 * gz + q1 * gy - q2 * gx) * dt
    norm = math.sqrt(q0 * q0 + q1 * q1 + q2 * q2 + q3 * q3)
    if norm > 1e-9:
        self.q = [q0 / norm, q1 / norm, q2 / norm, q3 / norm]


class ImuMadgwickFilter(Node):
    """Madgwick AHRS ROS2 节点."""

    def __init__(self):
        super().__init__('imu_madgwick_filter')

        # -- 参数 --
        self.declare_parameter('gain', 0.033)
        self.declare_parameter('frequency', 100.0)
        self.declare_parameter('gyro_noise', 0.001)
        self.declare_parameter('accel_noise', 0.05)

        # -- 滤波器实例 --
        gain = self.get_parameter('gain').value
        self._filter = MadgwickAHRS(beta=gain)
        self._filter.reset()

        # -- 订阅 /imu/data_raw --
        self._imu_sub = self.create_subscription(
            Imu, '/imu/data_raw', self._on_imu, 10)

        # -- 发布 /imu/data/madgwick --
        self._imu_pub = self.create_publisher(Imu, '/imu/data/madgwick', 10)

        # -- 诊断定时器 0.1Hz --
        self._diag_timer = self.create_timer(10.0, self._diag_callback)
        self._msg_count = 0
        self._last_q = self._filter.q.copy()
        self._init_done = False

        # 增益动态重载 (允许运行时调参)
        self.create_timer(2.0, self._reload_params)

        self.get_logger().info(
            f"[imu_madgwick] init: beta={gain:.4f}, "
            f"gyro_noise={self.get_parameter('gyro_noise').value:.4f}, "
            f"accel_noise={self.get_parameter('accel_noise').value:.3f}"
        )

    def _reload_params(self):
        new_gain = self.get_parameter('gain').value
        if abs(new_gain - self._filter.beta) > 0.0001:
            self._filter.beta = new_gain
            self.get_logger().info(
                f"[imu_madgwick] gain updated: {new_gain:.4f}")

    def _on_imu(self, msg: Imu):
        # 首条消息标记
        if self._msg_count == 0:
            self.get_logger().info(
                "[imu_madgwick] FIRST_MSG received from /imu/data_raw, starting filter pipeline")

        # 提取原始角速度 (rad/s) 和线加速度 (m/s^2)
        gx = msg.angular_velocity.x
        gy = msg.angular_velocity.y
        gz = msg.angular_velocity.z
        ax = msg.linear_acceleration.x
        ay = msg.linear_acceleration.y
        az = msg.linear_acceleration.z

        # 获取 dt
        dt = 0.01  # 默认 100Hz
        if self._msg_count > 0 and hasattr(self, '_last_stamp'):
            dt_ns = (msg.header.stamp.sec - self._last_stamp.sec) * 1e9
            dt_ns += msg.header.stamp.nanosec - self._last_stamp.nanosec
            dt = dt_ns / 1e9
            if dt > 0.15:
                self.get_logger().warn(
                    f"[imu_madgwick] dt outlier: {dt:.4f}s > 0.15s, capping",
                    throttle_duration_sec=5.0)
                dt = 0.01
            elif dt <= 0.0:
                dt = 0.01

        self._last_stamp = msg.header.stamp

        # 首次: 从加速度计初始化 roll/pitch
        if not self._init_done:
            accel_norm = math.sqrt(ax * ax + ay * ay + az * az)
            if 8.0 < accel_norm < 12.0:  # 重力加速度附近
                roll = math.atan2(ay, az)
                pitch = math.atan2(-ax, math.sqrt(ay * ay + az * az))
                cr = math.cos(roll * 0.5)
                sr = math.sin(roll * 0.5)
                cp = math.cos(pitch * 0.5)
                sp = math.sin(pitch * 0.5)
                self._filter.q[0] = cr * cp
                self._filter.q[1] = sr * cp
                self._filter.q[2] = cr * sp
                self._filter.q[3] = -sr * sp
                self._init_done = True
                self.get_logger().info(
                    f"[imu_madgwick] accel init: "
                    f"roll={math.degrees(roll):.1f}deg, "
                    f"pitch={math.degrees(pitch):.1f}deg")

        # Madgwick 更新
        self._filter.update(gx, gy, gz, ax, ay, az, dt)

        # 构建输出消息
        out = Imu()
        out.header.stamp = msg.header.stamp
        out.header.frame_id = msg.header.frame_id

        q = self._filter.q
        out.orientation.w = q[0]
        out.orientation.x = q[1]
        out.orientation.y = q[2]
        out.orientation.z = q[3]

        # 透传原始角速度和线加速度
        out.angular_velocity = msg.angular_velocity
        out.linear_acceleration = msg.linear_acceleration

        # 协方差: 对角阵, 姿态由 Madgwick beta 决定, gyro/accel 由噪声参数决定
        gyro_n = self.get_parameter('gyro_noise').value
        accel_n = self.get_parameter('accel_noise').value
        gv = gyro_n * gyro_n
        av = accel_n * accel_n
        # 姿态协方差 (roll, pitch: accel-based; yaw: gyro-based, 随时间增长)
        pv = 0.001  # ~1.8deg
        out.orientation_covariance = [
            pv, 0.0, 0.0,
            0.0, pv, 0.0,
            0.0, 0.0, pv * 10.0,  # yaw 漂移更大
        ]
        out.angular_velocity_covariance = [
            gv, 0.0, 0.0,
            0.0, gv, 0.0,
            0.0, 0.0, gv,
        ]
        out.linear_acceleration_covariance = [
            av, 0.0, 0.0,
            0.0, av, 0.0,
            0.0, 0.0, av,
        ]

        self._imu_pub.publish(out)
        self._msg_count += 1
        self._last_q = q

    def _diag_callback(self):
        q = self._filter.q
        w = math.degrees(
            2.0 * math.acos(max(-1.0, min(1.0, q[0]))))
        self.get_logger().info(
            f"[imu_madgwick ->] msgs={self._msg_count} "
            f"q_w={q[0]:.4f} angle={w:.1f}deg "
            f"beta={self._filter.beta:.4f}",
            throttle_duration_sec=9.0)


def main(args=None):
    rclpy.init(args=args)
    node = ImuMadgwickFilter()
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
