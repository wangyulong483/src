import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

"""
nav2_manual_check.launch.py — 手动验证禁区地图

用途: 启动底盘+传感器+Nav2(含禁区代价地图), 用键盘遥控小车走一圈,
      在 RViz 中观察 costmap 上禁区是否叠加正确.

用法:
  1. ros2 launch origincar_bringup nav2_manual_check.launch.py
  2. 在键盘终端用 i/j/l/, 控制小车
  3. PC 上打开 RViz, 订阅 /global_costmap/costmap 和 /local_costmap/costmap
  4. 看禁区 (keepout) 在代价地图上是不是画对了

止动: 按 k 或松开所有键即可停车
"""

def generate_launch_description():
    origincar_bringup_dir = get_package_share_directory('origincar_bringup')
    originbot_nav_dir = get_package_share_directory('originbot_navigation')

    return LaunchDescription([
        # ── t=0: 底盘 + 传感器 + TF + IMU + PID + mux + 深度相机 + QR ──
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

        # ── t=1s: Nav2 全栈 (地图 + 禁区 + costmap + planner + controller) ──
        # 不运行 competition_master, Nav2 无目标, controller 不输出指令
        TimerAction(period=1.0, actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(origincar_bringup_dir, 'launch', 'nav2_minimal.launch.py')
                )
            ),
        ]),

        # ── t=2s: Keepout 激活 ──
        # KeepoutFilter 订阅 /costmap_ctrl, 需要收到 CostmapFilterInfo 才知道用 /keepout_mask
        # 常规运行中由 competition_master 发布此消息; 手动模式下没有 competition_master, 手动发一次
        TimerAction(period=2.0, actions=[
            ExecuteProcess(
                cmd=['ros2', 'topic', 'pub', '-1', '/costmap_ctrl',
                     'nav2_msgs/msg/CostmapFilterInfo',
                     '{type: 0, filter_mask_topic: /keepout_mask, base: 0.0, multiplier: 1.0}'],
                name='keepout_activate',
                output='screen',
            ),
        ]),

        # ── t=3s: RViz2 ──
        TimerAction(period=3.0, actions=[
            Node(
                package='rviz2',
                executable='rviz2',
                name='rviz2',
                arguments=['-d', os.path.join(originbot_nav_dir, 'rviz', 'nav.rviz')],
                output='screen',
            ),
        ]),
    ])

# 键盘遥控: 本文件不启动 teleop_twist_keyboard (headless 无法交互).
# 请在机器人上另开 SSH 终端手动运行:
#   ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/cmd_vel
