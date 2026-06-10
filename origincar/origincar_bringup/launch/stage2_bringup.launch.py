import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, OpaqueFunction, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

"""
stage2_bringup.launch.py — Stage 2 总启动文件 (压缩版 + RViz2)

时间线: camera 与底盘并行, Nav2 尽早启动
  t=0s → 底盘 + TF + Madgwick + EKF + PID + 深度相机 + QR + VLM(可选)
  t=1s → Nav2 全栈 (odom/TF 已就绪, keepout 同步加载)
  t=4s → competition_master_stage2 (内部 8s timer, ~t=12s 首次发车)
  t=8s → RViz2 (所有话题就绪, 用于地图查看+确定点位)
"""

def _vision_ai_if_available(context):
    try:
        get_package_share_directory('racing_vision_ai')
    except Exception:
        return []
    return [Node(
        package='racing_vision_ai',
        executable='vision_ai_node',
        name='vision_ai_node',
        output='screen',
    )]

def generate_launch_description():
    origincar_bringup_dir = get_package_share_directory('origincar_bringup')
    originbot_nav_dir = get_package_share_directory('originbot_navigation')

    return LaunchDescription([
        # t=0s: 底盘 + 传感器 + 控制闭环
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(origincar_bringup_dir, 'launch', 'base_minimal.launch.py')
            )
        ),
        # t=0s: 深度相机 + QR + VLM (与底盘并行启动)
        TimerAction(period=0.0, actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(origincar_bringup_dir, 'launch', 'camera_all.launch.py')
                )
            ),
            OpaqueFunction(function=_vision_ai_if_available),
        ]),

        # t=1s: Nav2 导航栈 (odom+TF 已就绪)
        TimerAction(period=1.0, actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(origincar_bringup_dir, 'launch', 'nav2_minimal.launch.py')
                )
            ),
        ]),

        # t=4s: Stage 2 总控节点 (内部 8s timer → ~t=12s 首次发车)
        TimerAction(period=4.0, actions=[
            Node(
                package='origincar_bringup',
                executable='competition_master_stage2.py',
                name='competition_master_stage2',
                output='screen',
                emulate_tty=True,
                respawn=True,
                respawn_delay=2.0,
            ),
        ]),

        # t=8s: RViz2 (所有话题就绪, 用于地图查看+确定后续点位)
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
