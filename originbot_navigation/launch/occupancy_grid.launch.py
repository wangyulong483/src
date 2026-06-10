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
Occupancy Grid 启动文件

此文件用于启动 Cartographer Occupancy Grid 节点，将 Cartographer 的子图转换为
标准的 ROS 栅格地图（/map 话题），供导航系统使用。

主要功能：
- 启动 cartographer_occupancy_grid_node 节点
- 配置地图分辨率和发布周期
- 支持仿真时间和真实时间模式切换
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    """
    生成 Occupancy Grid 节点的启动描述
    
    此函数定义了 Occupancy Grid 节点的启动参数和配置，
    包括地图分辨率、发布周期和时间设置等关键参数。
    
    返回:
        LaunchDescription: 包含 Occupancy Grid 节点完整配置的启动描述
    """
    # 设置是否使用仿真时间的参数，默认为 false（使用真实时间）
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    
    # 设置地图分辨率，默认为 0.05 米/像素
    resolution = LaunchConfiguration('resolution', default='0.05')
    
    # 设置 OccupancyGrid 发布周期，默认为 1.0 秒
    publish_period_sec = LaunchConfiguration('publish_period_sec', default='1.0')

    return LaunchDescription([
        # 声明 resolution 参数
        # 控制发布的 OccupancyGrid 地图的分辨率
        DeclareLaunchArgument(
            'resolution',
            default_value=resolution,
            description='Resolution of a grid cell in the published occupancy grid'),

        # 声明 publish_period_sec 参数
        # 控制 OccupancyGrid 地图的发布频率
        DeclareLaunchArgument(
            'publish_period_sec',
            default_value=publish_period_sec,
            description='OccupancyGrid publishing period'),

        # 声明 use_sim_time 参数
        # 控制是否使用仿真时钟（Gazebo）而非系统时钟
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),

        # 启动 Cartographer Occupancy Grid 节点
        # 将 Cartographer 子图转换为标准 ROS 栅格地图
        Node(
            package='cartographer_ros',
            executable='cartographer_occupancy_grid_node',  # 修正：使用正确的可执行文件名
            name='occupancy_grid_node',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time}],
            arguments=['-resolution', resolution, '-publish_period_sec', publish_period_sec]),
    ])