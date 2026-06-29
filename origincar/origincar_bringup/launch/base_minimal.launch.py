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
base_minimal.launch.py — 最小系统集成启动（无管理层节点）

启动: 底盘 + 激光雷达 + TF + Madgwick + BMI088(可选) + 双IMU EKF
不启动: task_manager, mission_controller, competition_lifecycle_manager, pose_pid_corrector

IMU 架构:
  imu0: MPU6050(底盘) → STM32 → /imu/data_raw → Madgwick → /imu/data/madgwick
  imu1: BMI088(RDK X5) → /imu_data (imu_sensor, 独立启动)
  EKF 融合 odom + imu0(yaw姿态+角速度) + imu1(角速度)

开关:
  use_bmi088:=true  (默认) — 双IMU, EKF 读取 /imu_data, 启动 BMI088 驱动
  use_bmi088:=false        — 仅 MPU6050 (向后兼容)

不启动: task_manager, mission_controller, competition_lifecycle_manager, pose_pid_corrector
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

    return launch.LaunchDescription([
        DeclareLaunchArgument('use_ekf', default_value='true'),
        DeclareLaunchArgument('pub_odom_tf', default_value='false'),
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
                # RDK X5 IIO 驱动不提供 scale 文件 → 手动指定
                # BMI088 gyro @ ±1000°/s: 1 LSB = 0.000530 rad/s
                # BMI088 accel @ ±3g:     1 LSB = 0.003410 m/s²
                'gyro_scale_override': 0.000530,
                'accel_scale_override': 0.003410,
            }],
        ),

        # -- BMI088 Madgwick 滤波 (汽车级IMU → yaw姿态+角速度, 替代MPU6050为主IMU) --
        launch_ros.actions.Node(
            condition=IfCondition(use_bmi088),
            package='origincar_bringup',
            executable='imu_madgwick_filter.py',
            name='imu_madgwick_bmi088',
            output='screen',
            parameters=[Path(origincar_base_dir, 'config', 'imu_madgwick_bmi088.yaml')],
            respawn=True,
            respawn_delay=2.0,
            remappings=[
                ('/imu/data_raw', '/imu_data'),
                ('/imu/data/madgwick', '/imu/data/bmi088_madgwick'),
            ],
        ),

        # -- EKF 双IMU: use_ekf=true AND use_bmi088=true --
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

        # -- EKF 单IMU: use_ekf=true AND use_bmi088=false --
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

    ])
