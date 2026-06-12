# Origincar Pro — 自主驾驶 Ackermann 小车

> ROS2 Humble + RDK X5 | 全国大学生智能汽车竞赛
> 最后更新: 2026-06-12

---

## 快速开始

```bash
# 完整比赛（已验证可完赛）
ros2 launch origincar_bringup stage3_bringup.launch.py

# 阶段1（P点 → QR）
ros2 launch origincar_bringup stage1_bringup.launch.py

# 阶段2（P点 → QR → 通道入口）
ros2 launch origincar_bringup stage2_bringup.launch.py

# SLAM 建图
ros2 launch origincar_bringup slam_bringup.launch.py

# 保存地图
ros2 run nav2_map_server map_saver_cli -f ~/map

# 纯遥控底盘
ros2 launch origincar_base base_serial.launch.py akmcar:=true

# QR 检测调试
ros2 launch origincar_bringup camera_all.launch.py
```

---

## 1. 硬件平台

| 组件 | 型号 | 接口 | 关键参数 |
|------|------|------|----------|
| 主控 | RDK X5 | — | Cortex-A55 ×4, 10TOPS BPU, 5.2GB RAM, Ubuntu 22.04 |
| MCU | STM32F407 | /dev/ttyACM0, 115200bps | 电机/舵机/MPU6050/编码器/电压 |
| LiDAR | Leishen N10 | /dev/ttyACM1, 230400bps | 2D 360°, 5Hz, 2000点/圈 |
| 深度相机 | Aurora930 (Deptrum) | USB 3.0 | RGB+Depth 640×400@15fps, SDK v1.1.22 |
| IMU (底盘) | MPU6050 | STM32 I2C → 串口 | Mahony Ki=0, 零偏未补偿 |
| IMU (板载) | BMI088 | RDK X5 I2C-1 (IIO) | 陀螺噪声 ~1/10 MPU6050, 偏置 <2°/h |
| 底盘 | 阿克曼 | 276×189×150mm | wheelbase=0.143m, min_turning_radius≈0.30m |
| 电池 | 12V 锂电池 | — | /PowerVoltage 监测 |

### 软件环境

- **OS**: Ubuntu 22.04 (ARM aarch64), Swap ≥4GB
- **ROS2**: Humble Hawksbill
- **编译**: `colcon build --parallel-workers 2`（超过 2 会 OOM）
- **Source**: `/opt/tros/humble/setup.bash` + `/opt/ros/humble/setup.bash`
- **工作空间**: `/userdata/dev_ws`

---

## 2. 系统架构

### 2.1 分层总览

```
┌──────────────────────────────────────────────────────────────────┐
│  ORCHESTRATION   │ task_manager │ mission_controller │ lifecycle   │
│                  │ competition_master_stage1/2/3 (legacy)          │
├──────────────────┼────────────────────────────────────────────────┤
│  CONTROL         │ cmd_vel_mux │ velocity_pid │ pose_pid_corrector │
│                  │         cmd_vel_to_ackermann_drive              │
├──────────────────┼────────────────────────────────────────────────┤
│  NAVIGATION      │ AMCL │ SmacPlannerHybrid(REEDS_SHEPP) │ RPP    │
│  (Nav2)          │ BT Navigator │ ConstrainedSmoother │ VelSm      │
├──────────────────┼────────────────────────────────────────────────┤
│  PERCEPTION      │ imu_madgwick │ qr_decoder (ZBar) │ qr_decision  │
│                  │ vision_ai (火山引擎 VLM) │ cartographer         │
├──────────────────┼────────────────────────────────────────────────┤
│  SENSOR FUSION   │ EKF (robot_localization, 双IMU) │ odom2tf      │
├──────────────────┼────────────────────────────────────────────────┤
│  DRIVER          │ origincar_base (STM32) │ lslidar (N10)         │
│                  │ aurora930 │ bmi088_iio_bridge                   │
├──────────────────┼────────────────────────────────────────────────┤
│  HARDWARE        │ RDK X5 │ STM32 │ N10 │ Aurora930 │ MPU6050    │
└──────────────────┴────────────────────────────────────────────────┘
```

### 2.2 自定义节点

| 节点 | 包 | 语言 | 职责 |
|------|-----|------|------|
| `origincar_base` | origincar_base | C++ | STM32 串口桥接：发布 /odom, /imu/data_raw, /robotvel, /PowerVoltage；订阅 /ackermann_cmd |
| `lslidar_driver_node` | lslidar_driver | C++ | N10 LiDAR 驱动 → /scan (5Hz, frame=laser_link) |
| `qr_decoder_zbar` | qr_decoder | C++ | ZBar QR 解码 + 多尺度扫描 → /sign, /sign_pose |
| `odom2tf` | origincar_bringup | C++ | /odom → odom→base_footprint TF（use_ekf=false 时启用） |
| `cmd_vel_to_ackermann_drive` | origincar_base | Python | Twist → AckermannDriveStamped（wheelbase=0.143, steering_sign=-1） |
| `cmd_vel_mux` | origincar_bringup | Python | 3输入优先级多路复用器（nav=10, pid=20, stop=255）, 30Hz |
| `velocity_pid` | origincar_bringup | Python | 增量式 PID 速度闭环（30Hz），编码器反馈，方向切换积分重置 |
| `pose_pid_corrector` | origincar_bringup | Python | 末端精确停车 PID（0.5m 内激活），AMCL 协方差门控 |
| `imu_madgwick_filter` | origincar_bringup | Python | Madgwick 6-DOF AHRS（beta=0.033, 100Hz）→ /imu/data/madgwick |
| `bmi088_iio_bridge` | origincar_bringup | Python | BMI088 Linux IIO → /imu_data（100Hz, 无姿态） |
| `task_manager` | origincar_bringup | Python | 5态竞赛状态机, 10Hz 心跳 → /mission_cmd |
| `mission_controller` | origincar_bringup | Python | 执行 /mission_cmd → Nav2 Action / /stop_cmd_vel / /sign4return |
| `competition_lifecycle_manager` | origincar_bringup | Python | Nav2 运行时参数切换 + 紧急全栈重置（9节点） |
| `wait_for_odom` | origincar_bringup | Python | 启动屏障：等待 /odom 就绪（最长15s） |
| `calibrate_gui` | origincar_bringup | Python | 手动路点/禁区标定 GUI（PC端, matplotlib） |
| `field_calibrator` | origincar_bringup | Python | 自动 P点标定 + 锥桶测量 |
| `competition_master_stage1` | origincar_bringup | Python | [Legacy] 阶段1独立控制器 |
| `competition_master_stage2` | origincar_bringup | Python | [Legacy] 阶段2独立控制器 |
| `competition_master_stage3` | origincar_bringup | Python | [Legacy] 阶段3独立控制器（stage3_bringup 仍在使用） |
| `qr_decision` | origincar_qr | Python | QR 方向决策：奇数→顺时针, 偶数→逆时针, 3s 冷却 |
| `vision_ai_node` | racing_vision_ai | Python | VLM 图生文：/sign4return 触发 → 火山引擎 ARK API |

### 2.3 Nav2 基础设施节点

| 节点 | 包 | 职责 |
|------|-----|------|
| `ekf_filter_node` | robot_localization | 多传感器融合：/odom + /imu/data/madgwick(imu0) + /imu_data(imu1) → /odometry/filtered + odom→base_footprint TF |
| `amcl` | nav2_amcl | 粒子滤波定位：/scan + /map → map→odom TF |
| `map_server` | nav2_map_server | 静态地图服务（room.yaml） |
| `planner_server` | nav2 | SmacPlannerHybrid 全局规划器（REEDS_SHEPP） |
| `controller_server` | nav2 | RegulatedPurePursuit 局部控制器 |
| `bt_navigator` | nav2 | 行为树导航执行器 |
| `recoveries_server` | nav2 | 恢复行为（BackUp + Wait, 无Spin） |
| `global_costmap` / `local_costmap` | nav2 | 全局/局部代价地图, 含 keepout_filter |
| `velocity_smoother` | nav2 | 速度平滑（OPEN_LOOP, 20Hz） |
| `smoother_server` | nav2 | 路径平滑（ConstrainedSmoother, BT 中已移除） |
| `waypoint_follower` | nav2 | 路点跟随任务（WaitAtWaypoint, 200ms） |
| `keepout_mask_server` | nav2_map_server | 禁区代价地图 |
| `keepout_filter_info_server` | nav2_map_server | 禁区过滤器元数据 |
| `lifecycle_manager` | nav2_lifecycle_manager | Nav2 标准生命周期管理 |
| `lifecycle_manager_keepout` | nav2_lifecycle_manager | 禁区节点生命周期管理（独立） |

---

## 3. 控制流水线

### 3.1 cmd_vel 5级流水线（不可绕过）

```
Nav2 RPP → velocity_smoother (20Hz OPEN_LOOP) → /cmd_vel
  → [remap] → /nav_cmd_vel (p=10, timeout=0.5s) ──────────────┐
pose_pid_corrector → /pid_cmd_vel (p=20, timeout=0.3s) ────────┤
mission_controller → /stop_cmd_vel (p=255, 零值 Twist) ────────┤
                                                                v
                                                         cmd_vel_mux (30Hz)
                                                         超时自动回退到低优先级
                                                                │
                                                                v /cmd_vel_muxed
                                                         velocity_pid (30Hz)
                                                         增量式 PID, 反馈: /robotvel
                                                         反馈超时(0.5s) → 开环直通
                                                                │
                                                                v /cmd_vel_corrected
                                                         cmd_vel_to_ackermann_drive
                                                         steering = -1.0 × atan(0.143/(v/w))
                                                                │
                                                                v /ackermann_cmd
                                                         origincar_base → 11B serial → STM32
```

**优先级**: stop(255) > pid(20) > nav(10)。stop 零值发布即急停。  
**velocity_pid 参数**: Kp_vx=0.8, Ki_vx=0.6, Kd_vx=0.05, max_vx=0.85。Kp_wz=1.0, Ki_wz=0.4, Kd_wz=0.02, max_wz=2.8。积分限幅=0.8×max。方向切换时积分自动重置（最小间隔250ms）。

### 3.2 双IMU姿态融合

```
MPU6050 → STM32 Mahony (Ki=0) → /imu/data_raw
  → imu_madgwick_filter (beta=0.033, 100Hz) → /imu/data/madgwick
      │                                           (imu0: yaw姿态 + Z角速度)
BMI088 → Linux IIO → bmi088_iio_bridge (100Hz) → /imu_data
      │                                           (imu1: Z角速度, 无姿态)
      ├──→ EKF (15Hz, 2D, publish_tf=true)
             yaw noise: 单IMU=0.005, 双IMU=0.003
             → /odometry/filtered + TF: odom→base_footprint
```

EKF 频率从 20Hz 降至 15Hz（Cortex-A55 单步执行 117-134ms，超出 50ms 预算）。

### 3.3 完整话题拓扑

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
| aurora930 | /aurora/rgb/image_raw | Image | qr_decoder_zbar, vision_ai_node |
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
| velocity_pid | /cmd_vel_corrected | Twist | cmd_vel_to_ackermann_drive |
| cmd_vel_to_ackermann | /ackermann_cmd | AckermannDrive | origincar_base |

### 3.4 TF 树（REP-105）

```
map
  │  AMCL (导航) 或 Cartographer (建图)
  v
odom
  │  EKF (publish_tf=true, 默认) 或 odom2tf (use_ekf=false)
  v
base_footprint
  ├── base_link (static, z=+0.07m, URDF)
  │     ├── laser_link (URDF static, z=+0.075m)
  │     └── depth_camera_link (static, x=+0.14m, z=+0.05m)
  └── gyro_link (URDF static, 与 base_footprint 同原点)
```

**关键**: odom→base_footprint 必须恰好一个发布者。EKF 和 odom2tf 互斥。

| 模式 | odom→base_footprint 来源 | use_ekf | pub_odom_tf |
|------|--------------------------|---------|-------------|
| 比赛导航（默认） | EKF | true | false |
| 纯遥控/无EKF | odom2tf | false | true |
| Cartographer 建图 | EKF | true | false |

---

## 4. Nav2 导航配置

### 4.1 全局规划器 — SmacPlannerHybrid

| 参数 | 值 | 说明 |
|------|-----|------|
| motion_model | REEDS_SHEPP | 前进+倒退, 适应 Ackermann |
| minimum_turning_radius | 0.30m | wheelbase=0.143m, max_steer≈28° |
| max_iterations | 2000 | Cortex-A55 硬限制 |
| max_planning_time | 3.0s | 快速失败以便重试 |
| angle_quantization_bins | 48 | ARM 优化（默认72） |
| downsample_costmap | true | 2×降采样 |
| cache_obstacle_heuristic | false | 关闭以加速 configure() 72s→5s |
| reverse_penalty | 4.0 | 抑制路点倒车 |
| change_penalty | 0.2 | 方向切换惩罚 |
| smooth_path | true | 内建平滑，替代 SmoothPath BT 节点 |

### 4.2 局部控制器 — RegulatedPurePursuit

| 参数 | 值 | 说明 |
|------|-----|------|
| desired_linear_vel | 0.45m/s | 直线巡航速度 |
| max_linear_vel | 0.55m/s | 硬上限 |
| max_angular_vel | 1.50rad/s | 抑制窄道振荡 |
| lookahead_dist | 0.65m | ≥2×min_turning_radius(0.60m) |
| min_lookahead_dist | 0.55m | |
| max_lookahead_dist | 1.5m | |
| lookahead_time | 1.8s | |
| use_cost_regulated_linear_velocity_scaling | true | 障碍物逼近减速 |
| cost_scaling_dist | 0.12m | |
| cost_scaling_gain | 2.0 | |
| use_collision_detection | false | 窄道误触发, 用 cost 调控替代 |
| allow_reversing | true | REEDS_SHEPP 后退机动 |
| use_rotate_to_heading | false | 阿克曼必须关闭 |
| goal_tolerance.xy | 0.20m | |
| goal_tolerance.yaw | 3.14rad | 结构扫描需任意朝向 |

### 4.3 代价地图

| 参数 | 全局 | 局部 |
|------|------|------|
| 类型 | 全地图固定（map系） | 3m×3m 滚动窗口（odom系） |
| robot_footprint | 多边形 [[0.15,-0.10],[0.15,0.10],[-0.12,0.10],[-0.12,-0.10]] | 同 |
| inflation_radius | 0.12m | 0.12m |
| cost_scaling_factor | 5.0 | 5.0 |
| track_unknown_space | true | — |
| 传感器源 | /scan + /aurora/points2 | /scan + /aurora/points2 |
| aurora_points 高度 | 0.05-0.35m, persistence=0.5s | 同 |
| 插件 | static_layer, obstacle_layer, keepout_filter, inflation_layer | obstacle_layer, keepout_filter, inflation_layer |

**禁区系统**: keepout_filter 由独立 lifecycle_manager_keepout 管理。`override_lethal_cost=true, lethal_override_cost=252`（MAX_NON_OBSTACLE，可脱困但强力排斥）。

### 4.4 行为树（RPP）

非 infinite retries（-1），适配动态障碍物场景。

**单目标 (navigate_to_pose_ackermann_rpp.xml)**:
- 路径计算前 ClearCostmapAroundRobot(1.5m)
- FollowPath 失败：清局部代价地图 + Wait 0.5s
- 系统恢复：清代价地图 + BackUp 0.8m → Wait 3s → 清代价地图 + BackUp 1.5m
- 无 Spin（阿克曼）、无 SmoothPath（Humble NaN bug #4755）

**多路点 (navigate_through_poses_ackermann_rpp.xml)**:
- RemovePassedGoals(radius=0.4m) 后重新规划
- 恢复流程增加了 0.5s 等待传感器刷新

### 4.5 AMCL 定位

- 模型: DifferentialMotionModel（无原生 Ackermann 模型）
- alpha1-alpha5: 0.45（补偿阿克曼-差分模型差异）
- 粒子: 300-1500, likelihood_field
- recovery_alpha_fast: 0.1
- 初始位姿: (-1.985, -0.014, 0.262) — 来自 Cartographer 纯定位（1193帧, σ_xy=2-3mm）

---

## 5. STM32 串口协议

### RX 帧（STM32 → ROS2, 24B）

| 字节 | 字段 | 编码 | 说明 |
|------|------|------|------|
| 0 | Header | 0x7B | 帧头 |
| 1 | Flag_Stop | uint8 | 停止标志 |
| 2-3 | Vx | int16/1000 | X线速度 (m/s) |
| 4-5 | Vy | int16/1000 | Y线速度 (m/s) |
| 6-7 | Vz | int16/1000 | Z角速度 (rad/s) |
| 8-13 | accel_xyz | int16×3 / 1671.84 | 加速度 (m/s²) |
| 14-19 | gyro_xyz | int16×3 × 0.00026644 | 角速度 (rad/s) |
| 20-21 | voltage | int16/1000 | 电池电压 (V) |
| 22 | checksum | XOR(0..21) | 异或校验 |
| 23 | Tail | 0x7D | 帧尾 |

### TX 帧（ROS2 → STM32, 11B）

| 字节 | 字段 | Ackermann 模式 | 差速模式 |
|------|------|---------------|----------|
| 0 | Header | 0x7B | 0x7B |
| 1-2 | Reserved | 0, 0 | 0, 0 |
| 3-4 | speed | vx × 1000 | vx × 1000 |
| 5-6 | Y_speed | 0 (未使用) | vy × 1000 |
| 7-8 | steering | angle × 1000 / 2 | ω × 1000 |
| 9 | checksum | XOR(0..8) | XOR(0..8) |
| 10 | Tail | 0x7D | 0x7D |

**注意**: 构造函数中 `usart_port_name` 参数被声明但未使用——串口硬编码为 `/dev/ttyACM0`。转向编码为 `angle × 500`（STM32 端内部 ×2 恢复）。

### 里程计

```
Robot_Pos.X += 1.03 × (Vx·cosθ − Vy·sinθ) × dt
Robot_Pos.Y += 1.125 × (Vx·sinθ + Vy·cosθ) × dt
Robot_Pos.Z += Vz × dt
```

补偿系数 1.03/1.125 为编码器非线性经验校准（硬编码，非参数）。

---

## 6. 竞赛三阶段

### 阶段1: P点 → QR
- NavigateToPose → QR 点 (0.41, -3.17)
- 途中扫到 QR → 打印数据并停止
- 超时: 120s

### 阶段2: QR → 通道入口
- NavigateToPose → QR 点 → 扫到码
- 杀 ZBar → 等待 /qr_event (2s 超时)
- 倒车退避 (6s, vx=-0.15, wz=+2.80)：避开 keepout 致死区
- NavigateToPose → 通道入口 (0.38, -1.10)

### 阶段3: 完整赛道（stage3_bringup 完赛流程）
1. QR → 倒车退避
2. NavigateThroughPoses 通道巡航：
   - 顺时针（奇QR）: entry → (0.87, 0.83) → (3.21, -1.82)
   - 逆时针（偶QR）: entry → (1.85, -2.14) → (2.01, 1.09)
3. 触发 VLM (/sign4return=100) → 异步返回结果
4. NavigateToPose → P 点 (-1.985, -0.014, yaw=0.262)
5. 全局超时: 180s

### lifecycle_manager 模式参数

| 参数 | task1 | task2 | task3 |
|------|-------|-------|-------|
| inflation_radius | 0.18 | 0.12 | 0.18 |
| obstacle_range | 5.0 | 1.5 | 5.0 |
| desired_linear_vel | 0.70 | 0.40 | 0.70 |
| max_linear_vel | 0.80 | 0.50 | 0.80 |

---

## 7. Launch 文件

### 7.1 入口总览

| Launch 文件 | 用途 | 节点数 |
|------------|------|--------|
| `nav_bringup.launch.py` | 标准比赛导航（task_manager + Nav2） | ~22 |
| `stage1_bringup.launch.py` | 阶段1测试 | ~17 |
| `stage2_bringup.launch.py` | 阶段2测试 | ~18 |
| `stage3_bringup.launch.py` | **阶段3完整比赛（已验证完赛）** | ~19 |
| `slam_bringup.launch.py` | Cartographer 建图 | ~11 |
| `camera_all.launch.py` | QR 检测独立调试 | ~4 |
| `base_serial.launch.py` | 纯遥控底盘 | ~2 |

### 7.2 stage3_bringup 启动时序

```
t=0s  → base_minimal.launch.py（底盘+LiDAR+TF+EKF+Madgwick+BMI088+mux+PID）
t=0s  → camera_all.launch.py（Aurora930 + QR解码 + QR决策）
t=0s  → vision_ai_node（条件：racing_vision_ai 包存在）
t=1s  → nav2_minimal.launch.py（禁区 + Nav2 composition 模式）
t=4s  → competition_master_stage3.py（比赛编排主节点）
t=8s  → RViz2（可视化）
```

### 7.3 Launch 依赖链

```
stage3_bringup.launch.py
  ├── base_minimal.launch.py（底盘核心, 8节点）
  │     ├── base_serial.launch.py（STM32 串口驱动）
  │     ├── lslidar_driver_node（N10 LiDAR）
  │     ├── urdf2tf.launch.py（robot_state_publisher）
  │     ├── odom2tf（条件：use_ekf=false）
  │     ├── imu_madgwick_filter.py（条件：use_ekf=true）
  │     ├── bmi088_iio_bridge.py（条件：use_bmi088=true）
  │     ├── ekf_node（双IMU/单IMU 条件选择）
  │     ├── cmd_vel_mux.py
  │     └── velocity_pid.py
  ├── camera_all.launch.py（Aurora930 + QR）
  │     ├── aurora930_launch.py（外部：deptrum-ros-driver-aurora930）
  │     ├── depth_camera_tf（static_transform_publisher）
  │     ├── qr_decoder_zbar
  │     └── qr_decision
  ├── nav2_minimal.launch.py（Nav2 composition 模式）
  │     ├── keepout 服务器（3节点）
  │     └── Nav2 bringup_launch.py（composition=True）
  └── competition_master_stage3.py + RViz2
```

### 7.4 关键 Launch 参数

**base_minimal.launch.py**:

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `use_ekf` | true | EKF 传感器融合（发布 odom→base_footprint TF） |
| `pub_odom_tf` | false | odom2tf 发布 TF（仅 use_ekf=false 时） |
| `use_bmi088` | true | 双IMU EKF（MPU6050 + BMI088） |

**camera_all.launch.py**:

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `depth_cam_x/y/z` | 0.14/0.0/0.05 | 相机偏移 (m) |
| `depth_min_mm` | 50 | QR 深度过滤下限 (mm) |
| `depth_max_mm` | 4000 | QR 深度过滤上限 (mm) |

---

## 8. 配置文件索引

| 文件 | 位置 | 关键内容 |
|------|------|---------|
| originbot_nav2_rpp.yaml | originbot_navigation/param/ | Nav2 全栈：AMCL, SmacPlannerHybrid(REEDS_SHEPP), RPP, costmaps×2, smoother, velocity_smoother |
| originbot_nav2.yaml | originbot_navigation/param/ | DWA 备选：NavfnPlanner + DWB |
| ekf_dual_imu.yaml | origincar_base/config/ | EKF 双IMU：odom+imu0(MPU6050)+imu1(BMI088), 15Hz, yaw noise=0.003 |
| ekf.yaml | origincar_base/config/ | EKF 单IMU：odom+imu0, 15Hz, yaw noise=0.005 |
| imu_madgwick.yaml | origincar_base/config/ | Madgwick：beta=0.033, 100Hz |
| bmi088_imu.yaml | origincar_base/config/ | BMI088：I2C bus 1, acc 12g, gyro 1000dps, 40Hz |
| control_params.yaml | origincar_base/config/ | PID + mux：增益、优先级、超时 |
| lsx10.yaml | lslidar_driver/params/ | N10：/dev/ttyACM1, 5Hz, 230400bps |
| lds_2d.lua | originbot_navigation/config/ | Cartographer Route B：EKF odom, max_range=8.0m |
| vision_ai_config.yaml | racing_vision_ai/config/ | 火山引擎 ARK API |
| room.yaml | originbot_navigation/maps/ | 静态地图：163×141, 0.05m/px, origin=[-2.65, -4.5, 0] |
| keepout_mask.yaml | originbot_navigation/maps/ | 禁区掩码：同尺寸同原点对齐 |

---

## 9. 关键约束与调参备注

### cmd_vel 流水线
5级不可绕过。调试时逐级检查话题: /cmd_vel → /nav_cmd_vel → /cmd_vel_muxed → /cmd_vel_corrected → /ackermann_cmd。cmd_vel_mux 是唯一控制瓶颈。

### Ackermann 约束
lookahead_dist ≥ 0.65m（> 2×0.30m min_turning_radius），否则弯道冲入禁区。Nav2 odom_topic 指向原始 /odom（非 EKF 输出），此为有意设计。

### 双IMU 增强
/imu/data_raw (Mahony Ki=0) → imu_madgwick (beta=0.033) → EKF (yaw noise=0.005)。实测 1.5m/s 下 2min 漂移 15cm。双IMU (MPU6050+BMI088) 将 yaw noise 降至 0.003。BMI088 仅提供 Z 角速度（无姿态），作为汽车级陀螺冗余。

### 代价调控
use_collision_detection=false，改用 cost_scaling（dist=0.12, gain=2.0）。窄通道+锥桶场景下碰撞检测频繁误触发。

### 禁区生命周期独立
keepout 由 lifecycle_manager_keepout 单独管理。两节点必须先 activate，否则 KeepoutFilter 在 costmap configure 时收不到 /costmap_filter_info → 被丢弃。

### ARM 编译约束
colcon --parallel-workers 2（超过 2 → OOM）。EKF 频率 20→15Hz（Cortex-A55 单步超 50ms 预算）。LiDAR 5Hz（默认 10Hz 降至 5Hz 省 CPU）。SmacPlannerHybrid 关闭 cache_obstacle_heuristic（configure 72s → 5s）。

### Aurora930 心跳
`heartbeat failed!!!` 每 2s 一条日志——SDK v1.1.22 与 Firmware 1.7.2 心跳协议不兼容，数据流正常。launch 中设 `heart_enable:=false` 消除。

### 启动屏障
wait_for_odom 替代硬编码 sleep，最长等 15s。competition_master_* 内部额外 8s 延迟等 BT 激活（bt_navigator 生命周期约需 30s）。

### 编码器反馈
velocity_pid 依赖 /robotvel（编码器速度），超时 0.5s 退化为开环直通。方向切换时自动积分重置（最小间隔 250ms 防抖）。

### 已移除组件
USB 摄像头, YOLOv5 DNN 流水线 (hobot_usb_cam + dnn_node + websocket), racing_obstacle_detection_yolo 包。

---

## 10. 已知问题

| 问题 | 影响 | 状态 |
|------|------|------|
| smoother_server 被 lifecycle 激活但 BT 中已移除 SmoothPath（Humble NaN bug #4755） | 空转浪费 CPU, 不可修复（nav2_bringup 内部） | Nav2 上游限制 |
| /dev/ttyACM0 硬编码覆盖 ROS 参数 `usart_port_name` | 移植需改源码 | 已知限制 |
| Cartographer 与 AMCL 同时运行可能 TF 冲突 | 避免同时启动 | 使用注意 |
| Aurora930 `heartbeat failed!!!` 日志噪音 | 数据正常, 设 heart_enable:=false | 已绕过 |
| vision_ai_config.yaml 含明文 API key | 安全隐患 | 待处理 |
| Mahony 积分增益为零（Ki=0） | 陀螺零偏未补偿, yaw 持续漂移 | 由 Madgwick+EKF 补偿 |
| QR decoder 深度过滤仅 advisory | 深度无效时仍发布 /sign | 下游自行过滤 |
