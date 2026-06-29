import os
from pathlib import Path
import launch
import launch_ros
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch.actions import DeclareLaunchArgument
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource

"""
bringup.launch.py — 系统集成启动文件（底盘 + 激光雷达 + TF + 双IMU + EKF）

TF 发布策略（遵循 REP-105）:

  场景 A: 导航模式 (use_ekf:=true, pub_odom_tf:=false, 默认)
    - Madgwick 滤波: /imu/data_raw → /imu/data/madgwick (MPU6050 底盘)
    - BMI088: /imu_data (hobot_imu_sensor, 独立启动)
    - EKF 双IMU: /odom + /imu/data/madgwick(imu0) + /imu_data(imu1) → /odometry/filtered
    - EKF 发布 odom→base_footprint
    - AMCL 发布 map→odom

  场景 B: 纯底盘驱动 (use_ekf:=false)
    - odom2tf 发布 odom→base_footprint (原始编码器)

开关:
  use_bmi088:=true  (默认) — 双IMU EKF
  use_bmi088:=false        — 仅 MPU6050

不启动: task_manager, competition_lifecycle_manager, pose_pid_corrector
"""

def generate_launch_description():
    origincar_bringup_dir = get_package_share_directory('origincar_bringup')
    lslidar_ros2_dir = get_package_share_directory('lslidar_driver')
    origincar_base_dir = get_package_share_directory('origincar_base')

    use_ekf = LaunchConfiguration('use_ekf', default='true')
    pub_odom_tf = LaunchConfiguration('pub_odom_tf', default='false')
    use_bmi088 = LaunchConfiguration('use_bmi088', default='true')

    base_serial = launch.actions.IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [origincar_base_dir, '/launch', '/base_serial.launch.py']),
    )

    lslidar_launch = launch_ros.actions.Node(
        package='lslidar_driver',
        executable='lslidar_driver_node',
        name='lslidar_driver_node',
        output='screen',
        parameters=[Path(lslidar_ros2_dir, 'params', 'lsx10.yaml')],
        respawn=True,
        respawn_delay=2.0,
    )

    urdf2tf = launch.actions.IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [origincar_bringup_dir, '/launch', '/urdf2tf.launch.py']),
    )

    odom2tf = launch_ros.actions.Node(
        package='origincar_bringup',
        executable='odom2tf',
        output='screen',
        condition=UnlessCondition(use_ekf),
    )

    mission_controller = launch_ros.actions.Node(
        package='origincar_bringup',
        executable='mission_controller.py',
        output='screen',
    )

    return launch.LaunchDescription([
        DeclareLaunchArgument(
            'use_ekf', default_value='true',
            description='Enable EKF fusion'),
        DeclareLaunchArgument(
            'pub_odom_tf', default_value='false',
            description='Publish odom->base_footprint TF from raw /odom'),
        DeclareLaunchArgument(
            'use_bmi088', default_value='true',
            description='Enable dual-IMU EKF (BMI088 as imu1)'),
        base_serial,
        lslidar_launch,
        urdf2tf,
        odom2tf,

        # -- MPU6050 Madgwick 滤波 (底盘内置) --
        launch_ros.actions.Node(
            condition=IfCondition(use_ekf),
            package='origincar_bringup',
            executable='imu_madgwick_filter.py',
            name='imu_madgwick_filter',
            output='screen',
            parameters=[Path(origincar_base_dir, 'config', 'imu_madgwick.yaml')],
            respawn=True,
            respawn_delay=2.0,
        ),

        # -- BMI088 IMU 桥 (RDK X5 板载, srpi-config → IIO → /imu_data) --
        launch_ros.actions.Node(
            condition=IfCondition(use_bmi088),
            package='origincar_bringup',
            executable='bmi088_iio_bridge.py',
            name='bmi088_iio_bridge',
            output='screen',
            parameters=[{
                'rate': 100.0,
                'frame_id': 'gyro_link',
            }],
        ),

        # -- EKF 双IMU: use_ekf AND use_bmi088 --
        launch_ros.actions.Node(
            condition=IfCondition(PythonExpression([
                "'true' if '", use_ekf, "' == 'true' and '", use_bmi088, "' == 'true' else 'false'"
            ])),
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[Path(origincar_base_dir, 'config', 'ekf_dual_imu.yaml')],
        ),

        # -- EKF 单IMU: use_ekf AND NOT use_bmi088 --
        launch_ros.actions.Node(
            condition=IfCondition(PythonExpression([
                "'true' if '", use_ekf, "' == 'true' and '", use_bmi088, "' == 'false' else 'false'"
            ])),
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[Path(origincar_base_dir, 'config', 'ekf.yaml')],
        ),

        mission_controller,
    ])
