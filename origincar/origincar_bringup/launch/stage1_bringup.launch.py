import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

"""
stage1_bringup.launch.py — Stage 1 总启动文件 (压缩版)

时间线: camera 与底盘并行, Nav2 尽早启动
  t=0s → 底盘 + TF + Madgwick + EKF + PID + 深度相机 + QR (并行, 省 2s)
  t=1s → Nav2 全栈 (odom/TF 已就绪, keepout 同步加载)
  t=4s → competition_master_stage1 (内部 8s timer, ~t=12s 首次发车)
"""

def generate_launch_description():
    origincar_bringup_dir = get_package_share_directory('origincar_bringup')

    return LaunchDescription([
        # t=0s: 底盘 + 传感器 + 控制闭环
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(origincar_bringup_dir, 'launch', 'base_minimal.launch.py')
            )
        ),
        # t=0s: 深度相机 + QR 解码链 (与底盘并行启动)
        TimerAction(period=0.0, actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(origincar_bringup_dir, 'launch', 'camera_all.launch.py')
                )
            ),
        ]),

        # t=1s: Nav2 导航栈 (odom+TF 已就绪)
        TimerAction(period=1.0, actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(origincar_bringup_dir, 'launch', 'nav2_minimal.launch.py')
                )
            ),
        ]),

        # t=4s: Stage 1 总控节点 (内部 8s timer → ~t=12s 首次发车)
        TimerAction(period=4.0, actions=[
            Node(
                package='origincar_bringup',
                executable='competition_master_stage1.py',
                name='competition_master_stage1',
                output='screen',
                emulate_tty=True,
                respawn=True,
                respawn_delay=2.0,
            ),
        ]),
    ])
