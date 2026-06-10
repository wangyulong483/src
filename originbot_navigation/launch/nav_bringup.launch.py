#!/usr/bin/python3

# Copyright (c) 2022, www.guyuehome.com
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

"""
Nav2 导航启动文件 (RPP 默认 + DWA 备选)

此文件用于启动完整的 Nav2 导航系统（基于已有地图进行定位与路径规划）。

支持两种局部规划器模式：
  - rpp:  Regulated Pure Pursuit + SmacPlannerHybrid (阿克曼默认，推荐)
  - dwa:  DWB + NavfnPlanner (差分底盘备选)

主要功能：
  - 通过 IncludeLaunchDescription 引用 bringup.launch.py 启动底盘+雷达+TF
  - 启动 Nav2 导航栈（AMCL 定位 + 全局/局部规划 + 行为树）
  - 启动 Rviz2 可视化界面

行为树路径注入机制：
  Humble navigation_launch.py 的 RewrittenYaml.param_substitutions 仅含
  use_sim_time 和 autostart，不覆写 BT XML 参数。
  但裸文件名只有作为绝对路径写入 YAML 时，bt_navigator 才能可靠加载。
  我们采用 regex 替换（容错空格/引号差异）+ 复制 BT XML 到 /tmp/ 作为
  备用路径，确保任何 CWD 下都能找到。
"""

import os
import re
import shutil
import tempfile

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, TimerAction
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition, UnlessCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node


def _patch_bt_path(yaml_path, old_filename, new_abs_path):
    """Replace bare BT XML filename with absolute path in YAML using regex.

    Uses regex instead of simple string replacement to handle whitespace and
    quoting variations between editing environments.

    Returns the path to the patched temporary YAML file.
    """
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
    # Package directories
    originbot_navigation_dir = get_package_share_directory('originbot_navigation')
    nav2_bringup_dir = get_package_share_directory('nav2_bringup')
    origincar_bringup_dir = get_package_share_directory('origincar_bringup')
    deptrum_dir = get_package_share_directory('deptrum-ros-driver-aurora930')

    # Paths — original YAML files
    rviz_config_dir = os.path.join(originbot_navigation_dir, 'rviz', 'nav.rviz')
    dwa_param_path_orig = os.path.join(originbot_navigation_dir, 'param', 'originbot_nav2.yaml')
    rpp_param_path_orig = os.path.join(originbot_navigation_dir, 'param', 'originbot_nav2_rpp.yaml')

    # Behavior tree XML absolute paths
    rpp_bt_xml_path = os.path.join(originbot_navigation_dir, 'behavior_trees', 'navigate_to_pose_ackermann_rpp.xml')
    rpp_bt_through_poses_xml_path = os.path.join(originbot_navigation_dir, 'behavior_trees', 'navigate_through_poses_ackermann_rpp.xml')
    dwa_bt_xml_path = os.path.join(originbot_navigation_dir, 'behavior_trees', 'navigate_to_pose_ackermann_dwa.xml')

    # ---- Copy BT XML to /tmp/ as fallback ----
    _rpp_bt_tmp = '/tmp/navigate_to_pose_ackermann_rpp.xml'
    _rpp_bt_through_poses_tmp = '/tmp/navigate_through_poses_ackermann_rpp.xml'
    _dwa_bt_tmp = '/tmp/navigate_to_pose_ackermann_dwa.xml'
    shutil.copy(rpp_bt_xml_path, _rpp_bt_tmp)
    shutil.copy(rpp_bt_through_poses_xml_path, _rpp_bt_through_poses_tmp)
    shutil.copy(dwa_bt_xml_path, _dwa_bt_tmp)

    # ---- Generate patched YAML files with absolute BT paths ----
    rpp_param_path = _patch_bt_path(
        rpp_param_path_orig, 'navigate_to_pose_ackermann_rpp.xml', rpp_bt_xml_path)
    rpp_param_path = _patch_bt_path(
        rpp_param_path, 'navigate_through_poses_ackermann_rpp.xml', rpp_bt_through_poses_xml_path)
    dwa_param_path = _patch_bt_path(
        dwa_param_path_orig, 'navigate_to_pose_ackermann_dwa.xml', dwa_bt_xml_path)

    # Launch configurations
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    map_yaml_path = LaunchConfiguration('map', default=os.path.join(originbot_navigation_dir, 'maps', 'room.yaml'))

    # Planner type: rpp (default) or dwa
    planner_type = LaunchConfiguration('planner_type', default='rpp')
    rpp_mode = PythonExpression(["'", planner_type, "' == 'rpp'"])

    # Aurora930 depth camera (optional, enabled via use_depth_camera:=true)
    use_depth_camera = LaunchConfiguration('use_depth_camera', default='true')
    depth_cam_x = LaunchConfiguration('depth_cam_x', default='0.14')
    depth_cam_y = LaunchConfiguration('depth_cam_y', default='0.0')
    depth_cam_z = LaunchConfiguration('depth_cam_z', default='0.05')
    depth_cam_roll = LaunchConfiguration('depth_cam_roll', default='0.0')
    depth_cam_pitch = LaunchConfiguration('depth_cam_pitch', default='0.0')
    depth_cam_yaw = LaunchConfiguration('depth_cam_yaw', default='0.0')

    return LaunchDescription([
        # =====================================================================
        # 所有参数声明（必须顶层，不能放在 TimerAction 内）
        # =====================================================================
        DeclareLaunchArgument('use_sim_time', default_value=use_sim_time,
                              description='Use simulation clock if true'),
        DeclareLaunchArgument('map', default_value=map_yaml_path,
                              description='Full path to map file to load'),
        DeclareLaunchArgument('planner_type', default_value='rpp',
                              description='Local planner type: rpp (default, recommended) or dwa'),

        # ---- Aurora930 深度相机参数（use_depth_camera:=true 时启用）----
        DeclareLaunchArgument('use_depth_camera', default_value='true',
                              description='Enable Aurora930 depth camera for pointcloud obstacle detection'),
        DeclareLaunchArgument('depth_cam_x', default_value='0.14',
                              description='Camera X offset from base_link (m, forward)'),
        DeclareLaunchArgument('depth_cam_y', default_value='0.0',
                              description='Camera Y offset from base_link (m, left)'),
        DeclareLaunchArgument('depth_cam_z', default_value='0.05',
                              description='Camera Z offset from base_link (m, up)'),
        DeclareLaunchArgument('depth_cam_roll', default_value='0.0',
                              description='Camera roll from base_link (rad)'),
        DeclareLaunchArgument('depth_cam_pitch', default_value='0.0',
                              description='Camera pitch from base_link (rad, positive=tilt down)'),
        DeclareLaunchArgument('depth_cam_yaw', default_value='0.0',
                              description='Camera yaw from base_link (rad)'),

        # =====================================================================
        # 错峰启动 (TimerAction) — 防止 TF 树未就绪导致 AMCL/Nav2 初始化失败
        # 参考: amphibious_ws rescue_task 的 TimerAction 模式
        # =====================================================================

        # t=0s: 底盘 + 激光雷达 + TF（bringup.launch.py 统一管理）
        TimerAction(period=0.0, actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource([origincar_bringup_dir, '/launch', '/bringup.launch.py']),
                # use_ekf:=true 默认, EKF 发布融合后 odom→base_footprint TF
            ),
        ]),

        # t=3s: Keepout 禁区服务器 (mask + filter_info + lifecycle_manager)
        TimerAction(period=3.0, actions=[
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
                    'type': 0,  # 0=keepout
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
        ]),

        # t=3s: Aurora930 深度相机 + 静态TF + QR扫描 (确保底盘/激光雷达 TF 树已稳定)
        TimerAction(period=3.0, actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource([
                    deptrum_dir, '/launch', '/aurora930_launch.py'
                ]),
                condition=IfCondition(use_depth_camera),
                launch_arguments={
                    'rgb_enable': 'true',
                    'depth_enable': 'true',
                    'ir_enable': 'false',
                    'point_cloud_enable': 'true',
                    'rgb_fps': '15',
                    'ir_fps': '15',
                    'heart_enable': 'true',
                }.items(),
            ),
            Node(
                package='tf2_ros',
                executable='static_transform_publisher',
                name='depth_camera_tf',
                condition=IfCondition(use_depth_camera),
                arguments=[
                    depth_cam_x, depth_cam_y, depth_cam_z,
                    depth_cam_yaw, depth_cam_pitch, depth_cam_roll,
                    'base_link', 'depth_camera_link'
                ],
                output='screen',
            ),
            # QR 码解码 (C++/ZBar): /aurora/rgb + /aurora/depth → /sign, /sign_pose
            Node(
                package='qr_decoder',
                executable='qr_decoder',
                name='qr_decoder_zbar',
                output='screen',
                parameters=[{
                    'rgb_topic': '/aurora/rgb/image_raw',
                    'depth_topic': '/aurora/depth/image_raw',
                    'enable_depth_filter': True,
                    'depth_min_mm': 150,
                    'depth_max_mm': 2000,
                }],
            ),
            # QR 方向决策: /sign → qr_event (方向+CW/CCW), 3s 冷却
            Node(
                package='origincar_qr',
                executable='qr_decision',
                name='qr_decision',
                output='screen',
                parameters=[{
                    'cooldown_sec': 3.0,
                }],
            ),
        ]),

        # 启动屏障: 等待 /odom 数据就绪 (最多15s), 替代硬编码5s延迟
        TimerAction(period=2.0, actions=[
            Node(
                package='origincar_bringup',
                executable='wait_for_odom.py',
                name='wait_for_odom_barrier',
                arguments=['--timeout', '15'],
                output='screen',
            ),
        ]),

        # Nav2 导航栈（压缩自5.0s: 底盘1-2s内出/odom, 无需等5s）
        # SmacPlannerHybrid + RegulatedPurePursuit + 自定义 BT（碰撞检测联动）
        TimerAction(period=2.0, actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource([nav2_bringup_dir, '/launch', '/bringup_launch.py']),
                condition=IfCondition(rpp_mode),
                launch_arguments={
                    'map': map_yaml_path,
                    'use_sim_time': use_sim_time,
                    'params_file': rpp_param_path,
                    'use_composition': 'False',
                }.items(),
            ),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource([nav2_bringup_dir, '/launch', '/bringup_launch.py']),
                condition=UnlessCondition(rpp_mode),
                launch_arguments={
                    'map': map_yaml_path,
                    'use_sim_time': use_sim_time,
                    'params_file': dwa_param_path,
                    'use_composition': 'False',
                }.items(),
            ),
        ]),

        # t=12s: 竞赛管理层 (Nav2 action server 就绪后启动 — bt_navigator 激活需 ~30s)
        TimerAction(period=12.0, actions=[
            Node(
                package='origincar_bringup',
                executable='task_manager.py',
                name='task_manager',
                output='screen',
                parameters=[{
                    'use_sim_time': use_sim_time,
                }],
            ),
            Node(
                package='origincar_bringup',
                executable='competition_lifecycle_manager.py',
                name='competition_lifecycle_manager',
                output='screen',
                parameters=[{
                    'use_sim_time': use_sim_time,
                }],
            ),
            Node(
                package='origincar_bringup',
                executable='pose_pid_corrector.py',
                name='pose_pid_corrector',
                output='screen',
                parameters=[{
                    'use_sim_time': use_sim_time,
                }],
            ),
        ]),

        # t=10s: RViz2（最后启动，此时所有话题已就绪）
        TimerAction(period=10.0, actions=[
            Node(
                package='rviz2',
                executable='rviz2',
                name='rviz2',
                arguments=['-d', rviz_config_dir],
                parameters=[{'use_sim_time': use_sim_time}],
                output='screen',
            ),
        ]),
    ])
