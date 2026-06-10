from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('cooldown_sec', default_value='3.0',
                              description='Same QR number re-trigger cooldown (seconds)'),

        Node(
            package='origincar_qr',
            executable='qr_decision',
            name='qr_decision',
            parameters=[{
                'cooldown_sec': LaunchConfiguration('cooldown_sec'),
            }],
            output='screen',
        ),
    ])
