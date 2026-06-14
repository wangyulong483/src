# Origincar Pro — 自主驾驶 Ackermann 小车

> ROS2 Humble + RDK X5 | 全国大学生智能汽车竞赛 | 最优圈速 77.3s
> 最后更新: 2026-06-14

---

## 快速开始

```bash
# 完整比赛（已验证完赛, 77.3s）
ros2 launch origincar_bringup stage3_bringup.launch.py

# 阶段1（P点 → QR）
ros2 launch origincar_bringup stage1_bringup.launch.py

# 阶段2（P点 → QR → 通道入口）
ros2 launch origincar_bringup stage2_bringup.launch.py

# SLAM 建图 (Cartographer)
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
| 主控 | RDK X5 (Sunrise 5) | — | Cortex-A55 ×4, 10TOPS BPU, 5.2GB RAM, Ubuntu 22.04 |
| MCU | STM32F407 | /dev/ttyACM0, 115200bps | 电机/舵机/MPU6050/编码器/电压 |
| LiDAR | Leishen N10 | /dev/ttyACM1, 230400bps | 2D 360°, 5Hz, 2000点/圈 |
| 深度相机 | Aurora930 (Deptrum) | USB 3.0 | RGB+Depth 640×400@15fps, SDK v1.1.22 |
| IMU (底盘) | MPU6050 | STM32 I2C → 串口 | Mahony Ki=0, 零偏未补偿 |
| IMU (板载) | BMI088 | RDK X5 I2C-1 (IIO) | 陀螺噪声 ~1/10 MPU6050, 偏置 <2°/h, 现已切换为主IMU |
| 底盘 | 阿克曼 | 276×189×150mm | wheelbase=0.143m, min_turning_radius≈0.30m, max_steer≈28° |
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
│                  │ competition_master_stage1/2/3 (stage3 为主)     │
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
│  SENSOR FUSION   │ EKF (robot_localization, 双IMU)               │
├──────────────────┼────────────────────────────────────────────────┤
│  DRIVER          │ origincar_base (STM32) │ lslidar (N10)         │
│                  │ aurora930 │ bmi088_iio_bridge                   │
├──────────────────┼────────────────────────────────────────────────┤
│  HARDWARE        │ RDK X5 │ STM32 │ N10 │ Aurora930 │ MPU6050    │
│                  │ BMI088 (IIO)                                    │
└──────────────────┴────────────────────────────────────────────────┘
```

### 2.2 自定义节点

| 节点 | 包 | 语言 | 职责 |
|------|-----|------|------|
| `origincar_base` | origincar_base | C++ | STM32 串口桥接：发布 /odom, /imu/data_raw, /robotvel, /PowerVoltage；订阅 /ackermann_cmd |
| `lslidar_driver_node` | lslidar_driver | C++ | N10 LiDAR 驱动 → /scan (5Hz, frame=laser_link) |
| `qr_decoder_zbar` | qr_decoder | C++ | ZBar QR 解码 + 多尺度扫描 → /sign, /sign_pose；深度过滤 advisory only |
| `cmd_vel_to_ackermann_drive` | origincar_base | Python | Twist → AckermannDriveStamped (wheelbase=0.143, steering_sign=-1) |
| `cmd_vel_mux` | origincar_bringup | Python | 3输入优先级多路复用器 (nav=10, pid=20, stop=255), 30Hz |
| `velocity_pid` | origincar_bringup | Python | 增量式 PID 速度闭环 (30Hz), 编码器反馈, 方向切换积分重置 |
| `pose_pid_corrector` | origincar_bringup | Python | 末端精确停车 PID (0.5m 内激活), AMCL 协方差门控 |
| `imu_madgwick_filter` | origincar_bringup | Python | Madgwick 6-DOF AHRS (beta=0.033, 100Hz) → /imu/data/madgwick |
| `bmi088_iio_bridge` | origincar_bringup | Python | BMI088 Linux IIO → /imu_data (100Hz, 含手动 scale 校准) |
| `task_manager` | origincar_bringup | Python | 5态竞赛状态机, 10Hz 心跳 → /mission_cmd |
| `mission_controller` | origincar_bringup | Python | 执行 /mission_cmd → Nav2 Action / /stop_cmd_vel / /sign4return |
| `competition_lifecycle_manager` | origincar_bringup | Python | Nav2 运行时参数切换 + 紧急全栈重置 (9节点) |
| `wait_for_odom` | origincar_bringup | Python | 启动屏障：等待 /odom 就绪 (最长15s) |
| `calibrate_gui` | origincar_bringup | Python | 手动路点/禁区标定 GUI (PC端, matplotlib) |
| `field_calibrator` | origincar_bringup | Python | 自动 P点标定 + 锥桶测量 |
| `competition_master_stage1` | origincar_bringup | Python | [Legacy] 阶段1独立控制器 |
| `competition_master_stage2` | origincar_bringup | Python | [Legacy] 阶段2独立控制器 |
| `competition_master_stage3` | origincar_bringup | Python | **[Active] 阶段3完整比赛控制器 (stage3_bringup 使用)** |
| `qr_decision` | origincar_qr | Python | QR 方向决策：奇数→顺时针, 偶数→逆时针, 3s 冷却 |
| `vision_ai_node` | racing_vision_ai | Python | VLM 图生文：/sign4return 触发 → 火山引擎 ARK API |

### 2.3 Nav2 基础设施节点

| 节点 | 包 | 职责 |
|------|-----|------|
| `ekf_filter_node` | robot_localization | 多传感器融合：/odom + /imu_data(BMI088, imu0) + /imu/data/madgwick(MPU6050, imu1, differential) → /odometry/filtered + odom→base_footprint TF |
| `amcl` | nav2_amcl | 粒子滤波定位：/scan + /map → map→odom TF |
| `map_server` | nav2_map_server | 静态地图服务 (room.yaml) |
| `planner_server` | nav2 | SmacPlannerHybrid 全局规划器 (REEDS_SHEPP) |
| `controller_server` | nav2 | RegulatedPurePursuit 局部控制器 |
| `bt_navigator` | nav2 | 行为树导航执行器 (default_server_timeout=500ms, BT loop=10Hz) |
| `recoveries_server` | nav2 | 恢复行为 (BackUp + Wait, 无Spin) |
| `global_costmap` / `local_costmap` | nav2 | 全局/局部代价地图, 含 keepout_filter |
| `velocity_smoother` | nav2 | 速度平滑 (OPEN_LOOP, 20Hz) |
| `smoother_server` | nav2 | 路径平滑 (ConstrainedSmoother, BT 中已移除 — Humble NaN bug #4755) |
| `waypoint_follower` | nav2 | 路点跟随任务 (WaitAtWaypoint, 200ms) |
| `keepout_mask_server` | nav2_map_server | 禁区代价地图 |
| `keepout_filter_info_server` | nav2_map_server | 禁区过滤器元数据 → /costmap_filter_info_server (死胡同, 无人订阅) |
| `lifecycle_manager` | nav2_lifecycle_manager | Nav2 标准生命周期管理 |
| `lifecycle_manager_keepout` | nav2_lifecycle_manager | 禁区节点生命周期管理 (独立) |

---

## 3. 控制流水线

### 3.1 cmd_vel 5级流水线 (不可绕过)

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

> **已知问题**: velocity_pid 输出到 `/cmd_vel_corrected`, 但 origincar_base 实际订阅 `/cmd_vel` (通过 `cmd_vel` 参数)。PID 修正被静默丢弃——编码器反馈闭环从未生效。修改订阅目标会导致 origincar_base SIGABRT 崩溃 (exit -6), 根因待查。详见 [LRN-20260614-002]。

**velocity_pid 参数**: Kp_vx=0.8, Ki_vx=0.6, Kd_vx=0.05, max_vx=0.85。Kp_wz=1.0, Ki_wz=0.4, Kd_wz=0.02, max_wz=2.8。积分限幅=0.8×max。方向切换时积分自动重置 (最小间隔 250ms)。

### 3.2 双IMU姿态融合

```
MPU6050 → STM32 Mahony (Ki=0) → /imu/data_raw
  → imu_madgwick_filter (beta=0.033, 100Hz) → /imu/data/madgwick
      │                           (imu0: yaw姿态参考 + Z角速度)
BMI088 → Linux IIO → bmi088_iio_bridge (100Hz, 手动scale) → /imu_data
  → imu_madgwick_filter (beta=0.003, 100Hz) → /imu/data/bmi088_madgwick
      │                           (imu1: Z角速度 only, differential=true)
      ├──→ EKF (15Hz, 2D, publish_tf=true)
             yaw noise: 单IMU=0.005, 双IMU=0.003
             → /odometry/filtered + TF: odom→base_footprint
```

> **BMI088 角色**: 汽车级陀螺, 噪声 ~1/10 MPU6050, 偏置 <2°/h。通过 Madgwick (beta=0.003) 滤波提供低噪声角速度。EKF 中使用差分模式 (differential=true), 仅融合角速度增量以避免与 imu0 的 yaw 姿态冲突。bmi088_iio_bridge 手动 scale 校准 (RDK X5 IIO 无 `_scale` 文件): gyro_scale=0.00053 rad/s, accel_scale=0.00341 m/s²。

EKF 频率 20→15Hz (Cortex-A55 单步执行 117-134ms, 超出 50ms 预算)。

### 3.3 完整话题拓扑

| 发布者 | 话题 | 类型 | 订阅者 |
|--------|------|------|--------|
| origincar_base | /odom | Odometry | EKF, task_manager, qr_decoder, pose_pid_corrector, wait_for_odom, qr_decision |
| origincar_base | /imu/data_raw | Imu | imu_madgwick_filter |
| origincar_base | /robotvel | Data | velocity_pid |
| origincar_base | /PowerVoltage | Float32 | (monitoring) |
| imu_madgwick_filter (MPU6050) | /imu/data/madgwick | Imu | EKF (imu0, yaw姿态 + 角速度) |
| bmi088_iio_bridge | /imu_data | Imu | imu_madgwick_filter (BMI088) |
| imu_madgwick_filter (BMI088) | /imu/data/bmi088_madgwick | Imu | EKF (imu1, differential, 仅角速度) |
| EKF | /odometry/filtered | Odometry | cartographer |
| EKF | TF: odom→base_footprint | — | 全局 |
| lslidar_driver | /scan | LaserScan | AMCL, costmaps×2, cartographer |
| aurora930 | /aurora/rgb/image_raw | Image | qr_decoder_zbar, vision_ai_node |
| aurora930 | /aurora/depth/image_raw | Image | qr_decoder_zbar |
| aurora930 | /aurora/points2 | PointCloud2 | costmaps×2 |
| AMCL | TF: map→odom | — | 全局导航栈 |
| AMCL | /amcl_pose | PoseWithCovariance | task_manager, pose_pid_corrector, competition_master_stage3 |
| qr_decoder_zbar | /sign | String | qr_decision, task_manager, competition_master_* |
| qr_decision | /qr_event | String | task_manager, competition_master_stage2/3 |
| task_manager | /mission_cmd | String | mission_controller |
| task_manager | /heartbeat/task_manager | String | (monitoring) |
| mission_controller | /mission_status | String | task_manager |
| mission_controller | /stop_cmd_vel | Twist | cmd_vel_mux |
| mission_controller | /sign4return | Int32 | vision_ai_node |
| velocity_smoother | /cmd_vel → /nav_cmd_vel | Twist | cmd_vel_mux |
| pose_pid_corrector | /pid_cmd_vel | Twist | cmd_vel_mux |
| cmd_vel_mux | /cmd_vel_muxed | Twist | velocity_pid, competition_master_stage3 (diag) |
| velocity_pid | /cmd_vel_corrected | Twist | cmd_vel_to_ackermann_drive |
| cmd_vel_to_ackermann | /ackermann_cmd | AckermannDrive | origincar_base |
| competition_master_stage3 | /costmap_ctrl | CostmapFilterInfo | KeepoutFilter (QoS: TRANSIENT_LOCAL) |
| competition_master_stage3 | /plan | Path | competition_master_stage3 (diag) |

### 3.4 TF 树 (REP-105)

```
map
  │  AMCL (导航) 或 Cartographer (建图)
  v
odom
  │  EKF (publish_tf=true, 默认)
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
| 比赛导航 (默认) | EKF | true | false |
| 纯遥控/无EKF | odom2tf | false | true |
| Cartographer 建图 | EKF | true | false |

---

## 4. Nav2 导航配置

### 4.1 全局规划器 — SmacPlannerHybrid

| 参数 | 值 | 说明 |
|------|-----|------|
| motion_model | REEDS_SHEPP | 前进+倒退, 适应 Ackermann 窄空间 |
| minimum_turning_radius | 0.30m | wheelbase=0.143m, max_steer≈28° |
| max_iterations | 2000 | Cortex-A55 硬限制 |
| max_planning_time | 3.0s | 快速失败以便重试 |
| angle_quantization_bins | 48 | ARM 优化 (默认72) |
| downsample_costmap | true | 2×降采样 |
| cache_obstacle_heuristic | false | 关闭以加速 configure() 72s→5s |
| lookup_table_size | 20.0 | 运动基元查找表 (默认) |
| reverse_penalty | 2.0 | 抑制路点倒车 (官方推荐 1.3-5.0) |
| change_penalty | 0.10 | 方向切换惩罚 (官方推荐 0.0-0.3) |
| cost_penalty | 4.0 | |
| non_straight_penalty | 1.3 | |
| cache_obstacle_heuristic | true | 缓存静态代价图启发式, 重规划 20-40× 加速 |
| smooth_path | true | 内建平滑, 替代 SmoothPath BT 节点 |

> **已知限制**: Humble 中 `reverse_penalty` 对解析扩展无效 (Issue #6075), `AdaptiveToleranceGoalChecker` 不可用。

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
| goal_tolerance.yaw | 3.14rad | 结构扫描需任意朝向 (PI, 跳过朝向检查) |
| max_robot_pose_search_dist | -1.0 | 无限回溯 |

> **Humble RPP cusp bug (#4757)**: Humble 的 RPP 缺少 cusp 检测——路径中的方向切换点 (cusp) 导致 lookahead 跳过尖角, 车辆切角进入禁区。MPPI 有 cusp 检测 (`global_plan_up_to_inversion_`), RPP 没有。修复在 main/jazzy, 未 backport 到 Humble。当前缓解: tighter lookahead + cost_penalty。

### 4.3 代价地图

| 参数 | 全局 | 局部 |
|------|------|------|
| 类型 | 全地图固定 (map系) | 3m×3m 滚动窗口 (odom系) |
| robot_footprint | 多边形 [[0.15,-0.10],[0.15,0.10],[-0.12,0.10],[-0.12,-0.10]] | 同 |
| inflation_radius | 0.12m | 0.12m |
| cost_scaling_factor | 5.0 | 5.0 |
| track_unknown_space | true | — |
| allow_unknown | false | — |
| 传感器源 | /scan + /aurora/points2 | /scan + /aurora/points2 |
| aurora_points 高度 | 0.05-0.35m, persistence=0.5s | 同 |
| 插件 | static_layer, obstacle_layer, keepout_filter, inflation_layer | obstacle_layer, keepout_filter, inflation_layer |

### 4.4 禁区系统 (话题隔离方案)

最终可靠架构——消除 TRANSIENT_LOCAL 双发布者竞态:

```
costmap_filter_info_server → /costmap_filter_info_server  (无人订阅, 死胡同)
competition_master_stage3  → /costmap_ctrl               (独占发布, TRANSIENT_LOCAL)
KeepoutFilter              ← /costmap_ctrl               (唯一订阅源)
```

- **启动重置**: competition_master `__init__` 时立即发布 redirect → `/keepout_mask`，覆盖上轮 stale 消息
- **运行时禁用**: `_disable_keepout_and_clear()` 发布 `filter_mask_topic="/keepout_disabled"` (空 mask)
- **结束时恢复**: `_finish()` / `_timeout_shutdown()` 调用 `_reenable_keepout()` 恢复正常 redirect
- `override_lethal_cost=true, lethal_override_cost=252` (MAX_NON_OBSTACLE, 可脱困但强力排斥)

### 4.5 行为树

非 infinite retries (-1), 适配动态障碍物场景。

**单目标 (navigate_to_pose_ackermann_rpp.xml)**:
- 路径计算前 ClearCostmapAroundRobot(1.5m)
- FollowPath 失败: 清局部代价地图 + Wait 0.5s
- 系统恢复: 清代价地图 + BackUp 0.8m → Wait 3s → 清代价地图 + BackUp 1.5m
- 无 Spin (阿克曼), 无 SmoothPath (Humble NaN bug #4755)

**多路点 (navigate_through_poses_ackermann_rpp.xml)**:
- RemovePassedGoals(radius=0.4m) 后重新规划
- Recovery Fallback 中 ClearCostmap 后 Wait 0.5s (传感器刷新)
- 系统级恢复中 ClearCostmap 后 Wait 0.5s

### 4.6 AMCL 定位

- 模型: DifferentialMotionModel (无原生 Ackermann 模型)
- alpha1-alpha5: 0.45 (补偿阿克曼-差分模型差异)
- 粒子: 300-1500, likelihood_field
- recovery_alpha_fast: 0.1
- 初始位姿: (-1.985, -0.014, 0.262) — 来自 Cartographer 纯定位 (1193帧, σ_xy=2-3mm)

---

## 5. STM32 串口协议

### RX 帧 (STM32 → ROS2, 24B)

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

### TX 帧 (ROS2 → STM32, 11B)

| 字节 | 字段 | Ackermann 模式 | 差速模式 |
|------|------|---------------|----------|
| 0 | Header | 0x7B | 0x7B |
| 1-2 | Reserved | 0, 0 | 0, 0 |
| 3-4 | speed | vx × 1000 | vx × 1000 |
| 5-6 | Y_speed | 0 (未使用) | vy × 1000 |
| 7-8 | steering | angle × 1000 / 2 | ω × 1000 |
| 9 | checksum | XOR(0..8) | XOR(0..8) |
| 10 | Tail | 0x7D | 0x7D |

**注意**: 构造函数中 `usart_port_name` 参数被声明但未使用——串口硬编码为 `/dev/ttyACM0`。转向编码为 `angle × 500` (STM32 端内部 ×2 恢复)。

### 里程计

```
Robot_Pos.X += 1.03 × (Vx·cosθ − Vy·sinθ) × dt
Robot_Pos.Y += 1.125 × (Vx·sinθ + Vy·cosθ) × dt
Robot_Pos.Z += Vz × dt
```

补偿系数 1.03/1.125 为编码器非线性经验校准 (硬编码, 非参数)。

---

## 6. 竞赛三阶段

### 阶段1: P点 → QR
- NavigateToPose → QR 点 (0.41, -3.17)
- 途中扫到 QR → 打印数据并停止
- 超时: 120s

### 阶段2: QR → 通道入口
- NavigateToPose → QR 点 → 扫到码
- 杀 ZBar → 等待 /qr_event (2s 超时)
- 倒车退避 (6s, vx=-0.15, wz=+2.80): 避开 keepout 致死区
- NavigateToPose → 通道入口 (0.38, -1.10)

### 阶段3: 完整赛道 (stage3_bringup, 77.3s 完赛)

**状态机**: `INIT → NAV_TO_QR → BACKING_UP → CRUISE_CHANNEL → RETURN_P → DONE`

1. **INIT**: 启动重置 keepout redirect → `/keepout_mask`, 轮询等待 Nav2 action server 就绪
2. **NAV_TO_QR**: NavigateToPose → QR 点, 扫到码 → 杀 ZBar → 等 qr_decision
3. **BACKING_UP**: 倒车退避 (6s keepalive timer, vx=-0.15, wz=+2.80)
4. **CRUISE_CHANNEL**: `_disable_keepout_and_clear()` 禁用禁区, NavigateThroughPoses 巡航:
   - 顺时针 (奇QR): entry → (0.87, 0.83) → (3.21, -1.82)
   - 逆时针 (偶QR): entry → (1.85, -2.14) → (2.01, 1.09)
5. **RETURN_P**: 触发 VLM (/sign4return=100) → 异步等待结果, NavigateToPose → P 点 (-1.985, -0.014, yaw=0.262)
6. **DONE**: `_reenable_keepout()` 恢复禁区

**全局超时**: 180s。competition_master_stage3.py 仅做 3 处最小改动 (QoS fix + disable/enable keepout + finish restore)。

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
| `stage3_bringup.launch.py` | **阶段3完整比赛 (77.3s 最优基线)** | ~19 |
| `nav_bringup.launch.py` | 标准比赛导航 (task_manager + Nav2) | ~22 |
| `stage1_bringup.launch.py` | 阶段1测试 | ~17 |
| `stage2_bringup.launch.py` | 阶段2测试 | ~18 |
| `slam_bringup.launch.py` | Cartographer 建图 | ~11 |
| `camera_all.launch.py` | QR 检测独立调试 | ~4 |
| `base_serial.launch.py` | 纯遥控底盘 | ~2 |

### 7.2 stage3_bringup 启动时序

```
t=0s  → base_minimal.launch.py (底盘+LiDAR+TF+EKF+Madgwick+BMI088+mux+PID)
t=0s  → camera_all.launch.py (Aurora930 + QR解码 + QR决策)
t=0s  → vision_ai_node (条件: racing_vision_ai 包存在)
t=1s  → nav2_minimal.launch.py (禁区 + Nav2 composition 模式)
t=4s  → competition_master_stage3.py (比赛编排主节点, start_delay=0.5s 轮询)
t=8s  → RViz2 (可视化)
```

### 7.3 Launch 依赖链

```
stage3_bringup.launch.py
  ├── base_minimal.launch.py (底盘核心, 8节点)
  │     ├── base_serial.launch.py (STM32 串口驱动)
  │     ├── lslidar_driver_node (N10 LiDAR, output='log')
  │     ├── urdf2tf.launch.py (robot_state_publisher)
  │     ├── odom2tf (条件: use_ekf=false)
  │     ├── imu_madgwick_filter.py (条件: use_ekf=true)
  │     ├── bmi088_iio_bridge.py (条件: use_bmi088=true)
  │     ├── ekf_node (双IMU/单IMU 条件选择)
  │     ├── cmd_vel_mux.py
  │     └── velocity_pid.py
  ├── camera_all.launch.py (Aurora930 + QR)
  │     ├── aurora930_launch.py (外部: deptrum-ros-driver-aurora930)
  │     ├── depth_camera_tf (static_transform_publisher)
  │     ├── qr_decoder_zbar
  │     └── qr_decision
  ├── nav2_minimal.launch.py (Nav2 composition 模式)
  │     ├── keepout 服务器 (3节点)
  │     └── Nav2 bringup_launch.py (composition=True)
  └── competition_master_stage3.py + RViz2
```

### 7.4 关键 Launch 参数

**base_minimal.launch.py**:

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `use_ekf` | true | EKF 传感器融合 (发布 odom→base_footprint TF) |
| `pub_odom_tf` | false | odom2tf 发布 TF (仅 use_ekf=false 时) |
| `use_bmi088` | true | 双IMU EKF (BMI088 为主, MPU6050 差分辅助) |

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
| originbot_nav2_rpp.yaml | originbot_navigation/param/ | Nav2 全栈: AMCL, SmacPlannerHybrid(REEDS_SHEPP), RPP, costmaps×2, smoother, velocity_smoother |
| originbot_nav2.yaml | originbot_navigation/param/ | DWA 备选: NavfnPlanner + DWB |
| ekf_dual_imu.yaml | origincar_base/config/ | EKF 双IMU: odom+imu0(BMI088)+imu1(MPU6050 diff), 15Hz, yaw noise=0.003 |
| ekf.yaml | origincar_base/config/ | EKF 单IMU: odom+imu0, 15Hz, yaw noise=0.005 |
| imu_madgwick.yaml | origincar_base/config/ | MPU6050 Madgwick: beta=0.033, 100Hz |
| imu_madgwick_bmi088.yaml | origincar_base/config/ | BMI088 Madgwick: beta=0.01, gyro_noise=0.0001, 100Hz |
| control_params.yaml | origincar_base/config/ | PID + mux: 增益、优先级、超时 |
| lsx10.yaml | lslidar_driver/params/ | N10: /dev/ttyACM1, 5Hz, 230400bps |
| lds_2d.lua | originbot_navigation/config/ | Cartographer Route B: EKF odom, max_range=8.0m |
| vision_ai_config.yaml | racing_vision_ai/config/ | 火山引擎 ARK API |
| room.yaml | originbot_navigation/maps/ | 静态地图: 163×141, 0.05m/px, origin=[-2.65, -4.5, 0] |
| keepout_mask.yaml | originbot_navigation/maps/ | 禁区掩码: 同尺寸同原点对齐 |

### 行为树

| 文件 | 用途 |
|------|------|
| navigate_to_pose_ackermann_rpp.xml | 单目标导航 BT (无 Spin, 无 SmoothPath) |
| navigate_through_poses_ackermann_rpp.xml | 多路点导航 BT (Wait 0.5s after ClearCostmap) |

### 工具脚本

| 文件 | 用途 |
|------|------|
| originbot_navigation/tools/eval_trajectory.py | 定位精度验证: PGM/PNG 对齐 → 三子图 + 误差报告 |
| originbot_navigation/tools/plot_trajectory.py | 轨迹可视化: CSV → PGM 底图 + keepout 叠加 + 速度着色 |

---

## 9. 关键约束与调参备注

### cmd_vel 流水线
5级不可绕过。调试时逐级检查话题: /cmd_vel → /nav_cmd_vel → /cmd_vel_muxed → /cmd_vel_corrected → /ackermann_cmd。cmd_vel_mux 是唯一控制瓶颈。

### Ackermann 约束
lookahead_dist ≥ 0.65m (> 2×0.30m min_turning_radius), 否则弯道冲入禁区。Nav2 odom_topic 指向原始 /odom (非 EKF 输出), 此为有意设计。use_collision_detection=false, use_rotate_to_heading=false, yaw_goal_tolerance=3.14 (PI)。

### 双IMU 增强
MPU6050 (imu0) 通过 Madgwick (beta=0.033) 提供 yaw 姿态参考 + 角速度。BMI088 (imu1, differential=true) 通过独立 Madgwick (beta=0.003) 仅提供高精度 Z 角速度增量——汽车级陀螺, 噪声约 MPU6050 的 1/10, 偏置 <2°/h。差分模式避免与 imu0 yaw 姿态冲突。bmi088_iio_bridge 手动 scale 校准 (RDK X5 IIO 无 `_scale` 文件)。双IMU 将 yaw noise 从 0.005 降至 0.003。

### 代价调控
use_collision_detection=false, 改用 cost_scaling (dist=0.12, gain=2.0)。窄通道+锥桶场景下碰撞检测频繁误触发。regulated_linear_scaling_min_radius=0.20。

### 禁区生命周期独立
keepout 由 lifecycle_manager_keepout 单独管理。两节点必须先 activate, 否则 KeepoutFilter 在 costmap configure 时收不到 /costmap_filter_info → 被丢弃。competition_master 通过 `/costmap_ctrl` (独占话题) 控制禁区开关。

### ARM 编译约束
colcon --parallel-workers 2 (超过 2 → OOM)。EKF 频率 20→15Hz (Cortex-A55 单步超 50ms 预算)。LiDAR 5Hz (默认 10Hz 降至 5Hz 省 CPU)。`cache_obstacle_heuristic: true` 会添加 ~15s 启动预计算 (ARM), 但重规划速度提升 20-40× (当前已启用)。

### 77.3s 最优基线
2026-06-14 验证的最优配置: `reverse_penalty=4.0`, `change_penalty=0.2`, `cache_obstacle_heuristic=false`, `lookup_table_size=10.0`, `inflation_radius=0.20`, `cost_scaling_factor=2.0`。当前磁盘上的未提交参数为实验性调整, 未完全验证。

### Aurora930 心跳
`heartbeat failed!!!` 每 2s 一条日志——SDK v1.1.22 与 Firmware 1.7.2 心跳协议不兼容, 数据流正常。launch 中设 `heart_enable:=false` 消除。

### 启动屏障
wait_for_odom 替代硬编码 sleep, 最长等 15s。competition_master_stage3 使用 start_delay_sec=0.5s 轮询模式 (每 0.5s 检查 Nav2 action server 就绪, 替代旧版 8s 硬编码延迟)。

### 编码器反馈
velocity_pid 依赖 /robotvel (编码器速度), 超时 0.5s 退化为开环直通。方向切换时自动积分重置 (最小间隔 250ms 防抖)。**注意**: PID 输出 /cmd_vel_corrected 当前未连接到 STM32——见已知问题。

### CRLF 部署陷阱
Windows 编辑的 .py 文件上传到 Linux 后 shebang 变为 `python3\r` → exit 127 崩溃。`.gitattributes` 已设 `*.py text eol=lf`, 但 tar/scp 传输仍需手动 `sed -i 's/\r$//'`。

### 改前确认
任何代码修改前必须先提方案、解释原因、等用户确认。禁止 git checkout/reset --hard 等破坏性操作覆盖用户文件。

### 已移除组件
USB 摄像头, YOLOv5 DNN 流水线 (hobot_usb_cam + dnn_node + websocket), racing_obstacle_detection_yolo 包。escape_maneuver/cone_react/cost_penalty tuning/toggle_filter——反复尝试后证实为定时器炸弹/竞态条件, 已全部移除。

---

## 10. 已知问题

| 问题 | 影响 | 状态 |
|------|------|------|
| **velocity_pid 输出未连接 STM32**: /cmd_vel_corrected 无订阅者, 编码器反馈闭环从未生效。origincar_base 订阅 /cmd_vel 而非 /cmd_vel_corrected, 改参数会 SIGABRT | 所有 PID 修正被静默丢弃 | 待修复 |
| **RPP Humble cusp bug (#4757)**: REEDS_SHEPP cusp 导致 lookahead 跳过尖角, 切角入禁区。MPPI 有 cusp 检测, RPP 没有, 修复在 main/jazzy 未 backport | 弯道冲入禁区风险 | Nav2 上游限制 |
| smoother_server 被 lifecycle 激活但 BT 中已移除 SmoothPath (Humble NaN bug #4755) | 空转浪费 CPU | Nav2 上游限制 |
| /dev/ttyACM0 硬编码覆盖 ROS 参数 `usart_port_name` | 移植需改源码 | 已知限制 |
| Cartographer 与 AMCL 同时运行可能 TF 冲突 | 避免同时启动 | 使用注意 |
| Aurora930 `heartbeat failed!!!` 日志噪音 | 数据正常, 设 heart_enable:=false | 已绕过 |
| vision_ai_config.yaml 含明文 API key | 安全隐患 | 待处理 |
| Mahony 积分增益为零 (Ki=0) | MPU6050 陀螺零偏未补偿, yaw 持续漂移 | 由 Madgwick+EKF 补偿 |
| QR decoder 深度过滤仅 advisory——Aurora930 depth 与 RGB 帧率不同步, depth 可能为 0mm | 深度无效时仍发布 /sign | 下游自行过滤 |
| TRANSIENT_LOCAL keepout redirect 跨 ROS2 运行持久化 | competition_master 启动时重置修复 | 已缓解 |
| origincar_base 改订阅 /cmd_vel_corrected → SIGABRT (exit -6) | 无法连接 PID 输出到 STM32 | 根因待查 |

---

## 11. 部署到机器人

```bash
# 1. 上传文件
ssh_upload → 192.168.31.59:/userdata/dev_ws/src/<pkg>/

# 2. 修复 CRLF (每次上传后必须!)
sed -i 's/\r$//' /userdata/dev_ws/src/<pkg>/*.py

# 3. 构建 (C++ ~90s, Python ~3s)
bash -c 'source /opt/ros/humble/setup.bash && cd /userdata/dev_ws && colcon build --packages-select <pkg> --parallel-workers 2'

# 4. 运行
ros2 launch origincar_bringup stage3_bringup.launch.py
```

**重要**: ROS2 从 install/ 加载资源 (maps, params, launch)。部署到 src/ 后必须 colcon build 才生效。`/userdata/ros_ws/` 是深度相机驱动工作空间, 不可修改。

---

## 12. 项目目录结构

```
src/
├── origincar/
│   ├── origincar_base/          # STM32 串口驱动 + 控制节点 (C++/Python)
│   │   ├── src/                 # C++: origincar_base_node
│   │   ├── origincar_base/      # Python: cmd_vel_to_ackermann_drive
│   │   ├── launch/              # base_serial.launch.py
│   │   └── config/              # EKF, PID, Madgwick, BMI088 YAML
│   └── origincar_bringup/       # 主启动包 + 比赛编排
│       ├── launch/              # 所有 stage/slam/nav 入口 launch
│       └── src/                 # 20+ Python 节点
├── originbot_navigation/        # Nav2 配置 + 地图 + BT + 工具
│   ├── param/                   # 导航参数 YAML
│   ├── maps/                    # room.pgm/yaml + keepout_mask.pgm/yaml
│   ├── behavior_trees/          # 行为树 XML
│   ├── config/                  # Cartographer lua
│   ├── launch/                  # cartographer + mapping
│   └── tools/                   # eval_trajectory.py + plot_trajectory.py
├── qr_decoder/                  # C++ ZBar QR 解码器
├── origincar_qr/                # Python QR 方向决策
├── racing_vision_ai/            # 火山引擎 VLM 图生文
├── Lslidar_ROS2_driver-N10_V1.0/  # Leishen N10 LiDAR 驱动
├── .learnings/                  # 经验教训 + 错误记录 (7 文件)
├── Z_MD/                        # 日志 + 工作文档
│   ├── todo.md                  # 工作规范 (新对话必读)
│   └── log.md                   # 运行日志
├── .gitattributes               # LF 行尾强制 (Python/YAML/XML/launch/sh)
└── .mcp.json                    # SSH Manager 配置 → RDK X5 (192.168.31.59)
```
