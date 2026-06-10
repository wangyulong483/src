import os
import re
import tempfile
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

"""
nav2_minimal.launch.py — 最小 Nav2 导航栈 (use_composition:=True)

Composition 模式: 所有 Nav2 server (planner/controller/smoother/behavior/
bt_navigator/waypoint/velocity_smoother) 合并为单一 component_container_isolated 进程,
消除 DDS 序列化/反序列化和进程间通信开销。Nav2 官方强烈推荐嵌入式部署使用。

启动: keepout 禁区 + Nav2 全栈 (composition 模式)
不启动: 管理层节点 (task_manager, mission_controller, etc.)
"""

def _patch_bt_path(yaml_path, old_filename, new_abs_path):
    """将 YAML 中的 BT XML 裸文件名替换为绝对路径 (同 nav_bringup.launch.py)"""
    with open(yaml_path, 'r') as f:
        content = f.read()
    escaped = re.escape(old_filename)
    for key in ('default_nav_to_pose_bt_xml', 'default_nav_through_poses_bt_xml'):
        pattern = r'(' + key + r'\s*:\s*)"?' + escaped + r'"?'
        replacement = r'\1"' + new_abs_path + '"'
        content = re.sub(pattern, replacement, content)
    tmp = tempfile.NamedTemporaryFile(
        mode='w', suffix='_' + old_filename.replace('.xml', '.yaml'),
        delete=False, dir='/tmp')
    tmp.write(content)
    tmp.close()
    return tmp.name


def generate_launch_description():
    originbot_navigation_dir = get_package_share_directory('originbot_navigation')
    nav2_bringup_dir = get_package_share_directory('nav2_bringup')

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    map_yaml_path = LaunchConfiguration(
        'map', default=os.path.join(originbot_navigation_dir, 'maps', 'room.yaml'))

    # BT XML 绝对路径
    rpp_bt_pose_xml = os.path.join(
        originbot_navigation_dir, 'behavior_trees', 'navigate_to_pose_ackermann_rpp.xml')
    rpp_bt_through_xml = os.path.join(
        originbot_navigation_dir, 'behavior_trees', 'navigate_through_poses_ackermann_rpp.xml')

    # Patch YAML: 裸文件名 → 绝对路径
    rpp_param_orig = os.path.join(originbot_navigation_dir, 'param', 'originbot_nav2_rpp.yaml')
    rpp_param_path = _patch_bt_path(rpp_param_orig, 'navigate_to_pose_ackermann_rpp.xml', rpp_bt_pose_xml)
    rpp_param_path = _patch_bt_path(rpp_param_path, 'navigate_through_poses_ackermann_rpp.xml', rpp_bt_through_xml)

    return LaunchDescription([
        DeclareLaunchArgument('use_sim_time', default_value=use_sim_time),
        DeclareLaunchArgument('map', default_value=map_yaml_path),

        # t=0s: keepout 禁区服务器 + lifecycle_manager
        Node(
            package='nav2_map_server', executable='map_server',
            name='keepout_mask_server',
            parameters=[{
                'yaml_filename': os.path.join(originbot_navigation_dir, 'maps', 'keepout_mask.yaml'),
                'topic_name': '/keepout_mask',
                'frame_id': 'map',
            }], output='screen'),
        Node(
            package='nav2_map_server', executable='costmap_filter_info_server',
            name='keepout_filter_info_server',
            parameters=[{
                'type': 0,
                'filter_info_topic': '/costmap_filter_info',
                'mask_topic': '/keepout_mask',
                'base': 0.0, 'multiplier': 1.0,
            }], output='screen'),
        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager_keepout',
            output='screen',
            parameters=[{
                'use_sim_time': False,
                'autostart': True,
                'node_names': ['keepout_mask_server', 'keepout_filter_info_server'],
            }]),

        # t=1s: Nav2 导航栈 (压缩自3s: keepout已在t=0s激活, lifecycle可立即开始)
        TimerAction(period=1.0, actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource([
                    nav2_bringup_dir, '/launch', '/bringup_launch.py'
                ]),
                launch_arguments={
                    'map': map_yaml_path,
                    'use_sim_time': use_sim_time,
                    'params_file': rpp_param_path,
                    'use_composition': 'True',
                }.items(),
            ),
        ]),
    ])
