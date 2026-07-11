# Copyright 2019 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Darby Lim

"""
Cartographer 2D SLAM 启动文件

此文件用于独立启动 Cartographer 2D SLAM 系统（含 EKF + occupancy_grid）。

主要功能：
- Route B 架构（推荐默认）：EKF 融合 odom+IMU → /odometry/filtered
  Cartographer 作为纯"激光+里程计"系统使用，IMU由EKF统一处理
- 可选关闭 EKF（use_ekf:=false），Cartographer 直接使用原始 /odom
- 启动 occupancy_grid 节点发布栅格地图
- 支持仿真时间和真实时间模式切换
"""

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir


def generate_launch_description():
    """
    生成 Cartographer SLAM 的启动描述

    此函数定义了 Cartographer SLAM 系统的所有启动参数和节点配置，
    包括配置文件路径、时间设置、地图分辨率等关键参数。

    返回:
        LaunchDescription: 包含 Cartographer SLAM 系统完整配置的启动描述
    """
    # 设置是否使用仿真时间的参数，默认为 false（使用真实时间）
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    # Route B 架构（推荐）：EKF 融合 odom+IMU → 平滑里程计，IMU 不重复传入 Cartographer
    use_ekf = LaunchConfiguration('use_ekf', default='true')

    # 获取 originbot_navigation 包的共享目录路径
    cartographer_prefix = get_package_share_directory('originbot_navigation')

    # 设置 Cartographer 配置文件目录，默认为包内的 config 目录
    cartographer_config_dir = LaunchConfiguration('cartographer_config_dir', default=os.path.join(
                                                  cartographer_prefix, 'config'))

    # 设置 Lua 配置文件名，默认为 lds_2d.lua
    configuration_basename = LaunchConfiguration('configuration_basename',
                                                 default='lds_2d.lua')

    # 设置地图分辨率，默认为 0.05 米/像素
    resolution = LaunchConfiguration('resolution', default='0.05')

    # 设置 OccupancyGrid 发布周期，默认为 1.0 秒
    publish_period_sec = LaunchConfiguration('publish_period_sec', default='1.0')

    # 激光雷达话题名，默认 /scan（N10 雷达驱动发布的话题）
    scan_topic = LaunchConfiguration('scan_topic', default='scan')

    # EKF 配置文件路径 — 共用 origincar_base 的双IMU校准配置
    ekf_config_path = os.path.join(
        get_package_share_directory('origincar_base'), 'config', 'ekf_dual_imu.yaml')

    return LaunchDescription([
        # 声明 cartographer_config_dir 参数
        DeclareLaunchArgument(
            'cartographer_config_dir',
            default_value=cartographer_config_dir,
            description='Full path to config file to load'),

        # 声明 configuration_basename 参数
        DeclareLaunchArgument(
            'configuration_basename',
            default_value=configuration_basename,
            description='Name of lua file for cartographer'),

        # 声明 use_sim_time 参数
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),

        # 声明 use_ekf 参数
        DeclareLaunchArgument(
            'use_ekf',
            default_value='true',
            description='Enable EKF odometry fusion (Route B recommended). EKF fuses odom+IMU into /odometry/filtered. Cartographer uses this as pure laser+odometry system.'),

        # 声明 resolution 参数
        DeclareLaunchArgument(
            'resolution',
            default_value=resolution,
            description='Resolution of a grid cell in the published occupancy grid'),

        # 声明 publish_period_sec 参数
        DeclareLaunchArgument(
            'publish_period_sec',
            default_value=publish_period_sec,
            description='OccupancyGrid publishing period'),

        # 声明 scan_topic 参数
        DeclareLaunchArgument(
            'scan_topic',
            default_value='scan',
            description='LaserScan topic name (N10 default: /scan)'),

        # ============ EKF 里程计融合节点（仅在 use_ekf:=true 时启动）============
        # EKF 配置 publish_tf:=true，发布 odom→base_footprint
        # 必须配合 bringup.launch.py 设置 pub_odom_tf:=false，避免 TF 双重发布
        # 启动命令: ros2 launch origincar_bringup bringup.launch.py pub_odom_tf:=false
        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[ekf_config_path, {'use_sim_time': use_sim_time}],
            condition=IfCondition(use_ekf),
        ),

        # ============ Cartographer 主节点（use_ekf:=false）============
        # Route A: 直接使用原始 /odom。Lua 中 use_imu_data=false，IMU 由 Lua 控制不订阅
        Node(
            package='cartographer_ros',
            executable='cartographer_node',
            name='cartographer_node',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time}],
            arguments=['-configuration_directory', cartographer_config_dir,
                       '-configuration_basename', configuration_basename],
            remappings=[('scan', scan_topic)],
            condition=UnlessCondition(use_ekf),
        ),

        # ============ Cartographer 主节点（use_ekf:=true，默认推荐）============
        # Route B: 使用 EKF 融合后的 /odometry/filtered。IMU 由 EKF 统一处理，不再传入 Cartographer
        Node(
            package='cartographer_ros',
            executable='cartographer_node',
            name='cartographer_node',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time}],
            arguments=['-configuration_directory', cartographer_config_dir,
                       '-configuration_basename', configuration_basename],
            remappings=[('scan', scan_topic), ('odom', 'odometry/filtered')],
            condition=IfCondition(use_ekf),
        ),

        # 包含 occupancy_grid 启动文件
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([ThisLaunchFileDir(), '/occupancy_grid.launch.py']),
            launch_arguments={'use_sim_time': use_sim_time, 'resolution': resolution,
                              'publish_period_sec': publish_period_sec}.items(),
        ),
    ])
