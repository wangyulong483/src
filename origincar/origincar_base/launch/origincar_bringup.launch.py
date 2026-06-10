#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@file origincar_bringup.launch.py
@brief OriginCar 机器人启动文件
@details 该文件用于启动 OriginCar 机器人的所有基础组件，包括：
         - 底层驱动节点（串口通信）
         - TF 坐标变换
         - IMU 滤波
         - 里程计融合（EKF）
         - 关节状态发布
         
功能模块：
    1. base_serial.launch.py - 底层串口通信
    2. robot_mode_description.launch.py - 机器人模式描述
    3. TF 坐标变换（base_footprint -> base_link, gyro_link）
    4. IMU 滤波（Madgwick 算法）
    5. EKF 里程计融合（robot_localization）
    6. 关节状态发布
"""

import os
from pathlib import Path
import launch
from launch.actions import SetEnvironmentVariable
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import (DeclareLaunchArgument, GroupAction,
                            IncludeLaunchDescription, SetEnvironmentVariable)
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import PushRosNamespace
import launch_ros.actions
from launch.conditions import UnlessCondition

def generate_launch_description():
    """
    @brief 生成启动描述
    @return LaunchDescription 对象
    @details 配置并返回包含所有启动项的启动描述
    """
    # ============ 获取路径配置 ============
    # 获取 origincar_base 包的共享目录
    bringup_dir = get_package_share_directory('origincar_base')
    # 构建 launch 目录路径
    launch_dir = os.path.join(bringup_dir, 'launch')
    # EKF 配置文件路径
    ekf_config = Path(get_package_share_directory('origincar_base'), 'config', 'ekf.yaml')
    # IMU 配置文件路径 (imu_filter_madgwick ROS2 包, 暂未启用)
    imu_config = Path(get_package_share_directory('origincar_base'), 'config', 'imu.yaml')
    # Madgwick 自定义滤波器配置
    imu_madgwick_config = Path(get_package_share_directory('origincar_base'), 'config', 'imu_madgwick.yaml')

    # ============ 声明启动参数 ============
    # Cartographer SLAM 模式开关（默认关闭）
    carto_slam = LaunchConfiguration('carto_slam', default='true')
    carto_slam_dec = DeclareLaunchArgument('carto_slam',default_value='true')
            
    # ============ 包含子启动文件 ============
    # 启动底层串口通信节点（使用阿克曼模式）
    origincar_base = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(os.path.join(launch_dir, 'base_serial.launch.py')),
            launch_arguments={'akmcar': 'true'}.items(),  # 启用阿克曼小车模式
    )

    # ============ TF 坐标变换 ============
    # 发布 base_footprint 到 base_link 的静态变换
    base_to_link = launch_ros.actions.Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='base_to_link',
            arguments=['0.41', '0.12', '0','0', '0','0','base_footprint','base_link'],
    )

    # 发布 base_footprint 到 gyro_link 的静态变换 (IMU 与 base_footprint 重合)
    base_to_gyro = launch_ros.actions.Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='base_to_gyro',
            arguments=['0', '0', '0','0', '0','0','base_footprint','gyro_link'],
    )

    # ============ IMU 滤波 — 自定义 Madgwick AHRS ============
    # 输入: /imu/data_raw (STM32 MPU6050 + Mahony Ki=0)
    # 输出: /imu/data/madgwick (二阶 Madgwick 滤波, 补偿陀螺零偏)
    imu_madgwick_node = launch_ros.actions.Node(
        package='origincar_bringup',
        executable='imu_madgwick_filter.py',
        name='imu_madgwick_filter',
        output='screen',
        parameters=[imu_madgwick_config],
    )

    # ============ 里程计融合（EKF） ============
    # 融合 /odom (编码器) + /imu/data/madgwick (Madgwick 姿态)
    # carto_slam:=true 时 EKF 不启动, Cartographer 发布 map→odom 直接替代
    robot_ekf = launch_ros.actions.Node(
            condition=UnlessCondition(carto_slam),
            package='robot_localization',
            executable='ekf_node',
            parameters=[ekf_config],
            remappings=[("odometry/filtered", "odom_combined")]
            )

    # ============ 组装启动描述 ============
    ld = LaunchDescription()

    ld.add_action(carto_slam_dec)         # Cartographer 开关
    ld.add_action(origincar_base)         # 底层驱动 (STM32 串口)
    ld.add_action(base_to_link)           # TF: base_footprint → base_link
    ld.add_action(base_to_gyro)           # TF: base_footprint → gyro_link
    ld.add_action(imu_madgwick_node)      # Madgwick IMU 滤波
    ld.add_action(robot_ekf)              # EKF 融合 (carto_slam=false 时)

    return ld
