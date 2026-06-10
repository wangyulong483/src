import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

"""
slam_bringup.launch.py — 底盘 + Cartographer SLAM + RViz2 一键建图

用法:
  ros2 launch origincar_bringup slam_bringup.launch.py

架构:
  底盘 EKF (base_minimal) → /odometry/filtered + odom→base_footprint TF
  Cartographer 订阅 /scan + /odometry/filtered → /map + map→odom TF
  RViz2 显示 /map

建图完成后保存:
  ros2 run nav2_map_server map_saver_cli -f /userdata/dev_ws/src/originbot_navigation/maps/room
"""

def generate_launch_description():
    origincar_bringup_dir = get_package_share_directory('origincar_bringup')
    originbot_nav_dir = get_package_share_directory('originbot_navigation')
    carto_config = os.path.join(originbot_nav_dir, 'config')

    return LaunchDescription([
        # t=0s: 底盘 + 激光雷达 + TF + Madgwick + EKF + 控制闭环
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(origincar_bringup_dir, 'launch', 'base_minimal.launch.py')
            ),
        ),

        # t=3s: Cartographer SLAM (复用底盘 EKF 的 /odometry/filtered)
        TimerAction(period=3.0, actions=[
            Node(
                package='cartographer_ros',
                executable='cartographer_node',
                name='cartographer_node',
                output='screen',
                arguments=[
                    '-configuration_directory', carto_config,
                    '-configuration_basename', 'lds_2d.lua',
                ],
                remappings=[
                    ('scan', 'scan'),
                    ('odom', 'odometry/filtered'),  # 底盘 EKF 输出
                ],
            ),
            Node(
                package='cartographer_ros',
                executable='cartographer_occupancy_grid_node',
                name='cartographer_occupancy_grid_node',
                output='screen',
                parameters=[{'resolution': 0.05, 'publish_period_sec': 1.0}],
            ),
        ]),

        # t=5s: RViz2
        TimerAction(period=5.0, actions=[
            Node(
                package='rviz2',
                executable='rviz2',
                name='rviz2',
                arguments=['-d', os.path.join(originbot_nav_dir, 'rviz', 'nav.rviz')],
                output='screen',
            ),
        ]),
    ])
