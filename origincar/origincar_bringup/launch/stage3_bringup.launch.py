import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction, OpaqueFunction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

"""
stage3_bringup.launch.py — Stage 3 总启动文件

流程: QR扫码→通道入口→通道巡航(CCW/CW)→VLM图生文→返航P点
  t=0s → 底盘 + TF + Madgwick + EKF + PID + 深度相机 + QR
  t=1s → Nav2 全栈
  t=3s → 障碍物检测 + 粒子滤波跟踪 + costmap桥接
  t=4s → competition_master_stage3 (QR→入口→巡航→VLM→返航)
  t=8s → RViz2 (地图查看)
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
            OpaqueFunction(function=_vision_ai_if_available),  # VLM视觉AI节点

            # ── JPU hardware JPEG encoder (t+0s) ──
            # Encodes /aurora/rgb/image_raw → /aurora/rgb/image_jpeg using JPU
            # Replaces CPU cv2.imencode in vision_ai_node (saves 5-10ms per VLM trigger)
            Node(
                package='hobot_codec',
                executable='hobot_codec_republish',
                name='vlm_jpeg_encoder',
                output='screen',
                arguments=['--ros-args', '--log-level', 'warn'],
                parameters=[{
                    'in_format': 'bgr8',
                    'out_format': 'jpeg',
                    'sub_topic': '/aurora/rgb/image_raw',
                    'pub_topic': '/aurora/rgb/image_jpeg',
                    'jpg_quality': 85.0,
                }],
            ),

            # ── BGR→NV12 converter for YOLO BPU input (t+0s) ──
            Node(
                package='hobot_codec',
                executable='hobot_codec_republish',
                name='rgb_to_nv12',
                output='screen',
                arguments=['--ros-args', '--log-level', 'warn'],
                parameters=[{
                    'in_format': 'bgr8',
                    'out_format': 'nv12',
                    'in_mode': 'ros',
                    'out_mode': 'shared_mem',
                    'sub_topic': '/aurora/rgb/image_raw',
                    'pub_topic': '/hbmem_img',
                }],
            ),
        ]),

        TimerAction(period=1.0, actions=[
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(origincar_bringup_dir, 'launch', 'nav2_minimal.launch.py')
                )
            ),
        ]),

        # ── YOLO BPU obstacle detection (t+3s) ──
        # BGR→NV12 codec starts at t=0s; YOLO + bridge handle all obstacle perception
        TimerAction(period=3.0, actions=[
            # BPU YOLOv5 obstacle detection
            Node(
                package='racing_obstacle_detection_yolo',
                executable='racing_obstacle_detection_yolo',
                name='racing_obstacle_detection_yolo',
                output='screen',
                parameters=[{
                    'is_shared_mem_sub': True,
                    'sub_img_topic': '/hbmem_img',
                    'config_file': '/userdata/dev_ws/src/origincar/origincar_bringup/config/yolov5workconfig.json',
                }],
                arguments=['--ros-args', '--log-level', 'warn'],
            ),
            # PerceptionTargets → PointCloud2 bridge for costmap
            Node(
                package='origincar_bringup',
                executable='yolo_costmap_bridge.py',
                name='yolo_costmap_bridge',
                output='screen',
                emulate_tty=True,
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

        # ── Speed profile node (t+5s) ──
        # Subscribes to /plan; publishes /speed_limit based on
        # path curvature v(κ) = v_max/(1+β*|κ|^λ)
        TimerAction(period=5.0, actions=[
            Node(
                package='origincar_bringup',
                executable='speed_profile_node.py',
                name='speed_profile_node',
                output='screen',
                emulate_tty=True,
                parameters=[{
                    'v_max': 0.50,
                    'v_min': 0.15,
                    'beta': 0.47,
                    'lambda': 1.32,
                    'max_accel': 1.01,
                    'max_decel': -1.57,
                    'smoothing_window': 5,
                    'lookahead_idx': 10,
                }],
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
