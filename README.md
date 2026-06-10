# Origincar Pro — 自主驾驶 Ackermann 小车

> ROS2 Humble + RDK X5 | 全国大学生智能汽车竞赛
> 最后更新: 2026-06-10

---

## 1. 硬件平台

| 组件 | 型号 | 接口 | 说明 |
|------|------|------|------|
| 主控 | RDK X5 (Cortex-A55 x4, 10TOPS BPU) | — | Ubuntu 22.04, 5.2GB RAM |
| MCU | STM32F407 | /dev/ttyACM0, 115200bps | 电机/舵机/MPU6050/编码器/电压 |
| LiDAR | Leishen N10 | /dev/ttyACM1, 230400bps | 2D 360°, 5Hz |
| 深度相机 | Aurora930 (Deptrum) | USB 3.0 | RGB 640x400@15fps + Depth + PointCloud2 |
| IMU (底盘) | MPU6050 | STM32 I2C 采集 | 3轴陀螺+加速度计, Mahony Ki=0 |
| IMU (板载) | BMI088 | RDK X5 I2C-1 (IIO) | 陀螺噪声密度 10x 优于 MPU6050 |
| 底盘 | 阿克曼 | 276x189x150mm | wheelbase=0.143m, min_turning_radius≈0.30m |
| 电池 | 12V 锂电池 | — | /PowerVoltage 监测 |

### 软件环境

- **OS**: Ubuntu 22.04 (ARM aarch64), Swap ≥4GB
- **ROS2**: Humble Hawksbill
- **编译**: `colcon build --parallel-workers 2` (并行>2 OOM)
- **Source**: `/opt/tros/humble/setup.bash` (TROS, hbm_img_msgs) + `/opt/ros/humble/setup.bash`
- **工作空间**: `/userdata/dev_ws`

---

## 2. 系统架构

### 2.1 分层架构

```
┌──────────────────────────────────────────────────────────────────┐
│  ORCHESTRATION │ task_manager │ mission_controller │ lifecycle    │
│                │ competition_master_stage1/2/3 (legacy)          │
├────────────────┼─────────────────────────────────────────────────┤
│  CONTROL       │ cmd_vel_mux │ velocity_pid │ pose_pid_corrector │
│                │         cmd_vel_to_ackermann_drive              │
├────────────────┼─────────────────────────────────────────────────┤
│  NAVIGATION    │ AMCL │ SmacPlannerHybrid │ RPP │ costmaps ×2    │
│ (Nav2)         │ BT Navigator │ ConstrainedSmoother │ VelSm      │
├────────────────┼─────────────────────────────────────────────────┤
│  PERCEPTION    │ imu_madgwick │ qr_decoder (ZBar) │ qr_decision  │
│                │ cartographer │ vision_ai (cloud VLM / BPU LLM) │
├────────────────┼─────────────────────────────────────────────────┤
│  SENSOR FUSION │ EKF (robot_localization) │ odom2tf              │
├────────────────┼─────────────────────────────────────────────────┤
│  DRIVER        │ origincar_base (STM32) │ lslidar (N10)         │
│                │ aurora930 (Aurora930) │ bmi088_iio_bridge      │
├────────────────┼─────────────────────────────────────────────────┤
│  HARDWARE      │ RDK X5 │ STM32 │ N10 │ Aurora930 │ MPU6050     │
└────────────────┴─────────────────────────────────────────────────┘
```

### 2.2 节点总览

#### 自定义节点 (21个)

| 节点 | 包 | 语言 | 职责 |
|------|-----|------|------|
| `origincar_base` | origincar_base | C++ | STM32 串口桥接: 发布 /odom, /imu/data_raw, /robotvel, /PowerVoltage; 订阅 /ackermann_cmd |
| `lslidar_driver_node` | lslidar_driver | C++ | N10 LiDAR 驱动 → /scan (5Hz, frame=laser_link) |
| `qr_decoder_zbar` | qr_decoder | C++ | ZBar QR 解码 + 深度滤波 → /sign, /sign_pose |
| `odom2tf` | origincar_bringup | C++ | 从 /odom 发布 odom→base_footprint TF (use_ekf=false 时启用) |
| `cmd_vel_to_ackermann_drive` | origincar_base | Python | Twist → AckermannDriveStamped (wheelbase=0.143, steering_sign=-1) |
| `cmd_vel_mux` | origincar_bringup | Python | 3输入优先级多路复用器 (nav=10, pid=20, stop=255), 30Hz |
| `velocity_pid` | origincar_bringup | Python | 增量式 PID 速度闭环 (30Hz), 编码器反馈, 方向切换积分重置 |
| `pose_pid_corrector` | origincar_bringup | Python | 末端精确停车 PID (0.5m 内激活), AMCL 协方差门控 |
| `imu_madgwick_filter` | origincar_bringup | Python | Madgwick 6-DOF AHRS (beta=0.033, 100Hz) → /imu/data/madgwick |
| `bmi088_iio_bridge` | origincar_bringup | Python | BMI088 Linux IIO → /imu_data (100Hz, 无姿态) |
| `task_manager` | origincar_bringup | Python | 5态竞赛状态机, 10Hz 心跳 → /mission_cmd |
| `mission_controller` | origincar_bringup | Python | 执行 /mission_cmd → Nav2 Action / /stop_cmd_vel / /sign4return |
| `competition_lifecycle_manager` | origincar_bringup | Python | Nav2 运行时参数切换 + 紧急全栈重置 (9节点) |
| `wait_for_odom` | origincar_bringup | Python | 启动屏障: 等待 /odom 就绪 (最长15s) |
| `calibrate_gui` | origincar_bringup | Python | 手动路点/禁区标定 GUI (PC端, matplotlib) |
| `field_calibrator` | origincar_bringup | Python | 自动 P点标定 + 锥桶测量 |
| `competition_master_stage1` | origincar_bringup | Python | [Legacy] 阶段1独立控制器 |
| `competition_master_stage2` | origincar_bringup | Python | [Legacy] 阶段2独立控制器 |
| `competition_master_stage3` | origincar_bringup | Python | [Legacy] 阶段3独立控制器 (stage3_bringup 仍在使用) |
| `qr_decision` | origincar_qr | Python | QR 方向决策 (奇→CW, 偶→CCW, 3s 冷却) |
| `vision_ai_node` | racing_vision_ai | Python | VLM 图生文: /sign4return 触发 → 火山引擎 ARK API |

#### 外部/基础设施节点 (15个)

| 节点 | 包 | 职责 |
|------|-----|------|
| `ekf_filter_node` | robot_localization | 多传感器融合: /odom + /imu/data/madgwick (imu0) + /imu_data (imu1) → /odometry/filtered + odom→base_footprint TF |
| `amcl` | nav2_amcl | 粒子滤波定位: /scan + /map → map→odom TF |
| `map_server` | nav2_map_server | 静态地图服务 |
| `planner_server` | nav2 | SmacPlannerHybrid 全局规划器 (REEDS_SHEPP) |
| `controller_server` | nav2 | RegulatedPurePursuit 局部控制器 |
| `bt_navigator` | nav2 | 行为树导航执行器 |
| `recoveries_server` | nav2 | 恢复行为 (BackUp + Wait, 无Spin) |
| `global_costmap` / `local_costmap` | nav2 | 全局/局部代价地图, 含 keepout_filter |
| `velocity_smoother` | nav2 | 速度平滑 (OPEN_LOOP, 20Hz) |
| `smoother_server` | nav2 | 路径平滑 (ConstrainedSmoother, BT 中已移除) |
| `waypoint_follower` | nav2 | 路点跟随任务 |
| `keepout_mask_server` | nav2_map_server | 禁区代价地图 |
| `keepout_filter_info_server` | nav2_map_server | 禁区过滤器元数据 |
| `lifecycle_manager` | nav2_lifecycle_manager | Nav2 标准生命周期管理 |
| `lifecycle_manager_keepout` | nav2_lifecycle_manager | 禁区节点生命周期管理 |

---

## 3. 数据流

### 3.1 cmd_vel 控制流水线 (5级, 不可绕过)

```
Nav2 RPP → velocity_smoother (20Hz OPEN_LOOP) → /cmd_vel
  → [remap] → /nav_cmd_vel (p=10) ──────────────────────┐
pose_pid_corrector → /pid_cmd_vel (p=20) ────────────────┤
mission_controller → /stop_cmd_vel (p=255, 零值 Twist) ──┤
                                                          v
                                                   cmd_vel_mux (30Hz)
                                                   超时自动回退到低优先级
                                                          │
                                                          v /cmd_vel_muxed
                                                   velocity_pid (30Hz)
                                                   增量式 PID + 方向切换积分重置
                                                   feedback: /robotvel (编码器)
                                                   反馈超时→开环直通
                                                          │
                                                          v /cmd_vel_corrected
                                                   cmd_vel_to_ackermann_drive
                                                   steering = atan(0.143 / (v/w))
                                                   steering_sign = -1.0
                                                          │
                                                          v /ackermann_cmd
                                                   origincar_base
                                                   11B serial → STM32 → PWM
```

**优先级**: stop(255) > pid(20) > nav(10)。mission_controller 发布零值 Twist 到 /stop_cmd_vel 实现紧急停止。

**velocity_pid 参数**: Kp_vx=0.8, Ki_vx=0.6, Kd_vx=0.05, max_vx=0.85。Kp_wz=1.0, Ki_wz=0.4, Kd_wz=0.02, max_wz=2.8。积分限幅 = 0.8×max。

### 3.2 IMU 姿态融合 (双IMU)

```
MPU6050 → STM32 Mahony (Ki=0, 零偏未补偿) → /imu/data_raw
  → imu_madgwick_filter (beta=0.033, 100Hz) → /imu/data/madgwick
      │                                        (imu0: yaw姿态 + Z角速度)
      │
BMI088 → Linux IIO → bmi088_iio_bridge (100Hz) → /imu_data
      │                                            (imu1: Z角速度, 无姿态)
      │
      ├──→ EKF (15Hz, 2D, publish_tf=true)
      │      yaw noise: 单IMU=0.005, 双IMU=0.003
      │      sensor_timeout: 单IMU=2.0s, 双IMU=0.1s
      │    → /odometry/filtered + TF: odom→base_footprint
```

**注意**: EKF 频率从 20Hz 降至 15Hz（Cortex-A55 单步执行 117-134ms, 超出 50ms 预算）。

### 3.3 传感器→导航

```
/scan (5Hz) + /aurora/points2 (15fps)
  → costmaps (obstacle + inflation + keepout)
AMCL ← /scan + /map + odom→base_footprint TF
  → TF: map→odom
    → SmacPlannerHybrid (REEDS_SHEPP, 2x downsample)
      → ConstrainedSmoother (w_curve=20.0)
        → RPP (cost_regulated, lookahead=0.65)
          → velocity_smoother → cmd_vel pipeline → STM32
```

### 3.4 QR 导航流

```
Aurora930 /rgb + /depth
  → qr_decoder_zbar (ZBar + 深度滤波 150-2000mm)
    → /sign (String) + /sign_pose (PoseStamped)
      → qr_decision (奇偶→方向, 3s 冷却)
        → /qr_event ("1,CW,1.52,-0.03")
          → task_manager → /mission_cmd → mission_controller → Nav2 Action
```

### 3.5 VLM 图生文流

```
mission_controller → /sign4return=100
  → vision_ai_node: 抓取 RGB 帧 → JPEG(Base64) → 火山引擎 ARK API
    → /vlm_result (String) → competition_master_stage3 异步接收
```

### 3.6 完整话题拓扑

| 发布者 | 话题 | 类型 | 订阅者 |
|--------|------|------|--------|
| origincar_base | /odom | Odometry | EKF, task_manager, qr_decoder, pose_pid_corrector, wait_for_odom, qr_decision |
| origincar_base | /imu/data_raw | Imu | imu_madgwick_filter |
| origincar_base | /robotvel | Data | velocity_pid |
| origincar_base | /PowerVoltage | Float32 | (monitoring) |
| imu_madgwick_filter | /imu/data/madgwick | Imu | EKF (imu0) |
| bmi088_iio_bridge | /imu_data | Imu | EKF (imu1, 双IMU模式) |
| EKF | /odometry/filtered | Odometry | cartographer |
| EKF | TF: odom→base_footprint | — | 全局 |
| lslidar_driver | /scan | LaserScan | AMCL, costmaps×2, cartographer |
| aurora930 | /aurora/rgb/image_raw | Image | qr_decoder_zbar |
| aurora930 | /aurora/depth/image_raw | Image | qr_decoder_zbar |
| aurora930 | /aurora/points2 | PointCloud2 | costmaps×2 |
| AMCL | TF: map→odom | — | 全局导航栈 |
| AMCL | /amcl_pose | PoseWithCovariance | task_manager, pose_pid_corrector |
| qr_decoder_zbar | /sign | String | qr_decision, task_manager, competition_master_* |
| qr_decision | /qr_event | String | task_manager, competition_master_stage2/3 |
| task_manager | /mission_cmd | String | mission_controller |
| task_manager | /heartbeat/task_manager | String | (monitoring) |
| mission_controller | /mission_status | String | task_manager |
| mission_controller | /stop_cmd_vel | Twist | cmd_vel_mux |
| mission_controller | /sign4return | Int32 | vision_ai_node |
| velocity_smoother | /cmd_vel → /nav_cmd_vel | Twist | cmd_vel_mux |
| pose_pid_corrector | /pid_cmd_vel | Twist | cmd_vel_mux |
| cmd_vel_mux | /cmd_vel_muxed | Twist | velocity_pid |
| cmd_vel_mux | /cmd_vel_mux_state | String | (monitoring) |
| velocity_pid | /cmd_vel_corrected | Twist | cmd_vel_to_ackermann_drive |
| velocity_pid | /velocity_pid_active | Bool | (monitoring) |
| cmd_vel_to_ackermann | /ackermann_cmd | AckermannDrive | origincar_base |
| competition_lifecycle_manager | /competition_mode_active | String | (monitoring) |

### 3.7 TF 树 (REP-105)

```
map
  │  AMCL (导航) 或 Cartographer (建图)
  v
odom
  │  EKF (publish_tf=true, 默认) 或 odom2tf (use_ekf=false)
  v
base_footprint
  ├── base_link (static, z=+0.07m, 来自 URDF)
  │     ├── laser_link (URDF static, z=+0.075m)
  │     └── depth_camera_link (static, x=+0.14m, z=+0.05m)
  │           └── rgb_camera_link (aurora930 外参)
  └── gyro_link (URDF static, 与 base_footprint 同原点)
```

**关键约束**: odom→base_footprint 必须恰好一个发布者。use_ekf=true 时 EKF 发布 TF, odom2tf 禁用。

| 模式 | odom→base_footprint | use_ekf | pub_odom_tf |
|------|---------------------|---------|-------------|
| 比赛导航 (默认) | EKF | true | false |
| 纯遥控/无EKF | odom2tf | false | true |
| Cartographer 建图 | EKF | true | false |

---

## 4. 功能包详解

### 4.1 origincar_msg — 自定义消息

纯 IDL 定义包, 无节点。

- `Data.msg` — float32 x, y, z (robotpose 和 robotvel 复用)
- `Sign.msg` — int32 sign_data

### 4.2 origincar_base — 底盘核心驱动

**节点**: `origincar_base` (C++)

STM32 串口协议: 24B 接收帧 (传感器数据), 11B 发送帧 (速度指令), 帧头 `0x7B`, 帧尾 `0x7D`, 异或校验。

| 输出话题 | 帧率 | 用途 |
|----------|------|------|
| /odom (Odometry) | ~30Hz | child_frame=base_footprint, 编码器推算 + 1.03/1.125 补偿系数 |
| /imu/data_raw (Imu) | ~30Hz | Mahony Ki=0, 零偏未补偿, frame=gyro_link |
| /robotvel (Data) | ~30Hz | 编码器实测速度 (x=vx, z=wz) |
| /robotpose (Data) | ~30Hz | 编码器推算位姿 |
| /PowerVoltage (Float32) | ~1Hz | 电池电压 |

**注意**: 构造函数中硬编码 `/dev/ttyACM0` 覆盖 ROS 参数 `usart_port_name`。

**节点**: `cmd_vel_to_ackermann_drive` (Python)

`steering_angle = -1.0 × atan(0.143 / (v/w)) + 0.0` → /ackermann_cmd。

发送帧中 steering 编码为 `steering_angle × 1000 / 2`（STM32 端 ×2 恢复）。

### 4.3 origincar_bringup — 控制与管理层

**cmd_vel_mux** — 3输入优先级多路复用器 (30Hz)
- /nav_cmd_vel (p=10, timeout=0.5s) — Nav2 经 remap 注入
- /pid_cmd_vel (p=20, timeout=0.3s) — pose_pid_corrector
- /stop_cmd_vel (p=255, timeout=0.5s) — 紧急停止
- 输出: /cmd_vel_muxed + /cmd_vel_mux_state

**velocity_pid** — 增量式 PID 速度闭环 (30Hz)
- Kp_vx=0.8, Ki_vx=0.6, Kd_vx=0.05, max_vx=0.85
- Kp_wz=1.0, Ki_wz=0.4, Kd_wz=0.02, max_wz=2.8
- 积分限幅 = max_out × 0.8 (抗饱和)
- 方向切换检测: sign(desired_prev) ≠ sign(desired_curr) → 积分重置 (最小间隔 250ms)
- 反馈超时 0.5s → 开环直通
- cmd_vel 超时 0.3s → 停止

**task_manager** — 5态竞赛编排 (10Hz)
```
WAIT_START → TASK1_GOTO_QR → TASK2_GOTO_ENTRY → TASK2_CRUISE → TASK3_RETURN → DONE
```
- 驻留确认: 2.0s 内连续满足位置容差 0.15m + 角度容差 0.30rad
- 超时: T1=90s, T2=90s, T3=60s, 总=180s → 超时自动推进 +50s 罚时
- AMCL 协方差门控: max_pos_cov=0.25, max_yaw_cov=0.09

**mission_controller** — 指令执行器
- `goto:x,y,yaw` → Nav2 NavigateToPose Action
- `through:cw` / `through:ccw` → Nav2 NavigateThroughPoses Action
- `stop` → /stop_cmd_vel
- `trigger_vlm` → /sign4return=100
- 反馈 /mission_status (含 server_not_ready 重试机制)

**pose_pid_corrector** — 末端精确停车
- 激活范围: 0.5m (目标距离)
- 混合范围: 0.25m (RPP+PID 线性混合)
- Dead Zone: x=0.02m, yaw=0.03rad
- AMCL 协方差门控: max_pos_cov=0.25, max_yaw_cov=0.09
- PID X: Kp=1.2, Ki=0.05, Kd=0.1, max_vx=0.40
- PID Yaw: Kp=1.0, Ki=0.02, Kd=0.05, max_vyaw=0.80
- 阿克曼合成: wheelbase=0.143m

**competition_lifecycle_manager** — 模式切换 + 紧急重置
- task1/task2/task3 模式: 动态调整 costmap (inflation_radius, obstacle_range) + 速度 (desired_linear_vel)
- emergency 模式: 9节点全生命周期重置 (deactivate→cleanup→configure→activate, ~5.4s)
- 被管节点: controller_server, planner_server, bt_navigator, recoveries_server, global_costmap, local_costmap, velocity_smoother, smoother_server, waypoint_follower

**imu_madgwick_filter** — Madgwick 6-DOF AHRS
- beta=0.033, gyro_noise=0.001, accel_noise=0.05
- 丢弃 STM32 Mahony 四元数, 独立重算
- 100Hz → /imu/data/madgwick

**bmi088_iio_bridge** — RDK X5 BMI088 IIO 桥接
- 多策略设备检测 (按名称/part文件/属性探测)
- 100Hz → /imu_data (仅角速度+加速度, 无姿态)
- 设备不存在时优雅降级 (发布零值 + 诊断日志)

**odom2tf** — odom→base_footprint TF 发布器 (use_ekf=false 时启用)

**wait_for_odom** — 启动屏障, 阻塞至 /odom 就绪 (最长15s)

**calibrate_gui** — 手动路点/禁区标定 (PC端 matplotlib GUI)
- 左键添加路点, 右键拖绘禁区, "Go" 发 Nav2 goal
- 导出 trajectory_*.csv, waypoints_*.csv, keepout_*.pgm/yaml

**field_calibrator** (calibrate_p_point.py) — 自动场地标定
- Phase 1 (120s): Cartographer 纯定位求 P点 (σ<5mm)
- Phase 2 (15s): LiDAR+深度相机聚类测锥桶尺寸
- 输出 p_point.yaml + cone_params.yaml

### 4.4 origincar_description — URDF 模型

连杆: base_footprint → base_link (z=+0.07m) → laser_link (z=+0.075m) / gyro_link。全部 fixed joint。robot_state_publisher 发布静态 TF。

### 4.5 Aurora930 深度相机

**节点**: `aurora930_node` (C++, 命名空间 /aurora), SDK v1.1.22, Firmware 1.7.2

| 话题 | 类型 | 规格 |
|------|------|------|
| /aurora/rgb/image_raw | Image (bgr8) | 640x400, 15fps |
| /aurora/rgb/camera_info | CameraInfo | fx=416.49, fy=417.383, cx=316.832, cy=188.753 |
| /aurora/depth/image_raw | Image (mono16) | 640x400, mm 单位 |
| /aurora/points2 | PointCloud2 | 米制, RGBD 对齐 |

**已知问题**: `heartbeat failed!!!` 每2s一条日志——SDK v1.1.22 与 Firmware 1.7.2 心跳协议不兼容, 数据流正常。比赛中设 `heart_enable:=false, ir_enable:=false`。

### 4.6 lslidar_driver — N10 LiDAR

**节点**: `lslidar_driver_node` (C++, LifecycleNode), /dev/ttyACM1 @230400bps, 发布 /scan (LaserScan, 5Hz, frame=laser_link)。

### 4.7 originbot_navigation — 导航配置

纯配置包 (launch + YAML + XML), 无自定义节点。

**AMCL**: 300-1500粒子, likelihood_field, alpha=0.45 (补偿阿克曼-差分模型差异), recovery_alpha_fast=0.1。初始位姿: (-1.985, -0.014, 0.262)。

**SmacPlannerHybrid**: REEDS_SHEPP, min_turning_radius=0.30m, max_iterations=2000, max_planning_time=3.0s。reverse_penalty=15.0 (抑制路点倒车), change_penalty=2.0。2x降采样。

**RPP**: desired_linear_vel=0.45m/s, max=0.55m/s, max_angular_vel=1.50rad/s。lookahead_dist=0.65m (≥2×0.30m min_turning_radius)。cost_scaling_dist=0.12, gain=2.0。allow_reversing=true。goal_tolerance: xy=0.20, yaw=0.40。

**代价地图 ×2**: robot_radius≈0.12m, inflation_radius=0.12m, cost_scaling_factor=5.0。传感器: /scan + /aurora/points2 (height 0.05-0.35m, persistence=0.5s)。local: rolling_window 3m×3m (odom系)。global: 全地图 (map系), track_unknown_space=true。两者均含 keepout_filter。

**禁区**: 独立 lifecycle_manager_keepout 管理, 不与 Nav2 主 lifecycle_manager 共用。

**行为树 (RPP)**: 自定义 BT, 无 Spin (阿克曼), 无 SmoothPath (Humble NaN bug)。恢复: ClearCostmap→BackUp(0.3m)→Wait(3s)→BackUp(1.5m)。

**Velocity Smoother**: OPEN_LOOP, 20Hz, max_vel=[0.85,0,2.8]。

**Cartographer**: tracking_frame=base_footprint, published_frame=odom, min_range=0.3m, max_range=8.0m。

### 4.8 其他包

**origincar_qr**: `qr_decision` (Python) — /sign 解析→奇偶性→方向 (odd=CW, even=CCW), 3s冷却, 输出 /qr_event。

**qr_decoder**: `qr_decoder_zbar` (C++) — ZBar+深度滤波 (150-2000mm)+3D投影 (IR内参: fx=421.307, fy=422.254, cx=320.27, cy=197.01)。

**racing_vision_ai**: `vision_ai_node` (Python) — /sign4return 触发→抓取RGB→JPEG(Base64)→火山引擎 ARK API→日志输出。另含 BPU 本地 LLM daemon (InternVL2, ViT on BPU + llama.cpp on CPU, ~13.5s/query)。

**utils**: 已停用——`Nv122BGR` NV12→BGR8/JPEG 硬件转换, 备选。

---

## 5. Launch 文件

### 5.1 入口总览

| Launch 文件 | 用途 | 包含节点数 |
|------------|------|-----------|
| `nav_bringup.launch.py` | 标准比赛导航 (task_manager + Nav2) | ~28 |
| `stage1_bringup.launch.py` | 阶段1测试 (P→QR) | ~25 |
| `stage2_bringup.launch.py` | 阶段2测试 (QR→通道入口) | ~25 |
| `stage3_bringup.launch.py` | 阶段3测试 (完整比赛) | ~26 |
| `slam_bringup.launch.py` | Cartographer 建图 | ~12 |
| `camera_all.launch.py` | QR 检测独立调试 | ~5 |
| `base_serial.launch.py` | 纯遥控底盘 | ~2 |

### 5.2 nav_bringup.launch.py — 错峰启动时间线

| 时间 | 动作 |
|------|------|
| t=0s | bringup.launch.py: 底盘+LiDAR+TF+EKF+mux+velocity_pid+imu_madgwick+mission_controller |
| t=2s | wait_for_odom (最长15s 屏障) + Nav2 启动 (并行) |
| t=3s | 禁区 + Aurora930 + qr_decoder + qr_decision |
| t=10s | RViz2 |
| t=12s | task_manager + competition_lifecycle_manager + pose_pid_corrector |

### 5.3 Launch 参数

**nav_bringup.launch.py**:

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `use_sim_time` | false | 仿真时钟 |
| `map` | maps/room.yaml | 地图路径 |
| `planner_type` | rpp | rpp 或 dwa |
| `use_depth_camera` | true | 启用 Aurora930 |
| `depth_cam_x/y/z` | 0.14/0.0/0.05 | 相机偏移 (m) |

**bringup.launch.py / base_minimal.launch.py**:

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `use_ekf` | true | EKF 传感器融合 |
| `pub_odom_tf` | false | odom2tf 发布 TF |
| `use_bmi088` | true | 双IMU EKF |

### 5.4 Launch 依赖链

```
nav_bringup.launch.py
  ├── origincar_bringup/launch/bringup.launch.py
  │     ├── origincar_base/launch/base_serial.launch.py (akmcar:=true)
  │     ├── origincar_bringup/launch/urdf2tf.launch.py
  │     ├── origincar_base/launch/ekf.launch.py
  │     └── (mission_controller, cmd_vel_mux, velocity_pid, imu_madgwick, bmi088)
  ├── keepout + camera + qr (条件)
  └── nav2_bringup/bringup_launch.py (RPP 分支, use_composition=False)

stage1/2/3_bringup.launch.py
  ├── origincar_bringup/launch/base_minimal.launch.py (无 mission_controller)
  ├── origincar_bringup/launch/camera_all.launch.py
  ├── origincar_bringup/launch/nav2_minimal.launch.py (use_composition=True)
  └── competition_master_stageN.py (内部 8s 延迟)
```

---

## 6. 竞赛三阶段

### 阶段1: P点→QR发布点
- NavigateToPose → QR 点 (0.41, -3.17)
- 途中扫到 QR → 停止 + 打印数据
- 超时: 120s

### 阶段2: QR发布点→通道入口
- NavigateToPose → QR 点 → 扫到码
- 杀 ZBar 进程 → 等待 /qr_event (2s 超时)
- 倒车退避 (6s, vx=-0.15, wz=+2.80): 避开 keepout 致死区
- NavigateToPose → 通道入口 (0.38, -1.10)

### 阶段3: 完整赛道
- QR → 倒车退避 → NavigateThroughPoses 巡航
  - CW 路径 (奇QR): entry→(0.87,0.83)→(3.21,-1.82)
  - CCW 路径 (偶QR): entry→(1.85,-2.14)→(2.01,1.09)
- 触发 VLM (/sign4return=100) → 异步返回结果
- NavigateToPose → P 点 (-1.985, -0.014, yaw=0.262)
- 全局超时: 180s

### competition_lifecycle_manager 模式参数

| 参数 | task1 | task2 | task3 |
|------|-------|-------|-------|
| inflation_radius | 0.18 | 0.12 | 0.18 |
| cost_scaling_dist | 0.18 | 0.12 | 0.18 |
| obstacle_range | 5.0 | 1.5 | 5.0 |
| desired_linear_vel | 0.70 | 0.40 | 0.70 |
| max_linear_vel | 0.80 | 0.50 | 0.80 |

---

## 7. 配置文件参考

| 文件 | 包 | 关键内容 |
|------|-----|---------|
| originbot_nav2_rpp.yaml | originbot_navigation | Nav2 全栈: AMCL, SmacPlannerHybrid(REEDS_SHEPP), RPP, costmaps×2, smoother, velocity_smoother |
| originbot_nav2.yaml | originbot_navigation | DWA 备选: NavfnPlanner + DWB |
| ekf.yaml | origincar_base | EKF 单IMU: odom+imu0, 15Hz, yaw noise=0.005 |
| ekf_dual_imu.yaml | origincar_base | EKF 双IMU: odom+imu0+imu1, 15Hz, yaw noise=0.003 |
| imu_madgwick.yaml | origincar_base | Madgwick: beta=0.033, 100Hz |
| control_params.yaml | origincar_base | PID + mux: kp/ki/kd, priorities, timeouts |
| lsx10.yaml | lslidar_driver | N10: /dev/ttyACM1, 5Hz, 230400bps |
| vision_ai_config.yaml | racing_vision_ai | 火山引擎 ARK API: endpoint, api_key, prompt |
| room.yaml | originbot_navigation | 地图: 163×141, 0.05m/px |
| keepout_mask.yaml | originbot_navigation | 禁区掩码: 163×141, 0.05m/px |

---

## 8. STM32 串口协议

### RX 帧 (STM32→ROS2, 24B)

| 字节 | 字段 | 类型 | 说明 |
|------|------|------|------|
| 0 | Frame_Header | uint8 | 0x7B |
| 1 | Flag_Stop | uint8 | 停止标志 |
| 2-3 | Vx | int16/1000 | X 线速度 (m/s) |
| 4-5 | Vy | int16/1000 | Y 线速度 (m/s) |
| 6-7 | Vz | int16/1000 | Z 角速度 (rad/s) |
| 8-13 | accel_x/y/z | int16×3 | MPU6050 原始加速度 (ADC/1671.84→m/s²) |
| 14-19 | gyro_x/y/z | int16×3 | MPU6050 原始角速度 (ADC×0.00026644→rad/s) |
| 20-21 | voltage | int16/1000 | 电池电压 (V) |
| 22 | checksum | uint8 | XOR of bytes 0-21 |
| 23 | Frame_Tail | uint8 | 0x7D |

### TX 帧 (ROS2→STM32, 11B)

| 字节 | 字段 | 类型 | 说明 |
|------|------|------|------|
| 0 | Frame_Header | uint8 | 0x7B |
| 1-2 | Reserved | uint8×2 | 始终为 0 |
| 3-4 | speed | int16×1000 | 期望线速度 |
| 5-6 | Y_speed | int16 | (Ackermann 模式下未使用) |
| 7-8 | steering | int16 | Ackermann: angle×1000/2. Diff: ω×1000 |
| 9 | checksum | uint8 | XOR of bytes 0-8 |
| 10 | Frame_Tail | uint8 | 0x7D |

**注意**: Steering 编码为 `angle × 1000 / 2`, STM32 端内部 ×2 恢复。

---

## 9. 关键约束与调参备注

### cmd_vel 流水线
5级不可绕过。调试时逐级检查话题: /cmd_vel→/nav_cmd_vel→/cmd_vel_muxed→/cmd_vel_corrected→/ackermann_cmd。cmd_vel_mux 是唯一控制瓶颈。

### TF 互斥
EKF publish_tf=true 时 odom2tf 必须禁用。检查: `ros2 run tf2_tools view_frames`。

### Ackermann 约束
lookahead_dist≥0.65m (>2×0.30m min_turning_radius), 否则弯道冲入禁区。Nav2 odom_topic 指向原始 /odom (非 EKF 输出), 此为有意设计。

### IMU 增强链
/imu/data_raw (Mahony Ki=0)→imu_madgwick (beta=0.033)→EKF (yaw noise=0.005)。实测 1.5m/s 下 2min 漂移 15cm。双IMU (MPU6050+BMI088) 将 yaw noise 降至 0.003。

### 代价调控
use_collision_detection=false, 改用 cost_scaling (dist=0.12, gain=2.0)。窄通道+锥桶场景下碰撞检测频繁误触发。

### 禁区生命周期独立
keepout 由 lifecycle_manager_keepout 单独管理。两节点必须先 activate, 否则 KeepoutFilter 在 costmap configure 时收不到 /costmap_filter_info → 被丢弃。

### Planner 惩罚项耦合
联调每次只改一个参数。change_penalty 最敏感, 三项同时下调会联动放大导致振荡。当前: reverse_penalty=15.0, change_penalty=2.0。

### ARM 编译约束
colcon --parallel-workers 2 (超过2→OOM)。EKF 频率 20→15Hz (Cortex-A55 性能限制)。odom 补偿系数 1.03/1.125 (编码器非线性经验校准)。LiDAR 5Hz (10Hz 默认降至 5Hz 省 CPU)。

### Aurora930 心跳
heartbeat failed!!! 日志噪音。设 heart_enable:=false 消除。

### 启动屏障
wait_for_odom 替代硬编码 sleep, 最长等 15s。competition_master_* 内部额外 8s 延迟等 BT 激活。

### 编码器反馈
velocity_pid 依赖 /robotvel (编码器速度), 超时 0.5s 退化为开环直通。方向切换时自动积分重置 (最小间隔 250ms 防抖)。

### 已移除组件
USB 摄像头, YOLOv5 DNN 流水线 (hobot_usb_cam + dnn_node + websocket), racing_obstacle_detection_yolo 包。

---

## 10. 已知问题

| 问题 | 影响 | 状态 |
|------|------|------|
| smoother_server 被 Nav2 lifecycle 激活但 BT 中已移除 SmoothPath (Humble NaN bug) | 空转浪费 CPU, 不可从本侧修复 (nav2_bringup 内部) | nav2 上游限制 |
| /dev/ttyACM0 硬编码覆盖 ROS 参数 | 移植到其他设备需改源码 | 已知限制 |
| Cartographer 与 AMCL 同时运行可能 TF 冲突 | 避免同时启动 | 使用注意 |
| ConstrainedSmoother Humble NaN crash (nav2#4755) | SmoothPath 从 BT 移除, SmacPlanner 内建平滑替代 | 已绕过 |

---

## 11. 快捷命令

```bash
# 标准比赛启动
ros2 launch originbot_navigation nav_bringup.launch.py

# 阶段测试 (更快启动, 使用组件容器)
ros2 launch origincar_bringup stage1_bringup.launch.py
ros2 launch origincar_bringup stage2_bringup.launch.py
ros2 launch origincar_bringup stage3_bringup.launch.py

# SLAM 建图
ros2 launch origincar_bringup slam_bringup.launch.py

# 地图保存
ros2 run nav2_map_server map_saver_cli -f ~/map

# 纯遥控底盘
ros2 launch origincar_base base_serial.launch.py akmcar:=true

# QR 检测独立调试
ros2 launch origincar_bringup camera_all.launch.py

# 查看话题
ros2 topic list
ros2 topic echo /cmd_vel_muxed

# TF 树
ros2 run tf2_tools view_frames
```
