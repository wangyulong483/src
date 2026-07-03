# Origincar Pro — 自主驾驶 Ackermann 赛车

> ROS2 Humble + RDK X5 (Sunrise 5) | 全国大学生智能汽车竞赛 | 最优圈速 70.1s
> 最后审核: 2026-07-01 (全项目 3 Agent 并行审查, 136 项发现, 关键项已修复)

---

## 快速开始

```bash
# Stage 3 — 完整比赛 (QQ扫码→通道巡航→VLM→返航)
ros2 launch origincar_bringup stage3_bringup.launch.py

# Stage 1/2
ros2 launch origincar_bringup stage1_bringup.launch.py
ros2 launch origincar_bringup stage2_bringup.launch.py

# SLAM 建图
ros2 launch origincar_bringup slam_bringup.launch.py

# 保存地图
ros2 run nav2_map_server map_saver_cli -f ~/map

# 纯遥控底盘
ros2 launch origincar_base base_serial.launch.py akmcar:=true

# 轨迹分析 (PC端)
python originbot_navigation/tools/plot_trajectory.py [trajectory_*.csv]
```

---

## 1. 硬件平台

| 组件 | 型号 | 接口 | 关键参数 |
|------|------|------|----------|
| 主控 | RDK X5 (Sunrise 5) | — | Cortex-A55 ×4, 10 TOPS BPU, 5.2 GB RAM, Ubuntu 22.04 |
| MCU | STM32F407 | /dev/ttyACM0, 115200 bps | 电机/舵机/MPU6050/编码器/电池电压 |
| LiDAR | Leishen N10 | /dev/ttyACM1, 230400 bps | 2D 360°, 5 Hz, 2000 点/圈 |
| 深度相机 | Aurora930 (Deptrum) | USB 3.0 | RGB+Depth 640×400 @15fps, SDK v1.1.22 |
| IMU (底盘) | MPU6050 | STM32 I2C → 串口 | 辅助角速度源 (EKF imu1, differential=true) |
| IMU (板载) | BMI088 | RDK X5 I2C-1 (IIO) | 陀螺噪声 ~1/10 MPU6050, 偏置 <2°/h, **主 IMU** |
| 底盘 | 阿克曼 | 276×189×150 mm | wheelbase=0.143m, min_turning_radius≈0.30m, max_steer≈28° |
| 电池 | 12V 锂电池 | — | /PowerVoltage 监测 |

---

## 2. 软件包清单

| 包 | 路径 | 语言 | 状态 | 说明 |
|----|------|------|------|------|
| `origincar_base` | `origincar/origincar_base/` | Python | ★ 活跃 | 底盘串口驱动, EKF 定位, IMU 滤波 |
| `origincar_bringup` | `origincar/origincar_bringup/` | Python | ★ 活跃 | 启动文件, `competition_master_stage3`, `telemetry_recorder`, `bmi088_iio_bridge` |
| `origincar_description` | `origincar/origincar_description/` | URDF | ★ 活跃 | 底盘 URDF (`laser_slam_only.urdf`) |
| `origincar_qr` | `origincar_qr/` | Python | ★ 活跃 | QR 方向决策 (CW/CCW) |
| `qr_decoder` | `qr_decoder/` | C++ | ★ 活跃 | ZBar QR 解码 (多尺度: 原尺寸+0.5x) |
| `originbot_navigation` | `originbot_navigation/` | YAML/XML/Py | ★ 活跃 | Nav2 配置, BT, RViz, 工具, 地图 |
| `racing_vision_ai` | `racing_vision_ai/` | Python | ★ 活跃 | VLM 云端推理 (Volcengine Ark) |
| `object_tracker` | `object_tracker/` | Python | ★ 新增 | 深度检测→粒子滤波跟踪→costmap 桥接 |
| `offline_tuner` | `offline_tuner/` | Python | ⚡ 离线 | Optuna 自动调参平台 (17 文件, ~2750 行) |
| `deptrum-ros-driver-aurora930` | `deptrum_ros_driver/` | C++ | ⚡ 第三方 | Aurora930 ROS2 驱动 |

### 已移除的组件

| 组件 | 原因 | 参考 |
|------|------|------|
| `velocity_pid.py` + `cmd_vel_mux.py` + `pose_pid_corrector.py` | STM32 直读 `/cmd_vel`, PID 管线从未生效 | LRN-20260614-002, 2026-06-28 删除 |
| `/stop_cmd_vel` topic | 死胡同, stop 改为直接写 `/cmd_vel` | LRN-20260616-001 |

---

## 3. 软件架构

### 3.1 启动时序 (Stage 3)

```
t=0s  ─── base_minimal (底盘 + TF + Madgwick + EKF + PID)
     └── camera_all (Aurora930 RGB + Depth + PointCloud + QR 解码)

t=1s  ─── nav2_minimal (规划器 + 控制器 + BT + costmap + keepout)

t=3s  ─── object_tracker (深度检测→PF跟踪→costmap桥接)  ← 新增

t=4s  ─── competition_master_stage3 (状态机)
     │     INIT → NAV_TO_QR → BACKING_UP → CRUISE_CHANNEL → RETURN_P → DONE
     │     ├── QR 方向 (CW/CCW) 选择巡航路径
     │     ├── VLM 异步触发 (fire-and-forget)
     │     └── 14列 CSV + plans CSV + costmap PGM + summary JSON

t=8s  ─── RViz2
```

### 3.2 节点拓扑

```
┌────────────────────────────── 感知 ──────────────────────────────┐
│  Aurora930 ──→ qr_decoder ──→ /sign, /sign_pose                  │
│            ──→ depth_detector ──→ /detected_obstacle  (新增)    │
│  N10 LiDAR ──→ /scan ──→ Nav2 costmap + AMCL                    │
│  BMI088 ────→ bmi088_iio_bridge ──→ Madgwick ──→ EKF (imu0)    │
│  MPU6050 ───→ STM32 ──→ Madgwick ──→ EKF (imu1, differential)   │
└──────────────────────────────────────────────────────────────────┘
┌────────────────────────────── 规划 ──────────────────────────────┐
│  Nav2 SmacPlannerHybrid (REEDS_SHEPP, Ackermann)                 │
│  Nav2 RPP Controller (regulated_pure_pursuit)                    │
│  Nav2 ConstrainedSmoother                                        │
│  Behavior Tree: navigate_to_pose / navigate_through_poses        │
│  KeepoutFilter: 静态禁区 + 动态 /costmap_ctrl 控制               │
└──────────────────────────────────────────────────────────────────┘
┌────────────────────────────── 跟踪 ──────────────────────────────┐
│  depth_detector ─→ tracker_node (PF N=50 5Hz) ─→ PoseStamped    │
│                                                ─→ TwistStamped   │
│  costmap_publisher ─→ PointCloud2 ─→ Nav2 costmap (新增)        │
└──────────────────────────────────────────────────────────────────┘
┌────────────────────────────── 控制 ──────────────────────────────┐
│  Nav2 /cmd_vel ──→ STM32 (直连, 无 mux/PID)                     │
│  competition_master stop ──→ /cmd_vel (直接)                     │
│  competition_master backup ──→ /cmd_vel (10Hz keepalive)         │
└──────────────────────────────────────────────────────────────────┘
```

### 3.3 关键 Topic

| Topic | 类型 | 方向 | 说明 |
|-------|------|------|------|
| `/cmd_vel` | Twist | Nav2 → STM32 | 底盘直驱 (唯一控制通道) |
| `/scan` | LaserScan | N10 → Nav2/AMCL | LiDAR 扫描 |
| `/aurora/rgb/image_raw` | Image | Aurora930 → qr_decoder | QR 检测 |
| `/aurora/depth/image_raw` | Image | Aurora930 → depth_detector | 深度障碍物检测 (新增) |
| `/aurora/points2` | PointCloud2 | Aurora930 → Nav2 costmap | 点云障碍物层 |
| `/sign` | String | qr_decoder → competition_master | QR 内容 |
| `/qr_event` | String | qr_decision → competition_master | QR 方向 (CW/CCW) |
| `/costmap_ctrl` | CostmapFilterInfo | competition_master → KeepoutFilter | **独占**禁区控制 |
| `/tracked_obstacles_cloud` | PointCloud2 | costmap_publisher → Nav2 costmap | 跟踪障碍物 (新增) |
| `vlm_result` | String | vision_ai → competition_master | VLM 推理结果 |

---

## 4. 关键配置

### 4.1 Nav2 RPP 金参数 (70.1s 验证)

| 参数 | 值 | 说明 |
|------|-----|------|
| `desired_linear_vel` | 0.40 | 安全速度 (0.5m 通道 + 0.55m 膨胀) |
| `inflation_radius` | 0.55 | 大膨胀形成完整势场 |
| `cost_scaling_factor` | 2.0 | 平缓衰减 |
| `max_iterations` | 1500 | SmacPlannerHybrid |
| `use_fixed_curvature_lookahead` | true | 绕过 Humble RPP bug #5098 |
| `min_lookahead_dist` | 0.30 | |
| `max_lookahead_dist` | 0.90 | |
| `regulated_linear_scaling_min_speed` | 0.0 | ★ 弯道减速到零不 abort |
| `RateController hz` | 1.0 | 最大单项收益 |
| `backup_wz` | 0.80 | 防止 IMU 漂移 |

详细调参历史: [Z_MD/agent_do.md](Z_MD/agent_do.md)

### 4.2 阿克曼约束

| 参数 | 值 |
|------|-----|
| wheelbase | 0.143 m |
| min_turning_radius | ~0.30 m |
| max_steer | ~28° |
| lookahead_dist ≥ 2×min_turning_radius | **≥0.60 m** |

### 4.3 禁区架构

```
KeepoutFilter ← /costmap_ctrl (competition_master 独占发布, TRANSIENT_LOCAL)
costmap_filter_info_server → /costmap_filter_info_server (死胡同, 无人订阅)
启动时 reset publish → 覆盖上一轮 TRANSIENT_LOCAL 缓存
CRUISE_CHANNEL 禁区 ON → 防切角
RETURN_P 禁区 ON → 安全返航
```

详见: [.learnings/keepout.md](.learnings/keepout.md)

---

## 5. 开发工作流

### 5.1 部署流程

```bash
# 1. 本地编辑 → 2. 上传到 RDK X5 → 3. 修复 CRLF → 4. colcon build
scp -r file.py root@192.168.31.59:/userdata/dev_ws/src/<pkg>/
ssh root@192.168.31.59 "
  sed -i 's/\r$//' /userdata/dev_ws/src/<pkg>/**.py
  bash -c 'source /opt/ros/humble/setup.bash && colcon build --packages-select <pkg>'
"
```

详见: [.learnings/deploy.md](.learnings/deploy.md)

### 5.2 关键陷阱

| 陷阱 | 说明 |
|------|------|
| **CRLF** | Windows→Linux 上传的 `.py` 必须 `sed -i 's/\r$//'` 修复 shebang |
| **ROS2 install/** | 部署到 `src/` 后必须 `colcon build`, ROS2 从 `install/` 加载 |
| **chmod +x** | 新 Python 节点必须 `chmod +x`, colcon symlink 继承源文件权限 |
| **TRANSIENT_LOCAL** | 跨运行持久化, 启动时需 reset publish |
| **cmd_vel_mux 保活** | 任何定时运动必须 republish timer 防止 mux timeout 断连 (已删除 mux, 但模式保留) |
| **改代码前先问** | 任何代码修改前必须先提方案、解释原因、等用户确认 |

### 5.3 colcon Build 时间

```bash
# C++ 包 (~90s)
bash -c 'source /opt/ros/humble/setup.bash && colcon build --packages-select qr_decoder lslidar_driver'

# Python 包 (~3s)
bash -c 'source /opt/ros/humble/setup.bash && colcon build --packages-select origincar_bringup originbot_navigation object_tracker racing_vision_ai'
```

---

## 6. 轨迹与日志

### 6.1 输出文件 (远程 `/userdata/dev_ws/`)

```
trajectory_YYYYMMDD_HHMMSS.csv          ← 14列轨迹
trajectory_YYYYMMDD_HHMMSS_summary.json ← 摘要
trajectory_YYYYMMDD_HHMMSS_plans.csv    ← 全部规划历史
trajectory_YYYYMMDD_HHMMSS_costmap.pgm  ← 障碍物地图
```

### 6.2 分析工具 (PC端)

```bash
python originbot_navigation/tools/plot_trajectory.py trajectory_*.csv
# 输出: trajectory_*_map.png + trajectory_*_analysis.png → Z_PNG/outN/
```

### 6.3 rosbag2 录制

```
/tf, /tf_static, /scan, /odom, /amcl_pose, /plan, /local_plan,
/cmd_vel, /global_costmap/costmap, /local_costmap/costmap,
/sign, /qr_event, /vlm_result, /robotvel
```

---

## 7. 已知问题

### 7.1 平台限制

| 问题 | 影响 | 缓解 |
|------|------|------|
| Humble RPP cusp bug (#4757) | REEDS_SHEPP 方向切换导致切角 | `use_fixed_curvature_lookahead: true` |
| CPU 饱和 (75-100%) | Planner ~1.3Hz, 限制重规划频率 | EKF 15Hz (非 20Hz), 组件式合并 |
| Aurora930 深度/RGB 帧率不同步 | QR 检测 depth=0 | 深度过滤 advisory-only |
| Cortex-A55 无 VPU | 不能硬件解码 | 原始 Image 发布 |

### 7.2 代码已知问题 (2026-07-01 审查)

| # | 严重度 | 文件 | 问题 | 状态 |
|---|--------|------|------|------|
| 1 | H | `originbot_nav2_rpp.yaml:177,281` | keepout filter topic `/costmap_ctrl` 不匹配 launch 中的 `/costmap_filter_info` | 待修复 |
| 2 | H | `odom_ekf.launch.py` | `generate_launch_description()` 通过 `.add_action()` 构建但缺少显式 return (实际上有 `return ld`, 待重新验证) | 待验证 |
| 3 | M | `originbot_nav2_rpp.yaml:35` | AMCL 运动模型为 `DifferentialMotionModel` 但底盘为 Ackermann | 待评估影响 |
| 4 | M | `competition_master_stage3.py:1099-1109` | `_on_return_delay()` 死代码 (从未调用) | 低优先级 |
| 5 | M | `competition_master_stage3.py:861-872` | `_start_keepout_republish()` 从未被调度 | 待评估 |
| 6 | M | `.learnings/nav2_params.md:19-28` | 文档了已删除的 mux+PID 管线架构图 | 待更新 |
| 7 | M | `plot_trajectory.py:41,563` | 硬编码 Windows 路径 `C:/Users/27826/Desktop/src` | 跨平台不可用 |
| 8 | L | `racing_vision_ai/config/vision_ai_config.yaml:5` | API key 明文 | 安全风险 |

---

## 8. object_tracker (新增)

从 `object-detector-fusion-master` (ROS1) 移植的轻量障碍物检测+跟踪 pipeline:

```
Aurora930 depth → depth_detector → DBSCAN 聚类 → tracker_node (PF N=50 5Hz)
→ costmap_publisher → PointCloud2 → Nav2 costmap
```

| 节点 | 输入 | 输出 | 说明 |
|------|------|------|------|
| `depth_detector` | `/aurora/depth/image_raw` | `/detected_obstacle` | 深度切片→3D投影→DBSCAN→质心 |
| `tracker_node` | `/detected_obstacle` | `/tracked_object`, `/tracked_object_velocity` | 粒子滤波跟踪 (7D state) |
| `costmap_publisher` | `/tracked_object` | `/tracked_obstacles_cloud` | PointCloud2 桥接 Nav2 |

可调参数: `N` (粒子数), `update_rate` (Hz), `cost_threshold` (门控距离)
详见: [Z_MD/wiki.md](Z_MD/wiki.md)

---

## 9. 参考文档

| 文件 | 内容 |
|------|------|
| [Z_MD/agent_do.md](Z_MD/agent_do.md) | 全部运行历史与根因分析 (时间链, 2026-06-14 至今) |
| [Z_MD/wiki.md](Z_MD/wiki.md) | object-detector-fusion 引入研究 + 实施清单 |
| [Z_MD/todo.md](Z_MD/todo.md) | 工作规范, 部署流程, 关键陷阱, offline_tuner 文档 |
| [.learnings/](.learnings/) | 结构化经验库 (LEARNINGS, ERRORS, ackermann, keepout, deploy, nav2_params) |
