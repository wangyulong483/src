/**
 * @file origincar_base.cpp
 * @brief OriginCar 机器人底层驱动主程序
 * @details 实现与 STM32 下位机的串口通信，完成：
 *          - 速度指令解析与发送
 *          - IMU 和里程计数据接收与解算
 *          - 传感器数据发布（IMU、里程计、电压）
 */

#include "origincar_base/origincar_base.h"
#include "rclcpp/rclcpp.hpp"
#include "origincar_base/Quaternion_Solution.h"
#include "ackermann_msgs/msg/ackermann_drive_stamped.hpp" 
#include "origincar_msg/msg/data.hpp"

using std::placeholders::_1;
using namespace std;

// ============ 全局变量定义 ============
sensor_msgs::msg::Imu Mpu6050;  ///< 全局 IMU 数据对象
rclcpp::Node::SharedPtr node_handle = nullptr;  ///< 全局节点指针


/**
 * @brief 主函数
 * @param argc 命令行参数个数
 * @param argv 命令行参数数组
 * @return 返回值（0 表示正常退出）
 */
int main(int argc, char *argv[])
{
    rclcpp::init(argc, argv);           // 初始化 ROS2 系统 (installs proper SIGINT handler)
    origincar_base Robot_Control;       // 创建机器人控制对象
    Robot_Control.Control();            // 进入主控制循环
    rclcpp::shutdown();                 // 关闭 ROS2 系统
    return 0;
}

/**
 * @brief IMU 数据转换函数（高低字节转 short）
 * @param Data_High 高字节数据
 * @param Data_Low 低字节数据
 * @return 转换后的 short 类型值
 */
short origincar_base::IMU_Trans(uint8_t Data_High,uint8_t Data_Low)
{
    short transition_16;
    transition_16 = 0;
    transition_16 |=  Data_High<<8;     // 高字节左移 8 位
    transition_16 |=  Data_Low;         // 合并低字节
    return transition_16;
}

/**
 * @brief 里程计数据转换函数（高低字节转 float）
 * @param Data_High 高字节数据
 * @param Data_Low 低字节数据
 * @return 转换后的浮点型速度值
 * @details 将 16 位整数转换为以 m/s 为单位的速度值
 */
float origincar_base::Odom_Trans(uint8_t Data_High,uint8_t Data_Low)
{
    float data_return;
    short transition_16;
    transition_16 = 0;
    transition_16 |=  Data_High<<8;
    transition_16 |=  Data_Low;
    data_return   =  (transition_16 / 1000)+(transition_16 % 1000)*0.001;  // 转换为浮点数
    return data_return;
  }

/**
 * @brief Ackermann 转向指令回调函数
 * @param akm_ctl Ackermann 驱动指令消息指针
 * @details 接收阿克曼转向模型的线速度和转向角指令，
 *          打包成帧后通过串口发送给下位机
 */
void origincar_base::Akm_Cmd_Vel_Callback(const ackermann_msgs::msg::AckermannDriveStamped::SharedPtr akm_ctl)
{
    short  transition;
  
    Send_Data.tx[0]=FRAME_HEADER;     // 帧头
    Send_Data.tx[1] = 0;              // 保留字节
    Send_Data.tx[2] = 0; 

    transition=0;
    transition = akm_ctl->drive.speed*1000;  // 速度放大 1000 倍传输
    Send_Data.tx[4] = transition;            // 速度低字节
    Send_Data.tx[3] = transition>>8;         // 速度高字节

    transition=0;
    transition = akm_ctl->drive.steering_angle*1000/2;  // 转向角放大并除以 2
    Send_Data.tx[8] = transition;
    Send_Data.tx[7] = transition>>8;

    Send_Data.tx[9]=Check_Sum(9,SEND_DATA_CHECK);  // 计算校验和
    Send_Data.tx[10]=FRAME_TAIL;                   // 帧尾

    try {
      Stm32_Serial.write(Send_Data.tx,sizeof (Send_Data.tx));  // 通过串口发送
    } catch (serial::IOException& e) {
        RCLCPP_ERROR(this->get_logger(),("Unable to send data through serial port"));
    }
}

/**
 * @brief 普通速度指令回调函数
 * @param twist_aux Twist 类型速度消息指针
 * @details 接收线速度和角速度指令，
 *          打包成帧后通过串口发送给下位机
 */
void origincar_base::Cmd_Vel_Callback(const geometry_msgs::msg::Twist::SharedPtr twist_aux)
{
    short  transition;
    Send_Data.tx[0]=FRAME_HEADER;
    Send_Data.tx[1] = 0;
    Send_Data.tx[2] = 0; 

    transition=0;
    transition = twist_aux->linear.x*1000;  // X 轴线速度
    Send_Data.tx[4] = transition;
    Send_Data.tx[3] = transition>>8;

    transition=0;
    transition = twist_aux->linear.y*1000;  // Y 轴线速度
    Send_Data.tx[6] = transition;
    Send_Data.tx[5] = transition>>8;

    transition=0;
    transition = (twist_aux->angular.z)*1000;  // Z 轴角速度
    Send_Data.tx[8] = transition;
    Send_Data.tx[7] = transition>>8;

    Send_Data.tx[9]=Check_Sum(9,SEND_DATA_CHECK);
    Send_Data.tx[10]=FRAME_TAIL;

    try {
      if (akm_cmd_vel == "none") {  // 只有在未使用阿克曼模式时才发送
        Stm32_Serial.write(Send_Data.tx,sizeof (Send_Data.tx));
      } 
    } catch (serial::IOException& e) {
        RCLCPP_ERROR(this->get_logger(),("Unable to send data through serial port"));
    }
}

/**
 * @brief 信号切换回调函数（已禁用）
 * @param sign_switch 信号值指针
 * @details 用于重置机器人位置和速度（目前被注释掉）
 */
void origincar_base::Sign_Switch_Callback(const std_msgs::msg::Int32::SharedPtr sign_switch)
{
    // 位姿重置已移至管理节点, 驱动节点不修改状态
    (void)sign_switch;
}

/**
 * @brief 发布 IMU 传感器数据
 * @details 将 MPU6050 解算得到的姿态、角速度、加速度信息发布到 ROS2 话题
 */
void origincar_base::Publish_ImuSensor()
{
    sensor_msgs::msg::Imu Imu_Data_Pub;
    Imu_Data_Pub.header.stamp = rclcpp::Node::now();  // 设置时间戳
    Imu_Data_Pub.header.frame_id = gyro_frame_id;     // 设置坐标系
                                                  
    Imu_Data_Pub.orientation.x = Mpu6050.orientation.x;  // 四元数姿态
    Imu_Data_Pub.orientation.y = Mpu6050.orientation.y;
    Imu_Data_Pub.orientation.z = Mpu6050.orientation.z;
    Imu_Data_Pub.orientation.w = Mpu6050.orientation.w;
    // 姿态协方差（基于 MPU6050+Mahony互补滤波 实际噪声水平估算）
    // Roll/Pitch: 标准差约 0.045rad (~2.5°)，方差≈0.002
    // Yaw（无磁力计）: 标准差约 0.1rad (~5.7°)，方差≈0.01，反映无磁力计时的漂移
    // 参考: MPU6050 datasheet, Mahony filter community evaluation, ROS2 REP-103
    Imu_Data_Pub.orientation_covariance[0] = 0.002;
    Imu_Data_Pub.orientation_covariance[4] = 0.002;
    Imu_Data_Pub.orientation_covariance[8] = 0.01;
    Imu_Data_Pub.angular_velocity.x = Mpu6050.angular_velocity.x;  // 角速度
    Imu_Data_Pub.angular_velocity.y = Mpu6050.angular_velocity.y;
    Imu_Data_Pub.angular_velocity.z = Mpu6050.angular_velocity.z;
    // 角速度协方差（MPU6050陀螺仪RMS噪声约0.05°/s≈0.00087rad/s，方差≈7.6e-7）
    // 取稍大值 1e-5 以涵盖未建模的振动和温漂
    // 参考: MPU6050 datasheet rate noise density, Allan variance analysis
    Imu_Data_Pub.angular_velocity_covariance[0] = 1e-5;
    Imu_Data_Pub.angular_velocity_covariance[4] = 1e-5;
    Imu_Data_Pub.angular_velocity_covariance[8] = 1e-5;
    Imu_Data_Pub.linear_acceleration.x = Mpu6050.linear_acceleration.x;  // 线加速度
    Imu_Data_Pub.linear_acceleration.y = Mpu6050.linear_acceleration.y;
    Imu_Data_Pub.linear_acceleration.z = Mpu6050.linear_acceleration.z;
    // 线加速度协方差（MPU6050加速度计噪声密度~300μg/√Hz, 取0.05以涵盖振动）
    // 参考: MPU6050 datasheet, ROS2 community practice
    Imu_Data_Pub.linear_acceleration_covariance[0] = 0.05;
    Imu_Data_Pub.linear_acceleration_covariance[4] = 0.05;
    Imu_Data_Pub.linear_acceleration_covariance[8] = 0.05;

    imu_publisher->publish(Imu_Data_Pub);  // 发布消息

}

/**
 * @brief 发布里程计信息
 * @details 计算机器人位置、姿态和速度，并发布到 ROS2 话题
 */
void origincar_base::Publish_Odom()
{
    tf2::Quaternion q;
    q.setRPY(0,0,Robot_Pos.Z);  // 根据航向角设置四元数
    geometry_msgs::msg::Quaternion odom_quat=tf2::toMsg(q);
    
    origincar_msg::msg::Data robotpose;  // 位置消息
    origincar_msg::msg::Data robotvel;   // 速度消息
    nav_msgs::msg::Odometry odom;        // 里程计消息

    odom.header.stamp = rclcpp::Node::now();
    odom.header.frame_id = odom_frame_id;
    odom.child_frame_id = robot_frame_id;

    odom.pose.pose.position.x = Robot_Pos.X;  // X 位置
    odom.pose.pose.position.y = Robot_Pos.Y;  // Y 位置

    odom.pose.pose.position.z = 0.0;
    odom.pose.pose.orientation = odom_quat;   // 姿态四元数


    odom.twist.twist.linear.x =  Robot_Vel.X;  // X 线速度
    odom.twist.twist.linear.y =  Robot_Vel.Y;  // Y 线速度
    odom.twist.twist.angular.z = Robot_Vel.Z;  // Z 角速度

    robotpose.x = Robot_Pos.X;
    robotpose.y = Robot_Pos.Y;
    robotpose.z = Robot_Pos.Z;

    robotvel.x = Robot_Vel.X;
    robotvel.y = Robot_Vel.Y;
    robotvel.z = Robot_Vel.Z;

    odom_publisher->publish(odom);           // 发布里程计
    robotpose_publisher->publish(robotpose); // 发布位置
    robotvel_publisher->publish(robotvel);   // 发布速度
}

/**
 * @brief 发布电池电压信息
 * @details 定时发布当前电池电压到 ROS2 话题
 */
void origincar_base::Publish_Voltage()
{
    std_msgs::msg::Float32 voltage_msgs;
    static float Count_Voltage_Pub = 0;

    if (Count_Voltage_Pub++ > 10) {  // 每 10 次循环发布一次
        Count_Voltage_Pub = 0;
        voltage_msgs.data = Power_voltage;
        voltage_publisher->publish(voltage_msgs);
    }
}

/**
 * @brief 校验和计算函数
 * @param Count_Number 参与校验的字节数
 * @param mode 校验模式（0:接收数据校验，1:发送数据校验）
 * @return 计算得到的校验和
 */
unsigned char origincar_base::Check_Sum(unsigned char Count_Number,unsigned char mode)
{
    unsigned char check_sum = 0, k;

    if (mode == 0) {
      for(k=0; k < Count_Number; k++) {
        check_sum = check_sum^Receive_Data.rx[k];  // 接收数据异或校验
      }
    } else if (mode == 1) {
      for (k=0; k < Count_Number; k++) {
        check_sum = check_sum^Send_Data.tx[k];     // 发送数据异或校验
      }
    }

    return check_sum;
}

/**
 * @brief 从串口获取传感器数据
 * @return true 表示成功读取并校验通过，false 表示失败
 * @details 从串口读取 24 字节数据帧，解析出：
 *          - 机器人速度反馈
 *          - MPU6050 加速度和陀螺仪数据
 *          - 电池电压
 */
bool origincar_base::Get_Sensor_Data()
{
    short transition_16 = 0, j = 0, Header_Pos = 0, Tail_Pos = 0;
    uint8_t Receive_Data_Pr[RECEIVE_DATA_SIZE] = {0}; 
    Stm32_Serial.read(Receive_Data_Pr,sizeof (Receive_Data_Pr));  // 读取串口数据
    
    // 查找帧头和帧尾位置
    for (j = 0; j < 24; j++) {
      if (Receive_Data_Pr[j] == FRAME_HEADER)
      Header_Pos=j;
      else if (Receive_Data_Pr[j] == FRAME_TAIL)
      Tail_Pos = j;
    }

    // 根据帧头帧尾位置重组数据
    if (Tail_Pos == (Header_Pos + 23)) {
      memcpy(Receive_Data.rx, Receive_Data_Pr, sizeof(Receive_Data_Pr));
    }  else if (Header_Pos == (1 + Tail_Pos)) {
      for (j = 0;j < 24; j++)
      Receive_Data.rx[j] = Receive_Data_Pr[(j+Header_Pos) % 24];
    }  else {
    return false;  // 帧格式错误
    }

    Receive_Data.Frame_Header = Receive_Data.rx[0];
    Receive_Data.Frame_Tail = Receive_Data.rx[23];
    if (Receive_Data.Frame_Header == FRAME_HEADER) {
      if (Receive_Data.Frame_Tail == FRAME_TAIL) {
        if (Receive_Data.rx[22] == Check_Sum(22,READ_DATA_CHECK)||(Header_Pos == (1 + Tail_Pos))) {
          Receive_Data.Flag_Stop=Receive_Data.rx[1];  // 停止标志
          
          // 解析速度反馈
          Robot_Vel.X = Odom_Trans(Receive_Data.rx[2],Receive_Data.rx[3]);
          Robot_Vel.Y = Odom_Trans(Receive_Data.rx[4],Receive_Data.rx[5]);
          Robot_Vel.Z = Odom_Trans(Receive_Data.rx[6],Receive_Data.rx[7]); 

          // 解析 MPU6050 数据
          Mpu6050_Data.accele_x_data = IMU_Trans(Receive_Data.rx[8],Receive_Data.rx[9]);
          Mpu6050_Data.accele_y_data = IMU_Trans(Receive_Data.rx[10],Receive_Data.rx[11]);
          Mpu6050_Data.accele_z_data = IMU_Trans(Receive_Data.rx[12],Receive_Data.rx[13]);
          Mpu6050_Data.gyros_x_data = IMU_Trans(Receive_Data.rx[14],Receive_Data.rx[15]);
          Mpu6050_Data.gyros_y_data = IMU_Trans(Receive_Data.rx[16],Receive_Data.rx[17]);
          Mpu6050_Data.gyros_z_data = IMU_Trans(Receive_Data.rx[18],Receive_Data.rx[19]);

          // 转换为物理量
          Mpu6050.linear_acceleration.x = Mpu6050_Data.accele_x_data / ACCEl_RATIO;
          Mpu6050.linear_acceleration.y = Mpu6050_Data.accele_y_data / ACCEl_RATIO;
          Mpu6050.linear_acceleration.z = Mpu6050_Data.accele_z_data / ACCEl_RATIO;

          Mpu6050.angular_velocity.x =  Mpu6050_Data.gyros_x_data * GYROSCOPE_RATIO;
          Mpu6050.angular_velocity.y =  Mpu6050_Data.gyros_y_data * GYROSCOPE_RATIO;
          Mpu6050.angular_velocity.z =  Mpu6050_Data.gyros_z_data * GYROSCOPE_RATIO;

          // 解析电池电压
          transition_16 = 0;
          transition_16 |=  Receive_Data.rx[20]<<8;
          transition_16 |=  Receive_Data.rx[21];
          Power_voltage = transition_16/1000+(transition_16 % 1000)*0.001;

          return true;
        }
      }
    }

    return false;
}

/**
 * @brief 主控制循环
 * @details 循环执行以下任务：
 *          - 读取传感器数据
 *          - 解算里程计位置
 *          - 解算 IMU 姿态
 *          - 发布各类传感器消息
 */
void origincar_base::Control()
{
    rclcpp::Time current_time, last_time;
    current_time = rclcpp::Node::now();
    last_time = rclcpp::Node::now();
    while(rclcpp::ok()) {
      current_time = rclcpp::Node::now();
      Sampling_Time = (current_time - last_time).seconds();  // 计算采样周期
      
      if (true == Get_Sensor_Data()) {  // 如果成功获取传感器数据
        // 里程计位置解算（带补偿系数）
        Robot_Pos.X+=1.03*(Robot_Vel.X * cos(Robot_Pos.Z) - Robot_Vel.Y * sin(Robot_Pos.Z)) * Sampling_Time;
        Robot_Pos.Y+=1.125*(Robot_Vel.X * sin(Robot_Pos.Z) + Robot_Vel.Y * cos(Robot_Pos.Z)) * Sampling_Time;
        Robot_Pos.Z+=Robot_Vel.Z * Sampling_Time;

        // IMU 姿态解算
        Quaternion_Solution(Mpu6050.angular_velocity.x, Mpu6050.angular_velocity.y, Mpu6050.angular_velocity.z,\
                  Mpu6050.linear_acceleration.x, Mpu6050.linear_acceleration.y, Mpu6050.linear_acceleration.z);
        
        Publish_ImuSensor();   // 发布 IMU 数据
        Publish_Voltage();     // 发布电压数据
        Publish_Odom();        // 发布里程计数据
        rclcpp::spin_some(this->get_node_base_interface());  // 处理 ROS2 回调
      }
      last_time = current_time;
    }
}

/**
 * @brief 构造函数
 * @details 初始化 ROS2 节点、参数、发布者和订阅者，打开串口
 */
origincar_base::origincar_base()
: rclcpp::Node ("origincar_base")
{
  // 清零数据结构
  memset(&Robot_Pos, 0, sizeof(Robot_Pos));
  memset(&Robot_Vel, 0, sizeof(Robot_Vel));
  memset(&Receive_Data, 0, sizeof(Receive_Data));
  memset(&Send_Data, 0, sizeof(Send_Data));
  memset(&Mpu6050_Data, 0, sizeof(Mpu6050_Data));

  int serial_baud_rate = 115200;  // 默认波特率

  // 声明 ROS2 参数
  this->declare_parameter<std::string>("usart_port_name", "/dev/ttyCH343USB0");
  this->declare_parameter<std::string>("cmd_vel", "cmd_vel");
  this->declare_parameter<std::string>("akm_cmd_vel", "ackermann_cmd");
  this->declare_parameter<std::string>("odom_frame_id", "odom");
  this->declare_parameter<std::string>("robot_frame_id", "base_footprint");
  this->declare_parameter<std::string>("gyro_frame_id", "gyro_link");

  // 获取参数值
  this->get_parameter("serial_baud_rate", serial_baud_rate);
  this->get_parameter("usart_port_name", usart_port_name);
  this->get_parameter("cmd_vel", cmd_vel);
  this->get_parameter("akm_cmd_vel", akm_cmd_vel);
  this->get_parameter("odom_frame_id", odom_frame_id);
  this->get_parameter("robot_frame_id", robot_frame_id);
  this->get_parameter("gyro_frame_id", gyro_frame_id);

  // 创建发布者
  odom_publisher = create_publisher<nav_msgs::msg::Odometry>("odom", 10);
  imu_publisher = create_publisher<sensor_msgs::msg::Imu>("imu/data_raw", 10);
  voltage_publisher = create_publisher<std_msgs::msg::Float32>("PowerVoltage", 1);
  robotpose_publisher = create_publisher<origincar_msg::msg::Data>("robotpose", 10);
  robotvel_publisher = create_publisher<origincar_msg::msg::Data>("robotvel", 10);

  // 创建订阅者
  Cmd_Vel_Sub = create_subscription<geometry_msgs::msg::Twist>(
      cmd_vel, 1, std::bind(&origincar_base::Cmd_Vel_Callback, this, _1));
  Akm_Cmd_Vel_Sub = create_subscription<ackermann_msgs::msg::AckermannDriveStamped>(
      akm_cmd_vel, 1, std::bind(&origincar_base::Akm_Cmd_Vel_Callback, this, _1));

  Sign_Switch_Sub = create_subscription<std_msgs::msg::Int32>(
      "/sign4return", 1, std::bind(&origincar_base::Sign_Switch_Callback, this, _1));
  
  // 打开串口
  try  {
    Stm32_Serial.setPort("/dev/ttyACM0");
    Stm32_Serial.setBaudrate(serial_baud_rate);
    serial::Timeout _time = serial::Timeout::simpleTimeout(500);
    Stm32_Serial.setTimeout(_time);
    Stm32_Serial.open();
  } catch (serial::IOException& e) {
    RCLCPP_ERROR(this->get_logger(),"origincar_base can not open serial port,Please check the serial port cable! ");
  }
  if(Stm32_Serial.isOpen()) {
    RCLCPP_INFO(this->get_logger(),"origincar_base serial port opened");
    // Register a safe shutdown callback to send a stop command to the STM32
    // before the node is destroyed. rclcpp::on_shutdown() is called from a
    // proper thread context (not a signal handler), so all I/O and rclcpp
    // calls are safe here.
    rclcpp::on_shutdown([this]() {
      if (!Stm32_Serial.isOpen()) return;
      Send_Data.tx[0] = FRAME_HEADER;
      Send_Data.tx[1] = 0;
      Send_Data.tx[2] = 0;
      Send_Data.tx[4] = 0;
      Send_Data.tx[3] = 0;
      Send_Data.tx[6] = 0;
      Send_Data.tx[5] = 0;
      Send_Data.tx[7] = 0;
      Send_Data.tx[8] = 0;
      int check_sum = 0;
      for (int k = 0; k < 9; k++) {
        check_sum = check_sum ^ Send_Data.tx[k];
      }
      Send_Data.tx[9] = check_sum;
      Send_Data.tx[10] = FRAME_TAIL;
      try {
        Stm32_Serial.write(Send_Data.tx, sizeof(Send_Data.tx));
        RCLCPP_INFO(rclcpp::get_logger("origincar_base"),
                    "Stop command sent to STM32 on shutdown.");
      } catch (const serial::IOException& e) {
        RCLCPP_ERROR(rclcpp::get_logger("origincar_base"),
                     "Failed to send stop command on shutdown: %s", e.what());
      }
    });
  }
}


/**
 * @brief 析构函数
 * @details 打印关机日志
 */
origincar_base::~origincar_base()
{
  RCLCPP_INFO(this->get_logger(),"Shutting down");
}
