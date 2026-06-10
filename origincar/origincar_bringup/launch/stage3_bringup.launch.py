import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

"""
stage3_bringup.launch.py — Stage 3 总启动文件

流程: QR扫码→通道入口→通道巡航(CCW/CW)→VLM图生文→返航P点
  t=0s → 底盘 + TF + Madgwick + EKF + PID + 深度相机 + QR
  t=1s → Nav2 全栈
  t=4s → competition_master_stage3 (QR→入口→巡航→VLM→返航)
  t=8s → RViz2 (地图查看)
"""

def generate_launch_description():
    origincar_bringup_dir = get_package_share_directory('origincar_bringup')
    originbot_nav_dir = get_package_share_directory('originbot_navigation')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(origincar_bringup_dir, 'launch', 'base_minimal.launch.py')
            )
        ),
        TimerAction(period=0.0, actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(origincar_bringup_dir, 'launch', 'camera_all.launch.py')
                )
            ),
        ]),

        TimerAction(period=1.0, actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(origincar_bringup_dir, 'launch', 'nav2_minimal.launch.py')
                )
            ),
        ]),

        TimerAction(period=4.0, actions=[
            Node(
                package='origincar_bringup',
                executable='competition_master_stage3.py',
                name='competition_master_stage3',
                output='screen',
                emulate_tty=True,
                respawn=True,
                respawn_delay=2.0,
            ),
        ]),

        TimerAction(period=8.0, actions=[
            Node(
                package='rviz2',
                executable='rviz2',
                name='rviz2',
                arguments=['-d', os.path.join(originbot_nav_dir, 'rviz', 'nav.rviz')],
                output='screen',
            ),
        ]),
    ])
