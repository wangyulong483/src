from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('rgb_topic', default_value='/aurora/rgb/image_raw'),
        DeclareLaunchArgument('depth_topic', default_value='/aurora/depth/image_raw'),
        DeclareLaunchArgument('enable_depth_filter', default_value='true'),
        DeclareLaunchArgument('depth_min_mm', default_value='150'),
        DeclareLaunchArgument('depth_max_mm', default_value='2000'),

        Node(
            package='qr_decoder',
            executable='qr_decoder',
            name='qr_half_field_scanner',
            parameters=[{
                'rgb_topic': LaunchConfiguration('rgb_topic'),
                'depth_topic': LaunchConfiguration('depth_topic'),
                'enable_depth_filter': LaunchConfiguration('enable_depth_filter'),
                'depth_min_mm': LaunchConfiguration('depth_min_mm'),
                'depth_max_mm': LaunchConfiguration('depth_max_mm'),
            }],
            output='screen',
        ),
    ])
