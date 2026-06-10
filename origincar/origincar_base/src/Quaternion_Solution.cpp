/**
 * @file Quaternion_Solution.cpp
 * @brief 四元数姿态解算算法
 * @details 基于 MPU6050 的加速度计和陀螺仪数据，
 *          使用互补滤波算法计算机器人姿态（四元数表示）
 */

#include "origincar_base/Quaternion_Solution.h"
// 采样频率：原20Hz偏低，MPU6050陀螺仪带宽可达100Hz+
// 提升至30Hz以更好地捕获姿态动态，适合小车低速运动场景
// 参考: Mahony filter best practices, IMU update rate recommendations
#define SAMPLING_FREQ 30.0f // 采样频率 (Hz)

/**
 * @brief 快速平方根倒数算法
 * @param number 输入数值
 * @return 1/sqrt(number)
 * @details 使用著名的 0x5f375a86 魔术常数进行快速近似计算，
 *          用于四元数归一化
 */
float InvSqrt(float number)
{
  volatile long i;
    volatile float x, y;
    volatile const float f = 1.5F;
    x = number * 0.5F;
    y = number;
    i = * (( long * ) &y);              // 将浮点数按位解释为长整型
    i = 0x5f375a86 - ( i >> 1 );        // 核心算法：估算初始值
    y = * (( float * ) &i);             // 转回浮点数
    y = y * ( f - ( x * y * y ) );      // 牛顿迭代法优化精度

  return y;
}

// ============ 全局变量定义 ============
volatile float twoKp = 1.0f;     ///< 比例增益系数 (2 * Kp)，用于误差修正
volatile float twoKi = 0.0f;     ///< 积分增益系数 (2 * Ki)，用于消除累积误差
volatile float q0 = 1.0f, q1 = 0.0f, q2 = 0.0f, q3 = 0.0f;          ///< 四元数（传感器坐标系相对于辅助坐标系）
volatile float integralFBx = 0.0f,  integralFBy = 0.0f, integralFBz = 0.0f; ///< 积分误差项（已乘以 Ki）

/**
 * @brief 四元数姿态解算函数
 * @param gx X 轴陀螺仪角速度 (rad/s)
 * @param gy Y 轴陀螺仪角速度 (rad/s)
 * @param gz Z 轴陀螺仪角速度 (rad/s)
 * @param ax X 轴加速度计测量值 (m/s²)
 * @param ay Y 轴加速度计测量值 (m/s²)
 * @param az Z 轴加速度计测量值 (m/s²)
 * @details 使用 Mahony 互补滤波算法融合加速度计和陀螺仪数据，
 *          解算得到精确的姿态四元数
 * 
 * 算法步骤：
 * 1. 加速度计数据归一化
 * 2. 根据当前四元数计算估计的重力方向
 * 3. 计算估计重力与测量重力的叉积作为误差
 * 4. 使用 PI 控制器修正陀螺仪漂移
 * 5. 积分更新四元数
 * 6. 四元数归一化
 */
void Quaternion_Solution(float gx, float gy, float gz, float ax, float ay, float az)
{
  float recipNorm;           // 归一化系数
  float halfvx, halfvy, halfvz;  // 估计的重力方向分量
  float halfex, halfey, halfez;  // 误差分量
  float qa, qb, qc;          // 临时四元数变量
  
  // 仅当加速度计数据有效时计算反馈（避免除以零）
  if(!((ax == 0.0f) && (ay == 0.0f) && (az == 0.0f))) {
    // ========== 步骤 1: 加速度计数据归一化 ==========
    // 将加速度计采集的三维向量转化为单位向量
    recipNorm = InvSqrt(ax * ax + ay * ay + az * az);  // 计算模长的倒数
    ax *= recipNorm;  // 归一化
    ay *= recipNorm;      
    az *= recipNorm;      
    
    // ========== 步骤 2: 计算估计的重力方向 ==========
    // 把四元数换算成方向余弦中的第三行的三个元素（Z 轴方向）
    halfvx = q1 * q3 - q0 * q2;
    halfvy = q0 * q1 + q2 * q3;
    halfvz = q0 * q0 - 0.5f + q3 * q3;
    
    // ========== 步骤 3: 计算误差 ==========
    // 误差是估计的重力方向和测量的重力方向的叉积之和
    halfex = (ay * halfvz - az * halfvy);
    halfey = (az * halfvx - ax * halfvz);
    halfez = (ax * halfvy - ay * halfvx);
    
    // ========== 步骤 4: 积分反馈（消除累积误差）==========
    if(twoKi > 0.0f) {
      integralFBx += twoKi * halfex * (1.0f / SAMPLING_FREQ);  // 积分误差项
      integralFBy += twoKi * halfey * (1.0f / SAMPLING_FREQ);
      integralFBz += twoKi * halfez * (1.0f / SAMPLING_FREQ);
      gx += integralFBx;        // 应用积分反馈修正陀螺仪
      gy += integralFBy;
      gz += integralFBz;
    }
    else {
      integralFBx = 0.0f;       // 防止积分饱和
      integralFBy = 0.0f;
      integralFBz = 0.0f;
    }
    
    // ========== 步骤 5: 比例反馈 ==========
    gx += twoKp * halfex;  // 应用比例反馈
    gy += twoKp * halfey;
    gz += twoKp * halfez;
  }
  
  // ========== 步骤 6: 积分四元数变化率 ==========
  gx *= (0.5f * (1.0f / SAMPLING_FREQ));   // 预乘公共因子
  gy *= (0.5f * (1.0f / SAMPLING_FREQ));
  gz *= (0.5f * (1.0f / SAMPLING_FREQ));
  qa = q0;
  qb = q1;
  qc = q2;
  q0 += (-qb * gx - qc * gy - q3 * gz);  // 更新四元数 w 分量
  q1 += (qa * gx + qc * gz - q3 * gy);   // 更新四元数 x 分量
  q2 += (qa * gy - qb * gz + q3 * gx);   // 更新四元数 y 分量
  q3 += (qa * gz + qb * gy - qc * gx);   // 更新四元数 z 分量
  
  // ========== 步骤 7: 四元数归一化 ==========
  recipNorm = InvSqrt(q0 * q0 + q1 * q1 + q2 * q2 + q3 * q3);
  q0 *= recipNorm;
  q1 *= recipNorm;
  q2 *= recipNorm;
  q3 *= recipNorm;
  
  // ========== 步骤 8: 输出到全局 IMU 对象 ==========
  Mpu6050.orientation.w = q0;  // 设置四元数 w 分量
  Mpu6050.orientation.x = q1;  // 设置四元数 x 分量
  Mpu6050.orientation.y = q2;  // 设置四元数 y 分量
  Mpu6050.orientation.z = q3;  // 设置四元数 z 分量
}
