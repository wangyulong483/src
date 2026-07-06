# Origincar Pro — 自主驾驶 Ackermann 赛车

> ROS2 Humble + RDK X5 (Sunrise 5) | 全国大学生智能汽车竞赛 | 最优圈速 **70.1s**
> 最后审查: 2026-07-06 (4 Agent 并行全项目审查)

---

## 快速开始

```bash
# Stage 3 — 完整比赛 (底盘→感知→规划→YOLO→VLM→返航)
ros2 launch origincar_bringup stage3_bringup.launch.py

# Stage 1/2 — 简化赛段
ros2 launch origincar_bringup stage1_bringup.launch.py
ros2 launch origincar_bringup stage2_bringup.launch.py

# SLAM 建图
ros2 launch origincar_bringup slam_bringup.launch.py

# 保存地图
ros2 run nav2_map_server map_saver_cli -f ~/map

# 纯遥控底盘 (调试用)
ros2 launch origincar_base base_serial.launch.py akmcar:=true

# 轨迹分析 (PC端)
python originbot_navigation/tools/plot_trajectory.py [trajectory_*.csv]

# 离线调参 (PC端, 零 ROS 依赖)
python _analyze_plans.py --tune 1000 --tier tier1
```

---

## 1. 硬件平台

| 组件 | 型号 | 接口 | 关键参数 |
|------|------|------|----------|
| 主控 | RDK X5 (Sunrise 5) | — | Cortex-A55 ×4, 10 TOPS BPU, 5.2 GB RAM, Ubuntu 22.04 |
| MCU | STM32F407 | `/dev/ttyACM0`, 115200 bps | 电机/舵机/MPU6050/编码器/电池电压 |
| LiDAR | Leishen N10 | `/dev/ttyACM1`, 230400 bps | 2D 360°, 5 Hz, 2000 点/圈 |
| 深度相机 | Aurora930 (Deptrum) | USB 3.0 | RGB+Depth 640×400 @15fps, SDK v1.1.22 |
| IMU (主) | BMI088 | RDK X5 I2C-1 (IIO) | 陀螺噪声 ~0.000244 rad/s, 偏置 <2°/h |
| IMU (辅) | MPU6050 | STM32 I2C → 串口 | 辅助角速度源, 陀螺噪声 ~0.001 rad/s |
| 底盘 | 阿克曼 | 276×189×150 mm | wheelbase=0.143m, min_turning_radius≈0.30m, max_steer≈28° |
| 电池 | 12V 锂电池 | — | `/PowerVoltage` 监测 |

---

## 2. 软件包清单

| 包 | 路径 | 语言 | 状态 | 说明 |
|----|------|------|------|------|
| `origincar_base` | `origincar/origincar_base/` | C++/Python | ★ 活跃 | 底盘串口驱动, EKF 定位, Madgwick IMU 滤波 |
| `origincar_bringup` | `origincar/origincar_bringup/` | Python | ★ 活跃 | 启动文件, `competition_master_stage3`, `speed_profile_node`, `yolo_costmap_bridge`, `bmi088_iio_bridge` |
| `origincar_description` | `origincar/origincar_description/` | URDF | ★ 活跃 | 底盘 URDF (`laser_slam_only.urdf`: 4 links, 3 joints) |
| `origincar_msg` | `origincar/origincar_msg/` | ROS2 IDL | ★ 活跃 | 自定义消息 (`Data`, `Sign`) |
| `qr_decoder` | `qr_decoder/` | C++/Python | ★ 活跃 | ZBar QR 解码 (多尺度: 原尺寸+0.5x) + QR 方向决策 (CW/CCW) |
| `originbot_navigation` | `originbot_navigation/` | YAML/XML/Py | ★ 活跃 | Nav2 全部配置, BT XML, RViz, 分析工具, 地图 |
| `racing_vision_ai` | `racing_vision_ai/` | Python | ★ 活跃 | VLM 云端推理 (Volcengine Ark, sign4return=9 触发) |
| `racing_obstacle_detection_yolo` | `racing_obstacle_detection_yolo/` | C++ | ★ 活跃 | YOLOv5s BPU 推理 (10 TOPS), BGR→NV12 内置转换 |
| `offline_tuner` | `offline_tuner/` | Python | ⚡ 离线 | Optuna 自动调参平台 (17 文件, ~6300 行, 零 ROS 依赖) |
| `deptrum-ros-driver-aurora930` | 独立工作空间 | C++ | ⚡ 第三方 | Aurora930 ROS2 驱动 (`/userdata/ros_ws/`) |
| `Lslidar_ROS2_driver-N10_V1.0` | `Lslidar_ROS2_driver-N10_V1.0/` | C++ | ⚡ 第三方 | Leishen N10 LiDAR 驱动 |
| `ackermann_msgs` | `origincar/3rdparty/ackermann_msgs-ros2/` | ROS2 IDL | ⚡ 第三方 | Ackermann 消息定义 |
| `serial` | `origincar/3rdparty/serial_ros2/` | C++ | ⚡ 第三方 | 跨平台串口库 |
| `utils` | `origincar/utils/` | C++ | ◆ 备用 | NV12 图像传输节点 (仅 USB 摄像头 demo 用, 比赛不使用) |

### 已移除的组件

| 组件 | 原因 | 参考 |
|------|------|------|
| `velocity_pid.py` + `cmd_vel_mux.py` + `pose_pid_corrector.py` | STM32 直读 `/cmd_vel`, PID 管线从未生效 | LRN-20260614-002 |
| `/stop_cmd_vel` topic | 死胡同, stop 改为直接写 `/cmd_vel` | LRN-20260616-001 |
| BT `SmoothPath` 节点 | Humble ConstrainedSmoother NaN 崩溃 (nav2#4755) | — |
| BT `Spin` 节点 | Ackermann 不支持原地旋转 | — |

---

## 3. 软件架构

### 3.1 启动时序 (Stage 3)

```
t=0s  ─── base_minimal
         │  ├── base_serial (STM32 串口, /dev/ttyACM0, 115200)
         │  ├── lslidar_driver (N10 LiDAR, 5Hz)
         │  ├── robot_state_publisher (URDF)
         │  ├── imu_madgwick_filter (MPU6050 Madgwick, β=0.033, 100Hz)
         │  ├── bmi088_iio_bridge (BMI088 IIO, 100Hz)
         │  ├── imu_madgwick_bmi088 (BMI088 Madgwick, β=0.003, 100Hz)
         │  └── EKF (dual-IMU: BMI088 diff angular vel + MPU6050 yaw, 15Hz)
         │
         └── camera_all
            ├── aurora930_launch (RGB 15fps + Depth + PointCloud)
            ├── static TF: base_link→depth_camera_link (0.14, 0, 0.05)
            ├── qr_decoder (ZBar C++, /aurora/rgb/image_raw + depth advisory)
            └── qr_decision (方向 CW/CCW, cooldown 3.0s)

t=1s  ─── nav2_minimal (composition mode)
         │  ├── keepout_mask_server + costmap_filter_info_server
         │  ├── lifecycle_manager_keepout
         │  └── Nav2 bringup (AMCL + SmacPlannerHybrid + RPP + BT + costmap + keepout)

t=3s  ─── racing_obstacle_detection_yolo (BPU YOLOv5s, /aurora/rgb/image_raw)
         └── yolo_costmap_bridge (PerceptionTargets → PointCloud2 → Nav2 costmap)

t=4s  ─── competition_master_stage3 (状态机)
         │  INIT → NAV_TO_QR → BACKING_UP → CRUISE_CHANNEL → RETURN_P → DONE
         │  ├── QR 方向 (CW/CCW) 选择巡航路径
         │  ├── VLM 异步触发 (fire-and-forget, sign4return=9)
         │  ├── keepout /costmap_ctrl 动态控制 (CRUISE_CHANNEL + RETURN_P)
         │  └── 14列 CSV + plans CSV + summary JSON + costmap PGM

t=5s  ─── speed_profile_node (曲率→速度 v(κ)=v_max/(1+β·|κ|^λ), /speed_limit)

t=8s  ─── RViz2
```

### 3.2 节点拓扑

```
┌──────────────────────── 感知 ────────────────────────┐
│  Aurora930 ──→ qr_decoder (ZBar) ──→ /sign          │
│           ──→ YOLOv5 BPU ──→ /racing_obstacle_detection
│           ──→ /aurora/points2 ──→ Nav2 costmap      │
│  N10 LiDAR ──→ /scan ──→ Nav2 costmap + AMCL        │
│  BMI088 ────→ Madgwick ──→ EKF (imu1, diff vel)     │
│  MPU6050 ───→ Madgwick ──→ EKF (imu0, yaw)          │
└──────────────────────────────────────────────────────┘
┌──────────────────────── 规划 ────────────────────────┐
│  SmacPlannerHybrid (REEDS_SHEPP, Ackermann)          │
│    ├── built-in smooth_path (替代 BT ConstrainedSmoother)
│    ├── downsampled ×3, max_iterations=1500           │
│    └── cache_obstacle_heuristic=true                 │
│  RPP Controller (regulated_pure_pursuit)             │
│    ├── use_fixed_curvature_lookahead=true            │
│    ├── desired_linear_vel=0.50                       │
│    └── regulated_linear_scaling_min_speed=0.1        │
│  BT: navigate_to_pose / navigate_through_poses       │
│    └── 恢复: ClearCostmap→BackUp→Wait (无 Spin/SmoothPath)
│  KeepoutFilter: /costmap_ctrl 独占控制               │
│    + costmap_filter_info_server (死胡同, 无人订阅)    │
└──────────────────────────────────────────────────────┘
┌──────────────────────── 加速 ────────────────────────┐
│  speed_profile_node                                 │
│    plan → Menger curvature → v(κ) formula            │
│    → forward/backward smoothing → /speed_limit       │
│  参数: v_max=0.50, β=0.47, λ=1.32                   │
│       (17条CSV, 1736数据点拟合)                       │
└──────────────────────────────────────────────────────┘
┌──────────────────────── 控制 ────────────────────────┐
│  Nav2 /cmd_vel ──→ STM32 (直连, 无 mux/PID)          │
│  competition_master stop ──→ /cmd_vel (直接)         │
│  competition_master backup ──→ /cmd_vel (10Hz keepalive)
└──────────────────────────────────────────────────────┘
```

### 3.3 关键 Topic

| Topic | 类型 | 方向 | 说明 |
|-------|------|------|------|
| `/cmd_vel` | Twist | Nav2 → STM32 | 唯一控制通道 (直驱) |
| `/scan` | LaserScan | N10 → Nav2/AMCL | LiDAR 扫描, 5Hz |
| `/aurora/rgb/image_raw` | Image | Aurora930 → qr_decoder, YOLO | RGB 图像, BGR8 |
| `/aurora/depth/image_raw` | Image | Aurora930 → yolo_costmap_bridge | 深度图像 (advisory) |
| `/aurora/points2` | PointCloud2 | Aurora930 → Nav2 costmap | 点云障碍物层 |
| `/aurora/rgb/image_jpeg` | Image | JPU encoder → vision_ai | JPEG 压缩 (VLM 上传) |
| `/sign` | String | qr_decoder → competition_master | QR 内容 |
| `/qr_event` | String | qr_decision → competition_master | QR 方向 (CW/CCW) |
| `/costmap_ctrl` | CostmapFilterInfo | competition_master → KeepoutFilter | 独占禁区控制, TRANSIENT_LOCAL |
| `/tracked_obstacles_cloud` | PointCloud2 | yolo_costmap_bridge → Nav2 costmap | YOLO 检测→点云桥接 |
| `/racing_obstacle_detection` | PerceptionTargets | YOLO BPU → yolo_costmap_bridge | YOLOv5 检测结果 |
| `/speed_limit` | SpeedLimit | speed_profile_node → RPP | 曲率自适应速度限制 |
| `vlm_result` | String | vision_ai → competition_master | VLM 推理结果 |
| `/imu/data_raw` | Imu | BMI088 IIO → Madgwick | BMI088 原始数据, 100Hz |

### 3.4 YOLOv5 障碍物检测管线 (新增)

```
Aurora930 RGB (BGR8) → YOLOv5s BPU 推理 (10ms, 13-14fps) → /racing_obstacle_detection
→ yolo_costmap_bridge (深度采样→3D投影) → /tracked_obstacles_cloud (PointCloud2)
→ Nav2 local_costmap obstacle_layer
```

**YOLO 配置:**
- 模型: `yolov5s_tag_v2.0_detect_640x640_bayese_nv12` (PTQ 量化, `.bin`)
- 类别: 1 (obstacle), score_threshold=0.4, nms_threshold=0.5
- 输入: BGR8 ROS Image (内置 `GetNV12Pyramid` 转换, 无需 hobot_codec)
- BPU: `HB_BPU_CORE_0`, task_num=1
- 坐标: 自动缩放回原始分辨率

**yolo_costmap_bridge:**
- 订阅: `/racing_obstacle_detection` + `/aurora/depth/image_raw`
- 深度采样: 检测框中心点 (depth=0 时用 bbox 尺寸 fallback)
- 内参: FX=416.49, FY=417.38, CX=316.83, CY=188.75
- 输出: PointCloud2 (depth_camera_link → 3D 世界坐标)

---

## 4. 关键配置

### 4.1 Nav2 RPP 金参数 (70.1s 验证)

#### 控制器 (RPP)
| 参数 | 值 | 说明 |
|------|-----|------|
| `desired_linear_vel` | 0.50 | 基础速度 (speed_profile_node 通过 `/speed_limit` 动态覆盖) |
| `lookahead_dist` | 0.678 | ≥ 2×min_turning_radius(0.60m) |
| `min_lookahead_dist` | 0.263 | |
| `max_lookahead_dist` | 0.807 | |
| `use_fixed_curvature_lookahead` | **true** | ★ 绕过 Humble RPP bug #5098 |
| `curvature_lookahead_dist` | 0.8 | 固定曲率前视 |
| `regulated_linear_scaling_min_speed` | 0.1 | ★ 弯道减速而非 abort |
| `regulated_linear_scaling_min_radius` | 0.411 | |
| `use_collision_detection` | true | 防碰撞 |
| `use_rotate_to_heading` | false | Ackermann 禁止原地旋转 |
| `allow_reversing` | true | |
| `min_approach_linear_velocity` | 0.317 | |
| `xy_goal_tolerance` | 0.429 | P 点对接精度 |
| `yaw_goal_tolerance` | 3.14 | 放宽容忍度 |

#### 规划器 (SmacPlannerHybrid)
| 参数 | 值 | 说明 |
|------|-----|------|
| `motion_model_for_search` | REEDS_SHEPP | Ackermann 运动学 |
| `minimum_turning_radius` | 0.30 | 匹配底盘 |
| `max_iterations` | 1500 | 充分搜索 |
| `max_planning_time` | 1.596s | |
| `reverse_penalty` | 4.0 | 惩罚倒退 |
| `change_penalty` | 0.0343 | 低惩罚→平滑路径 |
| `cost_penalty` | 6.33 | |
| `analytic_expansion_ratio` | 4.0 | |
| `smooth_path` | **true** | ★ SmacPlanner 内置平滑 (替代 BT 中被移除的 ConstrainedSmoother) |
| `downsample_costmap` | true | |
| `downsampling_factor` | 3 | 降采样加速 |
| `cache_obstacle_heuristic` | true | |

#### Costmap
| 参数 | Local | Global | 说明 |
|------|-------|--------|------|
| `inflation_radius` | **0.55** | 0.596 | ★ 0.55 为关键突破: RETURN_P 从 88.5s→21.1s (-76%) |
| `cost_scaling_factor` | 2.0 | 2.864 | |
| `obstacle_layer` | scan + tracked_obstacles_cloud | scan + points2 | 多源融合 |
| `keepout_filter` | enabled (topic `/costmap_ctrl`) | enabled | 动态禁区 |

### 4.2 阿克曼约束

| 参数 | 值 |
|------|-----|
| wheelbase | 0.143 m |
| min_turning_radius | ~0.30 m |
| max_steer | ~28° |
| **lookahead_dist ≥ 2×min_turning_radius** | **≥0.60 m** |

### 4.3 EKF 双 IMU 架构

```
MPU6050 (imu0) ──→ Madgwick (β=0.033) ──→ EKF yaw + angular vel (relative)
BMI088 (imu1)  ──→ Madgwick (β=0.003) ──→ EKF angular vel only (differential)
Odom           ──→ EKF X pos + X/Y linear vel + Z angular vel (differential)
                              │
                              ▼
                    /odometry/filtered (15Hz)
```

BMI088 陀螺噪声 ~1/10 MPU6050 β 值低 10×, 用 `differential=true` 模式避免 yaw 冲突。

### 4.4 BT 恢复策略

```
NavigateRecovery (retries=-1 无限重试)
├── PipelineSequence
│   ├── RateController @1.0Hz ★
│   ├── ComputePathToPose (clear global → compute)
│   └── FollowPath (clear local + 0.5s 传感器稳定 → replan)
└── RecoveryFallback
    └── RoundRobin:
        1. ClearCostmap + BackUp 0.8m (wz=0.8, 防IMU漂移)
        2. Wait 3.0s
        3. ClearCostmap + BackUp 1.5m
```

**关键设计选择:**
- **RateController=1.0Hz** — 单次最大收益 (-14.5%): 防止机器人跑出 lookahead
- **无 SmoothPath** — Humble ConstrainedSmoother NaN 崩溃 (nav2#4755), 用 SmacPlanner built-in 替代
- **无 Spin** — Ackermann 无法原地旋转
- **无 mux/PID** — STM32 直读 `/cmd_vel`

### 4.5 禁区架构

```
KeepoutFilter ← /costmap_ctrl (competition_master 独占发布, TRANSIENT_LOCAL)
costmap_filter_info_server → /costmap_filter_info_server (死胡同, 无人订阅)
启动时 reset publish → 覆盖上一轮 TRANSIENT_LOCAL 缓存
CRUISE_CHANNEL: 禁区 ON → 防切角
RETURN_P: 禁区 ON → 安全返航
```

详见: [.learnings/keepout.md](.learnings/keepout.md)

---

## 5. 圈速演进

| 日期 | 圈速 | 关键变更 |
|------|------|----------|
| 2026-06-14 | **94.1s** | 基线 (初始 commit 完整 revert) |
| 2026-06-15 | 146.6s | 局部化回退, inflation=0.12 (RETURN_P 88.5s) |
| 2026-06-15 | **82.0s** | ★ **inflation_radius=0.55 验证**: RETURN_P 88.5s→21.1s (-76%) |
| 2026-06-15 | 85.3s | speed 过于激进 (desired=0.55) → keepout 卡死 36s |
| 2026-06-16 | **70.1s** 🏆 | ★ **RateController 0.5→1.0Hz**: CRUISE -27%, 总计 -14.5% |
| 2026-06-25 | 121.9s | CSV 系统新增; RETURN_P death spiral 66s+ |
| 2026-06-25 | 188.7s | 全局超时 (距 P 点仅 0.33m!) |
| 2026-07-05 | 57.7s | urdf2tf+hobot_codec 修复; CRUISE 8.7s (异常快, 疑似数据异常) |
| 2026-07-05 | **70.1s** | 参数回归修复 (local inflation 0.55 恢复, collision_detection ON) |

**三大突破:**
1. **inflation_radius=0.55** (6/15): 符合 Nav2 维护者 Steve Macenski 的推荐, 形成完整势场
2. **RateController=1.0Hz** (6/16): BT 重规划频率翻倍, 防止机器人跑出前视距离
3. **regulated_linear_scaling_min_speed=0.0→0.1** (6/16): 弯道减速到零不 abort, 避免 recovery→planner 冻结死循环

详细历史: [Z_MD/agent_do.md](Z_MD/agent_do.md)

---

## 6. 开发工作流

### 6.1 部署流程

```bash
# 1. 本地编辑 (Windows) → 2. 上传到 RDK X5 → 3. 修复 CRLF → 4. colcon build
# 使用 MCP SSH (推荐):
#   ssh-manager: server "myserver" (192.168.31.59:22)

# 或手动:
scp -r file.py root@192.168.31.59:/userdata/dev_ws/src/<pkg>/
ssh root@192.168.31.59 "
  sed -i 's/\r$//' /userdata/dev_ws/src/<pkg>/**.py
  bash -c 'source /opt/ros/humble/setup.bash && colcon build --packages-select <pkg>'
"
```

详见: [.learnings/deploy.md](.learnings/deploy.md)

### 6.2 关键陷阱

| 陷阱 | 说明 |
|------|------|
| **CRLF** | Windows→Linux 上传的 `.py` 必须 `sed -i 's/\r$//'` 修复 shebang |
| **ROS2 install/** | 部署到 `src/` 后必须 `colcon build`, ROS2 从 `install/` 加载 |
| **chmod +x** | 新 Python 节点必须 `chmod +x`, colcon symlink 继承源文件权限 |
| **TRANSIENT_LOCAL** | 跨运行持久化, 启动时需 reset publish 覆盖旧 keepout 状态 |
| **改代码前先问** | 任何代码修改前必须先提方案、解释原因、等用户确认 |
| **先理解再改动** | 不要重新设计能工作的代码，先对比已知正确版本理解原因 |

### 6.3 colcon Build

```bash
# C++ 包 (~90s)
bash -c 'source /opt/ros/humble/setup.bash && colcon build --packages-select qr_decoder lslidar_driver racing_obstacle_detection_yolo'

# Python 包 (~3s)
bash -c 'source /opt/ros/humble/setup.bash && colcon build --packages-select origincar_bringup originbot_navigation racing_vision_ai'
```

---

## 7. 轨迹与日志

### 7.1 输出文件 (远程 `/userdata/dev_ws/`)

```
trajectory_YYYYMMDD_HHMMSS.csv          ← 14列轨迹 (elapsed,x,y,yaw,state,cmd_vx,cmd_wz,
                                           plan_pts,plan_len,plan_end_xy,cpu,mem,temp)
trajectory_YYYYMMDD_HHMMSS_summary.json ← 摘要 (exit_reason, final_state, elapsed_total)
trajectory_YYYYMMDD_HHMMSS_plans.csv    ← 全部规划历史
trajectory_YYYYMMDD_HHMMSS_costmap.pgm  ← 全局 costmap 快照
```

### 7.2 分析工具 (PC端)

```bash
# 轨迹可视化 (彩色地图叠加 + 时间序列分析)
python originbot_navigation/tools/plot_trajectory.py trajectory_*.csv
# → trajectory_*_map.png + trajectory_*_analysis.png → Z_PNG/outN/

# 定位精度评估 (rosbag2 → AMCL vs 真实位置)
python originbot_navigation/tools/eval_trajectory.py data/rosbags/stage3_*
# → eval_plot.png + eval_report.txt + amcl_pose.csv

# 中线提取 (PGM → Voronoi skeleton → 平滑中线 CSV)
python originbot_navigation/tools/centerline_extractor.py
# → centerline.csv + centerline.png
```

### 7.3 rosbag2 录制

```
/tf, /tf_static, /scan, /odom, /amcl_pose, /plan, /local_plan,
/cmd_vel, /global_costmap/costmap, /local_costmap/costmap,
/sign, /qr_event, /vlm_result, /robotvel
```

---

## 8. 离线调参 (`offline_tuner/`)

零 ROS 依赖的 Nav2 参数优化平台 (17 文件, ~6300 行), 在 PC 端运行。

### 架构

```
CSV/rosbag → PhaseMetrics → Score Model (3 tier auto-upgrade)
                                │
                ┌───────────────┼───────────────┐
                ▼               ▼               ▼
           heuristic      correlation      path_based
           (0 CSV)        (1+ CSV)         (1+ CSV + map)
           weighted        corr(metric,    A* real path →
           formula         time)→weights   Ridge regression
                                              │
                                   30+ CSV → + LightGBM
                                │
                                ▼
                        Optuna TPE Search
                        (n_jobs=1, 单工作)
                                │
                                ▼
                        YAML Patch → 部署
```

### 参数空间

| Tier | 参数数 | 范围 |
|------|--------|------|
| tier1 | 7 | RPP 核心 (desired_vel, lookahead, inflation, max_iterations) |
| default | 19 | + costmap, planner, approach |
| full | 27 | + AMCL, BT, velocity_smoother |

### 常用命令

```bash
python _analyze_plans.py --tune 1000 --tier tier1              # 快速调参
python _analyze_plans.py --tune 2000 --freeze desired=0.50     # 冻结参数
python _analyze_plans.py --analyze-only                         # 纯分析
python _analyze_plans.py --compare out1 out2                    # 方案对比
python _analyze_plans.py --sensitivity                          # 灵敏度分析
```

**关键发现:** path_based 评分正确地将 inflation_radius=0.55 排在 0.25 之上 (heuristic 评分搞反了), 与 70.1s 真实记录验证一致。

---

## 9. 已知问题

### 9.1 平台限制

| 问题 | 影响 | 缓解 |
|------|------|------|
| Humble RPP cusp bug (#4757) | REEDS_SHEPP 尖角导致切角入禁区 | `use_fixed_curvature_lookahead: true` |
| Humble ConstrainedSmoother NaN (#4755) | BT SmoothPath 崩溃 | SmacPlanner built-in `smooth_path:true` |
| CPU 饱和 (75-100%) | Planner ~1.3Hz max, 限制重规划频率 | EKF 15Hz, composition mode, 降采样 ×3 |
| Aurora930 深度/RGB 帧率不同步 | QR 检测 depth=0 | 深度过滤 advisory-only |
| RETURN_P 致死空间死循环 | Planner 在 recovery 期间冻结, 路径过时 | inflation 0.55 + RateController 1.0Hz 大幅减少 |
| Cortex-A55 无 VPU | 不能硬件解码 | 原始 Image 直接发布; YOLO 内部 BGR→NV12 |
| Battery 电压跌落 | 舵机重载断电 | 电池安全监控节点 (`battery_safety_monitor`) |
| API key 明文 | `racing_vision_ai/config/vision_ai_config.yaml` | 安全风险 |

### 9.2 代码已知问题 (2026-07-06 审查)

| # | 严重度 | 文件 | 问题 | 状态 |
|---|--------|------|------|------|
| 1 | H | `originbot_nav2_rpp.yaml` | keepout filter topic `/costmap_ctrl` 与 launch 中的 `/costmap_filter_info_server` 不匹配 | 待修复 |
| 2 | H | `odom_ekf.launch.py` | `generate_launch_description()` 通过 `.add_action()` 构建但缺少显式 return | 待验证 |
| 3 | M | `originbot_nav2_rpp.yaml` | AMCL 运动模型为 `DifferentialMotionModel` 但底盘为 Ackermann | 待评估 |
| 4 | M | `competition_master_stage3.py` | `_on_return_delay()` 死代码 (从未调用) | 低优先级 |
| 5 | M | `competition_master_stage3.py` | `_start_keepout_republish()` 从未被调度 | 待评估 |
| 6 | M | `.learnings/nav2_params.md` | 文档了已删除的 mux+PID 管线 | 待更新 |
| 7 | M | `plot_trajectory.py:41,563` | 硬编码 Windows 路径 `C:/Users/27826/Desktop/src` | 跨平台不可用 |
| 8 | L | `vision_ai_config.yaml:5` | API key 明文 | 安全风险 |

---

## 10. 参考文档

| 文件 | 内容 |
|------|------|
| [Z_MD/agent_do.md](Z_MD/agent_do.md) | 全部操作历史与根因分析 (时间链, 2026-06-14 至今, 64KB) |
| [Z_MD/wiki.md](Z_MD/wiki.md) | 障碍物检测融合研究 + 粒子滤波实施路线图 |
| [Z_MD/todo.md](Z_MD/todo.md) | 工作规范, 部署流程, 关键陷阱, offline_tuner 文档 |
| [Z_MD/log.md](Z_MD/log.md) | 运行时 ROS2 日志 (持续追加) |
| [.learnings/](.learnings/) | 结构化经验库 (28 条 LRN, 10 条 ERR 已全部解决) |
| [.learnings/LEARNINGS.md](.learnings/LEARNINGS.md) | 修正/最佳实践/知识缺口 (50KB) |
| [.learnings/ERRORS.md](.learnings/ERRORS.md) | 错误目录与修复方案 (11KB) |
| [data/trajectories/](data/trajectories/) | 36 个轨迹文件 (22 CSV + 3 plans + 11 summary) |
| [data/rosbags/](data/rosbags/) | 7 个 rosbag2 录制 (2026-06-27~28) |
