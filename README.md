# Origincar Pro — 自主驾驶 Ackermann 小车

> ROS2 Humble + RDK X5 | 全国大学生智能汽车竞赛 | 最优圈速 77.3s
> 最后更新: 2026-06-25

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

# 轨迹分析 (PC端)
python originbot_navigation/tools/plot_trajectory.py [trajectory_*.csv]
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
| IMU (板载) | BMI088 | RDK X5 I2C-1 (IIO) | 陀螺噪声 ~1/10 MPU6050, 偏置 <2°/h, **主IMU** |
| 底盘 | 阿克曼 | 276×189×150mm | wheelbase=0.143m, min_turning_radius≈0.30m, max_steer≈28° |
| 电池 | 12V 锂电池 | — | /PowerVoltage 监测 |

### 软件环境

- **OS**: Ubuntu 22.04 (ARM aarch64), Swap ≥4GB
- **ROS2**: Humble Hawksbill
- **编译**: `colcon build --parallel-workers 2`（超过 2 会 OOM）
- **Source**: `/opt/tros/humble/setup.bash` + `/opt/ros/humble/setup.bash`
- **工作空间**: `/userdata/dev_ws`
- **深度相机空间**: `/userdata/ros_ws`（不可修改）

---

## 2. 系统架构

### 2.1 分层总览

```
┌──────────────────────────────────────────────────────────────────┐
│  ORCHESTRATION   │ competition_master_stage3 (★ 当前唯一使用)      │
│                  │ [LEGACY] task_manager + mission_controller     │
├──────────────────┼────────────────────────────────────────────────┤
│  CONTROL         │ cmd_vel_mux │ velocity_pid │ pose_pid_corrector │
│                  │ cmd_vel_to_ackermann_drive                     │
├──────────────────┼────────────────────────────────────────────────┤
│  NAVIGATION      │ AMCL │ SmacPlannerHybrid(REEDS_SHEPP) │ RPP    │
│  (Nav2)          │ BT Navigator │ ConstrainedSmoother │ VelSm      │
├──────────────────┼────────────────────────────────────────────────┤
│  PERCEPTION      │ imu_madgwick (×2) │ qr_decoder (ZBar)          │
│                  │ qr_decision │ vision_ai (火山引擎 VLM)         │
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

### 2.2 完整话题拓扑（含流向）

> ★ = stage3 实际使用　　⚡ = 已废弃但仍加载　　❌ = 无人订阅

| 发布者 | 话题 | 类型 | 订阅者 | 状态 |
|--------|------|------|--------|------|
| origincar_base | /odom | Odometry | EKF, competition_master_stage3, wait_for_odom, qr_decision | ★ |
| origincar_base | /imu/data_raw | Imu | imu_madgwick_filter (MPU6050) | ★ |
| origincar_base | /robotvel | Data | velocity_pid | ★ |
| origincar_base | /PowerVoltage | Float32 | (monitoring only) | ★ |
| imu_madgwick_filter (MPU6050) | /imu/data/madgwick | Imu | EKF (imu0, yaw姿态 + 角速度) | ★ |
| bmi088_iio_bridge | /imu_data | Imu | imu_madgwick_filter (BMI088) | ★ |
| imu_madgwick_filter (BMI088) | /imu/data/bmi088_madgwick | Imu | EKF (imu1, differential, 仅角速度) | ★ |
| EKF | /odometry/filtered | Odometry | cartographer (建图时) | ★ |
| EKF | TF: odom→base_footprint | — | 全局 | ★ |
| lslidar_driver | /scan | LaserScan | AMCL, costmaps×2 | ★ |
| aurora930 | /aurora/rgb/image_raw | Image | qr_decoder_zbar, vision_ai_node | ★ |
| aurora930 | /aurora/depth/image_raw | Image | qr_decoder_zbar | ★ |
| aurora930 | /aurora/points2 | PointCloud2 | costmaps×2 | ★ |
| AMCL | TF: map→odom | — | 全局导航栈 | ★ |
| AMCL | /amcl_pose | PoseWithCovariance | competition_master_stage3 | ★ |
| qr_decoder_zbar | /sign | String | qr_decision, competition_master_stage3 | ★ |
| qr_decision | /qr_event | String | competition_master_stage3 | ★ |
| velocity_smoother | /cmd_vel → /nav_cmd_vel | Twist | cmd_vel_mux | ★ |
| pose_pid_corrector | /pid_cmd_vel | Twist | cmd_vel_mux | ⚡ |
| competition_master_stage3 | /stop_cmd_vel | Twist | cmd_vel_mux | ★ |
| cmd_vel_mux | /cmd_vel_muxed | Twist | velocity_pid, competition_master_stage3 (diag) | ★ |
| velocity_pid | /cmd_vel_corrected | Twist | cmd_vel_to_ackermann_drive | ★ |
| cmd_vel_to_ackermann | /ackermann_cmd | AckermannDrive | origincar_base | ★ |
| competition_master_stage3 | /costmap_ctrl | CostmapFilterInfo | KeepoutFilter (QoS: TRANSIENT_LOCAL) | ★ |
| competition_master_stage3 | /sign4return | Int32 | vision_ai_node | ★ |
| vision_ai_node | /vlm_result | String | competition_master_stage3 | ★ |
| planner_server | /plan | Path | competition_master_stage3 (diag) | ★ |
| costmap_filter_info_server | /costmap_filter_info_server | CostmapFilterInfo | ❌ 无人订阅 | ⚡ |

### 2.3 TF 树 (REP-105)

```
map
  │  AMCL (导航) 或 Cartographer (建图)
  v
odom
  │  EKF (publish_tf=true)
  v
base_footprint
  ├── base_link (static, z=+0.07m, URDF)
  │     ├── laser_link (URDF static, z=+0.075m)
  │     └── depth_camera_link (static, x=+0.14m, z=+0.05m)
  └── gyro_link (URDF static, 与 base_footprint 同原点)
```

**关键**: odom→base_footprint 必须恰好一个发布者（EKF 或 odom2tf 互斥）。

| 模式 | odom→base_footprint 来源 | use_ekf | pub_odom_tf |
|------|--------------------------|---------|-------------|
| 比赛导航 | EKF | true | false |
| 纯遥控/无EKF | odom2tf | false | true |
| Cartographer 建图 | EKF | true | false |

---

## 3. 软件清单

### 3.1 生产节点（stage3 实际使用） ★

| 节点 | 文件 | 语言 | 职责 |
|------|------|------|------|
| `origincar_base` | origincar_base.cpp | C++ | STM32 串口桥接：发布 /odom, /imu/data_raw, /robotvel, /PowerVoltage；订阅 /ackermann_cmd |
| `lslidar_driver_node` | lslidar_driver | C++ | N10 LiDAR 5Hz → /scan (frame=laser_link) |
| `cmd_vel_to_ackermann_drive` | origincar_base/scripts/ | Python | Twist → AckermannDriveStamped (wheelbase=0.143, steering_sign=-1) |
| `cmd_vel_mux` | origincar_bringup/src/ | Python | 3输入优先级多路复用器 (nav=10, pid=20, stop=255), 30Hz |
| `velocity_pid` | origincar_bringup/src/ | Python | 增量式 PID 速度闭环 (30Hz), 编码器反馈, 方向切换积分重置 |
| `imu_madgwick_filter` (×2) | origincar_bringup/src/ | Python | Madgwick 6-DOF AHRS, MPU6050 beta=0.033, BMI088 beta=0.003 @100Hz |
| `bmi088_iio_bridge` | origincar_bringup/src/ | Python | BMI088 Linux IIO → /imu_data (100Hz, 手动 scale 校准) |
| `wait_for_odom` | origincar_bringup/src/ | Python | 启动屏障：等待 /odom 就绪 (最长15s) |
| `competition_master_stage3` | origincar_bringup/src/ | Python | **★ 主控制器**: 状态机编排, CSV 轨迹记录, 禁区控制 |
| `qr_decoder_zbar` | qr_decoder/src/ | C++ | ZBar QR 解码 + 多尺度扫描 → /sign, /sign_pose |
| `qr_decision` | origincar_qr/ | Python | QR 方向决策：奇数→顺时针, 偶数→逆时针, 3s 冷却 |
| `vision_ai_node` | racing_vision_ai/ | Python | VLM 图生文：/sign4return 触发 → 火山引擎 ARK API |

### 3.2 Nav2 基础设施（composition 模式）

| 节点 | 包 | 职责 |
|------|-----|------|
| `ekf_filter_node` | robot_localization | 双IMU融合: /odom + imu0(BMI088) + imu1(MPU6050 diff) → /odometry/filtered + odom→base_footprint TF |
| `amcl` | nav2_amcl | 粒子滤波定位: /scan + /map → map→odom TF |
| `map_server` | nav2_map_server | 静态地图 (room.yaml) |
| `planner_server` | nav2 | SmacPlannerHybrid 全局规划器 (REEDS_SHEPP) |
| `controller_server` | nav2 | RegulatedPurePursuit 局部控制器 (10Hz) |
| `bt_navigator` | nav2 | 行为树执行器 (BT loop=10Hz) |
| `behavior_server` | nav2 | 恢复行为 (BackUp + Wait + DriveOnHeading, 无Spin) |
| `global_costmap` / `local_costmap` | nav2 | 代价地图, 含 keepout_filter |
| `velocity_smoother` | nav2 | 速度平滑 (OPEN_LOOP, 20Hz) |
| `smoother_server` | nav2 | 路径平滑 (ConstrainedSmoother) ⚠️ BT 中已移除但 lifecycle 仍激活 |
| `waypoint_follower` | nav2 | 路点跟随 (WaitAtWaypoint, 200ms) |
| `keepout_mask_server` | nav2_map_server | 禁区代价地图 → /keepout_mask |
| `keepout_filter_info_server` | nav2_map_server | ❌ 禁区过滤器元数据 → /costmap_filter_info_server (无人订阅) |
| `lifecycle_manager_navigation` | nav2_lifecycle_manager | Nav2 标准生命周期 |
| `lifecycle_manager_keepout` | nav2_lifecycle_manager | 禁区节点独立生命周期 |

### 3.3 ⚡ 遗留/未使用节点

| 节点 | 文件 | 状态 | 说明 |
|------|------|------|------|
| `task_manager` | origincar_bringup/src/ | ⚡ 遗留 | 5态竞赛状态机, 被 competition_master_stage3 替代 |
| `mission_controller` | origincar_bringup/src/ | ⚡ 遗留 | 执行 /mission_cmd, 被 competition_master_stage3 内联替代 |
| `competition_lifecycle_manager` | origincar_bringup/src/ | ⚡ 遗留 | Nav2 运行时参数切换, 当前未使用 |
| `competition_master_stage1` | origincar_bringup/src/ | ⚡ 遗留 | 阶段1独立控制器, 被 stage3 覆盖 |
| `competition_master_stage2` | origincar_bringup/src/ | ⚡ 遗留 | 阶段2独立控制器, 被 stage3 覆盖 |
| `pose_pid_corrector` | origincar_bringup/src/ | ⚡ 未使用 | 末端精确停车 PID, 当前 stage3 流程中未激活 |
| `calibrate_gui` | origincar_bringup/src/ | ⚡ 工具 | 手动路点/禁区标定 GUI (PC端 matplotlib) |
| `calibrate_p_point` | origincar_bringup/src/ | ⚡ 工具 | 自动 P点标定 + 锥桶测量 |
| `telemetry_recorder` | origincar_bringup/src/ | ⚡ 被替代 | 5Hz CSV 遥测记录器 → `/tmp/telemetry.csv`，被 competition_master 内建 CSV (14列, 带时间戳) 替代 |
| `image_transport_node` | origincar/utils/src/ | ⚡ 遗留 | RDK X5 NV12→BGR 图像格式转换 (硬件共享内存→标准 ROS Image)，与已移除的 YOLO DNN 流水线配套 |
| `odom2tf` | origincar_bringup/src/ | ⚡ 备选 | 发布 odom→base_footprint TF, 仅 use_ekf=false 时 |

### 3.4 已移除的组件（不复存在）

- USB 摄像头 + YOLOv5 DNN 流水线 (hobot_usb_cam + dnn_node + websocket)
- racing_obstacle_detection_yolo 包
- escape_maneuver / cone_react / cost_penalty tuning / toggle_filter（定时器炸弹/竞态条件）

---

## 4. 控制流水线

### 4.1 cmd_vel 5级流水线

```
Nav2 RPP → velocity_smoother (20Hz OPEN_LOOP) → /cmd_vel
  → [remap] → /nav_cmd_vel (p=10, timeout=0.5s) ──────────────┐
pose_pid_corrector → /pid_cmd_vel (p=20, timeout=0.3s) ────────┤ [未激活]
competition_master → /stop_cmd_vel (p=255, 零值 Twist) ───────┤
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

**velocity_pid 参数**: Kp_vx=0.8, Ki_vx=0.60, Kd_vx=0.05, max_i=0.68。Kp_wz=1.0, Ki_wz=0.40, Kd_wz=0.02, max_i=2.24。方向切换时积分自动重置 (最小间隔 250ms)。

> ⚠️ **已知问题**: velocity_pid 输出到 `/cmd_vel_corrected`, 但 origincar_base 实际订阅 `/cmd_vel` (通过 `cmd_vel` 参数)。PID 修正被静默丢弃——编码器反馈闭环从未生效。修改 origincar_base 订阅目标会导致 SIGABRT 崩溃 (exit -6), 根因待查。

### 4.2 双IMU姿态融合

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

> **BMI088 角色**: 汽车级陀螺, 噪声 ~1/10 MPU6050, 偏置 <2°/h。bmi088_iio_bridge 手动 scale 校准 (RDK X5 IIO 无 `_scale` 文件): gyro_scale=0.00053 rad/s, accel_scale=0.00341 m/s²。

EKF 频率 20→15Hz（Cortex-A55 单步执行 117-134ms, 超出 50ms 预算）。

---

## 5. Nav2 导航配置

### 5.1 全局规划器 — SmacPlannerHybrid (REEDS_SHEPP)

| 参数 | 磁盘值 | 说明 |
|------|--------|------|
| motion_model | REEDS_SHEPP | 前进+倒退, 适应 Ackermann 窄空间 |
| minimum_turning_radius | 0.30m | wheelbase=0.143m, max_steer≈28° |
| max_iterations | 1500 | Cortex-A55 硬限制 |
| max_on_approach_iterations | 300 | 接近目标时的迭代上限 |
| max_planning_time | 1.5s | 快速失败以便重试 |
| angle_quantization_bins | 48 | ARM 优化 (默认72) |
| downsample_costmap | true | 2×降采样 |
| lookup_table_size | 20.0 | 运动基元查找表 |
| analytic_expansion_ratio | 3.0 | |
| analytic_expansion_max_length | 1.5m | |
| analytic_expansion_max_cost | 150.0 | |
| cache_obstacle_heuristic | true | 缓存静态代价图, 重规划 20-40× 加速 |
| reverse_penalty | 2.0 | 抑制路点倒车 (官方推荐 1.3-5.0) |
| change_penalty | 0.10 | 方向切换惩罚 (官方推荐 0.0-0.3) |
| cost_penalty | 4.0 | 代价图惩罚系数 |
| non_straight_penalty | 1.3 | 非直线惩罚 |
| smooth_path | true | 内建平滑 |
| allow_unknown | false | |

> ⚠️ 磁盘 YAML 使用 `reverse_penalty=2.0, change_penalty=0.10`。已验证 77.3s 基线使用 `reverse_penalty=4.0, change_penalty=0.20`——见 §14。

### 5.2 局部控制器 — RegulatedPurePursuit

> ⚠️ 下表中的值来自磁盘上的 `originbot_nav2_rpp.yaml`。**已验证最优基线 (77.3s)** 的参数可能不同——详见 §14 "参数分歧"。

| 参数 | 磁盘值 | 说明 |
|------|--------|------|
| desired_linear_vel | 0.50m/s | 直线巡航速度 |
| max_linear_vel | 0.60m/s | 硬上限 |
| min_linear_vel | -0.30m/s | 允许倒车 |
| max_angular_vel | 2.00rad/s | |
| lookahead_dist | 0.65m | ≥2×min_turning_radius(0.60m) |
| min_lookahead_dist | 0.30m | |
| max_lookahead_dist | 0.90m | |
| lookahead_time | 1.2s | |
| curvature_lookahead_dist | 0.80m | fixed curvature mode |
| use_velocity_scaled_lookahead_dist | true | |
| use_fixed_curvature_lookahead | true | |
| use_regulated_linear_velocity_scaling | true | |
| regulated_linear_scaling_min_radius | 0.30m | |
| regulated_linear_scaling_min_speed | 0.18m/s | |
| use_cost_regulated_linear_velocity_scaling | true | |
| cost_scaling_dist | 0.12m | |
| cost_scaling_gain | 2.0 | |
| inflation_cost_scaling_factor | 5.0 | |
| use_collision_detection | false | 窄道误触发 |
| min_approach_linear_velocity | 0.10m/s | |
| approach_velocity_scaling_dist | 0.80m | |
| allow_reversing | true | REEDS_SHEPP 后退机动 |
| use_rotate_to_heading | false | 阿克曼必须关闭 |
| use_interpolation | true | |
| goal_tolerance.xy | 0.20m | |
| goal_tolerance.yaw | 3.14rad | PI，跳过朝向检查 |
| max_robot_pose_search_dist | -1.0 | 无限回溯 |
| transform_tolerance | 0.2s | |

### 5.3 代价地图

> ⚠️ 磁盘 YAML 中 `inflation_radius=0.55` / `cost_scaling_factor=2.0`。已验证 77.3s 基线使用 `inflation_radius=0.20` / `cost_scaling_factor=2.0`——见 §14。

| 参数 | 全局 | 局部 |
|------|------|------|
| 类型 | 全地图固定 (map系) | 3m×3m 滚动窗口 (odom系) |
| update/publish 频率 | 1.0Hz / 1.0Hz | 5.0Hz / 2.0Hz |
| robot_footprint | 多边形 [[0.15,-0.10],[0.15,0.10],[-0.12,0.10],[-0.12,-0.10]] | 同 |
| inflation_radius | 0.55m | 0.55m |
| cost_scaling_factor | 2.0 | 2.0 |
| track_unknown_space | true | — |
| transform_tolerance | 0.5s | — |
| 传感器源 | /scan + /aurora/points2 | /scan + /aurora/points2 |
| aurora_points: max_obstacle_height | 0.35m | 0.35m |
| aurora_points: min_obstacle_height | 0.05m | 0.05m |
| aurora_points: obstacle_range | 3.5m | 3.5m |
| aurora_points: persistence | 0.5s | 0.5s |
| 插件 | static_layer, obstacle_layer, keepout_filter, inflation_layer | obstacle_layer, keepout_filter, inflation_layer |

### 5.4 禁区系统（话题隔离方案）

```
competition_master_stage3  → /costmap_ctrl (独占发布, TRANSIENT_LOCAL)
KeepoutFilter              ← /costmap_ctrl (唯一订阅源)
costmap_filter_info_server → /costmap_filter_info_server (❌ 死胡同, 无人订阅)
```

- **启动重置**: `__init__` 时立即发布 redirect → `/keepout_mask`，覆盖上轮 stale 消息
- **运行时禁用**: `_disable_keepout_and_clear()` 发布空 mask (`filter_mask_topic="/keepout_disabled"`)
- **结束时恢复**: `_finish()` / `_timeout_shutdown()` 调用 `_reenable_keepout()`
- `override_lethal_cost=true, lethal_override_cost=252` (MAX_NON_OBSTACLE, 可脱困但强力排斥)

### 5.5 行为树

**单目标** (`navigate_to_pose_ackermann_rpp.xml`):
- ClearCostmapAroundRobot(1.5m) before path computation
- FollowPath 失败: 清局部代价地图 + Wait 0.5s
- 系统恢复: 清代价地图 + BackUp 0.8m → Wait 3s → BackUp 1.5m
- 无 Spin (阿克曼), 无 SmoothPath (Humble NaN bug #4755)

**多路点** (`navigate_through_poses_ackermann_rpp.xml`):
- RemovePassedGoals(radius=0.4m) 后重新规划
- Recovery 中 ClearCostmap 后 Wait 0.5s (传感器刷新)

**DWA 备选** (`navigate_to_pose_ackermann_dwa.xml`): ⚡ 存在但未使用

### 5.6 AMCL 定位

- 模型: DifferentialMotionModel (无原生 Ackermann 模型)
- alpha1-alpha5: 0.45 (补偿阿克曼-差分模型差异)
- 粒子: 300-1500, likelihood_field
- recovery_alpha_fast: 0.1
- 初始位姿: (-1.985, -0.014, 0.262) — Cartographer 纯定位 (1193帧, σ_xy=2-3mm)

---

## 6. STM32 串口协议

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

**注意**: 构造函数中 `usart_port_name` 参数声明但未使用——串口硬编码为 `/dev/ttyACM0`。

### 里程计

```
Robot_Pos.X += 1.03 × (Vx·cosθ − Vy·sinθ) × dt
Robot_Pos.Y += 1.125 × (Vx·sinθ + Vy·cosθ) × dt
Robot_Pos.Z += Vz × dt
```

补偿系数 1.03/1.125 为编码器非线性经验校准 (硬编码, 非参数)。

---

## 7. 竞赛三阶段

### 阶段1: P点 → QR
- NavigateToPose → QR 点 (0.41, -3.17), 超时 120s
- 途中扫到 QR → 打印数据并停止

### 阶段2: QR → 通道入口
- NavigateToPose → QR → 扫到码 → 杀 ZBar → 等 qr_decision (2s)
- 倒车退避 (6s, vx=-0.15, wz=+2.80): 避开 keepout 致死区
- NavigateToPose → 通道入口 (0.38, -1.10)

### 阶段3: 完整赛道 ★ (77.3s 完赛)

**状态机**: `INIT → NAV_TO_QR → BACKING_UP → CRUISE_CHANNEL → RETURN_P → DONE`

| 状态 | 动作 | 超时 |
|------|------|------|
| INIT | 重置 keepout → /keepout_mask, 轮询 Nav2 action server | 0.5s 轮询 |
| NAV_TO_QR | NavigateToPose → QR 点 (0.41, -3.17) | 90s |
| BACKING_UP | 倒车退避 (vx=-0.15, wz=+0.80, 6s keepalive) | 6s |
| CRUISE_CHANNEL | 禁用禁区, NavigateThroughPoses 巡航 | 180s |
| RETURN_P | 触发 VLM → NavigateToPose → P 点 (-1.985, -0.014, yaw=0.262) | 120s |
| DONE | 恢复禁区, 停车, 保存 CSV | — |

**全局超时**: 180s

**巡航路径**:
- 顺时针 (奇QR): entry → (0.82, 0.56) → (2.23, 0.77) → VLM@(3.12, -1.34)
- 逆时针 (偶QR): entry → (1.73, -1.98) → (3.10, -1.35) → VLM@(2.10, 0.92, yaw=0.907)

**CSV 轨迹记录** (v2, 2026-06-25):
- 14列丰富数据: `elapsed_s, x_m, y_m, yaw_rad, state, cmd_vx, cmd_wz, plan_pts, plan_len_m, plan_end_x, plan_end_y, cpu_pct, mem_pct, cpu_temp_c`
- 文件名带时间戳: `trajectory_YYYYMMDD_HHMMSS.csv`
- 任何退出方式都保存: 正常完成/超时/Ctrl+C/异常崩溃
- 额外生成摘要 JSON: `trajectory_*_summary.json`

### lifecycle_manager 模式参数 (遗留, 当前未使用)

| 参数 | task1 | task2 | task3 |
|------|-------|-------|-------|
| inflation_radius | 0.18 | 0.12 | 0.18 |
| obstacle_range | 5.0 | 1.5 | 5.0 |
| desired_linear_vel | 0.70 | 0.40 | 0.70 |
| max_linear_vel | 0.80 | 0.50 | 0.80 |

---

## 8. Launch 文件

### 8.1 入口总览

| Launch 文件 | 用途 | 节点数 | 状态 |
|------------|------|--------|------|
| `stage3_bringup.launch.py` | **阶段3完整比赛 (77.3s 最优基线)** | ~19 | ★ 主用 |
| `stage1_bringup.launch.py` | 阶段1测试 | ~17 | 测试 |
| `stage2_bringup.launch.py` | 阶段2测试 | ~18 | 测试 |
| `slam_bringup.launch.py` | Cartographer 建图 | ~11 | 建图 |
| `camera_all.launch.py` | QR 检测独立调试 | ~4 | 调试 |
| `base_minimal.launch.py` | 底盘+LiDAR+TF+EKF+mux+PID | ~10 | 核心 |
| `base_serial.launch.py` | 纯遥控底盘 | ~2 | 遥控 |
| `nav2_minimal.launch.py` | Nav2 composition (禁区+导航) | ~8 | 核心 |
| `nav_bringup.launch.py` | 标准比赛导航 (task_manager) | ~22 | ⚡ 遗留 |
| `bringup.launch.py` | 旧版全栈启动 | ~20 | ⚡ 遗留 |
| `occupancy_grid.launch.py` | 占据栅格建图 | ~3 | 建图 |
| `usb_websocket_display.launch.py` | USB摄像头WebSocket显示 | ~3 | ⚡ 废弃 |
| `nav2_manual_check.launch.py` | Nav2 手动检查 | ~2 | ⚡ 工具 |
| `odom_ekf.launch.py` | 独立 EKF 启动 | ~2 | 调试 |
| `cartographer.launch.py` | Cartographer SLAM | ~6 | 建图 |

### 8.2 stage3_bringup 启动时序

```
t=0s  → base_minimal.launch.py (底盘+LiDAR+TF+EKF+Madgwick+BMI088+mux+PID)
t=0s  → camera_all.launch.py (Aurora930 + QR解码 + QR决策)
t=0s  → vision_ai_node (条件: racing_vision_ai 包存在)
t=1s  → nav2_minimal.launch.py (禁区 + Nav2 composition)
t=4s  → competition_master_stage3.py (主编排器, start_delay=0.5s 轮询)
t=8s  → RViz2
```

### 8.3 Launch 依赖链

```
stage3_bringup.launch.py
  ├── base_minimal.launch.py
  │     ├── base_serial.launch.py (STM32 串口)
  │     ├── lslidar_driver_node (N10, output='log')
  │     ├── urdf2tf.launch.py (robot_state_publisher)
  │     ├── odom2tf (条件: use_ekf=false)
  │     ├── imu_madgwick_filter.py (条件: use_ekf=true)
  │     ├── bmi088_iio_bridge.py (条件: use_bmi088=true)
  │     ├── ekf_node (双IMU/单IMU 条件)
  │     ├── cmd_vel_mux.py
  │     └── velocity_pid.py
  ├── camera_all.launch.py
  │     ├── aurora930 (外部: deptrum-ros-driver)
  │     ├── depth_camera_tf (static_transform_publisher)
  │     ├── qr_decoder_zbar
  │     └── qr_decision
  ├── nav2_minimal.launch.py
  │     ├── keepout 服务器 (3节点)
  │     └── Nav2 bringup (composition=True)
  └── competition_master_stage3.py + RViz2
```

### 8.4 关键 Launch 参数

**base_minimal.launch.py**:

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `use_ekf` | true | EKF 传感器融合 |
| `pub_odom_tf` | false | odom2tf 发布 TF (仅 use_ekf=false) |
| `use_bmi088` | true | 双IMU EKF (BMI088 为主) |

**camera_all.launch.py**:

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `depth_cam_x/y/z` | 0.14/0.0/0.05 | 相机偏移 (m) |
| `depth_min_mm` | 50 | QR 深度过滤下限 |
| `depth_max_mm` | 4000 | QR 深度过滤上限 |

---

## 9. 配置文件索引

| 文件 | 位置 | 用途 | 状态 |
|------|------|------|------|
| `originbot_nav2_rpp.yaml` | originbot_navigation/param/ | **★ 主配置**: AMCL, SmacPlannerHybrid, RPP, costmaps, smoother, velocity_smoother | ★ 主用 |
| `originbot_nav2.yaml` | originbot_navigation/param/ | DWA 备选: NavfnPlanner + DWB | ⚡ 备选 |
| `ekf_dual_imu.yaml` | origincar_base/config/ | **★ 双IMU EKF**: odom+imu0(BMI088)+imu1(MPU6050 diff), 15Hz | ★ 主用 |
| `ekf.yaml` | origincar_base/config/ | 单IMU EKF: odom+imu0, 15Hz | 备选 |
| `ekf.yaml` | originbot_navigation/config/ | ⚠️ **重复**: 与 origincar_base/config/ekf.yaml 内容不同的副本 | ❓ 冗余 |
| `imu_madgwick.yaml` | origincar_base/config/ | MPU6050 Madgwick: beta=0.033, 100Hz | ★ |
| `imu_madgwick_bmi088.yaml` | origincar_base/config/ | BMI088 Madgwick: beta=0.003, gyro_noise=0.0002, 100Hz | ★ |
| `bmi088_imu.yaml` | origincar_base/config/ | BMI088 IIO 配置: gyro_scale=0.00053, accel_scale=0.00341 | ★ |
| `imu.yaml` | origincar_base/config/ | 通用 IMU 参数 | ❓ 用途待确认 |
| `control_params.yaml` | origincar_base/config/ | PID + mux: 增益、优先级、超时 | ★ |
| `lsx10.yaml` | lslidar_driver/params/ | N10 LiDAR: /dev/ttyACM1, 5Hz, 230400bps | ★ |
| `lds_2d.lua` | originbot_navigation/config/ | Cartographer Route B: EKF odom, max_range=8.0m | 建图 |
| `vision_ai_config.yaml` | racing_vision_ai/config/ | 火山引擎 ARK API ⚠️ 含明文 API key | ★ |

### 行为树

| 文件 | 用途 | 状态 |
|------|------|------|
| `navigate_to_pose_ackermann_rpp.xml` | 单目标导航 (无 Spin, 无 SmoothPath) | ★ |
| `navigate_through_poses_ackermann_rpp.xml` | 多路点导航 (Wait 0.5s after ClearCostmap) | ★ |
| `navigate_to_pose_ackermann_dwa.xml` | DWA 控制器备选 | ⚡ 未使用 |

### 工具脚本

| 文件 | 用途 |
|------|------|
| `originbot_navigation/tools/eval_trajectory.py` | 定位精度验证: PGM/PNG 对齐 → 三子图 + 误差报告 |
| `originbot_navigation/tools/plot_trajectory.py` | 轨迹分析: CSV → 地图叠加 + 速度/规划/资源 4面板图 |

---

## 10. 部署

```bash
# 1. 上传
ssh_upload → 192.168.31.59:/userdata/dev_ws/src/<pkg>/

# 2. 修复 CRLF (每次上传后必须!)
sed -i 's/\r$//' /userdata/dev_ws/src/<pkg>/*.py

# 3. 构建 (C++ ~90s, Python ~3s)
bash -c 'source /opt/ros/humble/setup.bash && cd /userdata/dev_ws && \
  colcon build --packages-select <pkg> --parallel-workers 2'

# 4. 运行
ros2 launch origincar_bringup stage3_bringup.launch.py

# 5. 轨迹分析 (拉回PC后)
python originbot_navigation/tools/plot_trajectory.py
python originbot_navigation/tools/plot_trajectory.py trajectory_20260625_143022.csv
python originbot_navigation/tools/plot_trajectory.py --list
```

**重要**: ROS2 从 install/ 加载资源 (maps, params, launch)。部署到 src/ 后必须 colcon build。

---

## 11. 已知问题

| # | 问题 | 影响 | 状态 |
|---|------|------|------|
| 1 | **velocity_pid→STM32 断连**: /cmd_vel_corrected 无人订阅, origincar_base 读 `/cmd_vel` 参数硬订阅, 改参 SIGABRT | 编码器反馈闭环从未生效 | 根因待查 |
| 2 | **RPP Humble cusp 子 bug (#5098)**: cusp 检测 **存在** (`findVelocitySignChange`) 但不约束 `curvature_lookahead_dist` (仅约束 `lookahead_dist`)。`use_fixed_curvature_lookahead=true` 时曲率计算越过 cusp → 错误转向 | DIR_SWITCH 振荡 | 设 `use_fixed_curvature_lookahead: false` 绕过 |
| 3 | **smoother_server 空转**: lifecycle 激活但 BT 中已移除 SmoothPath (Humble NaN #4755) | 浪费 CPU | 可从 lifecycle 移除 |
| 4 | **keepout_filter_info_server 死胡同**: 发布到 /costmap_filter_info_server, 无人订阅 | 浪费 1 进程 | 可移除 |
| 5 | `/dev/ttyACM0` 硬编码: `usart_port_name` 参数声明但未使用 | 移植需改源码 | 已知限制 |
| 6 | Aurora930 `heartbeat failed!!!` 日志噪音 | 数据正常, 已设 heart_enable:=false | 已绕过 |
| 7 | vision_ai_config.yaml 含明文 API key | 安全隐患 | 待处理 |
| 8 | MPU6050 Mahony Ki=0: 陀螺零偏未补偿 | yaw 漂移, 由 Madgwick+EKF 补偿 | 双IMU缓解 |
| 9 | QR decoder 深度过滤 advisory only: depth 与 RGB 帧率不同步 | 深度无效时仍发布 /sign | 下游自行过滤 |
| 10 | TRANSIENT_LOCAL keepout 跨运行持久化 | competition_master 启动重置修复 | 已缓解 |
| 11 | Cartographer 与 AMCL 同时运行 TF 冲突 | 避免同时启动 | 使用注意 |
| 12 | colcon --parallel-workers >2 → OOM | 构建限制 | ARM 约束 |

---

## 12. 架构审计

### 12.1 冗余组件 ⚠️

| 冗余 | 详情 | 建议 |
|------|------|------|
| **task_manager + mission_controller** | 被 competition_master_stage3 完全替代, 但仍存在于代码库, nav_bringup 还在用 | 删除或标记为 legacy-only |
| **competition_master_stage1/2** | 功能被 stage3 覆盖, 标记 legacy 但未清理 | 可删除, stage3 可独立跑 stage1/2 |
| **competition_lifecycle_manager** | 运行时参数切换, 当前流程未使用 | 删除或集成到 stage3 |
| **pose_pid_corrector** | 末端精确停车 PID, 当前未激活, 但 launch 中仍加载 | 从 base_minimal 移除或修复激活 |
| **telemetry_recorder** | CSV 遥测记录器, 被 competition_master 内建 CSV 替代 | 删除 |
| **ekf.yaml ×2** | `origincar_base/config/` 和 `originbot_navigation/config/` 各有一份, 内容不同 | 合并, 保留 origincar_base 版本 |
| **smoother_server** | lifecycle 激活但 BT 中 SmoothPath 已移除 | 从 lifecycle_manager 配置中移除 |
| **keepout_filter_info_server** | 发布无人订阅的 /costmap_filter_info_server | 移除, 仅保留 keepout_mask_server |
| **DWA 配置+BT** | originbot_nav2.yaml + navigate_to_pose_ackermann_dwa.xml | 备选保留或清理 |
| **image_transport_node** | YOLO DNN 流水线残留 | 删除 |
| **usb_websocket_display.launch.py** | USB 摄像头 WebSocket 显示, 硬件已移除 | 删除 |
| **双 Madgwick 实例** | MPU6050 + BMI088 各跑一个 Madgwick, EKF 仅用 BMI088 角速度 | 可考虑: 如果 MPU6050 Madgwick 的 yaw 姿态也没用, 则可移除该实例 |
| **bringup.launch.py / nav_bringup.launch.py** | 旧版启动入口, 使用 task_manager 架构 | 清理或统一到 stage3_bringup |

### 12.2 缺失能力 ❌

| 缺失 | 影响 | 建议 |
|------|------|------|
| **无动态障碍物处理** | 通道内遇到动态障碍物无规避能力 | 添加 costmap 动态层或简单 stop-and-wait |
| **无电池安全关机** | 低电压时无自动回 P 点/停机 | battery_safety_monitor 曾存在但已移除, 需恢复 |
| **无运行时可视化反馈** | 无法在 RViz 外监控状态 | competition_master 已有 diag log, 可加 /diagnostics |
| **无自动重跑** | 失败后需手动重启 | 添加 watchdog + auto-restart |
| **VLM 结果无超时处理** | 火山引擎 API 挂掉时 VLM 永远不返回 | 添加 VLM 超时 fallback |
| **QR 无重试机制** | 扫不到码直接走回退方向, 无第二次机会 | 在原地微调位姿后重扫 |
| **编码器反馈闭环缺失** | PID 修正被静默丢弃 (已知问题 #1) | 修复 origincar_base 订阅 /cmd_vel_corrected |
| **无仿真环境** | 所有调参在真车上, 迭代慢 | WSL Nav2 离线仿真方案 (已有文档) 可扩展 |
| **无 CI/自动化测试** | 每次改参数需手动跑完整赛道 | 添加 rosbag 回放 + 参数扫描脚本 |
| **轨迹分析无自动化** | CSV 手动拉到 PC 分析 | 添加 analysis cron: 每次跑完自动生成图表 |
| **无配置版本管理** | 参数修改无记录, 回滚困难 | git tag 每次验证通过的配置 |

### 12.3 架构优化路线图

**短期 (1-2天, 低风险)**:
1. 清理冗余节点: 删除 telemetry_recorder, 移除 smoother_server 和 keepout_filter_info_server lifecycle 激活
2. 合并重复配置: 统一 ekf.yaml
3. 修复 RETURN_P timeout 保存 CSV ✅ (已完成)
4. 移除 vision_ai_config.yaml 明文 key, 改用环境变量

**中期 (3-5天, 需测试)**:
1. 修复 velocity_pid→STM32 断连 (已知问题 #1, 需调查 SIGABRT 根因)
2. 精简 launch: 条件加载 legacy 节点
3. 添加电池安全监控恢复
4. 添加 VLM 超时 fallback
5. 统一所有 stage1/2/3 到 competition_master_stage3 (参数化阶段选择)

**长期 (1-2周, 需重测试)**:
1. WSL 离线仿真完善 (Nav2 + rosbag 回放)
2. 自动化参数扫描 (grid search on key params)
3. 添加 rosbag 录制 + 自动分析 pipeline
4. 升级到 Nav2 Jazzy (获得完整 cusp 修复, 解决已知问题 #2)
5. 代码重构: competition_master 拆分为独立的状态机库 + 场景配置

---

## 13. 项目目录结构

```
src/
├── origincar/                          # 底盘包
│   ├── origincar_base/                 # STM32 串口驱动 + 基础控制
│   │   ├── src/                        # C++: origincar_base_node, Quaternion_Solution
│   │   ├── scripts/                    # Python: cmd_vel_to_ackermann_drive.py
│   │   ├── launch/                     # base_serial, ekf, robot_mode_description
│   │   └── config/                     # EKF, PID, Madgwick, BMI088 YAML
│   ├── origincar_bringup/              # 主启动包 + 比赛编排 ★
│   │   ├── launch/                     # 15 个 launch 文件 (stage1-3, slam, nav, camera...)
│   │   └── src/                        # 18 个 Python 节点
│   ├── origincar_description/          # URDF/XACRO 机器人模型
│   ├── origincar_msg/                  # 自定义 ROS2 消息 (当前空)
│   ├── utils/src/                      # image_transport_node (⚡ 遗留)
│   └── 3rdparty/                       # ackermann_msgs + serial 第三方包
├── originbot_navigation/               # Nav2 配置 + 地图 + BT
│   ├── param/                          # originbot_nav2_rpp.yaml (★主用) + nav2.yaml (备选)
│   ├── maps/                           # room.pgm/yaml + keepout_mask.pgm/yaml (163×141, 0.05m/px)
│   ├── behavior_trees/                 # 3 个 BT XML (rpp×2 + dwa×1)
│   ├── config/                         # Cartographer lua + ⚠️重复的 ekf.yaml
│   ├── launch/                         # cartographer, nav_bringup, occupancy_grid, odom_ekf
│   └── tools/                          # eval_trajectory.py + plot_trajectory.py
├── qr_decoder/                         # C++ ZBar QR 解码器
│   ├── src/qr_decoder.cpp              # 核心解码逻辑
│   └── launch/                         # 独立启动
├── origincar_qr/                       # Python QR 方向决策
│   ├── origincar_qr/qr_decision.py     # 奇偶判断 + 冷却
│   └── test/                           # flake8 + pep257 测试
├── racing_vision_ai/                   # 火山引擎 VLM 图生文
│   ├── racing_vision_ai/vision_ai_node.py
│   ├── config/vision_ai_config.yaml    # ⚠️ 含明文 API key
│   └── launch/vision_ai.launch.py
├── Lslidar_ROS2_driver-N10_V1.0/       # Leishen N10 LiDAR 驱动
│   ├── lslidar_driver/src/lsiosr.cpp
│   └── lslidar_driver/params/lsx10.yaml
├── .learnings/                         # 经验教训 (7 文件, 41 条目)
├── Z_MD/                               # 工作文档
│   ├── todo.md                         # ★ 工作规范 (新对话必读)
│   ├── log.md                          # 运行日志 (~1200行)
│   ├── agent_do.md                     # Agent 执行记录
│   └── wiki.md                         # 维基参考
├── .claude/                            # Claude 配置 (settings + memory)
├── .gitattributes                      # LF 行尾强制
├── .mcp.json                           # MCP SSH Manager → 192.168.31.59
├── trajectory*.csv                     # 生成的轨迹 CSV 文件
├── trajectory*.png                     # 生成的轨迹图表
├── deployments.log                     # 部署历史
└── errors.log                          # 错误日志
```

---

## 14. 参数分歧：磁盘 vs 验证基线

> ⚠️ 磁盘上的 `originbot_nav2_rpp.yaml` 参数**不是** 77.3s 验证最优配置。以下是对比：

| 参数 | 磁盘值 (当前) | 77.3s 验证基线 | 影响 |
|------|--------------|----------------|------|
| `reverse_penalty` | 2.0 | **4.0** | 磁盘值抑制倒退不足, 路点间频繁 DIR_SWITCH |
| `change_penalty` | 0.10 | **0.20** | 磁盘值方向切换惩罚过低 |
| `inflation_radius` | 0.55m | **0.20m** | 磁盘值膨胀过大, 窄道无法通过 |
| `lookahead_dist` | 0.65m | 0.65m | 一致 ✅ |
| `min_lookahead_dist` | 0.30m | **0.55m** | 磁盘值过小, 近距离安全余量不足 |
| `max_lookahead_dist` | 0.90m | **1.5m** | 磁盘值过小, 弯道预瞄不足 |
| `lookahead_time` | 1.2s | **1.8s** | 磁盘值响应过快, 弯道切角风险 |
| `desired_linear_vel` | 0.50m/s | **0.45m/s** | 磁盘值稍快 |
| `cost_scaling_factor` | 2.0 | 2.0 | 一致 ✅ |
| `max_iterations` | 1500 | **2000** | 磁盘值限制更严 |
| `max_planning_time` | 1.5s | **3.0s** | 磁盘值更快失败, 但可能无解 |
| `cache_obstacle_heuristic` | true | **false** (77.3s) | 磁盘启用→重规划快 20-40× 但启动慢 15s |
| `lookup_table_size` | 20.0 | **10.0** (77.3s) | 磁盘值预计算开销大 |

**建议**: 跑完整赛道前先 diff 确认参数是否与 77.3s 基线一致。每次修改参数后用 git tag 标记已验证配置。

### 14.1 重复 EKF 配置

| 文件 | frequency | sensor_timeout | imu0 topic | 使用者 |
|------|-----------|----------------|------------|--------|
| `origincar_base/config/ekf.yaml` | **15Hz** | 2.0s | `/imu/data/madgwick` | `bringup.launch.py` (单IMU fallback) |
| `originbot_navigation/config/ekf.yaml` | **20Hz** | 0.5s | `imu/data/madgwick` | `odom_ekf.launch.py` (独立 EKF) |

两份 ekf.yaml 同时存在，内容不同。当前 stage3 使用 `ekf_dual_imu.yaml` (15Hz, 双IMU)，不受此影响。建议合并并删除未使用的副本。

| 约束 | 值 | 说明 |
|------|-----|------|
| lookahead_dist | ≥0.65m | > 2×min_turning_radius(0.30m), 否则弯道冲入禁区 |
| cmd_vel mux 保活 | republish timer | 任何定时运动必须用 timer 保活, 防 mux timeout 断连 |
| colcon workers | ≤2 | ARM 编译, 超2 OOM |
| EKF 频率 | 15Hz (降频) | Cortex-A55 单步超 50ms 预算 |
| LiDAR 频率 | 5Hz (降频) | 省 CPU |
| yaw_goal_tolerance | 3.14 (PI) | 跳过朝向检查 |
| use_collision_detection | false | 窄道+锥桶误触发 |
| use_rotate_to_heading | false | 阿克曼必须关闭 |
| CRLF | 每次上传后 sed | Windows→Linux 行尾陷阱 |
| 部署 | 必须 colcon build | ROS2 从 install/ 加载, src/ 修改不生效 |
| 改代码前 | 先提方案等确认 | 不可直接 git reset/checkout 覆盖 |
| 调试顺序 | top→down | 先检查 /cmd_vel→/nav_cmd_vel→/cmd_vel_muxed→/ackermann_cmd→串口 |
