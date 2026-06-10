/**
 * @file origincar_base.h
 * @brief OriginCar 机器人底层驱动头文件
 * @details 该文件定义了 OriginCar 机器人的基础控制类，包括：
 *          - 串口通信（与下位机 STM32 通信）
 *          - 里程计解算
 *          - IMU 数据处理
 *          - 速度控制
 */

#ifndef _ORIGINCAR_BASE_H_
#define _ORIGINCAR_BASE_H_

#include <memory>
#include <inttypes.h>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include <csignal>
#include <thread>

#include <iostream>
#include <string.h>
#include <string>
#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <unistd.h>
#include <rcl/types.h>
#include <sys/stat.h>

#include <serial/serial.h>
#include <fcntl.h>
#include <stdbool.h>
#include <std_msgs/msg/string.hpp>
#include <std_msgs/msg/float32.hpp>
#include <std_msgs/msg/int32.hpp>
#include <geometry_msgs/msg/pose.hpp>
#include <geometry_msgs/msg/vector3.hpp>
#include <geometry_msgs/msg/pose_stamped.hpp>
#include "tf2_geometry_msgs/tf2_geometry_msgs.hpp"
#include "tf2_msgs/msg/tf_message.hpp"
#include "tf2/LinearMath/Transform.h"
#include "tf2/LinearMath/Quaternion.h"
#include "ackermann_msgs/msg/ackermann_drive_stamped.hpp"
#include "origincar_msg/msg/data.hpp"
#include "origincar_msg/msg/sign.hpp"  // 匹配信号发送
#include <sensor_msgs/msg/imu.hpp>
#include <nav_msgs/msg/odometry.hpp>
using namespace std;


// ============ 通信协议定义 ============
#define SEND_DATA_CHECK   1          ///< 发送数据校验标志位
#define READ_DATA_CHECK   0          ///< 接收数据校验标志位
#define FRAME_HEADER      0X7B       ///< 数据帧帧头标识
#define FRAME_TAIL        0X7D       ///< 数据帧帧尾标识
#define RECEIVE_DATA_SIZE 24         ///< 下位机发送的数据长度（字节）
#define SEND_DATA_SIZE    11         ///< ROS 向下位机发送的数据长度（字节）
#define PI 				  3.1415926f ///< 圆周率常量

// ============ 传感器参数定义 ============
#define GYROSCOPE_RATIO   0.00026644f  ///< 陀螺仪数据转换比例系数
#define ACCEl_RATIO 	  1671.84f       ///< 加速度计数据转换比例系数

extern sensor_msgs::msg::Imu Mpu6050;  ///< 全局 IMU 数据对象

// ============ 协方差矩阵定义 ============
/// @brief 里程计位置协方差矩阵（默认）
const double odom_pose_covariance[36]   = {1e-3,    0,    0,   0,   0,    0,
										      0, 1e-3,    0,   0,   0,    0,
										      0,    0,  1e6,   0,   0,    0,
										      0,    0,    0, 1e6,   0,    0,
										      0,    0,    0,   0, 1e6,    0,
										      0,    0,    0,   0,   0,  1e3 };

/// @brief 里程计位置协方差矩阵（备用）
const double odom_pose_covariance2[36]  = {1e-9,    0,    0,   0,   0,    0,
										      0, 1e-3, 1e-9,   0,   0,    0,
										      0,    0,  1e6,   0,   0,    0,
										      0,    0,    0, 1e6,   0,    0,
										      0,    0,    0,   0, 1e6,    0,
										      0,    0,    0,   0,   0, 1e-9 };

/// @brief 里程计速度协方差矩阵（默认）
const double odom_twist_covariance[36]  = {1e-3,    0,    0,   0,   0,    0,
										      0, 1e-3,    0,   0,   0,    0,
										      0,    0,  1e6,   0,   0,    0,
										      0,    0,    0, 1e6,   0,    0,
										      0,    0,    0,   0, 1e6,    0,
										      0,    0,    0,   0,   0,  1e3 };

/// @brief 里程计速度协方差矩阵（备用）
const double odom_twist_covariance2[36] = {1e-9,    0,    0,   0,   0,    0,
										      0, 1e-3, 1e-9,   0,   0,    0,
										      0,    0,  1e6,   0,   0,    0,
										      0,    0,    0, 1e6,   0,    0,
										      0,    0,    0,   0, 1e6,    0,
										      0,    0,    0,   0,   0, 1e-9} ;

// ============ 数据结构定义 ============

/// @brief 速度和位置数据结构
/// @details 存储机器人在三维空间中的线速度和角速度
typedef struct __Vel_Pos_Data_
{
	float X;  ///< X 轴方向的速度或位置
	float Y;  ///< Y 轴方向的速度或位置
	float Z;  ///< Z 轴方向的速度或位置（通常为角速度或航向角）

} Vel_Pos_Data;

/// @brief MPU6050 IMU 原始数据结构
/// @details 存储加速度计和陀螺仪的原始 ADC 值
typedef struct __MPU6050_DATA_
{
	short accele_x_data;  ///< X 轴加速度原始数据
	short accele_y_data;  ///< Y 轴加速度原始数据
	short accele_z_data;  ///< Z 轴加速度原始数据
    short gyros_x_data;   ///< X 轴陀螺仪原始数据
	short gyros_y_data;   ///< Y 轴陀螺仪原始数据
	short gyros_z_data;   ///< Z 轴陀螺仪原始数据

} MPU6050_DATA;

/// @brief 发送数据结构
/// @details 用于封装发送给下位机的控制指令
typedef struct _SEND_DATA_
{
	uint8_t tx[SEND_DATA_SIZE];  ///< 发送数据缓冲区（11 字节）
	float X_speed;               ///< X 轴速度指令
	float Y_speed;               ///< Y 轴速度指令
	float Z_speed;               ///< Z 轴速度指令
	unsigned char Frame_Tail;    ///< 帧尾标识
} SEND_DATA;

/// @brief 接收数据结构
/// @details 用于解析从下位机接收的传感器数据
typedef struct _RECEIVE_DATA_
{
	uint8_t rx[RECEIVE_DATA_SIZE];  ///< 接收数据缓冲区（24 字节）
	uint8_t Flag_Stop;              ///< 停止标志位
	unsigned char Frame_Header;     ///< 帧头标识
	float X_speed;                  ///< X 轴速度反馈
	float Y_speed;                  ///< Y 轴速度反馈
	float Z_speed;                  ///< Z 轴速度反馈
	float Power_Voltage;            ///< 电池电压
	unsigned char Frame_Tail;       ///< 帧尾标识
} RECEIVE_DATA;

// ============ 主控制类定义 ============

/// @brief OriginCar 机器人基础控制类
/// @details 该类继承自 rclcpp::Node，实现以下功能：
///          - 串口通信管理
///          - 里程计解算与发布
///          - IMU 数据处理与发布
///          - 速度指令接收与转发
class origincar_base : public rclcpp::Node

{
public:
	origincar_base();   ///< 构造函数，初始化节点和串口
	~origincar_base();  ///< 析构函数，释放资源
	
	void Control();     ///< 主控制循环函数
	void Publish_Odom();///< 发布里程计信息

public : 
	serial::Serial Stm32_Serial;  ///< 串口通信对象，用于与 STM32 下位机通信

private:
	void declare_parameters();  ///< 声明 ROS2 参数
	void get_parameters();      ///< 获取 ROS2 参数值

	// 回调函数
	void Cmd_Vel_Callback(const geometry_msgs::msg::Twist::SharedPtr twist_aux);  ///< 处理线速度/角速度指令
	void Akm_Cmd_Vel_Callback(const ackermann_msgs::msg::AckermannDriveStamped::SharedPtr akm_ctl);  ///< 处理阿克曼转向指令

	// 数据发布函数
	void Publish_ImuSensor();  ///< 发布 IMU 传感器数据
	void Publish_Voltage();    ///< 发布电池电压信息
	auto createQuaternionMsgFromYaw(double yaw);  ///< 根据偏航角创建四元数消息

	// 数据处理函数
	bool Get_Sensor_Data();  ///< 从串口读取并解析传感器数据
	unsigned char Check_Sum(unsigned char Count_Number,unsigned char mode);  ///< 计算校验和
	short IMU_Trans(uint8_t Data_High,uint8_t Data_Low);  ///< IMU 数据格式转换（高低字节转 short）
	float Odom_Trans(uint8_t Data_High,uint8_t Data_Low);  ///< 里程计数据格式转换（高低字节转 float）

	void Sign_Switch_Callback(const std_msgs::msg::Int32::SharedPtr sign_switch);  ///< 处理信号切换（已注释）

private:
	// 时间相关
	rclcpp::Time _Now, _Last_Time;  ///< 当前时间和上次时间戳
	float Sampling_Time;            ///< 采样时间间隔

	// 订阅者
	rclcpp::Subscription<geometry_msgs::msg::Twist>::SharedPtr Cmd_Vel_Sub;  ///< cmd_vel 订阅者
	rclcpp::Subscription<ackermann_msgs::msg::AckermannDriveStamped>::SharedPtr Akm_Cmd_Vel_Sub;  ///< ackermann_cmd 订阅者

	// 发布者
	rclcpp::Publisher<nav_msgs::msg::Odometry>::SharedPtr odom_publisher;  ///< 里程计发布者
	rclcpp::Publisher<std_msgs::msg::Float32>::SharedPtr voltage_publisher;  ///< 电压发布者
	rclcpp::Publisher<sensor_msgs::msg::Imu>::SharedPtr imu_publisher;  ///< IMU 数据发布者

	rclcpp::Publisher<std_msgs::msg::Float32>::SharedPtr test_publisher;  ///< 测试用发布者

	rclcpp::Publisher<origincar_msg::msg::Data>::SharedPtr robotpose_publisher;  ///< 机器人位置发布者
	rclcpp::Publisher<origincar_msg::msg::Data>::SharedPtr robotvel_publisher;  ///< 机器人速度发布者

	rclcpp::Publisher<tf2_msgs::msg::TFMessage>::SharedPtr tf_pub_;  ///< TF 消息发布者
	rclcpp::TimerBase::SharedPtr test_timer;  ///< 测试定时器

	rclcpp::TimerBase::SharedPtr odom_timer;   ///< 里程计定时器
	rclcpp::TimerBase::SharedPtr imu_timer;    ///< IMU 定时器
	rclcpp::TimerBase::SharedPtr voltage_timer;  ///< 电压定时器

	rclcpp::TimerBase::SharedPtr robotpose_timer;   ///< 位置定时器
	rclcpp::TimerBase::SharedPtr robotvel_timer;    ///< 速度定时器

	rclcpp::Subscription<std_msgs::msg::Int32>::SharedPtr Sign_Switch_Sub;  ///< 信号切换订阅者（未使用）

	// 参数字符串
	string usart_port_name, robot_frame_id, gyro_frame_id, odom_frame_id, akm_cmd_vel, test;
	std::string cmd_vel;  ///< cmd_vel 话题名称
	int serial_baud_rate;  ///< 串口波特率

	// 数据缓冲区
	RECEIVE_DATA Receive_Data;  ///< 接收数据缓冲区
	SEND_DATA Send_Data;        ///< 发送数据缓冲区

	// 机器人状态
	Vel_Pos_Data Robot_Pos;  ///< 机器人位置（X, Y, Z 航向角）
	Vel_Pos_Data Robot_Vel;  ///< 机器人速度（线速度和角速度）
	MPU6050_DATA Mpu6050_Data;  ///< MPU6050 原始数据
	float Power_voltage;  ///< 电池电压
    size_t count_;  ///< 计数器（用于定时发布）
};


#endif //_ORIGINCAR_BASE_H_
