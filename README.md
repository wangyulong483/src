# Origincar Pro — Ackermann 自主驾驶赛车

> **ROS2 Humble · RDK X5 · 21届地瓜赛项**
> **架构**: Nav2 (开阔大厅) + 视觉控制 (窄环道) 混合导航
> **RMW**: CycloneDDS | **深度相机**: 目标 30fps

---

## 模块图

```
┌──────────────────────────────────────────────────────┐
│ 段1+2a (大厅): Nav2 全栈                              │
│   AMCL + Planner + RPP + Costmap + Keepout            │
│   P ──→ QR ──→ 通道入口                               │
├──────────────────────────────────────────────────────┤
│ 段2b (环道): 视觉 PID 居中 + LiDAR 锥桶绕行            │
│   摄像头(HSV黄色→PID) + 雷达(定位+锥桶) + IMU(里程计)   │
│   环道巡航 → 第4拐弯VLM → 出口判定                     │
├──────────────────────────────────────────────────────┤
│ 段3 (返航): Nav2 NavigateToPose                       │
│   环道出口 ──→ P 点                                    │
└──────────────────────────────────────────────────────┘
```

---

## 硬件平台

| 组件 | 型号 | 接口 | 环道作用 | 大厅作用 |
|------|------|------|----------|----------|
| 主控 | RDK X5 (A55×4, 10 TOPS) | — | — | — |
| MCU | STM32F407 | `/dev/ttyACM0`, 115200 | 驱动+MPU6050 | 同 |
| LiDAR | N10 (LSX10) | `/dev/ttyACM1`, 5Hz | 定位+锥桶检测 | 定位+costmap避障 |
| 深度相机 | Aurora930 (Orbbec) | USB 3.0, 目标 30fps | RGB: 车道线 (深度不用) | RGB: QR解码 |
| IMU | BMI088 + MPU6050 | IIO sysfs + STM32 | 撑里程计(yaw不漂) | 同 |
| 底盘 | Ackermann | wheelbase=0.143m, min_turn=0.30m, ±28° | — | — |

---

## 模块接口

### 模块图

```
┌──────────────┐  ┌──────────┐  ┌───────────┐
│ STM32 驱动    │  │ N10 LiDAR │  │ Aurora930 │  ← 硬件层
│ /odom /imu   │  │ /scan    │  │ /rgb /depth│
└──────┬───────┘  └────┬─────┘  └─────┬─────┘
       │               │              │
┌──────▼───────────────▼──────────────▼──────┐
│              感知 & 融合层                   │
│  Madgwick(×2)  QR解码  AMCL  EKF(dual-IMU) │
│  /imu/data/*   /sign   /amcl_pose  /odom   │
└──────────────────┬─────────────────────────┘
                   │
┌──────────────────▼─────────────────────────┐
│               导航层 (Nav2)                 │
│  Planner + RPP + Costmap + Keepout + Smoother│
│  /plan  /cmd_vel  /speed_limit             │
└──────────────────┬─────────────────────────┘
                   │
┌──────────────────▼─────────────────────────┐
│            编排层 (Stage 2)                  │
│  competition_master_stage2                 │
│  INIT → NAV_TO_QR → BACKING_UP →           │
│  NAV_TO_ENTRY → DONE                       │
└────────────────────────────────────────────┘
```

---

### M1: STM32 底盘驱动

| 项目 | 值 |
|------|-----|
| **包** | `origincar_base` |
| **节点** | `origincar_base_node` (C++) |
| **职责** | STM32 串口通信: 发布传感器数据, 订阅控制指令 |

**输入**:
| Topic | 类型 | 用途 |
|-------|------|------|
| `/cmd_vel` | Twist | 速度指令 (直驱模式) |
| `/ackermann_cmd` | AckermannDriveStamped | 阿克曼转向指令 |

**输出**:
| Topic | 类型 | 频率 | 用途 |
|-------|------|------|------|
| `/odom` | Odometry | 20Hz | 轮式里程计 (X×1.03, Y×1.125 补偿) |
| `/imu/data_raw` | Imu | 100Hz | MPU6050 原始数据 (Mahony Ki=0 初处理) |
| `/PowerVoltage` | Float32 | — | 电池电压 |

**参数**: `wheelbase=0.143`, 串口帧 `0x7B...0x7D`, XOR 校验

---

### M2: LiDAR 驱动

| 项目 | 值 |
|------|-----|
| **包** | `lslidar_driver` |
| **节点** | `lslidar_driver_node` (C++, LifecycleNode) |

**输出**:
| Topic | 类型 | 频率 | 用途 |
|-------|------|------|------|
| `/scan` | LaserScan | 5Hz | 2D 360° 扫描, frame=`laser_link` |

**参数**: `params/lsx10.yaml` (N10, serial `/dev/ttyACM1`, 230400 bps, 2000 pts)

---

### M3: Aurora930 深度相机

| 项目 | 值 |
|------|-----|
| **包** | `deptrum-ros-driver-aurora930` (外部, `/userdata/ros_ws/`) |
| **帧率** | 目标 30fps (当前 15fps) |

**输出**:
| Topic | 类型 | 频率 | 用途 |
|-------|------|------|------|
| `/aurora/rgb/image_raw` | Image (BGR8) | 30fps | 段1+2a: QR解码 → 段2b: HSV黄色分割→PID |
| `/aurora/depth/image_raw` | Image (16UC1, mm) | 30fps | 段1+2a: QR深度辅助 → 段2b: 不使用 |
| `/aurora/points2` | PointCloud2 | 30fps | 段1+2a: VoxelLayer → 段2b: 不使用 |

---

### M4: IMU 姿态 (Madgwick ×2)

| 项目 | 值 |
|------|-----|
| **包** | `origincar_bringup` |
| **节点** | `imu_madgwick_filter.py` ×2, `bmi088_iio_bridge.py` |

| 实例 | 输入 | 输出 | β | 频率 |
|------|------|------|---|------|
| MPU6050 | `/imu/data_raw` (100Hz, STM32) | `/imu/data/madgwick` | 0.033 | 100Hz |
| BMI088 | `/imu_data` (50Hz, sysfs IIO) | `/imu/data/bmi088_madgwick` | 0.003 | 50Hz |

**参数**: `config/imu_madgwick.yaml`, `config/imu_madgwick_bmi088.yaml`, `gyro_scale=0.00053 rad/s/LSB`

---

### M5: 定位融合 (EKF)

| 项目 | 值 |
|------|-----|
| **包** | `robot_localization` |
| **节点** | `ekf_filter_node` |

**输入**:
| 源 | Topic | 模式 | 融合量 |
|----|-------|------|--------|
| odom0 | `/odom` | differential | X, Vx, Vy, ωz |
| imu0 | `/imu/data/madgwick` (MPU6050) | relative | yaw + ωz |
| imu1 | `/imu/data/bmi088_madgwick` | differential | ωz only |

**输出**: `odom→base_footprint` TF, 15Hz, `two_d_mode=true`

**参数**: `config/ekf_dual_imu.yaml`, `sensor_timeout=0.2s`, `imu0_twist_rejection=1.542`

---

### M6: 定位 (AMCL)

| 项目 | 值 |
|------|-----|
| **包** | `nav2_amcl` |
| **输入** | `/scan` + `/map` (room.pgm) → 粒子滤波 |

**输出**:
| 接口 | 类型 | 用途 |
|------|------|------|
| `map→odom` TF | transform | 定位修正 |
| `/amcl_pose` | PoseWithCovarianceStamped | 机器人位姿 |

**参数**: `DifferentialMotionModel` (Humble 无 Ackermann 模型), 300-1500 粒子, `initial_pose=(-1.985,-0.014, yaw=0.262)`

---

### M7: QR 解码

| 项目 | 值 |
|------|-----|
| **包** | `qr_decoder` |
| **节点** | `qr_decoder_zbar` (C++/ZBar) → `qr_decision` (Python) |

**管线**:
```
Aurora930 RGB → ZBar(QR only, 多尺度) → /sign → 格式验证(1-4位数字) → 奇偶→方向
                                                                              │
                                                                    /qr_event ("1584,逆时针,x,y")
```

| Topic | 类型 | 方向 |
|-------|------|------|
| `/sign` | String | C++→Python (QR 原始文本) |
| `/sign_pose` | PoseStamped | C++ 输出 (odom 帧) |
| `/qr_event` | String | Python 输出 (格式: "数字,方向,x,y") |
| `/sign_switch_sign_data` | Int32 | Python 输出 (3=CW, 4=CCW) |

**参数**: `fx=421.3, fy=422.3, cx=320.3, cy=197.0`, 冷却 3.0s

---

### M8: 导航 (Nav2 — 大厅段)

| 项目 | 值 |
|------|-----|
| **启动** | `nav2_minimal.launch.py` (composition 模式) |
| **使用段** | 段1+2a (P→QR→入口) + 段3 (出口→P) |

| 组件 | 算法 | 频率 | 关键参数 |
|------|------|------|----------|
| **Planner** | SmacPlannerHybrid (REEDS_SHEPP) | ~1.3Hz | `min_turning_radius=0.30`, `smooth_path=true`, `cache_obstacle_heuristic=true` |
| **Controller** | RegulatedPurePursuit | 10Hz | `lookahead_dist=0.678`, `min_lookahead=0.60`, `desired_linear_vel=0.50` |
| **Velocity Smoother** | OPEN_LOOP | 20Hz | `max=[0.65,0,2.8]`, `min=[-0.3,0,-2.8]` |
| **Local Costmap** | obstacle+voxel+keepout+inflation | 5Hz | 3×3m rolling, `inflation=0.55`, `resolution=0.05` |
| **Global Costmap** | static+obstacle+voxel+keepout+inflation | 1Hz | map frame, `inflation=0.5955` |
| **Recovery** | BackUp(0.3m)+Wait(3s) | — | 无 Spin (Ackermann 约束) |

**输入**:
| Topic | 来源 | 用途 |
|-------|------|------|
| `/scan` | N10 LiDAR | obstacle_layer 障碍物检测 |
| `/aurora/points2` | Aurora930 | voxel_layer 3D 点云 → 2D 投影 |
| `/map` | room.pgm | static_layer 底图 |
| `/costmap_ctrl` | competition_master | keepout 控制 |
| `/speed_limit` | speed_profile_node | 动态速度限制 (可选) |

**输出**:
| Topic | 用途 |
|-------|------|
| `/cmd_vel` | 最终速度指令 (经 velocity_smoother) |
| `/plan` | 全局路径 |
| `/local_plan` | 局部路径 |
| `/global_costmap/costmap` | 全局代价地图 |
| `/local_costmap/costmap` | 局部代价地图 |

**参数文件**: `originbot_navigation/param/originbot_nav2_rpp.yaml`

---

### M9: 禁区 (Keepout)

| 项目 | 值 |
|------|-----|
| **Mask** | `keepout_mask.pgm` (163×141, 0.05m/pix, scale mode) |
| **发布** | `keepout_mask_server` → `/keepout_mask` |
| **控制** | `competition_master` → `/costmap_ctrl` (TRANSIENT_LOCAL) |

**cost 分布 (v3 梯度)**:
| 区域 | PGM pixel | Costmap cost | 效果 |
|------|-----------|-------------|------|
| 通道中心 | 252 | ~3 | FREE, 优先车道 |
| 通道河谷 | 213-252 | 3→55 | 引导居中 |
| 禁区悬崖 | 1-113 | 140→253 | 陡峭推回 |
| 禁区内部 | 0 | **254** | **LETHAL**, 绝不穿越 |

**动态控制**:
| 操作 | 触发 | Topic |
|------|------|-------|
| 启用 | 启动/段切换 | `/costmap_ctrl → /keepout_mask` |
| 禁用 | 锥桶绕行 | `/costmap_ctrl → /keepout_disabled` |

---

### M10: 编排 (Stage 2 状态机)

| 项目 | 值 |
|------|-----|
| **节点** | `competition_master_stage2.py` (Python) |
| **启动** | `ros2 launch origincar_bringup stage2_bringup.launch.py` |

**状态机**:
```
INIT → NAV_TO_QR → BACKING_UP → NAV_TO_ENTRY → DONE (段1+2a 完成)
                                              ↓
                                    channel_controller 接管 (段2b)
```

### M11: 环道视觉控制 (段2b)

| 项目 | 值 |
|------|-----|
| **节点** | `channel_controller.py` (Python, 待实现) |
| **传感器** | RGB(HSV黄色分割→PID), LiDAR(定位+锥桶), IMU(里程计) |

**控制模式**:
| 场景 | 方式 | 输出 |
|------|------|------|
| 直道 | PID 居中 (横向误差 → wz) | vx=0.45 |
| 弯道 | PID 居中 (前视自然过弯) | vx=0.20, IMU ωz > 阈值判定 |
| 锥桶 | 固定轨迹 (左转→直行→右转) | vx=0.15, wz=±1.2 |
| 出口 | 视觉(黄色<20%) + AMCL(出口区域) | 切段3 |

**锥桶绕行**:
```
检测: LiDAR 前方90°聚类 (0.05-0.20m宽, ≥3帧/1.5s)
绕行: BYPASS_LEFT(3s) → BYPASS_FWD(2s) → BYPASS_RIGHT(3s)
超时: 8s → 停车
```

**VLM**: 第4拐弯处触发 /sign4return=100 (异步, 不等结果)

**输入**:
| Topic | 用途 |
|-------|------|
| `/sign` | QR 检测触发 |
| `/qr_event` | 获取巡航方向 |
| `/odom` | 机器人位姿 |

**输出**:
| Topic | 类型 | 用途 |
|-------|------|------|
| `/cmd_vel` | Twist | 后退时直驱控制 |
| `/costmap_ctrl` | CostmapFilterInfo | keepout 重置/控制 |

**动作**: `navigate_to_pose` (Nav2 action, P→QR, QR→入口)

---

## 启动

```bash
# Stage 2 — P→QR→通道入口
ros2 launch origincar_bringup stage2_bringup.launch.py
```

**时序**:
| t | 启动 |
|---|------|
| 0s | base_minimal (STM32 + LiDAR + IMU + EKF) + camera_all (Aurora930 + QR) |
| 1s | nav2_minimal (keepout + Nav2) |
| 4s | competition_master_stage2 |
| 8s | RViz2 |

---

## 关键 Topic

| Topic | 类型 | 发布者 → 订阅者 |
|-------|------|----------------|
| `/cmd_vel` | Twist | velocity_smoother → STM32 |
| `/odom` | Odometry | STM32 → EKF, AMCL |
| `/scan` | LaserScan | N10 → AMCL, costmap |
| `/imu/data/madgwick` | Imu | Madgwick(MPU6050) → EKF |
| `/imu/data/bmi088_madgwick` | Imu | Madgwick(BMI088) → EKF |
| `/aurora/rgb/image_raw` | Image(BGR8) | Aurora930 → QR |
| `/sign` | String | QR(C++) → QR(Python), stage2 |
| `/qr_event` | String | QR(Python) → stage2 |
| `/plan` | Path | planner → controller, speed_profile |
| `/costmap_ctrl` | CostmapFilterInfo | stage2 → keepout_filter |

---

## 部署

```bash
# 1. 打包
tar czf deploy.tar.gz -C src origincar/ originbot_navigation/ qr_decoder/ Lslidar_ROS2_driver-N10_V1.0/

# 2. 上传 + 构建
ssh root@192.168.31.59
cd /userdata/dev_ws && tar xzf deploy.tar.gz -C src/
find src/ -name '*.py' -exec sed -i 's/\r$//' {} \;
bash -c 'source /opt/ros/humble/setup.bash && colcon build --packages-select origincar_bringup origincar_base originbot_navigation qr_decoder lslidar_driver'
```

---

## 包清单

| 包 | 语言 | 职责 |
|----|------|------|
| `origincar_base` | C++ + Python | STM32 驱动 + EKF/Madgwick 配置 |
| `origincar_bringup` | Python + C++ | 启动编排 + Stage2 状态机 + IMU 桥 |
| `origincar_description` | URDF | 机器人模型 (base/laser/gyro link) |
| `origincar_msg` | ROS2 IDL | Data.msg (x/y/z) |
| `originbot_navigation` | YAML/XML/Python | Nav2 参数 + BT + 地图 + 工具 |
| `qr_decoder` | C++ + Python | ZBar QR 解码 + 方向决策 |
| `lslidar_driver` | C++ | N10 LiDAR 驱动 |
| `ackermann_msgs` (3rd) | ROS2 IDL | Ackermann 消息定义 |
| `serial` (3rd) | C++ | 跨平台串口库 |

> **RMW**: CycloneDDS | **目标**: RDK X5 @ 192.168.31.59 | **工作空间**: `/userdata/dev_ws/`
