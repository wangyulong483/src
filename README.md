# Origincar Pro — 自主驾驶 Ackermann 赛车

> **ROS2 Humble · RDK X5 (Sunrise 5, 10 TOPS) · 全国大学生智能汽车竞赛 (21届地瓜赛项)**
> **当前最优**: 116.5s DONE (2026-07-07, 含死锁脱困修复) | **历史最优**: 70.1s (2026-06-16)
> **RMW**: CycloneDDS (2026-07-08 切换, SHM zero-copy, 大消息延迟更低)

---

## 目录

1. [硬件平台](#1-硬件平台)
2. [快速启动](#2-快速启动)
3. [系统架构](#3-系统架构)
4. [状态机](#4-状态机)
5. [包详解](#5-包详解)
6. [导航配置](#6-导航配置)
7. [禁区系统](#7-禁区系统)
8. [死锁脱困](#8-死锁脱困)
9. [速度曲线](#9-速度曲线)
10. [YOLO 障碍物检测](#10-yolo-障碍物检测)
11. [QR 扫码系统](#11-qr-扫码系统)
12. [VLM 图生文](#12-vlm-图生文)
13. [IMU 双路姿态估计](#13-imu-双路姿态估计)
14. [行为树](#14-行为树)
15. [分析工具](#15-分析工具)
16. [圈速演进](#16-圈速演进)
17. [已知问题与平台限制](#17-已知问题与平台限制)
18. [优化杠杆](#18-优化杠杆)
19. [部署流程](#19-部署流程)
20. [关键文件索引](#20-关键文件索引)

---

## 1. 硬件平台

| 组件 | 型号 | 关键参数 |
|------|------|----------|
| 主控 | RDK X5 (Sunrise 5) | Cortex-A55 ×4 @1.8GHz, 10 TOPS BPU (Bernoulli2架构), 4GB LPDDR4, Ubuntu 22.04 |
| MCU | STM32F407 | `/dev/ttyACM0`, 115200 bps, 电机/舵机/MPU6050 IMU/编码器/电池电压 |
| LiDAR | Leishen N10 | `/dev/ttyACM1`, 5 Hz, 2D 360°, 型号 LSX10 |
| 深度相机 | Aurora930 (Orbbec) | USB 3.0, RGB+Depth 640×400 @15fps, ToF, SDK v1.1.22 |
| IMU | BMI088 (板载) + MPU6050 (底盘) | 双 IMU 融合; BMI088 陀螺噪声 ~1/10 MPU6050 (0.014°/s/√Hz vs ~0.15°/s/√Hz) |
| 底盘 | 阿克曼 | 276×189×150mm, wheelbase=0.143m, min_turning_radius=0.30m, 前轮转向±28° |

### 赛场布局

```
┌─────────────────────────────────────────┐
│  A大厅 (5×2m)                            │
│  P点(-1.985, -0.014) ──── QR任务发布点   │
│                           (0.41, -3.17)  │
├─────────────────────────────────────────┤
│  B通道 (5×0.5m)   黄色通道               │
├─────────────────────────────────────────┤
│  C诊疗区 (5×2.5m)  黄色环形通道(宽0.5m)   │
│  人形立牌 + ≥5个随机锥桶                 │
└─────────────────────────────────────────┘
```

---

## 2. 快速启动

```bash
# Stage 3 — 完整比赛流程 (QR扫码→巡航→VLM→返航)
ros2 launch origincar_bringup stage3_bringup.launch.py

# Stage 2 — QR扫码 + 通道入口导航
ros2 launch origincar_bringup stage2_bringup.launch.py

# Stage 1 — 仅 QR 扫码 (最小集成测试)
ros2 launch origincar_bringup stage1_bringup.launch.py
```

### Stage 3 启动时序 (t=0s 起)

| 时间 | 启动组件 | 说明 |
|------|----------|------|
| t=0s | base_minimal + camera_all + JPU + VLM | 硬件驱动 + 摄像头 + QR + VLM + JPEG硬件编码器 |
| t=1s | nav2_minimal (keepout + Nav2全栈) | 禁区地图先于导航激活，composition模式合并所有Nav2服务器 |
| t=3s | YOLO BPU + yolo_costmap_bridge | 依赖 Aurora930 已开始推流 (t=0s) |
| t=4s | competition_master_stage3 | 状态机发车 (respawn=true, 崩溃自动重启) |
| t=5s | speed_profile_node | 依赖 /plan topic (Nav2 生命周期激活后) |
| t=8s | RViz2 | 纯可视化，最晚启动 |

---

## 3. 系统架构

### 3.1 完整节点拓扑与数据流

```
┌────────────────────────────────────────────────────────────────────────────┐
│                               SENSORS (传感器层)                            │
├────────────────────────────────────────────────────────────────────────────┤
│  STM32 ──── /imu/data_raw (MPU6050, 100Hz) ──→ imu_madgwick_filter        │
│  STM32 ──── /odom (轮式里程计, 20Hz) ──→ EKF                              │
│  BMI088 ─── bmi088_iio_bridge (sysfs 轮询, 50Hz) ──→ /imu_data             │
│             ──→ imu_madgwick_bmi088 ──→ /imu/data/bmi088_madgwick ──→ EKF  │
│  N10 LiDAR ─ /scan (5Hz) ──→ AMCL + costmap obstacle_layer                 │
│  Aurora930 ─ /aurora/rgb/image_raw (BGR8, 15fps) ──→ QR + YOLO + JPU      │
│  Aurora930 ─ /aurora/depth/image_raw (16UC1 mm, 15fps) ──→ QR + YOLO桥接   │
└────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────┐
│                            PROCESSING (处理层)                              │
├────────────────────────────────────────────────────────────────────────────┤
│  qr_decoder_zbar (C++/ZBar) ──→ /sign (QR文本) ──→ qr_decision            │
│  qr_decision (Python) ──→ /qr_event ("1584,逆时针,x,y") ──→ master        │
│                                                                             │
│  racing_obstacle_detection_yolo (C++/BPU)                                   │
│    /aurora/rgb/image_raw (BGR8) → FeedImg() → BGR→NV12(自动) → BPU推理     │
│    → /racing_obstacle_detection (PerceptionTargets, ~14fps)                 │
│                                                                             │
│  yolo_costmap_bridge (Python)                                               │
│    /racing_obstacle_detection + /aurora/depth/image_raw                      │
│    → ROI 3×3深度采样 → 相机3D投影 → /tracked_obstacles_cloud (PointCloud2) │
│                                                                             │
│  speed_profile_node (Python, 20Hz)                                          │
│    /plan → Menger曲率 → v(κ)=v_max/(1+β·|κ|^λ) → 前后向平滑               │
│    → /speed_limit (nav2_msgs/SpeedLimit, 绝对m/s)                           │
│                                                                             │
│  hobot_codec (JPU硬件)                                                      │
│    /aurora/rgb/image_raw (BGR8) → JPEG (85%) → /aurora/rgb/image_jpeg       │
│    省 CPU 5-10ms/VLM触发 vs cv2.imencode                                    │
└────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────┐
│                         NAVIGATION (导航层, Nav2 composition)                │
├────────────────────────────────────────────────────────────────────────────┤
│  AMCL: /scan + /odom/filtered + /map → /amcl_pose + TF(map→odom)           │
│                                                                             │
│  Planner (SmacPlannerHybrid, REEDS_SHEPP):                                  │
│    /global_costmap + /goal_pose → /plan (~1.3Hz, max 1500 iterations)       │
│    cache_obstacle_heuristic: true (官方~40×重规划加速)                       │
│    downsampling_factor: 3 (×3 降采样, 省CPU)                                │
│                                                                             │
│  Controller (RPP, 10Hz):                                                    │
│    /plan + /local_costmap + /speed_limit → /cmd_vel (Twist)                 │
│                                                                             │
│  Velocity Smoother (20Hz, OPEN_LOOP):                                       │
│    /cmd_vel → /cmd_vel (smoothed), max: [0.65, 0.0, 2.8]                    │
│                                                                             │
│  Costmaps (local + global):                                                 │
│    ObstacleLayer: /scan + /tracked_obstacles_cloud                          │
│    KeepoutFilter: /costmap_ctrl → /keepout_mask (独占通道)                  │
│    InflationLayer: local 0.55m, global 0.5955m                              │
│    StaticLayer: /map (global only, TRANSIENT_LOCAL)                         │
└────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────┐
│                           CONTROL (控制层)                                  │
├────────────────────────────────────────────────────────────────────────────┤
│  Nav2 /cmd_vel ────────────→ STM32 (直连, 无中间PID/mux)                    │
│  competition_master backup → /cmd_vel (10Hz 保活, 独占发布)                  │
│  competition_master stop   → /cmd_vel (零 Twist)                            │
│  competition_master escape → /cmd_vel (直驱倒车, 绕过Nav2碰撞检测)           │
│                                                                             │
│  ★ 架构简化 (2026-06-28): 删除 cmd_vel_mux + velocity_pid +                 │
│    pose_pid_corrector + control_params.yaml. STM32 一直直读 /cmd_vel,       │
│    从未订阅 /cmd_vel_corrected. 70.1s 记录在完全绕过管线的情况下取得.        │
└────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────┐
│                              VLM (图生文)                                   │
├────────────────────────────────────────────────────────────────────────────┤
│  competition_master → /sign4return (Int32=100)                              │
│  vision_ai_node → 匹配 target_sign → 订阅 /aurora/rgb/image_jpeg (单帧)     │
│    → base64编码 → Volcengine Ark API → /vlm_result (String, 异步)           │
│  ★ competition_master 发 VLM 后立即返航，不等待结果.                         │
└────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 关键 Topic 一览

| Topic | 类型 | 发布者 | 订阅者 | 备注 |
|-------|------|--------|--------|------|
| `/cmd_vel` | Twist | velocity_smoother, competition_master | STM32 (origincar_base_node) | 控制直连 |
| `/odom` | Odometry | origincar_base_node (C++) | EKF, speed_profile, qr_decoder | 轮式里程计 |
| `/scan` | LaserScan | lslidar_driver_node (5Hz) | AMCL, costmap obstacle_layer | N10 LiDAR |
| `/imu/data_raw` | Imu | origincar_base_node (来自STM32 MPU6050) | imu_madgwick_filter | 100Hz |
| `/imu/data/madgwick` | Imu | imu_madgwick_filter (Python, β=0.033) | EKF (imu0) | MPU6050 Madgwick |
| `/imu_data` | Imu | bmi088_iio_bridge (Python, 50Hz) | imu_madgwick_bmi088 | BMI088 raw |
| `/imu/data/bmi088_madgwick` | Imu | imu_madgwick_bmi088 (Python, β=0.003) | EKF (imu1, differential) | BMI088 Madgwick |
| `/aurora/rgb/image_raw` | Image (BGR8) | deptrum-ros-driver | QR, YOLO, JPU | 640×400 @15fps |
| `/aurora/depth/image_raw` | Image (16UC1 mm) | deptrum-ros-driver | QR (advisory), yolo_costmap_bridge | ToF 深度 |
| `/aurora/rgb/image_jpeg` | CompressedImage | hobot_codec (JPU) | vision_ai_node | HW JPEG |
| `/sign` | String | qr_decoder_zbar (C++/ZBar) | competition_master, qr_decision | QR 原始文本 |
| `/qr_event` | String | qr_decision (Python) | competition_master | "1584,逆时针,x,y" |
| `/racing_obstacle_detection` | PerceptionTargets | YOLO BPU (C++) | yolo_costmap_bridge, competition_master (diag) | ~14fps |
| `/tracked_obstacles_cloud` | PointCloud2 | yolo_costmap_bridge | costmap obstacle_layer (local+global) | depth_camera_link |
| `/speed_limit` | SpeedLimit | speed_profile_node (20Hz) | RPP controller_server | 绝对m/s, percentage=false |
| `/plan` | Path | planner_server | speed_profile_node, competition_master | 全局路径 |
| `/costmap_ctrl` | CostmapFilterInfo | competition_master (独占) | keepout_filter (local+global) | TRANSIENT_LOCAL, 隔离通道 |
| `/sign4return` | Int32 | competition_master | vision_ai_node | VLM 触发信号 |
| `/vlm_result` | String | vision_ai_node | competition_master | VLM 推理结果(异步) |

### 3.3 语言分工

| 语言 | 节点 | 原因 |
|------|------|------|
| **C++** | origincar_base, lslidar_driver, qr_decoder_zbar, racing_obstacle_detection_yolo, Nav2 servers (composition) | 性能关键路径 (串口/LiDAR/BPU推理/ZBar/规划) |
| **Python** | competition_master, yolo_costmap_bridge, speed_profile_node, imu_madgwick_filter, bmi088_iio_bridge, qr_decision, vision_ai_node, telemetry_recorder | 快速迭代 (状态机/传感器桥接/算法原型/云端API) |

---

## 4. 状态机

### 4.1 状态流转

```
INIT → NAV_TO_QR → BACKING_UP → CRUISE_CHANNEL → (VLM触发) → RETURN_P → DONE
                                                    ↑ 不等结果, 立即继续
```

### 4.2 各状态详解

| 状态 | 动作 | 导航方式 | 超时 | 关键细节 |
|------|------|----------|------|----------|
| **INIT** | 等待 Nav2 action server 就绪 (轮询), CPU governor→performance, rosbag 录制, 启动时重置 keepout (/costmap_ctrl→/keepout_mask) | — | — | start_delay_sec=0.1s |
| **NAV_TO_QR** | 导航到 QR 任务发布点 (0.41, -3.17) | NavigateToPose | 90s | QR检测→取消当前goal→等待BT cancel确认(3s)→`pkill qr_decoder_zbar`→等/qr_event(2s) |
| **BACKING_UP** | 右后退摆正车头 (阿克曼不可原地旋转) | 直驱 /cmd_vel | 6s | vx=-0.15, wz=0.80, **10Hz保活**防 mux timeout(0.5s). wz 从 2.80→0.80 消除 IMU yaw 漂移 |
| **CRUISE_CHANNEL** | 穿巡航路点: Entry→WP1→WP2→VLM | NavigateThroughPoses (3-4路点) | 180s | 方向由QR决定: odd=CW(顺时针), even=CCW(逆时针). 路点从15条DONE轨迹共识校准. 启动 keepout 2s 重发布 + 1Hz 卡死检测 |
| **VLM_TRIGGER** | 发布 /sign4return=100, 后台等待VLM结果 | — | 30s | 发布后**立即**转入 RETURN_P. VLM 结果异步记录 |
| **RETURN_P** | PostVLM→P点 返航 | NavigateToPose (两段) | 120s | 使用当前 yaw 为目标朝向; yaw_goal_tolerance=3.14 (PI, 无朝向要求). 到达后 kill rosbag + 保存 CSV + 恢复硬禁区 |
| **TIMEOUT** | 全局超时 (180s) 或段超时 | — | — | 强制停车 + 保存轨迹 + 恢复禁区 |

### 4.3 方向决策 (QR 奇偶性)

```
QR数字 % 2 == 1 → "顺时针" (CW, odd QR)
QR数字 % 2 == 0 → "逆时针" (CCW, even QR)
未扫到 → 回退方向 "逆时针" (default_qr_direction)
```

CW 与 CCW 使用同一组路点的反序 (同环反向). CW数据无独立校准, 复用CCW共识点反序.

### 4.4 巡航路点 (2026-07-08 校准)

**CCW (逆时针, even QR)**: 4路点: WP1(1.50,-1.45) → WP2(3.02,-1.02) → VLM(2.02,0.94) → PostVLM(0.96,-0.06)
- 前3个用于 NavigateThroughPoses; PostVLM 注入 RETURN_P 首段作为窄通道引导

**CW (顺时针, odd QR)**: 4路点: PostVLM(0.96,-0.06) → VLM(2.02,0.94) → WP2(3.02,-1.02) → WP1(1.50,-1.45)
- CCW 逆序; VLM=CW拍照点=WP2位置 (用户确认)

路点通过 `recalibrate_waypoints.py` 从 15 条干净 DONE 轨迹 (剔除 4 条 CRUISE>40s 环道卡死) 的逐分量中位数+Snap-to-Free 算法校准.

---

## 5. 包详解

### 5.1 origincar_bringup — 核心编排包 (12 Python + 1 C++, ~3450 LOC)

**职责**: 启动文件 + 比赛状态机 (3个stage) + 速度曲线 + YOLO桥接 + IMU IIO驱动 + Madgwick滤波 + 标定工具 + 遥测

**关键节点**:

| 可执行文件 | 语言 | LOC | 功能 |
|-----------|------|-----|------|
| `competition_master_stage3.py` | Python | ~1784 | Stage3 完整状态机 (详见 §4) |
| `competition_master_stage2.py` | Python | ~414 | Stage2: NAV_TO_QR→NAV_TO_ENTRY→DONE |
| `competition_master_stage1.py` | Python | ~195 | Stage1: NAV_TO_QR→DONE (最小集成测试) |
| `speed_profile_node.py` | Python | ~400 | 曲率→速度映射 (详见 §9) |
| `yolo_costmap_bridge.py` | Python | ~179 | PerceptionTargets→PointCloud2 (详见 §10) |
| `bmi088_iio_bridge.py` | Python | ~488 | BMI088 sysfs IIO驱动 (详见 §13) |
| `imu_madgwick_filter.py` | Python | ~310 | Madgwick 6-DOF AHRS, 双实例 (MPU6050+BMI088) (详见 §13) |
| `telemetry_recorder.py` | Python | ~90 | 5Hz CSV 记录器 (pose/cmd_vel/odom/plan/goal) → /tmp/telemetry.csv |
| `odom2tf.cpp` | C++ | ~46 | /odom→TF(odom→base_footprint) 广播 |
| `calibrate_gui.py` | Python | ~397 | Matplotlib 交互式路点+禁区标定 |
| `calibrate_p_point.py` | Python | ~270 | 全自动 P点+锥桶标定 |
| `wait_for_odom.py` | Python | ~59 | 启动屏障: 等待 /odom 数据 (15s超时) |

**启动文件**:

| 文件 | 功能 |
|------|------|
| `stage3_bringup.launch.py` | Stage3 总启动: t=0s base+camera+QR+VLM+JPU, t=1s Nav2+keepout, t=3s YOLO+bridge, t=4s master, t=5s speed, t=8s RViz. 设置 RMW_IMPLEMENTATION=rmw_cyclonedds_cpp |
| `stage2_bringup.launch.py` | Stage2: t=0s base+camera+QR+VLM, t=1s Nav2, t=4s master_stage2, t=8s RViz |
| `stage1_bringup.launch.py` | Stage1: t=0s base+camera+QR, t=1s Nav2, t=4s master_stage1 |
| `base_minimal.launch.py` | 最小硬件: STM32 + LiDAR + URDF TF + MPU6050 Madgwick + BMI088 IIO(可选) + EKF(双/单IMU) |
| `nav2_minimal.launch.py` | Nav2 composition + keepout双mask服务器 + lifecycle_manager. 正则修补 BT XML 路径到 YAML |
| `camera_all.launch.py` | Aurora930 + depth_camera_link TF + qr_decoder_zbar + qr_decision |

### 5.2 origincar_base — 底盘驱动包 (2 C++, ~800 LOC)

**职责**: STM32 串口通信. 将 ROS2 Twist 转为11字节二进制帧, 解析24字节传感器帧 (速度反馈/MPU6050/电池).

**origincar_base_node** (C++ 单节点):
- 串口协议: 帧头 0x7B, 帧尾 0x7D, XOR 校验
- 发布: `/odom` (Odometry), `/imu/data_raw` (Imu from MPU6050), `/PowerVoltage` (Float32), `/robotpose`, `/robotvel`
- 订阅: `/cmd_vel` (Twist), `/ackermann_cmd` (AckermannDriveStamped)
- 里程计补偿: X *= 1.03, Y *= 1.125
- Quaternion_Solution: Mahony 互补滤波 (Ki=0, 比例-only), 快速平方根倒数 (0x5f375a86), 30Hz

**cmd_vel_to_ackermann_drive.py** (Python 桥接):
- Twist→AckermannDriveStamped: steering = atan(wheelbase * omega / vel)
- wheelbase=0.143m, steering_sign=-1.0 (ROS CCW→STM32 CW 符号转换)

**EKF 配置文件** (详见 §13):
- `ekf_dual_imu.yaml`: odom + imu0(MPU6050: yaw姿态+Z角速度) + imu1(BMI088: Z角速度, differential)
- `ekf.yaml`: odom + imu0 only (单IMU回退)

### 5.3 originbot_navigation — 导航配置包 (YAML/XML/Python 工具, ~850 LOC)

**职责**: Nav2 参数、行为树、地图、禁区 mask、分析工具.

| 文件 | 类型 | 功能 |
|------|------|------|
| `param/originbot_nav2_rpp.yaml` | YAML (~425行) | 全 Nav2 参数 (详见 §6) |
| `behavior_trees/navigate_to_pose_ackermann_rpp.xml` | BT XML | NavigateToPose 行为树 (详见 §14) |
| `behavior_trees/navigate_through_poses_ackermann_rpp.xml` | BT XML | NavigateThroughPoses 行为树 (详见 §14) |
| `maps/room.yaml, room.pgm` | 地图 | 静态占据栅格地图 (163×141, 0.05m/pix) |
| `maps/keepout_mask.yaml, keepout_mask.pgm` | 禁区 | 硬禁区 mask (致死 cost=254) |
| `maps/keepout_mask_soft.yaml, keepout_mask_soft.pgm` | 软禁区 | 软禁区 mask (occ~90→cost~229, 高成本可穿) |
| `tools/recalibrate_waypoints.py` | 工具 | 从历史DONE轨迹共识校准路点 (详见 §15) |
| `tools/plot_trajectory.py` | 工具 | 4面板轨迹可视化 (详见 §15) |
| `tools/eval_trajectory.py` | 工具 | AMCL 定位精度验证 (详见 §15) |
| `tools/centerline_extractor.py` | 工具 | Voronoi骨架中线提取 (~560 LOC) (详见 §15) |
| `launch/nav_bringup.launch.py` | 启动 | 完整 Nav2 + 可选 RPP/DWA + Cartographer |

### 5.4 qr_decoder — QR 扫码包 (1 C++ + 1 Python, ~360 LOC)

**qr_decoder_zbar** (C++/ZBar, ~250 LOC):
- ZBar ImageScanner, QR only (其他码制禁用)
- 多尺度解码: 原分辨率 → 0.5× 降采样 (cv::INTER_AREA) 回退
- 深度滤波: **advisory only** (Aurora930 深度/RGB 帧率不同步 → depth=0mm 不拒绝有效 QR)
- 发布: `/sign` (String, QR文本), `/sign_pose` (PoseStamped, odom 帧)
- 参数: fx=421.3, fy=422.3, cx=320.3, cy=197.0

**qr_decision** (Python, ~108 LOC):
- 纯逻辑节点: 接收 `/sign` → 验证(1-4位纯数字, 1-9999) → 奇偶→方向
- 冷却: 3.0s (同号忽略)
- 发布: `/qr_event` ("1584,逆时针,x,y"), `/qr_result`, `/sign_switch_sign_data` (3=CW, 4=CCW)

### 5.5 racing_obstacle_detection_yolo — YOLO BPU 检测包 (3 C++, ~850 LOC)

**racing_obstacle_detection_yolo** (C++, DnnNode 子类, ~500 LOC):
- YOLOv5s PTQ 后量化模型 (yolov5s_tag_v2.0_detect_640x640_bayese_nv12)
- **双输入模式**: 共享内存 (HbmMsg1080P NV12, zero-copy) 或 ROS Image (BGR8, FeedImg→BGR→NV12 自动转换)
- BPU core 0/1, 1 inference task
- 发布: `/racing_obstacle_detection` (ai_msgs/PerceptionTargets)
- **parser.cpp** (~246 LOC): YOLOv5 输出张量解析: sigmoid + stride grid + NMS (score=0.3, nms=0.65, top_k=5000). 支持 PTQ 反量化
- **image_utils.cpp** (~143 LOC): BGR→NV12 + letterbox 缩放 (保持宽高比, 灰边填充). HB SysMem 分配 (cached + cache flush). 16字节 stride 对齐
- **config**: `yolov5workconfig.json`: 1类 ("obstacle"), strides=[8,16,32], 标准 YOLOv5s anchors

### 5.6 racing_vision_ai — VLM 云端推理包 (1 Python, ~230 LOC)

**vision_ai_node** (Python, ament_python):
- 订阅 `/sign4return` (Int32); 匹配 target_sign=100 → 单帧订阅 `/aurora/rgb/image_jpeg`
- base64 编码 → Volcengine Ark API (model: ep-20260502193326-428m8)
- 发布: `/vlm_result` (String)
- Prompt: 医疗巡检场景 (描述人形立牌姿态/着装/动作/场景, &lt;100字)
- 配置: `vision_ai_config.yaml` (API key, model_id, prompt)

### 5.7 其他包

| 包 | 职责 |
|----|------|
| `origincar_description` | URDF 机器人模型: base_link(0.276×0.164×0.08m) + gyro_link + laser_link |
| `origincar_msg` | 自定义消息: Data.msg (x,y,z float), Sign.msg (sign_data int32) |
| `origincar/utils` | image_transport_node (YOLO launch 使用的图像传输) |
| `ackermann_msgs` (3rdparty) | AckermannDriveStamped 消息类型 |
| `serial_ros2` (3rdparty) | 跨平台串口库 |
| `deptrum-ros-driver-aurora930` (外部) | Aurora930 驱动, 独立工作空间 `/userdata/ros_ws/` |

---

## 6. 导航配置

完整参数见 [originbot_nav2_rpp.yaml](originbot_navigation/param/originbot_nav2_rpp.yaml) (~425行). 以下为关键参数及其设计原理.

### 6.1 控制器 (Regulated Pure Pursuit)

| 参数 | 值 | 设计原理 |
|------|-----|----------|
| `desired_linear_vel` | 0.50 | 基础巡航速度, 被 /speed_limit 动态覆盖 |
| `lookahead_dist` | 0.6776 | ★ 硬约束: ≥2×min_turning_radius=0.60m (Ackermann 运动学) |
| `min_lookahead_dist` | 0.2628 | 最小前视距离 |
| `max_lookahead_dist` | 0.8067 | 最大前视距离 |
| `lookahead_time` | 1.2415 | 速度缩放前视因子 |
| `use_velocity_scaled_lookahead_dist` | true | 高速远看, 低速近看 |
| `allow_reversing` | true | 允许倒车 (REEDS_SHEPP 需要) |
| `use_collision_detection` | true | 防碰撞 |
| `max_allowed_time_to_collision_up_to_carrot` | 0.35 | ★ 2026-07-08: 1.0→0.35, 碰撞检测前视从~0.55m缩到~0.18m, 防P点锥桶假阳性卡死 |
| `use_regulated_linear_velocity_scaling` | true | 弯道减速 |
| `regulated_linear_scaling_min_radius` | 0.411 | 开始减速的弯道半径 |
| `regulated_linear_scaling_min_speed` | 0.20 | ★ 2026-07-08: 0.1→0.20, 弯道最低速翻倍, 匹配 speed_profile v_min |
| `use_cost_regulated_linear_velocity_scaling` | true | 高成本区减速 |
| `cost_scaling_gain` | 1.5 | ★ 2026-07-08: 2.7066→1.5, 降低cost区减速强度 |
| `cost_scaling_dist` | 0.0894 | 成本缩放特征距离 |
| `inflation_cost_scaling_factor` | 5.0 | 膨胀层成本对车速的影响 |
| `use_rotate_to_heading` | false | 阿克曼不可原地旋转 |
| `max_linear_vel` / `min_linear_vel` | 0.6244 / -0.3 | 速度包络 |
| `max_linear_accel` / `max_linear_decel` | 1.7993 / 2.2 | 加速度包络 |
| `xy_goal_tolerance` | 0.4291 | ★ P点到位精度 |
| `yaw_goal_tolerance` | 3.14 | PI=无朝向要求 |
| `transform_tolerance` | 0.2 | TF 时间容差 |
| `speed_limit_topic` | /speed_limit | 动态速度限制输入 |

### 6.2 规划器 (SmacPlannerHybrid)

| 参数 | 值 | 设计原理 |
|------|-----|----------|
| `motion_model_for_search` | REEDS_SHEPP | Ackermann + 倒车 |
| `minimum_turning_radius` | 0.30 | 实测最小转弯半径 |
| `angle_quantization_bins` | 40 | 角度离散化 |
| `max_iterations` | 1500 | 规划迭代上限 |
| `max_planning_time` | 1.596s | 规划时间上限 |
| `analytic_expansion_ratio` | 4.0 | 每 N 次搜索后尝试解析扩展到目标 |
| `analytic_expansion_max_length` | 1.5 | 解析扩展最大长度 |
| `reverse_penalty` | 4.0 | 惩罚倒退 (★ 注: #6075 导致近目标时解析扩展忽略此值, 仅搜索阶段有效) |
| `change_penalty` | 0.20 | ★ 2026-07-07: 0.0343→0.20. 抑制换向尖角(cusp). Humble RPP 无 use_fixed_curvature_lookahead (Iron+ 功能), #5098 曲率前视 cusp 抖动不适用. cusp 抑制靠 planner 层 change_penalty+reverse_penalty 实现 |
| `non_straight_penalty` | 1.8469 | 鼓励直行 (高于官方推荐 1.0-1.3, 但实测有效) |
| `cost_penalty` | 6.33 | 代价敏感度 |
| `cache_obstacle_heuristic` | true | ★ 官方~40×重规划加速. 仅在不清除 costmap 时生效 (BT 已改为仅失败时清) |
| `smooth_path` | true | ★ 内置平滑 (替代被移除的 ConstrainedSmoother, 因其 Humble NaN 崩溃 nav2#4755) |
| `downsample_costmap` | true | 规划前降采样 |
| `downsampling_factor` | 3 | ×3 降采样, 省 CPU |
| `allow_unknown` | false | 禁止穿越未知空间 (配合 room 阈值恢复, 防穿墙) |
| **Smoother 子参数** | | |
| `smoother.max_iterations` | 300 | |
| `smoother.w_smooth` | 0.3 | 平滑权重 |
| `smoother.w_data` | 0.2 | 数据保真权重 |
| `smoother.do_refinement` | true | 迭代细化 |

### 6.3 代价地图 (Costmap)

| 参数 | Local | Global | 说明 |
|------|-------|--------|------|
| `update_frequency` | 5.0 Hz | 1.0 Hz | |
| `publish_frequency` | 2.0 Hz | 1.0 Hz | |
| `global_frame` | odom | map | Local 跟随机器人 |
| `width × height` | 3m × 3m | (full map) | |
| `resolution` | 0.05 | 0.05 | m/pixel |
| `robot_footprint` | [0.15,-0.10]→[-0.12,-0.10] | 同 | 0.27×0.20m 矩形 |
| `transform_tolerance` | 0.5 | 0.5 | ★ 2026-07-08: 0.1→0.5. LiDAR 5Hz 扫描时间戳可早至200ms前, 默认0.1不足→丢帧 |
| `inflation_radius` | 0.55 | 0.5955 | ★ 形成完整势场; 窄道有挤压风险 (§17) |
| `cost_scaling_factor` | 2.0 | 2.8637 | |
| **Plugins** | obstacle + keepout + inflation | static + obstacle + keepout + inflation | Local 无 static_layer |
| `keepout_filter.filter_info_topic` | /costmap_ctrl | /costmap_ctrl | ★ 共享独占通道, local+global 对 lethal 判断必须一致 |

**Observation Sources**:

| Source | Topic | Type | Range | Marking | Clearing |
|--------|-------|------|-------|---------|----------|
| scan | /scan | LaserScan | — | ✓ | ✓ |
| tracked_obstacles | /tracked_obstacles_cloud | PointCloud2 | 3.5m | ✓ | ✓ |

tracked_obstacles 参数: sensor_frame=depth_camera_link, obstacle_height=0.05-0.5m, observation_persistence=1.0s

### 6.4 AMCL 定位

| 参数 | 值 | 设计原理 |
|------|-----|----------|
| `robot_model_type` | DifferentialMotionModel | ★ Nav2 Humble AMCL 仅有 Differential+Omni 两种, 无 Ackermann 模型. Ackermann 约束由 REEDS_SHEPP+RPP 在规划/控制层处理. 2026-07-06 EXA MCP 验证 |
| `max_particles` / `min_particles` | 1500 / 300 | |
| `resample_interval` | 2 | ★ 回退基线: 每次重采样(=1)导致粒子退化, 日志双IMU yaw分歧~55° |
| `alpha1-5` | 0.45 | 均匀噪声模型 |
| `laser_model_type` | likelihood_field_prob | |
| `max_beams` | 60 | |
| `update_min_a` / `update_min_d` | 0.1 / 0.1 | ★ 回退基线: 恢复定位更新频率, 防CRUISE段定位滞后 |
| `transform_tolerance` | 1.0 | AMCL TF 容差 |
| `initial_pose` | x=-1.985, y=-0.014, yaw=0.262 | P点预设 (set_initial_pose: true) |

### 6.5 其他 Nav2 节点

**Velocity Smoother** (20Hz, OPEN_LOOP):
- max_velocity: [0.65, 0.0, 2.8] (★ 2026-07-07: 0.85→0.65, 匹配 RPP max_linear_vel=0.6244)
- max_accel: [1.5, 0.0, 2.5], max_decel: [-1.8, 0.0, -2.5]

**Recoveries Server**:
- BackUp: distance=0.3m, speed=0.12m/s (系统级; BT 中有独立的 0.8m/1.5m 后退)
- Wait: duration=3.0s

**ConstrainedSmoother** (已配置但 BT 中未调用):
- 参数存在但无效 — Smoother 因 Humble NaN 崩溃 (nav2#4755) 已从 BT 移除
- SmacPlanner 内置 `smooth_path:true` 替代
- RPP cusp 缓解: w_cost_cusp_multiplier=3.0, cusp_zone_length=2.5 (通过 planner smoother 间接生效)

**Waypoint Follower**: loop_rate=20Hz, waypoint_pause_duration=50ms (WaitAtWaypoint)

---

## 7. 禁区系统

### 7.1 Topic 隔离架构

```
costmap_filter_info_server → /costmap_filter_info_server  (死胡同, 无人订阅)
competition_master          → /costmap_ctrl               (独占发布者, TRANSIENT_LOCAL)
KeepoutFilter (local+global) ← /costmap_ctrl              (唯一订阅者)
```

**设计原因**: TRANSIENT_LOCAL 双发布者导致消息缓存竞态 — 上轮 disable 消息可能覆盖重启后的 reset → 禁区永久失效. 隔离 topic 消除竞态.

### 7.2 双 Mask 方案

| Mask | Topic | 像素值→occupancy→cost | 效果 |
|------|-------|----------------------|------|
| 硬禁区 | `/keepout_mask` | 254→100%→cost 254 (LETHAL) | 正常操作, 不可穿越, 防驶出通道 |
| 软禁区 | `/keepout_mask_soft` | 25→~90→cost~229 (INSCRIBED) | 高成本可穿, 锥桶堵塞时 clip 绕行 |

**软禁区设计**: Humble KeepoutFilter 忽略 CostmapFilterInfo 的 base/multiplier (EXA 验证). 软化必须靠 mask 像素值本身 — soft mask 用 scale mode + 极端阈值(0.99/0.01)让 gray-25 像素 → occupancy~90 → cost~229. 规划器强烈偏好留在环道(cost 0), 但可在锥桶完全堵死时 clip 穿软禁区.

### 7.3 动态控制 (competition_master)

| 操作 | mask topic | 触发条件 |
|------|-----------|----------|
| **启动重置** | `/keepout_mask` | `__init__`: 发布 reset 消息, 覆盖上轮残留 |
| **软化** | `/keepout_mask_soft` | 卡死检测: 4s 位移<0.03m + YOLO检测到锥桶(≥2帧/1.5s) + CRUISE_CHANNEL 状态 |
| **恢复** | `/keepout_mask` | 移动 >1.2m 离开软化点 |
| **震荡锁** | `/keepout_mask_soft` (锁定) | 软↔硬循环 ≥3次 → 本段保持软禁区, 优先穿行防死锁 |
| **重发布** | 当前 mask | 巡航/返航段每 2s 重发, 防 TRANSIENT_LOCAL 竞态覆盖 |
| **清 costmap** | — | 每次切 mask 后立即双清 (global+local), 让新 mask 即时生效 |

---

## 8. 死锁脱困

### 8.1 问题根源 (Nav2 #3186)

当 car footprint 进入 lethal 格 (障碍层锥桶致死或禁区致死):
1. `planner_server`: "Starting point in lethal space! Cannot create feasible plan." → 拒绝规划
2. `controller_server` (RPP): collision_detection → 输出 0 ("Collision Ahead") → 拒绝移动
3. `recoveries_server` (BackUp): 同样检测到碰撞 → "Collision Ahead" → 拒绝后退
4. **死锁闭环**: 全部拒绝移动, Nav2 无法自救

减小 inflation **救不了**: 内切 253 是 footprint 决定的 (footprint 大小固定), 与 inflation_radius 无关.

### 8.2 两级脱困

| 级别 | 机制 | 触发 | 原理 | 限制 |
|------|------|------|------|------|
| **1** | 软化禁区 | 卡死检测: 4s内位移<0.03m, 连续2次 | keepout 254→229, 规划器可 clip 穿行 | 仅救 keepout 致死, 不救障碍层锥桶致死 |
| **2** | 直驱倒车 | 软化后仍卡死 + CRUISE + YOLO检测到锥桶 | ★ 独占 /cmd_vel 直退 0.4m @ -0.12m/s, 10Hz 保活. **绕过所有 Nav2 碰撞检测** (planner/RPP/BackUp). 完成后清双 costmap + 保持软禁区 + 重发目标 | 2次/跑, 防死循环 |

### 8.3 卡死检测细节

- 频率: 1Hz
- 记录: 最近 5s pose history
- 判定: 3.5s 内位移 <0.03m → 真卡死 (非慢速过弯)
- 防误触: 仅 CRUISE_CHANNEL + YOLO锥桶(≥2帧/1.5s) 时软化
- RETURN_P / 无锥桶场景不软化 (无必要, 可能破坏正常导航)

### 8.4 防震荡

- 软化→恢复阈值: robot 移动 >1.2m 离开软化点 (reharden_clearance)
- 每段独立计数: soften_cycles 按段重置
- 震荡锁: ≥3 次软↔硬 → 本段保持软禁区 (优先穿行, 宁受+10s罚时也不死锁)
- 2026-07-07 修复: keepout 重发布必须发**当前** mask topic, 而非始终硬 mask (原来每2s悄悄恢复硬禁区, 反复取消软逃逸)

---

## 9. 速度曲线

[speed_profile_node.py](origincar/origincar_bringup/src/speed_profile_node.py) — 曲率自适应速度限制.

### 9.1 算法流程

```
/plan (全局路径) → Menger曲率 (3点法) → 移动平均平滑 (窗口=5)
  → v(κ) = v_max / (1 + β·|κ|^λ)   (GracefulController 公式)
  → 前向加速约束 (dv ≤ max_accel·dt)
  → 后向减速约束 (dv ≤ |max_decel|·dt)
  → 机器人当前位置前视 N 个路点 → /speed_limit (nav2_msgs/SpeedLimit)
```

### 9.2 参数 (17条CSV拟合, 1736数据点)

| 参数 | 值 | 说明 |
|------|-----|------|
| `v_max` | 0.50 | 直道速度上限 |
| `v_min` | 0.20 | 急弯安全下限 |
| `β` (曲率敏感度) | 0.25 | ★ 2026-07-08: 0.47→0.25, 弯道更快 |
| `λ` (降速形状) | 1.20 | ★ 2026-07-08: 1.32→1.20, 减速更平缓 |
| `max_accel` | 0.80 | m/s² (launch参数, 不同于代码默认1.01) |
| `max_decel` | -1.20 | m/s² |
| `smoothing_window` | 5 | 曲率移动平均窗口 |
| `lookahead_idx` | 10 | 前视路点数 |

**接口**: 发布 `/speed_limit` (nav2_msgs/SpeedLimit, percentage=false=绝对m/s). RPP `setSpeedLimit()` 在每路点覆盖 `desired_linear_vel`.
**调试**: 同步发布 `/speed_profile_debug` (Path, 速度编码在 pose.z, RViz 颜色映射).

> **2026-07-08 关键修复**: 原发布 `std_msgs/Float32`, 与 Nav2 controller_server 订阅的 `nav2_msgs/SpeedLimit` 类型不匹配 → ROS2 静默丢弃所有消息. 节点从 2026-07-01 部署以来 7 天从未真正生效. 已修正.

---

## 10. YOLO 障碍物检测

### 10.1 完整管线

```
Aurora930 RGB (BGR8, 640×400 @15fps)
  → racing_obstacle_detection_yolo (C++/BPU)
    FeedImg() → cv_bridge → BGR→NV12 (letterbox 640×640, 自动)
    → BPU YOLOv5s PTQ 推理 (~10ms, ~14fps)
    → NMS (score≥0.4, iou≤0.5, top_k=5000)
    → /racing_obstacle_detection (PerceptionTargets)
  → yolo_costmap_bridge (Python)
    ROI 中心 → /aurora/depth/image_raw 3×3 深度采样(中值)
    → 相机3D: x=(cx-CX)*z/FX, y=(cy-CY)*z/FY
    (深度=0 → bbox高度回退: z=FY*0.30m/bbox_h_px)
    → /tracked_obstacles_cloud (PointCloud2, depth_camera_link)
  → Nav2 costmap obstacle_layer (marking+clearing, 3.5m, 1.0s persistence)
```

### 10.2 BPU 模型

| 项目 | 值 |
|------|-----|
| 模型 | yolov5s_tag_v2.0_detect_640x640_bayese_nv12 |
| 权重文件 | `yolov5s_4_13.bin` (PTQ 后量化) |
| 输入 | NV12, 640×640, BPU DMA |
| 类别 | 1 类 ("obstacle") |
| 检测头 | 3 (strides=8,16,32), 标准 YOLOv5s anchors |
| 推理时间 | ~10ms (BPU) |
| 帧率 | ~14fps (含预处理) |

### 10.3 YOLO 用于卡死检测门控

competition_master 直接订阅 `/racing_obstacle_detection`, 记录检测时间戳:
- 持久性判断: ≥2帧/1.5s (滤除 YOLO 偶发假阳性)
- **软化禁区前必须确认 YOLO 检测到锥桶** — 防止 RETURN_P 或无锥桶场景误软化

---

## 11. QR 扫码系统

### 11.1 管线

```
Aurora930 RGB (BGR8)
  → qr_decoder_zbar (C++/ZBar)
    多尺度: 原分辨率 → 0.5× 降采样回退
    内容校验: min_qr_length
    深度滤波: advisory only (50-4000mm)
    → /sign (QR文本) + /sign_pose (odom帧)
  → qr_decision (Python)
    格式验证 (1-4位纯数字 1-9999)
    方向决策: odd=CW (顺时针), even=CCW (逆时针)
    冷却 3.0s
    → /qr_event ("1584,逆时针,x,y")
  → competition_master
    收到 /sign → cancel goal → wait 3s BT cleanup
    → kill qr_decoder_zbar → 等 /qr_event (2s超时)
    → 确定 CW/CCW → BACKING_UP → CRUISE_CHANNEL
```

### 11.2 设计要点

- **ZBar 符号迭代和 /sign 发布在同一 zbar::Image 上**: C++ 节点中符号迭代和结果发布在同一扫描周期内完成
- **深度过滤 advisory only**: Aurora930 RGB/Depth 帧率不同步, depth=0mm 时拒绝会导致有效 QR 被丢弃
- **qr_decision 轻量化**: 纯逻辑节点, 不编译图像 — 只依赖 C++ qr_decoder 的 `/sign` 输出
- **资源管理**: QR 检测后立即 pkill zbar (CPU密集), qr_decision 收到方向后也 pkill

---

## 12. VLM 图生文

### 12.1 管线

```
competition_master 到达 VLM 路点
  → /sign4return (Int32=100)
  → vision_ai_node
    匹配 target_sign → 单帧订阅 /aurora/rgb/image_jpeg (JPU硬件编码)
    → base64 编码 → Volcengine Ark API (ep-20260502193326-428m8)
    → /vlm_result (String, 异步)
  → competition_master: ★ 发 VLM 后立即转入 RETURN_P, 不等结果
```

### 12.2 优化

- **JPU 硬件编码**: `hobot_codec` BGR→JPEG 比 cv2.imencode 省 5-10ms/VLM 触发
- **Prompt**: 2026-07-08 按 rule.md 重写为医疗巡检场景 ("观察人形立牌, 描述姿态/着装/动作/场景特征, &lt;100字")
- **API**: Volcengine Ark SDK, 火山引擎. API key 通过 YAML 或环境变量 ARK_API_KEY

---

## 13. IMU 双路姿态估计

### 13.1 传感器架构

```
MPU6050 (底盘, STM32)
  → /imu/data_raw (100Hz, Mahony Ki=0 初处理)
  → imu_madgwick_filter (β=0.033, 100Hz)
  → /imu/data/madgwick → EKF imu0 (yaw姿态 + Z角速度)

BMI088 (RDK X5 板载, IIO:device1)
  → bmi088_iio_bridge (sysfs 轮询, 50Hz)
    手动 scale: gyro=0.00053 rad/s/LSB, accel=0.00341 m/s²/LSB
    2s 零偏校准 (200样本)
  → /imu_data → imu_madgwick_bmi088 (β=0.003, 50Hz)
  → /imu/data/bmi088_madgwick → EKF imu1 (仅 Z角速度, differential=true)
```

### 13.2 EKF 融合策略 (ekf_dual_imu.yaml, 15Hz)

| 传感器 | 模式 | 融合量 | 原因 |
|--------|------|--------|------|
| odom0 | differential | X位置, X/Y线速度, Z角速度 | 轮式里程计 20Hz |
| imu0 (MPU6050) | relative | Yaw姿态 + Z角速度 | 提供绝对 yaw 参考 (Madgwick β=0.033, 适度信任加速度计) |
| imu1 (BMI088) | **differential** | 仅 Z角速度增量 | ★ 避免双 yaw 冲突. BMI088 加速度计初始 yaw 因安装朝向偏差不可靠. 仅贡献汽车级陀螺角速度精度 (噪声 ~1/10 MPU6050) |

**关键参数**:
- frequency: 15Hz (20→15, A55 无法在50ms内完成 15×15 EKF + 双IMU)
- sensor_timeout: 0.2s (2026-07-08: 0.5→0.2, 15Hz=~3周期容差)
- two_d_mode: true
- imu0_twist_rejection_threshold: 1.542
- imu1_twist_rejection_threshold: 2.0 (放宽, 汽车级陀螺)
- yaw process_noise: 0.003 (双IMU, 低于单IMU的 0.005)
- imu0_queue_size: 30, imu1_queue_size: 20
- publish_tf: true (odom→base_footprint)

### 13.3 Madgwick 参数对比

| 参数 | MPU6050 | BMI088 | 原理 |
|------|---------|--------|------|
| β (gain) | 0.033 | 0.003 | β ∝ gyro_noise·√(BW). BMI088 噪声低 ~10×, 更信任陀螺 |
| 频率 | 100Hz | 50Hz | BMI088 54Hz 实际吞吐受 sysfs 轮询限制 |
| gyro_noise | 0.001 | 0.000244 | rad/s/√Hz (Bosch 0.014°/s/√Hz) |
| accel_noise | 0.05 | 0.010 | m/s² |

---

## 14. 行为树

### 14.1 NavigateToPose (navigate_to_pose_ackermann_rpp.xml)

```
RecoveryNode(retries=-1, 无限重试)
├── PipelineSequence (流水线: 规划与跟随可重叠执行)
│   ├── RateController(1.0Hz)  ← 最高杠杆参数: 0.5→1.0Hz, CRUISE -27%
│   │   └── RecoveryNode(1 retry)
│   │       ├── ComputePathToPose
│   │       └── Fallback: GoalUpdated | ClearGlobalCostmap  ← 仅失败时清图
│   └── RecoveryNode(1 retry)
│       ├── FollowPath
│       └── Fallback: GoalUpdated | (ClearLocalCostmap + Wait 0.5s)
└── RecoveryFallback (系统级恢复)
    └── RoundRobin
        ├── (ClearGlobal+Local + BackUp 0.8m @ 0.12m/s)  ← 窄通道锥桶脱困
        ├── Wait 3.0s  ← 给动态障碍物移走时间
        └── (ClearGlobal+Local + BackUp 1.5m @ 0.12m/s)  ← 二级大后退
```

### 14.2 NavigateThroughPoses (navigate_through_poses_ackermann_rpp.xml)

与 NavigateToPose 相同结构, 差异:
- ComputePathToPose → ComputePathThroughPoses
- 前加 RemovePassedGoals (radius=0.4m, base_footprint): 每轮重规划前移除已过路点
- 恢复时多一个 Wait(0.5s) after ClearGlobalCostmap

### 14.3 关键设计决策

| 决策 | 原因 |
|------|------|
| **移除 Spin** | 阿克曼不可原地旋转 (永久移除) |
| **移除 SmoothPath** | Humble ConstrainedSmoother 已知 NaN 崩溃 (nav2#4755); SmacPlanner 内置 smooth_path:true 替代 |
| **移除每周期 ClearEntireCostmap** | ★ 2026-07-07 恢复官方默认 BT. 每周期清图摧毁 cache_obstacle_heuristic (~40× 加速) + YOLO 累积障碍. 改为仅规划失败时清 |
| **RateController 1.0Hz** | 0.5Hz 时机器人每2s移动1.2m (0.60m/s), 超出 lookahead_dist(0.65m) → 追逐过期路径 → 冲入禁区 → 恢复惩罚 4-7s |
| **GoalUpdated 在恢复分支首位** | 若目标已变更则立即重规划, 不浪费时间在恢复上 |

---

## 15. 分析工具

所有工具位于 [originbot_navigation/tools/](originbot_navigation/tools/).

### 15.1 recalibrate_waypoints.py — 路点共识校准

**算法**:
1. 加载 `data/trajectories/` 所有 `final_state=="DONE"` 的 CSV
2. **质量过滤**: 丢弃 `CRUISE_CHANNEL > 40s` 的卡死运行 (点云噪声, 非可穿越走廊)
3. **逐路点逐运行最近点**: 对每个路点名找该运行对应阶段数据中离旧路点最近的点
4. **逐分量中位数**: 取所有运行 x 和 y 各自的中位数 (鲁棒抗离群)
5. **Snap-to-Free**: 若中位数落在 keepout 上, 螺旋搜索 (25格, 15°步) 最近可行驶格

**输出**: `trajectories_waypoints_calibrated.png` (叠加图) + stdout 新旧路点 delta 表 + 可直接粘贴到 `competition_master_stage3.py` 的参数块.

### 15.2 plot_trajectory.py — 4面板轨迹可视化

- 自动检测旧格式(4列)和新格式(14列: elapsed, x, y, yaw, state, cmd_vx, cmd_wz, plan_pts, plan_len, plan_end_x/y, cpu, mem, cpu_temp)
- **Map面板**: room.pgm 底图 + keepout_mask.pgm 红色叠加 + 状态着色轨迹 + 起终点标记 + 路点星标
- **分析面板**(新格式): 速度命令 + 规划器输出(plan点数+长度, 双轴) + 系统资源(CPU%/MEM%/CPU温度°C)
- 自动在多目录搜索最新 CSV (含 RDK X5 `/userdata/dev_ws`)

### 15.3 eval_trajectory.py — AMCL 定位精度验证

- 交互式 PGM-PNG 配准 (4角点 click → 透视变换)
- rosbag 解析 (支持 rosbags 库和 rosbag2_py)
- P点误差: 取最后 N 个 AMCL 位置均值, 计算与真值欧氏距离 (cm)
- 通道协方差: 通道边界框内 AMCL 协方差均值
- 输出: 3面板图 (warped PGM+AMCL, cropped PNG+AMCL, P点zoom+误差) + 评估报告 + AMCL CSV

### 15.4 centerline_extractor.py — Voronoi 骨架中线

- EDT (欧氏距离变换) + 形态学骨架化 → 1像素宽中线
- 可选 keepout 叠加 + robot_radius 膨胀
- 最大连通分量追踪 (端点→贪心方向优先→DFS 回退)
- 移动平均平滑 (窗口=3)
- 输出: `centerline.csv` (x_m, y_m) + `centerline.png`

---

## 16. 圈速演进

| 日期 | 圈速 | 关键变更 | 阶段 |
|------|------|----------|------|
| 2026-06-12 | **94.1s** | 初始基线: 首次完整跑通 QR+VLM+返航, RateController=1.0Hz | 基线确立 |
| 2026-06-14 | 77.3s | PID/mux 管线绕过, w_cusp tuning | "最优基线" |
| 2026-06-15 | **82.0s** ★ | **inflation 0.25→0.55** (RETURN_P 88.5s→21.1s, -76%) | 突破 |
| 2026-06-15 | 175.4s | 回归: desired=0.55 + inflation 回退 0.25 (0.25 是恐怖谷) | 失败 |
| 2026-06-16 | **70.1s** 🏆 | ★ **RateController 0.5→1.0Hz** (CRUISE -27%, 总 -14.5%) + regulated_linear_scaling_min_speed=0.0 + max_iter=1500 | **历史最优** |
| 2026-07-07 | **116.5s** | ★ 死锁脱困 A+B 修复 (软禁区+直驱倒车) + WP1校准 + 巡航→返航清图 + BT 仅失败时清 | 修复后首跑 |
| 2026-07-08 | — | ★ 传感器全栈优化: speed_profile 消息类型修复 (Float32→SpeedLimit), 路点共识校准 (15条DONE), collision 前视 0.35s, CycloneDDS, LiDAR TF 容差 0.5s, BMI088@50Hz, EKF timeout 0.2s, 弯道最低速 0.1→0.20, 速度曲线 β 0.47→0.25 | 持续优化中 |

### 关键教训

1. **inflation=0.25 是恐怖谷** (LRN-20260615-001): 足够大以混淆 10cm 分辨率规划器, 但不足以形成完整势场. 0.55 创造自然中线谷底, SmacPlanner 沿谷底走.
2. **一张 costmap 服务不了两种宽度** (LRN-20260707-001): inflation=0.55 在 0.5m 环道撑爆通道, 但在开阔大厅是 RETURN_P 的突破参数. 这是结构性问题, 不是参数问题.
3. **RateController 是 #1 优化杠杆** (LRN-20260705-002): 单参数 0.5→1.0Hz 降低 14.5% 总时间. 防止机器人超越自己的前视距离.

---

## 17. 已知问题与平台限制

### 17.1 Humble 特有 Bug

| Bug | Issue | 影响 | 缓解措施 |
|-----|-------|------|----------|
| **RPP 无 cusp 检测** | nav2#4757 | REEDS_SHEPP 尖角→换向→切角入禁区 | `change_penalty: 0.20` + `reverse_penalty: 4.0` 在 planner 层抑制换向 |
| **RPP cusp 前视点抖动** | nav2#5098 | 转向振荡 (wz=±1.22) | ★ Humble RPP 无 `use_fixed_curvature_lookahead` (Iron+ only), 此 bug 不适用! Jazzy 已修 (PR#5134) |
| **ConstrainedSmoother NaN** | nav2#4755 | Smoother 崩溃整个 Nav2 栈 | 已从 BT 移除; SmacPlanner 内置 `smooth_path:true` 替代 |
| **KeepoutFilter 忽略 base/multiplier** | - | `_soften_keepout(multiplier=0.4)` = 7天空操作 | ★ 软化靠 mask topic 切换 (像素值), 不靠 multiplier 参数 |
| **KeepoutFilter 缺 override_lethal_cost** | PR#5187 (Jazzy+) | 禁区内永久 lethal, 无官方自救 | 软 mask 方案 + 直驱倒车脱困 |
| **楞死死锁** | nav2#3186 | Footprint 进 lethal → 全部 Nav2 action 拒绝 | 直驱 /cmd_vel 倒车绕过碰撞检测 |
| **reverse_penalty 近目标失效** | nav2#6075 | 解析扩展忽略 reverse_penalty | 接受更高值 (4.0) 作用于搜索阶段 |
| **AMCL 无 AckermannMotionModel** | - | 仅 Differential + Omni | alpha 0.45 补偿运动模型失配; Ackermann约束由 REEDS_SHEPP+RPP 处理 |

### 17.2 RDK X5 硬件限制

| 限制 | 详情 | 缓解 |
|------|------|------|
| **CPU 75-100%** | A55×4 满负载运行 | Nav2 composition (消除 DDS 序列化) + ×3 降采样 + EKF 20→15Hz |
| **BMI088 IIO 轮询 ~46Hz** | Python sysfs 轮询, 无硬件中断 | 配置 50Hz 匹配硬件能力 |
| **inflation 0.5955 挤压窄道** | 全局 costmap 无法区分环道/大厅 | WP1 延长线偏移 + 软化禁区兜底 (§8) |
| **LiDAR 扫描时间戳超前 TF** | 5Hz LiDAR, scan 可早至 200ms 前 | `transform_tolerance: 0.5` (2026-07-08) |

### 17.3 开发陷阱

| 陷阱 | 说明 | 预防 |
|------|------|------|
| **CRLF** | Windows→Linux .py 文件 `\r` 残留 → `python3\r: No such file` | 每次上传后 `sed -i 's/\r$//' *.py` |
| **ROS2 install/ vs src/** | 部署到 `src/` 不 colcon build 是空操作 | 地图/配置部署后必须 `colcon build` |
| **TRANSIENT_LOCAL 跨运行持久化** | 上轮 disable 消息在重启后仍被重发 | 启动 `__init__` 发布 reset 消息 |
| **colcon build 需要 bash** | SSH dash 无 `source` 内置命令 | `bash -c 'source setup.bash && colcon build ...'` |
| **文件权限 644** | Windows→Linux 新文件 +x 缺失 | `chmod +x` 所有新 Python 节点 |
| **Python 节点 respawn** | competition_master crash → stale state → 重复 goal | respawn=true + 启动时 /costmap_ctrl reset |
| **巡航→返航不清 costmap** | 巡航段 LiDAR/YOLO 残留障碍带进 RETUN_P | `_through_result_cb` 成功分支无条件双清 |

---

## 18. 优化杠杆

### 18.1 提速

| 杠杆 | 当前值 | 方向 | 预期收益 | 风险 |
|------|--------|------|----------|------|
| `desired_linear_vel` | 0.50 | ↑ 0.55-0.60 | 全局加速 | 弯道刹不住, 冲出赛道 |
| `speed_profile β` | 0.25 | ↓ 0.15 | 弯道更快 | 冲出弯道 |
| `regulated_linear_scaling_min_speed` | 0.20 | ↑ 0.25 | 弯道出口更快 | 窄弯不可控 |
| `lookahead_dist` | 0.678 | ↓ 0.60 | 跟线更紧 (激进) | <0.60m 违反 Ackermann 约束 |
| `inflation_radius` (local) | 0.55 | ↓ 0.40 | 窄道更宽, 少软化 | 开阔段贴墙风险 |
| `cost_penalty` | 6.33 | ↑ 8-10 | 路径更居中 | 窄道可能找不到路 |
| `max_iterations` | 1500 | ↑ 2000 | 更优路径 | 规划延迟增加 |
| `max_planning_time` | 1.596s | ↑ 2.0s | 允许更复杂路径 | 路径时效性降低 |
| `cost_scaling_gain` | 1.5 | ↓ 1.0 | cost 区减速更弱 | 碰撞风险增加 |

### 18.2 路点优化

| 杠杆 | 方法 |
|------|------|
| WP 位置 | 沿 postVLM→WP1 延长线偏移, 避开窄口 |
| WP 间距 | 均匀分布, 避免相邻 WP 跨越 inflation 挤压区 |
| 共识校准 | `recalibrate_waypoints.py` 自动从 DONE 轨迹校准 |
| **不要加密路点** | 更多路点 = 更多 cusp 点 (Humble RPP #4757), 反效果 (LRN-20260615-002) |

### 18.3 禁区控制

| 杠杆 | 方法 | 当前值 |
|------|------|--------|
| 软化阈值 | `reharden_clearance`: 越大越安全, 越少震荡 | 1.2m |
| 软 mask 浓度 | 调 keepout_mask_soft.pgm 灰度值 | gray-25 → occupancy~90 → cost~229 |
| 震荡锁 | `_max_soften_cycles`: 超过则本段锁定软禁区 | 3 |
| 卡死判定窗口 | 位移阈值和时间 | <0.03m / 3.5s |

### 18.4 架构升级 (需代码改动)

| 方向 | 描述 | 复杂度 |
|------|------|--------|
| **双 inflation/区域 costmap** | 环道 0.15, 大厅 0.55 — 用 KeepoutFilter 做区域 masking | 高 |
| **VoxelLayer 替代 ObstacleLayer** | Nav2 官方推荐, 3D→2D 投影更智能 | 中 |
| **MPPI 替代 RPP** | 有 cusp 检测 (#5098 已在 MPPI 中修复), 更优控制 | 高 (需 cross-compile C++) |
| **speed_profile β/λ 在线自适应** | 根据实时弯道表现调参 | 中 |

---

## 19. 部署流程

### 19.1 环境

| 项目 | 值 |
|------|-----|
| 目标 | RDK X5, 192.168.31.59:22, root |
| 工作空间 | `/userdata/dev_ws/` (主), `/userdata/ros_ws/` (Aurora930 驱动, 独立) |
| RMW | CycloneDDS (SHM zero-copy, 官方推荐) |
| 编辑环境 | Windows → WSL2 |

### 19.2 部署步骤

```bash
# 1. 本地打包 (Windows/WSL2)
cd /mnt/c/Users/27826/Desktop/src
tar czf deploy.tar.gz \
  origincar/ originbot_navigation/ qr_decoder/ \
  racing_obstacle_detection_yolo/ racing_vision_ai/

# 2. 上传到 RDK X5
# 方法A: MCP SSH (VS Code)
#   mcp__ssh-manager__ssh_deploy: server="myserver", options={backup:true}
# 方法B: sshpass
sshpass -p 'root' scp deploy.tar.gz root@192.168.31.59:/userdata/dev_ws/

# 3. 远程解压 + CRLF修复 + 权限
ssh root@192.168.31.59 "
  cd /userdata/dev_ws/src
  tar xzf /userdata/dev_ws/deploy.tar.gz
  find . -name '*.py' -exec sed -i 's/\r$//' {} \;
  find . -name '*.py' -exec chmod +x {} \;
"

# 4. 编译
# C++ 包 (~90s)
ssh root@192.168.31.59 \
  "bash -c 'source /opt/ros/humble/setup.bash && cd /userdata/dev_ws && colcon build --packages-select qr_decoder racing_obstacle_detection_yolo'"

# Python 包 (~3s)
ssh root@192.168.31.59 \
  "bash -c 'source /opt/ros/humble/setup.bash && cd /userdata/dev_ws && colcon build --packages-select origincar_bringup originbot_navigation racing_vision_ai'"

# 5. 运行
ssh root@192.168.31.59
cd /userdata/dev_ws
source install/setup.bash
ros2 launch origincar_bringup stage3_bringup.launch.py
```

### 19.3 关键检查清单

- [ ] `.py` 文件无 `\r` (CRLF): `file *.py | grep CRLF`
- [ ] `.py` 文件有 +x: `ls -la *.py`
- [ ] 地图文件在 `install/` 中: `ls install/originbot_navigation/share/originbot_navigation/maps/`
- [ ] `colcon build` 成功无错误
- [ ] `/costmap_ctrl` topic 列出: `ros2 topic list | grep costmap_ctrl`
- [ ] YOLO config 路径正确: `/userdata/dev_ws/src/origincar/origincar_bringup/config/yolov5workconfig.json`

---

## 20. 关键文件索引

### 20.1 必读文件

| 文件 | 用途 |
|------|------|
| [origincar/origincar_bringup/src/competition_master_stage3.py](origincar/origincar_bringup/src/competition_master_stage3.py) | ★ 状态机 (最核心文件, ~1784行) |
| [originbot_navigation/param/originbot_nav2_rpp.yaml](originbot_navigation/param/originbot_nav2_rpp.yaml) | ★ 全部 Nav2 参数 (~425行) |
| [origincar/origincar_bringup/launch/stage3_bringup.launch.py](origincar/origincar_bringup/launch/stage3_bringup.launch.py) | ★ 总启动文件 (时序编排) |
| [originbot_navigation/behavior_trees/navigate_through_poses_ackermann_rpp.xml](originbot_navigation/behavior_trees/navigate_through_poses_ackermann_rpp.xml) | ★ 多路点行为树 |
| [originbot_navigation/behavior_trees/navigate_to_pose_ackermann_rpp.xml](originbot_navigation/behavior_trees/navigate_to_pose_ackermann_rpp.xml) | 单目标行为树 |

### 20.2 代码文件

| 文件 | 功能 |
|------|------|
| [origincar/origincar_bringup/src/speed_profile_node.py](origincar/origincar_bringup/src/speed_profile_node.py) | 曲率→速度曲线 |
| [origincar/origincar_bringup/src/yolo_costmap_bridge.py](origincar/origincar_bringup/src/yolo_costmap_bridge.py) | YOLO→costmap桥接 |
| [origincar/origincar_bringup/src/bmi088_iio_bridge.py](origincar/origincar_bringup/src/bmi088_iio_bridge.py) | BMI088 IIO驱动 |
| [origincar/origincar_bringup/src/imu_madgwick_filter.py](origincar/origincar_bringup/src/imu_madgwick_filter.py) | Madgwick 姿态滤波 |
| [origincar/origincar_base/src/origincar_base.cpp](origincar/origincar_base/src/origincar_base.cpp) | STM32 串口驱动 |
| [qr_decoder/src/qr_decoder.cpp](qr_decoder/src/qr_decoder.cpp) | ZBar QR 解码 |
| [qr_decoder/qr_decision.py](qr_decoder/qr_decision.py) | QR 方向决策 |
| [racing_obstacle_detection_yolo/src/sample.cpp](racing_obstacle_detection_yolo/src/sample.cpp) | YOLO BPU 推理 |
| [racing_vision_ai/racing_vision_ai/vision_ai_node.py](racing_vision_ai/racing_vision_ai/vision_ai_node.py) | VLM 云端推理 |
| [origincar/origincar_bringup/src/telemetry_recorder.py](origincar/origincar_bringup/src/telemetry_recorder.py) | 5Hz 遥测记录 |

### 20.3 配置文件

| 文件 | 功能 |
|------|------|
| [origincar/origincar_base/config/ekf_dual_imu.yaml](origincar/origincar_base/config/ekf_dual_imu.yaml) | 双IMU EKF |
| [origincar/origincar_base/config/imu_madgwick_bmi088.yaml](origincar/origincar_base/config/imu_madgwick_bmi088.yaml) | BMI088 Madgwick |
| [origincar/origincar_base/config/imu_madgwick.yaml](origincar/origincar_base/config/imu_madgwick.yaml) | MPU6050 Madgwick |
| [origincar/origincar_bringup/config/yolov5workconfig.json](origincar/origincar_bringup/config/yolov5workconfig.json) | YOLO BPU 模型配置 |
| [racing_vision_ai/config/vision_ai_config.yaml](racing_vision_ai/config/vision_ai_config.yaml) | VLM API 配置 |
| [originbot_navigation/maps/room.yaml](originbot_navigation/maps/room.yaml) | 静态地图 |
| [originbot_navigation/maps/keepout_mask.yaml](originbot_navigation/maps/keepout_mask.yaml) | 硬禁区 |
| [originbot_navigation/maps/keepout_mask_soft.yaml](originbot_navigation/maps/keepout_mask_soft.yaml) | 软禁区 |

### 20.4 工具与文档

| 文件 | 功能 |
|------|------|
| [Z_MD/todo.md](Z_MD/todo.md) | 工作规范, 陷阱清单, 部署流程 (权威工作规范) |
| [Z_MD/log.md](Z_MD/log.md) | 运行时 ROS2 日志 |
| [Z_MD/wiki.md](Z_MD/wiki.md) | 问题排查与修复记录 |
| [.learnings/LEARNINGS.md](.learnings/LEARNINGS.md) | 结构化经验库 (~40条目) |
| [.learnings/ERRORS.md](.learnings/ERRORS.md) | 错误与修复记录 (~13条目) |
| [originbot_navigation/tools/recalibrate_waypoints.py](originbot_navigation/tools/recalibrate_waypoints.py) | 路点共识校准 |
| [originbot_navigation/tools/plot_trajectory.py](originbot_navigation/tools/plot_trajectory.py) | 轨迹可视化 |
| [originbot_navigation/tools/eval_trajectory.py](originbot_navigation/tools/eval_trajectory.py) | AMCL 精度验证 |
| [originbot_navigation/tools/centerline_extractor.py](originbot_navigation/tools/centerline_extractor.py) | 中线提取 |
| [data/trajectories/](data/trajectories/) | 29条历史运行轨迹 CSV+JSON |
| [data/rosbags/](data/rosbags/) | 7个 rosbag 记录 |

---

## 附录: 包清单

| 包 | 位置 | 语言 | 职责 |
|----|------|------|------|
| `origincar_bringup` | `origincar/origincar_bringup/` | Python + C++ | 启动编排 + 状态机 + 速度曲线 + YOLO桥接 + IMU桥 |
| `origincar_base` | `origincar/origincar_base/` | C++ + Python | STM32 串口驱动 + EKF + Madgwick 配置 |
| `originbot_navigation` | `originbot_navigation/` | YAML/XML/Python | Nav2 参数 + 行为树 + 地图 + 禁区 + 分析工具 |
| `qr_decoder` | `qr_decoder/` | C++ + Python | ZBar QR 解码 + 方向决策 |
| `racing_obstacle_detection_yolo` | `racing_obstacle_detection_yolo/` | C++ | YOLOv5s BPU 推理 (RDK X5) |
| `racing_vision_ai` | `racing_vision_ai/` | Python | VLM 云端推理 (Volcengine Ark) |
| `origincar_description` | `origincar/origincar_description/` | URDF/Xacro | 机器人 URDF 模型 |
| `origincar_msg` | `origincar/origincar_msg/` | ROS2 IDL | 自定义消息定义 |
| `origincar/utils` | `origincar/utils/` | C++ | 图像传输工具 |
| `lslidar_driver` | `Lslidar_ROS2_driver-N10_V1.0/` | C++ | Leishen N10 LiDAR 驱动 |
| `ackermann_msgs` (3rdparty) | `origincar/3rdparty/` | ROS2 IDL | Ackermann 消息定义 |
| `serial_ros2` (3rdparty) | `origincar/3rdparty/` | C++ | 跨平台串口库 |
| **外部** | | | |
| `deptrum-ros-driver-aurora930` | `/userdata/ros_ws/` (独立) | C++ | Aurora930 深度相机驱动 |

---

> **维护**: 本 README 基于 2026-07-09 4 Agent 并行全项目审查生成. 代码变更后请同步更新.
> **相关记忆**: [项目 memory](C:\Users\27826\.claude\projects\c--Users-27826-Desktop-src\memory\MEMORY.md) — 21 条结构化项目知识.
