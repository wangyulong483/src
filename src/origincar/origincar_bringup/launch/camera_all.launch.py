import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python import get_package_share_directory


def generate_launch_description():
    # === QR深度过滤参数 ===
    depth_min_arg = DeclareLaunchArgument(
        'depth_min_mm', default_value='50',
        description='最小深度(mm), 近距离QR(5cm+)允许扫描'
    )
    depth_max_arg = DeclareLaunchArgument(
        'depth_max_mm', default_value='4000',
        description='最大深度(mm)，半场范围需要4m'
    )
    depth_min_mm = LaunchConfiguration('depth_min_mm')
    depth_max_mm = LaunchConfiguration('depth_max_mm')

    # === 深度相机安装位姿 (base_link → depth_camera_link) ===
    depth_cam_x = LaunchConfiguration('depth_cam_x', default='0.14')
    depth_cam_y = LaunchConfiguration('depth_cam_y', default='0.0')
    depth_cam_z = LaunchConfiguration('depth_cam_z', default='0.05')
    depth_cam_roll = LaunchConfiguration('depth_cam_roll', default='0.0')
    depth_cam_pitch = LaunchConfiguration('depth_cam_pitch', default='0.0')
    depth_cam_yaw = LaunchConfiguration('depth_cam_yaw', default='0.0')

    # === Aurora930 深度相机驱动 ===
    aurora_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('deptrum-ros-driver-aurora930'),
                'launch', 'aurora930_launch.py')
        ),
        launch_arguments={
            'rgb_enable': 'true',
            'depth_enable': 'true',
            'ir_enable': 'true',     # IR=深度传感器, 必须开启才有 /aurora/points2 和 /aurora/depth/image_raw
            'point_cloud_enable': 'true',
            'rgb_fps': '15',
            'ir_fps': '15',
            'heart_enable': 'false',   # 关闭心跳: SDK v1.1.22 与固件 v1.7.2 协议不兼容
            'stream_sdk_log_enable': 'false',
        }.items()
    )

    # depth_camera_link 静态TF: 必须在Aurora930启动时同步发布，
    # 否则PointCloud2消息时间戳早于TF缓存最早记录 → costmap持续丢帧
    # 使用 new-style --x/--y/--z/--roll/--pitch/--yaw/--frame-id/--child-frame-id 标志
    # (旧式位置参数会触发 ROS_WARN)
    camera_tf = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='depth_camera_tf',
        arguments=[
            '--x', depth_cam_x,
            '--y', depth_cam_y,
            '--z', depth_cam_z,
            '--roll', depth_cam_roll,
            '--pitch', depth_cam_pitch,
            '--yaw', depth_cam_yaw,
            '--frame-id', 'base_link',
            '--child-frame-id', 'depth_camera_link',
        ],
        output='screen',
    )

    # === qr_decoder (C++, ZBar) — 3D坐标+解码 终端输出 ===
    qr_decoder_node = Node(
        package='qr_decoder',
        executable='qr_decoder',
        name='qr_decoder_zbar',
        output='screen',
        parameters=[{
            'rgb_topic': '/aurora/rgb/image_raw',
            'depth_topic': '/aurora/depth/image_raw',
            'enable_depth_filter': True,
            'depth_min_mm': depth_min_mm,
            'depth_max_mm': depth_max_mm,
        }],
        arguments=['--ros-args', '--log-level', 'info']
    )

    # === qr_decision (Python) — 方向判断 + 停车控制（仅订阅 /sign，不重复解码） ===
    qr_decision_node = Node(
        package='qr_decoder',
        executable='qr_decision.py',
        name='qr_decision',
        output='screen',
        parameters=[{
            'cooldown_sec': 3.0,
        }],
    )

    return LaunchDescription([
        DeclareLaunchArgument('depth_cam_x', default_value='0.14'),
        DeclareLaunchArgument('depth_cam_y', default_value='0.0'),
        DeclareLaunchArgument('depth_cam_z', default_value='0.05'),
        DeclareLaunchArgument('depth_cam_roll', default_value='0.0'),
        DeclareLaunchArgument('depth_cam_pitch', default_value='0.0'),
        DeclareLaunchArgument('depth_cam_yaw', default_value='0.0'),
        depth_min_arg,
        depth_max_arg,
        camera_tf,
        aurora_node,
        qr_decoder_node,
        qr_decision_node,
    ])
