#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@file base_serial.launch.py
@brief OriginCar 底层串口通信启动文件
@details 该文件用于启动 OriginCar 的底层串口通信节点，支持两种模式：
         1. 阿克曼转向模式 (akmcar=true) - 使用 ackermann_cmd 话题
         2. 普通差速模式 (akmcar=false) - 直接使用 cmd_vel 话题
         
工作模式说明:
    - 阿克曼模式：额外启动 cmd_vel 转换节点，将普通速度指令转为阿克曼转向指令
    - 差速模式：直接使用 cmd_vel 控制机器人
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition, UnlessCondition
import launch_ros.actions

def generate_launch_description():
    """
    @brief 生成启动描述
    @return LaunchDescription 对象
    """
    # 定义 akmar 参数（默认为 false，即差速模式）
    akmcar = LaunchConfiguration('akmcar', default='false')

    # ============ 机器人基础参数配置 ============
    robot_parameters = [
        {'usart_port_name': '/dev/ttyACM0',      # 串口设备名称（STM32 连接的串口）
         'serial_baud_rate': 115200,             # 串口波特率
         'robot_frame_id': 'base_footprint',     # 机器人基座坐标系 ID - 改为base_footprint作为机器人在地面的投影
         'odom_frame_id': 'odom',                # 里程计坐标系 ID - 改为标准的 odom
         'cmd_vel': 'cmd_vel',                   # 速度指令话题名称
         'product_number': 0}                    # 产品编号（暂未使用）
    ]

    return LaunchDescription([
        # ============ 声明启动参数 ============
        DeclareLaunchArgument(
            'akmcar',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'  # 参数描述（实际应为是否使用阿克曼模式）
        ),

        # ============ 阿克曼转向模式 ============
        # 当 akmcar=true 时启动以下两个节点
        launch_ros.actions.Node(
            condition=IfCondition(akmcar),  # 条件：akmcar=true
            package='origincar_base',
            executable='origincar_base_node',  # 底层驱动节点
            parameters=robot_parameters + [{'akm_cmd_vel': 'ackermann_cmd'}],  # 使用 ackermann_cmd 话题
            remappings=[('/cmd_vel', 'cmd_vel')],  # 重映射 cmd_vel 话题
            respawn=True,
            respawn_delay=2.0,
        ),

        launch_ros.actions.Node(
            condition=IfCondition(akmcar),  # 条件：akmcar=true
            package='origincar_base',
            executable='cmd_vel_to_ackermann_drive.py',  # 速度转换脚本
            name='cmd_vel_to_ackermann_drive',  # 节点名称
            # 功能：订阅 cmd_vel -> 转换为 ackermann_cmd -> 发布
        ),

        # ============ 普通差速模式 ============
        # 当 akmcar=false 时启动
        launch_ros.actions.Node(
            condition=UnlessCondition(akmcar),  # 条件：akmcar=false
            package='origincar_base',
            executable='origincar_base_node',  # 底层驱动节点
            parameters=robot_parameters + [{'akm_cmd_vel': 'none'}],  # 不使用 ackermann_cmd
            # 直接使用 cmd_vel 控制机器人
            respawn=True,
            respawn_delay=2.0,
        )
    ])