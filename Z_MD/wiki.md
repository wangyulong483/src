# 外部项目深度分析 Wiki

> **分析日期**: 2026-07-09
> **分析项目**: ackermann_car-main, racing_control-develop, rdkx5-smart-medical-car--main
> **对照项目**: Origincar Pro (RDK X5 + ROS2 Humble + Nav2)

---

## 目录

1. [ackermann_car-main — ROS2 Ackermann 仿真模板](#1-ackermann_car-main)
2. [racing_control-develop — 地平线赛道巡线控制](#2-racing_control-develop)
3. [rdkx5-smart-medical-car — 清越队同级竞赛方案](#3-rdkx5-smart-medical-car)
4. [多项目交叉对比](#4-多项目交叉对比)
5. [可采纳优化清单](#5-可采纳优化清单)

---

## 1. ackermann_car-main

**来源**: 开源 ROS2 Ackermann 仿真项目
**结构**: 1 包 (ackermann_car) × 7 Python 节点 + Gazebo Ignition 仿真
**用途**: Nav2 阿克曼导航教学/仿真模板

### 1.1 Nav2 参数对比

#### Planner (SmacPlannerHybrid)

| 参数 | ackermann_car | Origincar Pro (我们) | 差异分析 |
|------|---------------|----------------------|----------|
| `motion_model_for_search` | REEDS_SHEPP | REEDS_SHEPP | 相同 |
| `minimum_turning_radius` | 0.30 | 0.30 | 相同 |
| `angle_quantization_bins` | **72** | 40 | ★ 他们更精细: 72 bins = 5°/bin, 我们 40 = 9°/bin. 更多bin→更平滑路径但更慢规划 |
| `max_iterations` | **1,000,000** | 1500 | ★ 极端差异! 仿真 vs 嵌入式的取舍 |
| `max_planning_time` | **5.0s** | 1.596s | 仿真不着急, RDK X5 必须省 CPU |
| `analytic_expansion_ratio` | **2.5** | 4.0 | 他们更频繁解析扩展 (更激进尝试直连目标) |
| `analytic_expansion_max_length` | **2.5** | 1.5 | 更长解析扩展步长 |
| `reverse_penalty` | 4.0 | 4.0 | 相同 |
| `change_penalty` | **0.25** | 0.20 | 他们更抑制换向 (cusp 更少但灵活性更低) |
| `non_straight_penalty` | **1.3** | 1.8469 | ★ 他们接近官方推荐 (1.0-1.3), 我们偏离较大 |
| `cost_penalty` | **3.5** | 6.33 | ★ 他们对代价敏感度低得多 (更激进贴墙) |
| `retrospective_penalty` | **0.015** | — | ★ 我们没有! 逆时惩罚可避免规划绕圈 |
| `cache_obstacle_heuristic` | **false** | true | 他们不缓存 (仿真不需要), 我们缓存获 ~40× 加速 |
| `downsample_costmap` | **false** | true | 他们不降采样, 我们 ×3 |
| `allow_unknown` | **true** | false | ★ 他们允许穿越未知区域 (仿真安全), 我们严禁 |
| `tolerance` | **0.25** | 默认 | 目标容差 |
| `lookup_table_size` | **20.0** | 默认 | 预计算查找表 |

**关键教训**:
- `angle_quantization_bins: 72` 值得在我们项目测试: 更精细角度→更平滑 REEDS_SHEPP 路径, 可能减少 cusp. 但代价是规划时间 (A55 可能承受不起)
- `non_straight_penalty: 1.3` (vs 我们的 1.85): 他们鼓励适当转弯, 我们的 1.85 过度惩罚所有转弯可能导致路径僵硬
- `cost_penalty: 3.5` (vs 我们的 6.33): 我们过于保守, 可能把规划器推向不必要的绕行
- `retrospective_penalty: 0.015`: **我们缺少此参数**, 可防止规划器在原地绕圈

#### Controller (Regulated Pure Pursuit)

| 参数 | ackermann_car | Origincar Pro (我们) | 差异分析 |
|------|---------------|----------------------|----------|
| `controller_frequency` | **20.0 Hz** | 10.0 Hz (默认) | ★ 他们双倍控制频率! |
| `desired_linear_vel` | 0.20 | 0.50 | 仿真保守速度 |
| `lookahead_dist` | **0.45** | 0.6776 | 他们更短前视 (更激进跟线) |
| `min_lookahead_dist` | **0.20** | 0.2628 | |
| `max_lookahead_dist` | **0.65** | 0.8067 | |
| `lookahead_time` | 1.5 | 1.2415 | |
| `use_fixed_curvature_lookahead` | **false** | true | ★ 他们不用固定曲率前视! |
| `curvature_lookahead_dist` | 0.4 | 0.8 | |
| `max_allowed_time_to_collision` | **2.0** | 0.35 | ★ 极端差异: 他们 2.0s(模拟), 我们 0.35s(窄道实战) |
| `regulated_linear_scaling_min_radius` | **0.25** | 0.411 | 他们更早减速 |
| `regulated_linear_scaling_min_speed` | 0.10 | 0.20 | |
| `use_collision_detection` | true | true | |
| `allow_reversing` | true | true | |
| `max_angular_vel` | **1.2** | 默认 | 有明确的角速度限制 |
| `speed_lim_angular` | **true** | — | ★ 我们没有! 弯道时同时限制角速度 |
| `min_approach_linear_velocity` | **0.05** | — | 接近目标时最低速度 |
| `approach_velocity_scaling_dist` | **0.6** | — | 0.6m 内开始减速进场 |
| `max_robot_pose_search_dist` | **10.0** | — | 路径上搜索最近点的最大距离 |

**关键教训**:
- `controller_frequency: 20Hz` → **高优先级测试**: 我们的 10Hz 对 0.50m/s 巡航可能不够 (每周期移动 5cm)
- `use_fixed_curvature_lookahead: false` → 他们不用. ★ Humble 无此功能 (Iron+ only), 我们 YAML 的值被静默忽略了 7 个月 (2026-07-09 audit 确认)
- `speed_lim_angular: true` → 我们没有但应该有 — 弯道处同时限制角速度防止侧滑
- `approach_velocity_scaling_dist: 0.6` → 我们没有显式进场减速, 完全靠 speed_profile_node 覆盖

#### Local Costmap

| 参数 | ackermann_car | Origincar Pro (我们) | 差异分析 |
|------|---------------|----------------------|----------|
| `update_frequency` | **20.0 Hz** | 5.0 Hz | ★ 4× 更新频率 |
| `publish_frequency` | 10.0 Hz | 2.0 Hz | 5× 发布频率 |
| `width × height` | **6m × 6m** | 3m × 3m | ★ 2× 尺寸: 更大的局部视野 |
| `rolling_window` | true | true | |
| `plugins` | **voxel_layer** + inflation | obstacle + keepout + inflation | ★ 他们用 VoxelLayer! |
| `inflation_radius` | **0.40** | 0.55 | 他们更小 (更激进) |
| `cost_scaling_factor` | 3.0 | 2.0 | 他们衰减更快 |
| `footprint` | [0.20,0.14] × 4 | [0.15,-0.10]→[-0.12,-0.10] | 他们对称矩形 |
| `footprint_padding` | 0.05 | — | 他们有膨胀 |
| `transform_tolerance` | 1.0 | 0.5 | 他们更宽容 |

**关键教训**:
- **VoxelLayer 替代 ObstacleLayer**: 3D→2D 投影更智能, 可过滤地面点. 但 RDK X5 CPU 能否承受?
- `local_costmap 6m×6m` + `global_frame: odom`: 更大的局部视野让 RPP 看到更远的障碍. 我们 3m×3m 可能不够 (以 0.5m/s 只需 6s 穿越)
- `footprint_padding: 0.05`: 机器人轮廓额外膨胀, 我们没有但有 inflation 0.55 补偿

#### Global Costmap

| 参数 | ackermann_car | Origincar Pro (我们) | 差异分析 |
|------|---------------|----------------------|----------|
| `update_frequency` | 3.0 Hz | 1.0 Hz | 3× 更新频率 |
| `publish_frequency` | 3.0 Hz | 1.0 Hz | 3× |
| `inflation_radius` | **0.40** | 0.5955 | ★ 重要差异 |
| `cost_scaling_factor` | 3.0 | 2.8637 | 接近 |
| `track_unknown_space` | **true** | — | ★ 我们没开启 |
| `plugins` | static+obstacle+inflation | static+obstacle+keepout+inflation | 他们有3个, 我们有4个(+keepout) |

#### AMCL

| 参数 | ackermann_car | Origincar Pro (我们) | 差异分析 |
|------|---------------|----------------------|----------|
| `alpha1-4` | **0.15-0.2** | 0.45 (uniform) | ★ 他们噪声模型小得多 |
| `update_min_a` | **0.01** | 0.1 | ★ 他们频繁更新 (10× 更敏感) |
| `update_min_d` | **0.01** | 0.1 | ★ 同上 |
| `resample_interval` | **1** | 2 | 他们每次重采样 (粒子多样化) |
| `max_particles` | 2000 | 1500 | |
| `min_particles` | 500 | 300 | |
| `sigma_hit` | 0.2 | — | 他们定义击中噪声 |
| `laser_likelihood_max_dist` | 2.0 | — | 似然计算最大距离 |
| `recovery_alpha_fast/slow` | 0.0 | — | 无快速恢复 |
| `beam_skip_*` | 已配置 | — | 他们配置了跳束 (但 do_beamskip=false) |

**关键教训**:
- `alpha: 0.15-0.2` (vs 我们的 0.45): 我们噪声模型过大 — 过度补偿运动模型失配. 如果 EKF 输出可靠, 可以尝试 0.2-0.3
- `update_min_a/d: 0.01` (vs 我们的 0.1): 他们几乎每帧更新. 我们的 0.1 可能让粒子在不同步的 LiDAR scan 前落后

### 1.2 行为树

```xml
<!-- ackermann_car 行为树 (简版) -->
<RecoveryNode retries="6">              <!-- ★ 有限重试 -->
  <PipelineSequence>
    <RateController hz="1.0">           <!-- 同我们 -->
      <RecoveryNode retries="1">
        <ComputePathToPose/>
        <ClearEntireCostmap name="ClearGlobalCostmap"/>  <!-- ★ 每规划失败清全图 -->
      </RecoveryNode>
    </RateController>
    <RecoveryNode retries="1">
      <FollowPath/>
      <ClearEntireCostmap name="ClearLocalCostmap"/>     <!-- ★ 每跟随失败清局部 -->
    </RecoveryNode>
  </PipelineSequence>
  <ReactiveFallback>                    <!-- ★ 他们用 ReactiveFallback! -->
    <GoalUpdated/>
    <RoundRobin>
      <Sequence>                        <!-- 先双清清图 -->
        <ClearLocal/>
        <ClearGlobal/>
      </Sequence>
      <BackUp dist="0.15" speed="0.025"/>  <!-- ★ 超保守: 0.15m @ 0.025m/s -->
      <Wait duration="5"/>
    </RoundRobin>
  </ReactiveFallback>
</RecoveryNode>
```

**与我们 BT 的关键差异**:

| 方面 | ackermann_car | Origincar Pro |
|------|---------------|---------------|
| 恢复次数 | **6** (有限) | 无限 (-1) |
| 恢复fallback | **ReactiveFallback** | RecoveryFallback |
| BackUp 距离 | **0.15m** (极短) | 0.8m → 1.5m |
| BackUp 速度 | **0.025m/s** (极慢) | 0.12m/s |
| 每周期清图 | **是** (清全局) | 否 (仅失败时) |
| SmoothPath | 无 | 无 (已移除) |
| Spin | 无 | 无 (阿克曼不可转) |

**关键教训**:
- `ReactiveFallback` vs `RecoveryFallback`: Reactive 一旦有子节点成功就停止 (更响应式); Recovery 执行所有子节点. 我们应用 Reactive 在 GoalUpdated 场景
- `ClearGlobalCostmap` 每规划失败 (他们) vs 我们每周期 BT 成功时不清. 我们已改为仅失败时清 — 正确
- BackUp 0.15m@0.025m/s 在仿真中工作 (没有物理约束), 实战中太慢 — 我们的 0.8m 更有意义

### 1.3 阿克曼运动学实现

**ackermann_controller.py** — 这是我们项目**最大的缺失模块**:

```python
# 核心方程式
R = L / tan(delta)           # 自行车模型转弯半径
R_inner = R - d/2            # 内轮转弯半径
R_outer = R + d/2            # 外轮转弯半径
delta_inner = atan(L / R_inner)  # 内轮转角 (更大)
delta_outer = atan(L / R_outer)  # 外轮转角 (更小)
v_inner = v * (R - d/2) / R      # 内轮线速度 (更慢)
v_outer = v * (R + d/2) / R      # 外轮线速度 (更快)
```

**我们项目的状态**: STM32 通过 `cmd_vel_to_ackermann_drive.py` 将 Twist→AckermannDrive (`steering = atan(wheelbase * omega / vel)`, `wheelbase=0.143m`), 然后发 11 字节二进制帧. STM32 自己做舵机/差速控制. **不需要** `ackermann_controller.py` 这样的全运动学解算.

但 `ackermann_controller.py` 的价值:
- **Watchdog 0.5s**: 超时自动停车 (我们有类似机制 — cmd_vel mux timeout 0.5s, 但已移除 mux)
- **转向限幅**: `max_steer=0.70 rad (~40°)`, 我们的 STM32 直接接收 steering 不做限幅 **(潜在风险)**
- **差速解算参考**: 后轮差速公式可用于 STM32 固件优化

### 1.4 Twist→Ackermann 桥接

```python
# nav2_ackermann_bridge.py (ackermann_car-main) 和 twist_to_ackermann.py
delta = atan(L * omega / v)  # L=0.30m
delta = clamp(delta, -0.7, 0.7)
```

对比我们的 `cmd_vel_to_ackermann_drive.py`:
```python
steering = atan(wheelbase * omega / vel)  # wheelbase=0.143m
steering_sign = -1.0  # ROS CCW→STM32 CW 符号转换
```

差异: 他们的 wheelbase=0.30m, 我们的=0.143m. 我们的更短轴距 → 相同 omega/v 下的 steering 角更小 → 更敏捷转向. 他们的限幅 ±0.7rad, 我们没有显式限幅.

### 1.5 URDF 模型参数

| 参数 | ackermann_car | Origincar Pro |
|------|---------------|---------------|
| 车长 | 0.40m | 0.276m |
| 车宽 | 0.20m | 0.164m |
| 车高 | 0.08m | 0.08m |
| wheelbase | 0.30m | 0.143m |
| track_width | 0.28m | — |
| wheel_radius | 0.05m | — |
| max_steer | ±0.70 rad (40°) | ±28° (~0.49 rad) |
| chassis_mass | 2.0 kg | — |
| ros2_control | ✅ Ignition | ❌ (STM32 直驱) |

### 1.6 SLAM 配置

他们包含完整的 `slam_toolbox` 在线+离线 SLAM 配置:
- `slam_toolbox.yaml`: 离线建图 (2D LiDAR SLAM, 40m max_range)
- `slam_toolbox_online.yaml`: 在线 SLAM (降低分辨率以提速)

我们项目使用预先构建的静态地图 (`room.yaml`), 不使用 SLAM. 这是正确的 — 比赛场地固定.

---

## 2. racing_control-develop

**来源**: 地平线官方 TROS Racing Control 包 (C++ 实现)
**功能**: 赛道中线巡线 + 锥桶避障
**适用场景**: 有视觉车道线+锥桶的竞速赛道 (非我们的医疗巡检场景)

### 2.1 核心算法

#### 巡线控制 (LineFollowing)

```cpp
// 输入: 赛道中线检测结果 (image coordinates)
int x = point_msg.points[0].point[0].x;  // 检测到的中点 x 坐标
int y = point_msg.points[0].point[0].y;  // 检测到的中点 y 坐标 (距离)

float temp = x - 320.0;  // 相对于图像中心 (640×...)
// 死区: ±20px
if ((-20 < x) && (x < 0)) temp = -20;
else if ((x > 0) && (x < 20)) temp = 20;

// 核心公式:
angular_z = follow_angular_ratio * temp / 150.0 * y / 224.0;
//          = -1.0 * (x-320) / 150 * y / 224
linear.x = follow_linear_speed;  // 固定 1.5 m/s!
```

**算法分析**:
- `temp/150`: 归一化横向偏差 (150px = 半幅)
- `y/224`: 距离加权 (远处偏越大→转向越小, 近处偏越小→转向越大) ← **反直觉!** 正常应该远处偏→转向更温和 (前瞻). 这里 y 在分母位置导致距越近转向越大 — 可能是 bug 或特定赛道调参
- `follow_linear_speed=1.5m/s`: 非常激进! 我们巡航 0.50m/s
- Dead zone ±20px: 小偏差不转向, 防抖动

#### 避障控制 (ObstaclesAvoiding)

```cpp
int center_x = target.rois[0].rect.x_offset + target.rois[0].rect.width / 2;
float temp = center_x - 320.0;  // 障碍物相对图像中心

// 核心公式:
angular_z = avoid_angular_ratio * 700 / temp;
//          = 1.1 * 700 / (center_x - 320)
linear.x = avoid_linear_speed;  // 固定 0.25 m/s
```

**算法分析**:
- `700/temp`: **反比控制** — 障碍物离中心越近, 转向越大 (远离障碍物)
- 若障碍物在左边 (temp<0) → angular_z<0 → 右转避开 ✅
- `avoid_linear_speed=0.25`: 避障时减速
- **问题**: 没有前向障碍物检测 (正前方障碍物 temp≈0 → 除零!), 依赖 bottom_threshold 做深度过滤

#### 优先级仲裁

```cpp
// 1. 无锥桶 → 巡线
// 2. 有锥桶 + 深度不够(bottom < bottom_threshold) → 巡线 (锥桶太远)
// 3. 有锥桶 + 置信度不够 → 巡线
// 4. 有锥桶 + 深度够 + 置信度够 → 避障
```

这是一个简单但有效的仲裁策略 — 和我们 YOLO 卡死检测门控逻辑类似 (≥2帧/1.5s 才触发软化).

### 2.2 与我们的对比

| 方面 | racing_control | Origincar Pro |
|------|----------------|---------------|
| 控制方式 | 视觉中线跟踪 (类PID) | Nav2 RPP + 全局路径 |
| 速度来源 | 固定线速度 | speed_profile_node 曲率自适应 |
| 避障策略 | 图像坐标反比转向 | YOLO→costmap→RPP碰撞检测 |
| 框架 | 单独 C++ 节点 | 完整 Nav2 栈 |
| 巡航速度 | **1.5 m/s** | 0.50 m/s |
| 适用场景 | 结构化赛道+车道线 | 无车道线的自由导航 |

### 2.3 可借鉴点

1. **Dead zone (±20px) 概念**: 我们 speed_profile_node 无 dead zone — 微小曲率变化也可能导致速度抖动. 可加曲率 dead band
2. **深度门控避障**: bottom_threshold 过滤远处障碍物 — 我们已有类似 (YOLO 置信度+帧数). 但我们的 depth 采样在 yolo_costmap_bridge 中不考虑距离过滤
3. **动态参数**: 他们的参数通过 ROS2 parameter 机制动态获取 (每轮 MessageProcess 都 get_parameter) — 可在线调参
4. **反比避障公式**: `1.1 * 700 / (center_x - 320)` — 转向强度与障碍物偏移成反比, 比固定转向更平滑

---

## 3. rdkx5-smart-medical-car (清越队) — 全文件深度分析

**队伍**: 清越 / 河北建筑工程学院 / 本科组
**平台**: RDK X5 + ROS2 Humble
**方案**: 纯 Python 实现, 无 Nav2, 无 BPU 推理, 无 SLAM
**规模**: 5 packages × 8 Python nodes, ~800 行核心逻辑

### 3.1 项目全景

#### 3.1.1 完整文件清单 (35个文件)

```
rdkx5-smart-medical-car--main/
├── README.md / README_cn.md
├── LICENSE
├── .gitignore
└── ros2_ws/
    ├── README.md / README_cn.md
    ├── requirements.txt
    ├── install_dependencies.sh
    ├── docs/技术文档.md              ← 完整竞赛技术文档 (550行)
    └── src/
        ├── task_manager/             ← 任务编排 (1 Python node)
        │   ├── task_manager/task_manager_node.py
        │   ├── launch/task_manager.launch.py
        │   ├── launch/competition.launch.py   ← 总启动: IncludeLaunchDescription 组合
        │   ├── setup.py, package.xml
        │   └── resource/task_manager
        ├── navigation/               ← 导航三件套 (3 Python nodes)
        │   ├── navigation/path_planner_node.py
        │   ├── navigation/motion_controller_node.py
        │   ├── navigation/obstacle_avoidance_node.py
        │   ├── config/navigation_params.yaml
        │   ├── launch/navigation.launch.py
        │   ├── setup.py, package.xml
        │   └── resource/navigation
        ├── qr_detector/              ← QR扫码 (1 Python node)
        │   ├── qr_detector/qr_detector_node.py
        │   ├── launch/qr_detector.launch.py
        │   ├── setup.py, package.xml
        │   └── resource/qr_detector
        ├── human_detector/           ← 人形检测+大模型 (2 Python nodes)
        │   ├── human_detector/human_detector_node.py
        │   ├── human_detector/llm_interface_node.py
        │   ├── launch/human_detector.launch.py
        │   ├── setup.py, package.xml
        │   └── resource/human_detector
        └── voice_output/             ← TTS语音播报 (1 Python node)
            ├── voice_output/voice_output_node.py
            ├── launch/voice_output.launch.py
            ├── setup.py, package.xml
            └── resource/voice_output
```

#### 3.1.2 依赖清单

```
# requirements.txt
opencv-python>=4.8.0    # QR + YOLO 图像处理
pyzbar>=0.1.9           # QR 解码 (Python wrapper over libzbar)
ultralytics>=8.0.0      # YOLOv8 (CPU 推理!)
requests>=2.30.0        # HTTP → GPT-4o / 本地 LLM
numpy>=1.24.0
PyYAML>=6.0

# install_dependencies.sh
pip install opencv-python pyzbar ultralytics requests numpy
```

**关键观察**: 
- `ultralytics` (YOLOv8) 是最大的依赖 (~200MB+ 含 PyTorch). 在 RDK X5 的 ARM64 上安装 PyTorch 非常痛苦.
- 没有 `hobot_dnn` (BPU), 没有 `sensor_msgs` (显式列出), 没有 ROS2 包依赖 — 所有依赖通过 pip 安装.
- 这暗示他们**可能没有在实际 RDK X5 硬件上完整运行过 YOLOv8n** — ARM64 PyTorch + ultralytics 在 A55 上的 CPU 推理延迟 >500ms.

#### 3.1.3 话题通信全景图

```
                          ┌──────────────────────────┐
                          │     task_manager_node     │
                          │   (任务编排 & 状态机)      │
                          └─────┬────────┬───────┬───┘
                                │        │       │
                    ┌───────────┘        │       └──────────┐
                    ▼                    ▼                  ▼
          /task_manager/task_info  /task_manager/status  /cmd_vel (紧急停止)
          (String)                 (String)              (Twist)
                    │                    │
     ┌──────────────┼──────────┐         └──────→ voice_output_node
     ▼              ▼          ▼                  (espeak TTS)
path_planner  human_detector  (无订阅者)
     │              │
     ▼              ├──→ llm_interface_node
/path_planner/path  │    (GPT-4o / 本地 LLM)
(Path)              │         │
     │              │         ▼
     ▼              │    /llm_interface/image_caption
motion_controller   │    (String)
(P控制 100Hz)       │         │
     │              │         └──→ voice_output_node
     │              ▼              (TTS 播报结果)
     │         /human_detector/human_image (base64)
     │         /human_detector/detection_result (JSON)
     │
     ├──→ /cmd_vel (Twist) → STM32
     ├──→ /motion_controller/current_waypoint (Int32) → task_manager
     │
     └── obstacle_avoidance_node ← /scan (LaserScan)
              │
              ├──→ /obstacle_detected (Bool) → motion_controller
              └──→ /cmd_vel_obstacle (Twist) → motion_controller (避障优先)

qr_detector_node ← /camera/image_raw (Image)
     └──→ /qr_detector/task_info (String) → task_manager + voice_output

human_detector_node ← /camera/image_raw (Image)
     └──→ /human_detector/human_image (base64 String)
     └──→ /human_detector/detection_result (JSON String)
```

**关键架构观察**:
1. **避障优先级仲裁**: `motion_controller` 收到 `/obstacle_detected=True` 时, 直接发布 `/cmd_vel_obstacle` 并 return — **绝对优先级**, 不经过 task_manager
2. **路径完成检测**: `motion_controller → /current_waypoint (Int32) → task_manager` 是唯一的状态反馈链路 — 脆弱
3. **VLM 异步**: `human_detector → llm_interface → voice_output` 是独立于 task_manager 的旁路 — task_manager 只记录 `human_detected` flag, 不等待 VLM 结果
4. **无 TF 树, 无 odom 订阅**: motion_controller 硬编码 `current_x=y=yaw=0`, path_planner 在 `map` frame 下发绝对坐标 — 隐含假设 "里程计完美且坐标系已对齐"

### 3.2 逐文件源码深度分析

#### 3.2.1 task_manager_node.py (239 行) — 状态机核心

**完整状态机**:
```
Task 0 (STANDBY) → Task 1 (NAV_TO_QR) → Task 2 (CRUISE) → Task 3 (RETURN_P) → Task 4 (DONE)
```

**逐行关键逻辑**:

```python
# 1. 启动即发车 (line 227)
node.start_task()  # 无外部触发, main() 中直接调用

# 2. 状态转移条件:
# 0→1: start_task() 直接设置
# 1→2: QR callback 收到数据 (line 113)
# 2→3: current_waypoint > 8 (line 151)   ← ★ 硬编码 magic number!
# 3→4: current_waypoint > 10 (line 181)  ← ★ 必须和 path_planner 路点数一致!

# 3. 超时处理 (line 166-169):
if elapsed >= self.max_time (180s):
    self.publish_status('时间到')
    self.stop_robot()      # 发布零 Twist
    return                  # ★ 仅 return, 不清理资源!
```

**与我们 competition_master_stage3.py (1784行) 的逐项对比**:

| 功能 | 清越队 | 我们 | 差距原因 |
|------|--------|------|----------|
| 状态数 | 5 (0-4) | 7 (INIT/NAV_TO_QR/BACKING_UP/CRUISE_CHANNEL/RETURN_P/DONE + TIMEOUT) | 我们有 BACKING_UP + 显式 TIMEOUT |
| 状态转移触发 | 回调 + magic number | Nav2 action result (SUCCEEDED/CANCELED/ABORTED) | 我们基于真实导航结果 |
| 段超时 | 无 (仅全局 180s) | 每段独立: NAV_TO_QR=90s, CRUISE=180s, RETURN_P=120s | 我们防止单段卡死 |
| QR 处理 | 收到即转 (无取消流程) | Cancel goal → wait 3s BT cleanup → kill ZBar → wait /qr_event 2s | 我们防 BT 残留竞态 |
| 卡死检测 | 无 | 1Hz, 3.5s / 0.03m 阈值, YOLO 门控 | 我们独有的脱困能力 |
| 禁区控制 | 无 | 启动重置 + 软化/恢复 + 震荡锁 | 专用子系统 |
| 方向决策 | `'clockwise' in task_info` (字符串匹配) | `QR数字 % 2` (奇偶校验) | 我们的更结构化 |
| 路点管理 | 无 (path_planner 独立) | CRUISE 路点动态选择 + RETURN_P 两段注入 | 我们的路点可配置 |
| 崩溃恢复 | 无 | respawn=true + 启动时重置状态 | 我们防 Python 崩溃 |
| VLM 集成 | 旁路: 不影响状态机 | 路点触发 /sign4return=100, 不等结果即继续 | 都是异步, 我们更可控 |
| 资源清理 | 无 (仅 stop_robot 发零 Twist) | Kill rosbag + 保存 CSV + 恢复硬禁区 + 停车 | 我们赛后数据完整 |
| 保活 | 无 | 直驱 /cmd_vel 10Hz 保活 | 防止 STM32 timeout |

**我们能学到的简化**:

1. **`publish_status()` 模式** (line 208-217): 统一的 String 状态发布, 任何人都能订阅. 我们的状态散布在 log 和 print 中, 没有一个集中的 `/status` topic. **应该加**.

2. **1Hz 监控循环** (line 156-187): 独立于事件回调的周期性检查. 我们的所有逻辑都在回调中 (action result / QR / 卡死检测), 没有周期性"心跳"检查. 可以在我们的 `competition_master` 中加一个 1Hz `_periodic_check()` 统一做: 超时检查, 状态发布, keepout 重发布.

3. **`start_task()` 自动发车** (line 189-197): 不需要外部 `ros2 service call` 触发. 我们的 `__init__` 后需要等待 Nav2 action server 就绪 (正确), 但就绪后可以自动开始而不是等外部信号.

4. **简洁的状态表示**: `current_task` 用整数 0-4 比我们的一堆 `self.state` + `self._return_phase` + `self._entry_goal_sent` + ... 更清晰. 我们可以考虑把子状态也统一为枚举.

**他们的关键缺陷** (我们不应学):

1. **Magic number 状态转移**: `current_waypoint > 8` 和 `> 10` 必须与 path_planner 路点数精确匹配. 加一个路点整个状态机就坏了.
2. **无 QR 回退方向**: 如果 QR 扫码完全失败, state 永远停在 1, 直到全局 180s 超时. 我们的 `default_qr_direction` 是正确的.
3. **无段超时**: 如果机器人在某段卡死 (如 Nav2 #3186 楞死), 等 180s 才超时.
4. **stop_robot() 后无资源清理**: rosbag, CSV, 禁区状态 — 全丢失.

#### 3.2.2 path_planner_node.py (191 行) — 硬编码路点生成

**完整路点定义**:
```python
# 坐标系: 以 P 为原点 (0,0), 场地 5m × 5m
POINT_P          = (0.0, 0.0)     # 发车点
TASK_POINT       = (5.0, 2.0)     # QR 任务发布点 (区域A右上角)
CHANNEL_ENTRY    = (5.0, 2.25)    # 黄色通道入口
C_CHANNEL_START  = (5.0, 2.5)     # 区域C环形通道起点
C_CHANNEL_END    = (5.0, 5.0)     # 区域C环形通道终点 (但实际终点是回到起点)

# 顺时针 (CW): 绕环形区域逆时针 (从上方看)
# 12路点 → 12段 → 总长约 18m
CW:  P→Task→Entry→Start→(4.5,2.5)→(4.5,5)→(0.5,5)→(0.5,2.5)→(4.5,2.5)→End→Entry→P

# 逆时针 (CCW): 绕环形区域顺时针 (从上方看)
# 12路点 → 12段
CCW: P→Task→Entry→Start→(0.5,2.5)→(0.5,5)→(4.5,5)→(4.5,2.5)→End→Entry→P
```

**路点间距分析**:
```
P→Task:        5.39m (最长段, 对角线! 危险 — 无中间路点)
Task→Entry:    0.25m (非常近)
Entry→Start:   0.25m (非常近)
Start→(4.5,2.5)/(0.5,2.5): 0.5m
环形四边:      4.0m 或 2.5m (每边)
返回段:        5.39m (同P→Task)
```

**与我们路点的详细对比**:

| 维度 | 清越队 | Origincar Pro |
|------|--------|---------------|
| 路点数 | 12 (CW/CCW 各独立定义) | 4 (CW 复用 CCW 反序) |
| 最长段 | 5.39m (P→Task 对角线) | ~2-3m (Nav2 自动插值) |
| 路点来源 | 硬编码 (场地测量) | 15条 DONE 轨迹中位数共识 |
| 方向决策 | `'clockwise' in QR_text` | `int(QR) % 2 == 1 → CW` |
| 回退方向 | 无 (default_path 是直线不绕环) | `default_qr_direction = "CCW"` |
| 路径优化 | 无 (固定路点) | Nav2 SmacPlannerHybrid 自动优化 |
| 锥桶绕行 | 依赖 obstacle_avoidance 简单避障 | costmap + planner 全局重规划 |
| VLM 拍照点 | 无独立路点 (human_detector 持续检测) | WP2 (VLM 路点) |
| PostVLM 窄通道 | 无 (直接环形出口→Entry→P) | PostVLM 注入 RETURN_P 首段 |

**清越队路点设计的 3 个关键问题**:

1. **P→Task 是 5.39m 对角线**: 无中间路点, P 控制器会走直线穿越区域A. 如果区域A中间有锥桶 → 依赖避障节点临时反应 → 可能冲出赛道.
2. **环形通道路点重复**: `C_CHANNEL_START(5.0,2.5)` 和环路最后一角 `(4.5,2.5)` 间距仅 0.5m, 然后回到 `C_CHANNEL_END(5.0,5.0)` (实际坐标也是 5.0,2.5 附近). 重复路点导致机器人在同一位置附近"确认两次".
3. **路点不在通道中心线上**: `(4.5, 0.5)` 这些坐标是区域C环形通道的内/外边界? 没有考虑通道宽度 0.5m → robot 需要精确在 0.5m 宽通道中间.

#### 3.2.3 motion_controller_node.py (205 行) — P 控制器

**完整控制算法**:
```python
# 输入: /path_planner/path (Path), /obstacle_detected (Bool), /cmd_vel_obstacle (Twist)
# 输出: /cmd_vel (Twist), /motion_controller/current_waypoint (Int32)
# 频率: 100Hz (timer 0.1s)

# Step 1: 避障优先 (line 131-133)
if self.obstacle_detected:
    self.cmd_vel_publisher.publish(self.obstacle_cmd_vel)  # 直接转发避障指令
    return  # ★ 绝对优先级, 跳过所有正常控制

# Step 2: 获取目标路点 (line 136-138)
target_pose = self.path.poses[self.current_waypoint]

# Step 3: ★ 硬编码机器人位置为原点! (line 141-143)
current_x = 0.0; current_y = 0.0; current_yaw = 0.0

# Step 4: 计算误差 (line 146-148)
dx = target_x - current_x    # = target_x - 0 = target_x (绝对坐标)
dy = target_y - current_y
distance = sqrt(dx² + dy²)

# Step 5: 路点到达判定 (line 151-159)
if distance < target_position_tolerance (0.3m):
    self.current_waypoint += 1
    # 如果到达最后一个路点 → stop()
```

**为什么硬编码原点能工作?** — 理论分析:

路点坐标是**绝对地图坐标**, `current_x=0` 意味着 "机器人始终认为自己在 (0,0, yaw=0)". 这在以下情况下能工作:
- 机器人从 (0,0, yaw=0) 出发 → 第一个目标 `TASK_POINT(5.0, 2.0)` → 距离 5.39m → 控制器输出 `v=min(0.5*5.39, 0.5)=0.5m/s`, `ω=1.0*atan2(2,5)=0.38rad/s` → 机器人向东北方向移动.
- 一旦机器人移动 0.3m 到达第一个路点 → `current_waypoint += 1` → 新目标变成 (5.0, 2.25)...
- **关键**: 路点间距 ≤ 0.5m 时, 绝对坐标误差 ≈ 上一路点到达后的剩余距离, 近似于真实误差.

但这在以下情况下**必然失败**:
- 机器人被锥桶推离路径 → 真实位置 ≠ 预期位置 → 后续所有路点的 `dx,dy` 都是错的
- 轮子打滑 → 里程计漂移累积 → 绝对坐标完全失效
- 长段 (5.39m P→Task) 中间无反馈 → 走偏了不知道

**与我们 RPP 的逐项对比**:

| 控制维度 | 清越队 P 控制 | Origincar RPP |
|----------|---------------|---------------|
| 控制频率 | 100Hz | 10Hz |
| 位置反馈 | 无 (硬编码原点) | AMCL + EKF (粒子滤波+双IMU) |
| 前视距离 | 无 (直接追踪当前路点) | 0.68m (速度自适应) |
| 弯道预测 | 无 | RPP 内置曲率缩放 (regulated_linear_scaling_min_radius) |
| 速度规划 | `kp*distance` capped, yaw_error减速 | 曲率自适应 + 前向/后向平滑 |
| 碰撞检测 | 无 | RPP built-in + costmap |
| 倒车 | 无 | allow_reversing=true |
| 阿克曼约束 | 无 (Twist 不区分阿克曼/差速) | REEDS_SHEPP 路径 + RPP 阿克曼适配 |
| 目标到达 | 欧氏距离 <0.3m | xy_goal_tolerance=0.43m |
| 角速度限制 | max_angular_speed=1.0 | max_angular_vel=1.2 |
| 收敛性保证 | 无 (纯P 有稳态误差) | 几何收敛 (pure pursuit 数学保证) |

**有价值的简化思路** — 我们可借鉴:

1. **yaw_error 减速** (line 175-176): `if abs(yaw_error) > 0.3: v *= 0.3`. 这是一个**无需路径曲率**的弯道减速. 我们的 speed_profile_node 需要全局路径 + Menger 曲率 + 移动平均 + 前后向平滑. 他们的方法 3 行代码实现了类似效果.

2. **避障绝对优先** (line 131-133): `if obstacle_detected: publish(obstacle_cmd_vel); return`. 我们通过 costmap obstacle_layer → RPP collision_detection → cost_regulated_linear_velocity_scaling 间接实现, 延迟高. 但我们的方法更平滑 (连续减速 vs 硬切换).

3. **到达下一个路点自动前进** (line 151-153): 不需要 Nav2 action result 检测. 但 fragility 高 (跳路点整个状态机就卡住).

#### 3.2.4 obstacle_avoidance_node.py (137 行) — 基础避障

**完整算法逐行分析**:
```python
# 输入: /scan (LaserScan), 输出: /obstacle_detected (Bool) + /cmd_vel_obstacle (Twist)
# 参数: safety_distance=0.5 (launch) vs 0.25 (yaml) ← ★ 不一致!

def scan_callback(self, msg):
    ranges = msg.ranges
    min_range = min(ranges)                             # 全局最近距离
    obstacle_detected = min_range < self.safety_distance

    if obstacle_detected:
        self.avoid_obstacle(ranges)                     # 避障
    else:
        self.clear_path()                               # 发零 Twist 清除

def avoid_obstacle(self, ranges):
    left_ranges = ranges[:len(ranges)//3]               # 前 1/3 = 左侧 (~120°)
    right_ranges = ranges[-len(ranges)//3:]             # 后 1/3 = 右侧 (~120°)
    left_avg = sum(left_ranges) / len(left_ranges)      # ★ 所有值平等求和, 
    right_avg = sum(right_ranges) / len(right_ranges)   #   inf/nan 未处理!

    if left_avg > right_avg:
        twist.angular.z = self.turn_speed (0.5)          # 左转 (更多空间)
    else:
        twist.angular.z = -self.turn_speed               # 右转
    # ★ 线速度为 0! 避障时纯原地旋转 → 阿克曼做不到!
```

**3 个致命缺陷**:

1. **阿克曼不可原地旋转**: `linear.x=0, angular.z=±0.5` 是差速底盘才能执行的指令. 阿克曼需要线速度才能转向 (`steering = atan(L*ω/v)`). 他们的 `cmd_vel_to_ackermann_drive` (如果有) 会在 v=0 时输出 steering=0 → 机器人直行撞障碍.

2. **inf/nan 毒性**: LiDAR 的 `ranges` 数组包含 `inf` (无回波) 和 `nan` (无效测量). `sum()` 遇到 inf/nan 直接污染 `left_avg`/`right_avg`. 需要先过滤.

3. **仅看左右 1/3**: 正前方 1/3 (最危险方向) 被完全忽略! 正前方有墙 → `min_range` 很小触发避障 → 只比较左右 → 可能两侧都大 → 随机选一边 → 仍然撞墙.

**对比我们的 costmap 避障**:
- 我们: LiDAR → ObstacleLayer (raytrace + marking + clearing) → InflationLayer (potential field) → RPP collision_detection → 成本感知速度缩放
- 他们: LiDAR → min() → 左右比较 → 固定角速度
- **我们的方法慢但安全, 他们的方法快但危险**

#### 3.2.5 qr_detector_node.py (111 行) — pyzbar QR 解码

```python
# ZBar 封装: pyzbar.decode(cv_image)
# 去重: current_time - last_qr_time > 2.0s
# 编码: 假设 UTF-8
# 输出: /qr_detector/task_info (String, QR文本原始内容)
```

**与我们 qr_decoder_zbar (C++/ZBar) 的详细对比**:

| 维度 | 清越队 (pyzbar Python) | Origincar Pro (ZBar C++) |
|------|------------------------|--------------------------|
| 库 | pyzbar (Python wrapper) | ZBar native C++ |
| 性能 | ~30-50ms/帧 (Python overhead) | ~5-10ms/帧 (native) |
| 多尺度 | 无 (单分辨率) | 原分辨率 → 0.5× 降采样回退 |
| 深度滤波 | 无 | Advisory only (50-4000mm) |
| 码制过滤 | 无 (所有码制) | QR only (其他禁用) |
| 内容校验 | 无 (任意文本都发) | min_qr_length 校验 |
| 去重 | 2s 时间窗口 | qr_decision 3s 冷却 + 同号忽略 |
| 输出 | 原始 String | /sign (raw) + /sign_pose (odom帧) + /qr_event (结构化) |
| 结构化解析 | 无 (task_manager 直接匹配子串) | qr_decision: 奇偶→方向, 提取数字+坐标 |
| 资源管理 | 无 (节点持续运行) | QR检测后 pkill qr_decoder_zbar |

**我们能学到的**:
- pyzbar 2s 时间窗口去重 — 简单有效. 但我们的 qr_decision 同号忽略更精确.
- 他们不校验 QR 内容 — 任何文本都转发. 我们的 min_qr_length 更安全, 但过于严格可能漏掉有效短码.

#### 3.2.6 human_detector_node.py (145 行) — YOLOv8n CPU 人形检测

```python
model = YOLO('yolov8n.pt')           # 3.2M 参数, nano 版本
detection_interval = 2.0             # 每 2 秒检测一次
confidence_threshold = 0.5           # person class_id=0 才接受

# 检测到 → 裁剪 bbox → cv2.imencode('.jpg') → base64 → 发布
# ★ 只处理第一个人 (break after first detection)
```

**RDK X5 CPU 性能估算**:
- YOLOv8n 在 A55 @1.8GHz 上的 CPU 推理 (~TFLite/NCNN): **300-500ms/帧**
- ultralytics PyTorch 推理 (如果有 PyTorch ARM64): **>1000ms/帧**
- 这意味着 2s 间隔勉强够用 — 但在此期间 CPU 100% 占用, 导航控制被饿死

**与我们 YOLO 方案的对比**:

| 维度 | 清越队 | Origincar Pro |
|------|--------|---------------|
| 模型 | YOLOv8n (3.2M params) | YOLOv5s PTQ 量化 |
| 推理硬件 | **CPU** (A55) | **BPU** (10 TOPS) |
| 推理时间 | 300-1000ms (估算) | ~10ms |
| 检测目标 | Person (class_id=0) | Obstacle/cone (1类) |
| 用途 | 人形→VLM | 锥桶→costmap |
| CPU占用 | 极高 (PyTorch/ultralytics) | 极低 (仅前后处理) |
| 模型加载 | YOLO('yolov8n.pt') — 每次启动下载? | 预编译 .bin 权重 |
| 帧率 | 0.5fps (2s间隔) | ~14fps |

**结论**: 清越队的 YOLOv8n 方案在 RDK X5 上**几乎不可能实时运行**. 这很可能是开发阶段的占位代码, 实际比赛时会替换为 BPU 推理或云端推理.

#### 3.2.7 llm_interface_node.py (193 行) — 双模式大模型接口

```python
# 两种模式 (通过 ROS param 'local_llm_enabled' 切换):
# Mode 1 (local_llm_enabled=False, 默认): GPT-4o via OpenAI API
#   POST https://api.openai.com/v1/chat/completions
#   Model: gpt-4o
#   Max tokens: 500
#   Timeout: 30s
#   Prompt: '请详细描述这张图片。'
#
# Mode 2 (local_llm_enabled=True): 本地 LLM via REST API
#   POST {local_llm_url}/generate
#   Body: {image: base64, prompt: '请详细描述这张图片中的人形目标。'}
#   Timeout: 30s
#   Response: {caption: "..."}
```

**与我们 VLM 方案的详细对比**:

| 维度 | 清越队 | Origincar Pro |
|------|--------|---------------|
| 触发 | 持续 (human_detector 检测到人→自动发) | 事件 (到达 VLM 路点→/sign4return=100) |
| 图像来源 | 裁剪的人形 bbox | 整帧 /aurora/rgb/image_jpeg |
| 编码 | cv2.imencode (CPU) | hobot_codec JPU (硬件) |
| API 端点 | api.openai.com | Volcengine Ark (火山引擎) |
| 模型 | gpt-4o | ep-20260502193326-428m8 |
| 本地 LLM | ✅ 支持 (REST /generate) | ❌ 不支持 |
| Prompt | 通用 ("描述这张图片") | 医疗巡检场景定制 (姿态/着装/动作, <100字) |
| 状态机影响 | 旁路 (不影响导航) | 触发后立即继续 (不等结果) |
| API Key | ROS param (明文!) | YAML 配置文件 |

**清越队方案的优势**:
1. **本地 LLM 支持**: `local_llm_enabled` param 切换. 比赛现场网络不稳定时可用本地模型. 我们可以加这个.
2. **双模式 clean 架构**: `generate_caption()` → `call_local_llm()` or `call_cloud_llm()`. 代码结构清晰.

**清越队方案的问题**:
1. **API Key 明文在 ROS param**: `self.api_key = self.declare_parameter('api_key', '').value` → `ros2 param get` 直接暴露. 我们放 YAML 文件更好.
2. **Prompt 不针对竞赛场景**: "请详细描述这张图片" vs 我们的医疗巡检定制 prompt.
3. **持续检测触发 VLM**: 绕环一圈可能触发多次 GPT-4o 调用 → 成本高 + 网络延迟影响下一帧检测.

#### 3.2.8 voice_output_node.py (121 行) — TTS 语音播报

```python
# 订阅 3 个话题:
# - /qr_detector/task_info → "任务信息: {data}"
# - /llm_interface/image_caption → "检测到人物: {data}"
# - /task_manager/status → 直接播报

# 平台自适应:
# Linux: espeak "text"              (命令行 TTS, 零依赖)
# Windows: PowerShell System.Speech
```

**我们可借鉴的**:
- 独立 voice_output 节点是好的架构 — 单一职责, 可独立测试.
- espeak 零依赖 (apt install espeak), 适合嵌入式.
- 平台自适应 (`platform.system()`) 是跨平台开发的好做法.

**我们可改进的**:
- espeak 音质很差 (机器人语音). 竞赛允许车载屏幕显示 — 也许屏幕显示比语音更实用.
- 没有中文语音支持 (espeak 中文效果极差). 需要换用 `espeak-ng` 或 `gtts`.

#### 3.2.9 启动文件架构

**competition.launch.py** — 总启动 (IncludeLaunchDescription 模式):
```python
# 4 个 IncludeLaunchDescription + 1 个 Node:
# 1. qr_detector.launch.py
# 2. human_detector.launch.py
# 3. navigation.launch.py        ← 内含 obstacle_avoidance + path_planner + motion_controller
# 4. voice_output.launch.py
# 5. Node: task_manager_node
```

**与我们 stage3_bringup.launch.py 的对比**:

| 维度 | 清越队 | Origincar Pro |
|------|--------|---------------|
| 组合方式 | IncludeLaunchDescription (静态) | TimerAction 时序编排 (t=0s,1s,3s,4s,5s,8s) |
| 启动顺序 | 不保证 (LaunchDescription 顺序不代表启动顺序) | 严格时序 (TimerAction 延迟) |
| 参数传递 | 无 (各包独立读 YAML) | launch argument + 环境变量 (RMW_IMPLEMENTATION) |
| 硬件驱动 | 无 (假设已运行) | base_minimal.launch.py (STM32+LiDAR+URDF+EKF) |
| 导航 | 3 个独立 Python 节点 | Nav2 composition (多 server 合并为一个进程) |
| 生命周期管理 | 无 | lifecycle_manager (localization + navigation) |
| RViz | 无 | t=8s 延迟启动 |
| 崩溃恢复 | 无 | respawn=true (competition_master) |

**关键教训**:
- 清越队的 `IncludeLaunchDescription` 更简洁, 但没有启动时序保证. 实际中 hardware driver 必须先于 QR/导航 启动.
- 我们不需要 RViz 在嵌入式上运行 — 可以去掉 t=8s 的 rviz2.

### 3.3 5 维深度对比

#### 3.3.1 状态机 & 任务编排

| 维度 | 清越队 | 我们 | 谁更好 |
|------|--------|------|--------|
| 代码量 | 239 行 | 1784 行 | 他们 (简洁) |
| 状态建模 | 5 整数状态 | 7 状态 + 子阶段 + 布尔标志 | 我们 (更精确) |
| 段超时 | 无 | 每段独立 | 我们 (必要) |
| 卡死检测 | 无 | 1Hz + 位移 + YOLO门控 | 我们 (关键) |
| 禁区控制 | 无 | 5 种操作 (重置/软化/恢复/震荡锁/重发布) | 我们 (赛道必需) |
| 崩溃恢复 | 无 | respawn + 启动时状态重置 | 我们 |
| 状态发布 | /task_manager/status (String) | 无集中 topic | 他们 (应加) |
| 启动方式 | 自动 `start_task()` | 等待 Nav2 就绪后自动 | 各有优势 |

**核心洞察**: 他们证明了 200 行可以实现一个完整的竞赛状态机. 我们的 1784 行不是因为过度工程, 而是因为处理了真实世界的复杂性: Nav2 异步结果等待、卡死检测与恢复、禁区动态控制. **但我们应该加一个 /status topic**.

#### 3.3.2 导航方案

| 场景 | 清越队硬编码+P控制 | 我们的 Nav2 |
|------|---------------------|-------------|
| 场地固定无锥桶 | ✅ 完美工作 | ✅ 工作 (但过重) |
| 锥桶堵塞通道 | ❌ 无法绕行 (P控制+简单避障不够) | ✅ planner 重规划 + 软禁区 |
| 锥桶在长直线段中间 | ❌ 5.39m P→Task 段无反馈 → 撞 | ✅ costmap 提前发现并绕行 |
| 轮子打滑/定位漂移 | ❌ 不可恢复 (无定位反馈) | ✅ AMCL 重定位 |
| Channel 出入口导航 | ⚠️ 依赖路点精确放置 | ✅ planner 自动寻找可行路径 |
| 意外障碍移动 | ❌ 无法处理 | ✅ costmap clearing + 重规划 |
| CPU 占用 | ✅ 极低 (~5%) | ❌ 75-100% |
| 调试难度 | ✅ 简单 (print 即可) | ❌ 需 RViz + rosbag + plot 工具 |
| 换场地 | ❌ 重新测量+硬编码 | ✅ 换 map + 路点配置 |

**核心洞察**: 清越队方案是"已知环境最优路径回放" — 假设场地完全已知且无意外. 我们的方案是"自主导航" — 处理不确定性. **竞赛中, 不确定性是常态**: 锥桶位置随机, 光照变化, 轮子打滑. Nav2 的复杂性为此买单.

#### 3.3.3 感知管线

| 传感器 | 清越队用途 | 我们用途 |
|--------|-----------|----------|
| 单目摄像头 | QR (pyzbar) + 人形检测 (YOLOv8n CPU) | QR (ZBar C++) |
| 深度相机 | 未使用 (代码中无订阅) | QR 深度校验 + YOLO 3D 投影 |
| LiDAR | 简单避障 (左右比较) | AMCL 定位 + costmap obstacle_layer |
| IMU | 未使用 | 双 IMU EKF 融合 |
| 里程计 | 未使用 (硬编码原点!) | EKF + AMCL |

**核心洞察**: 清越队仅用了摄像头和 LiDAR 的最基础功能. 我们多传感器融合的代价是复杂度, 但获得了定位鲁棒性和深度感知.

#### 3.3.4 VLM 管线

清越队的持续检测方案 vs 我们的路点触发方案 — 各有优劣:

| 维度 | 持续检测 (清越队) | 路点触发 (我们) |
|------|-------------------|-----------------|
| 检测时机 | 任何时候 (绕环中任意位置) | VLM 路点 (固定位置) |
| 漏检风险 | 低 (持续扫描) | 低 (路点到达保证) |
| 多次触发 | 高 (同一人可能检测多次) | 低 (只触发一次) |
| CPU 开销 | 高 (YOLO 持续 2s 间隔) | 低 (仅路点处拍照) |
| API 成本 | 高 (可能多次 GPT-4o 调用) | 低 (一次调用) |
| 人形定位 | 天然 (YOLO bbox 即位置) | 无 (需要额外推理) |
| 图像质量 | 高 (裁剪到人形区域) | 中 (整帧, 人形可能小) |

**最优方案可能是两者结合**: 路点触发拍照 (保证一次), 但如果路点前就检测到人形 → 提前触发 (省时间).

#### 3.3.5 语音播报

清越队的独立 voice_output_node 设计值得借鉴:
- 单一职责: 只做 TTS, 不耦合业务逻辑
- 多话题订阅: QR / VLM / Status 三类信息统一播报
- 平台自适应: Linux/Win 自动切换 TTS 引擎

我们缺少这个. 当前我们的状态信息散布在 `self.get_logger().info()` 中, 没有语音输出. 但比赛规则要求 "语音文字播报或提示音定义播报" 或 "车载屏幕显示" — 我们目前两者都没有!

### 3.4 我们能从清越队学到的 10 件事

| # | 学习点 | 来源文件 | 如何应用到我们项目 |
|---|--------|----------|-------------------|
| 1 | **加 /status topic** | task_manager_node.py:208-217 | competition_master 加 `self.status_pub` 发布 String 状态, 1Hz 更新 |
| 2 | **独立 voice_output 节点** | voice_output_node.py | 新建 `voice_output` 包, 订阅 /status, 用 espeak-ng 或 gTTS 播报 |
| 3 | **IncludeLaunchDescription 组合** | competition.launch.py | stage3_bringup.launch.py 拆分为可复用的 sub-launch 文件 |
| 4 | **yaw_error 减速** | motion_controller_node.py:175-176 | speed_profile_node 加 yaw_error 维度的速度惩罚 (备份, 非替代) |
| 5 | **自动发车** | task_manager_node.py:227 | INIT 等待 Nav2 就绪后自动进入 NAV_TO_QR (已有, 确认工作) |
| 6 | **双模式 VLM** | llm_interface_node.py:87-90 | vision_ai_node 加 `local_llm_enabled` param + 本地 REST API 调用路径 |
| 7 | **1Hz 集中监控循环** | task_manager_node.py:156-187 | competition_master 加 `_periodic_check()`: 超时/状态发布/keepout重发布 |
| 8 | **YAML 配置文件分离** | navigation_params.yaml | 将路点/QR坐标/禁区参数从代码中移到 YAML |
| 9 | **启动依赖脚本** | install_dependencies.sh | 提供 `install_deps.sh` 自动化 pip 依赖安装 |
| 10 | **技术文档模板** | 技术文档.md | 参考其结构完善我们的竞赛方案文档 |

### 3.5 清越队能向我们学到的 10 件事

| # | 我们的优势 | 他们缺失的 | 影响 |
|---|-----------|-----------|------|
| 1 | AMCL 定位 | 硬编码原点 | 任何定位漂移导致任务失败 |
| 2 | Nav2 全局规划 | 固定路点 | 锥桶堵塞无法绕行 |
| 3 | Costmap 避障 | 简单左右比较 | 窄通道/多锥桶无法处理 |
| 4 | Keepout 禁区 | 无禁区概念 | 驶出黄色通道无保护 |
| 5 | 段超时 | 仅全局 180s | 单段卡死浪费全部时间 |
| 6 | 卡死检测+脱困 | 无 | 楞死=比赛结束 |
| 7 | BPU YOLO | YOLOv8n CPU | 10 TOPS BPU 完全浪费 |
| 8 | 双 IMU EKF | 无 IMU | 定位精度差, 转弯漂移 |
| 9 | QR 方向奇偶校验 | 字符串子串匹配 | "clockwise" 拼写错误→回退路径(直线不绕环) |
| 10 | 数据驱动路点校准 | 硬编码 | 15条DONE轨迹共识 vs 单次手动测量 |

### 3.6 具体可采纳的代码改进

**改进 1: 加 /status topic 到 competition_master**

```python
# 在 competition_master_stage3.py 的 __init__ 中:
self.status_pub = self.create_publisher(String, '/task_manager/status', 10)

# 在状态切换时:
def _transition_to(self, new_state):
    self.state = new_state
    msg = String()
    msg.data = f'状态: {new_state}, 耗时: {time.time()-self.start_time:.1f}s'
    self.status_pub.publish(msg)
```

**改进 2: YAML 路点配置**

```yaml
# 新建 config/waypoints.yaml
waypoints:
  ccw:
    wp1: [1.50, -1.45]
    wp2: [3.02, -1.02]
    vlm: [2.02, 0.94]
    post_vlm: [0.96, -0.06]
  qr_point: [0.41, -3.17]
  p_point: [-1.985, -0.014]
```

**改进 3: VLM 双模式支持**

```python
# 在 vision_ai_node.py 中加:
self.declare_parameter('use_local_llm', False)
self.declare_parameter('local_llm_url', 'http://localhost:8080')

def generate_caption(self, image_base64):
    if self.get_parameter('use_local_llm').value:
        return self._call_local(image_base64)
    else:
        return self._call_volcengine(image_base64)
```

---

### 3.7 EXA MCP 搜索验证 — 清越队技术方案的可行性评估

> 8 个搜索主题, 40+ 结果, 12 篇深度提取

#### 3.7.1 pyzbar vs ZBar C++ — 性能实测

| 维度 | pyzbar (Python) | ZBar C++ (我们) |
|------|-----------------|-----------------|
| 延迟 | ~30-50ms/帧 | ~5-10ms/帧 |
| ARM 兼容 | 需 libzbar0 (轻量) | 需 libzbar (相同) |
| Python 开销 | cv_bridge + numpy 转换 | 直接操作 cv::Mat |
| 实际竞赛使用 | e-Yantra 等竞赛广泛使用 | 我们的定制管线 |

**验证结论**: pyzbar 在 ARM 上够用 (30-50ms), 2s 去重窗口合理. 但 ZBar C++ 快 3-5×.

#### 3.7.2 YOLOv8n 在 ARM 上的真实性能

Jetson Orin Nano 8GB 基准 (VnRobo 2026):

| 格式 | FPS (640×640) | 延迟 | GPU 内存 | mAP@50 |
|------|:---:|------|----------|:---:|
| PyTorch FP32 | 15 | 67ms | 1.2 GB | 37.3 |
| TensorRT FP32 | 32 | 31ms | 680 MB | 37.3 |
| **TensorRT FP16** | **58** | **17ms** | 420 MB | 37.2 |
| TensorRT INT8 | 72 | 14ms | 310 MB | 36.8 |

**对 RDK X5 的推断**:
- 清越队用 `ultralytics` (PyTorch) → 在 A55 @1.8GHz 上**无法达到 15fps**
- Orin Nano 有 GPU (1024 CUDA cores), RDK X5 只有 BPU (无 GPU)
- A55 CPU 上 PyTorch YOLOv8n: 估算 **300-1000ms/帧** → 2s 间隔不够 → **CPU 100% 导致导航饿死**
- **结论: 清越队的 YOLOv8n CPU 方案在实际 RDK X5 上几乎不可能正常运行**

#### 3.7.3 控制器对比 — P 控制 vs RPP 的量化差异

| 控制器 | 速度上限 | 路径误差 | CPU 占用 | 适用场景 |
|--------|----------|----------|----------|----------|
| 简单 P 控制 | **<0.5 m/s** | 大 | ~1% | 低速 + 已知路径 |
| RPP (Pure Pursuit) | <1.0 m/s | 中 | ~5% | 差速 + 简单路径 |
| Vector Pursuit | <1.5 m/s | 小 (比RPP少~50%CPU) | ~3% | **阿克曼 + 高速** |
| DWB | <1.5 m/s | 小 | ~15% | 复杂环境 |
| MPPI | <1.5 m/s | 最小 | ~30% | 窄通道 + 极端环境 |

**关键发现 (IEEE 2025)**: 
- PID+Pure Pursuit vs P 控制: **圈速快 13.5%, 均速高 15%, 但横向加速度高 31.2%**
- RPP 在 1.5 m/s 以上 "完全失败, 剧烈振荡" → **我们的 0.50 m/s 远低于天花板**
- MPPI 是唯一在窄通道中 100% 成功的控制器

#### 3.7.4 混合方案推荐 — 竞赛最优策略

| 组件 | 简单方案 | Nav2 方案 | **推荐混合方案** |
|------|----------|-----------|-----------------|
| 全局规划 | 硬编码路点 | SmacPlannerHybrid | **已知段用路点, 未知/堵塞段用 Nav2** |
| 局部控制 | P 控制 | RPP | Vector Pursuit (速度+阿克曼优化) |
| 任务编排 | 扁平 FSM | BT | Karelics Task Manager 包装 Nav2 actions |
| 感知 | pyzbar + YOLO Python | C++ BPU | C++ 检测 + Python VLM/API |
| 语音输出 | subprocess espeak | 无 | rosspeaks ROS2 节点 (非阻塞) |

#### 3.7.5 清越队能避开的 Nav2 陷阱 (我们无法避开)

| Nav2 陷阱 | 清越队如何避开 |
|-----------|---------------|
| RPP cusp bug (Humble #4757) | P 控制器无 cusp 检测逻辑 |
| KeepoutFilter 忽略 multiplier | 无 keepout — 手动在路点中避开 |
| TRANSIENT_LOCAL 跨运行持久化 | 无 costmap — 只有路点 |
| Planner 在大地图中超时 | 无 planner — 路点即时 |
| Inflation 填充窄通道 | 无 inflation — 手动留边距 |
| MPPI 吃满 ARM CPU | P 控制用 ~1% CPU |

#### 3.7.6 最关键的洞察

> **"确定性强于精巧"** — 在时间压力下, 硬编码路点 + P 控制 + 扁平 FSM 的方案可以在已知赛道上达到 100% 成功率. Nav2 增加了灵活性但引入了更多故障模式.

> **混合方案是最优竞赛策略**: Nav2 用于困难部分 (动态避障, 运动学约束路径), 借鉴简单方案的简洁用于容易部分 (已知路点, 任务排序, 状态输出). **不要用 planner 做路点能做的事**.

### 3.8 最终评估: 清越队方案的可行性评分

| 子系统 | 代码质量 | 实际可行性 | 与我们差距 |
|--------|:---:|:---:|:---:|
| 状态机 | ⭐⭐⭐⭐ | ⭐⭐⭐ (缺超时/恢复) | 我们更鲁棒 |
| 路径规划 | ⭐⭐ | ⭐⭐⭐ (已知场地够用) | 我们更灵活 |
| 运动控制 | ⭐⭐ | ⭐⭐ (硬编码原点致命) | 我们大幅领先 |
| 避障 | ⭐ | ⭐ (阿克曼不可原地转) | 我们大幅领先 |
| QR 检测 | ⭐⭐⭐ | ⭐⭐⭐⭐ (pyzbar 够用) | 性能接近 |
| 人形检测 | ⭐⭐⭐ | ⭐ (CPU YOLO 不可行) | 我们 BPU 碾压 |
| VLM | ⭐⭐⭐⭐ | ⭐⭐⭐ (依赖网络) | 各有优势 |
| 语音 | ⭐⭐⭐ | ⭐⭐⭐ (espeak 够用) | 他们领先 (我们有方案) |
| 启动管理 | ⭐⭐⭐ | ⭐⭐⭐ (无时序保证) | 我们更可靠 |
| **总体** | **⭐⭐½** | **⭐⭐½** | **我们在鲁棒性上显著领先, 他们在简洁性上值得学习** |

---

### 3.9 优先级可采纳改进清单 (来自清越队方案分析)

> 综合源码分析 + EXA MCP 搜索 + 架构对比 Agent 三路结果

| 优先级 | 改进项 | 灵感来源 | 节省代码量 | 风险 |
|:---:|--------|----------|:---:|:---:|
| **P0** | Keepout 默认非致命 (cost 250 替代 254), 移除运行时 mask 切换 | 清越队无 keepout 复杂度 | ~200 行 | 低 — 更软的禁区仍阻止进入 |
| **P0** | 加 `/status` topic (String) 到 competition_master, 1Hz 发布 | `publish_status()` 模式 | +20 行 | 无 |
| **P1** | 合并 `qr_decision` 逻辑到 C++ `qr_decoder_zbar` | 清越队单节点 QR | ~100 行 | 低 |
| **P1** | 独立 `voice_output` 节点 (espeak-ng + /status 订阅) | `voice_output_node.py` | +80 行 | 低 — 满足规则语音要求 |
| **P1** | 1Hz 集中监控循环 `_periodic_check()` | `task_loop()` 模式 | 重构 ~50 行 | 低 |
| **P2** | VLM 双模式: 本地 LLM fallback (`local_llm_enabled` param) | `llm_interface_node.py` | +40 行 | 低 |
| **P2** | 路点/QR坐标/禁区参数移到 YAML | `navigation_params.yaml` | 重构 | 低 |
| **P2** | 替换 `NavigateThroughPoses` 巡航为逐路点 `ComputePathToPose` 循环 | 清越队简单导航 | ~50 行 | 中 — 失去 RPP 路点间平滑 |
| **P3** | Benchmark `speed_profile_node` 是否真正提升圈速 | 清越队无速度曲线 | 若移除: ~400 行 | 中 — 可能降低弯道速度 |
| **P3** | 消去 `_pending_entry_nav` + backup 序列; 让 Nav2 从 QR 点规划到第一个巡航路点 | 清越队直接导航 | ~150 行 | 高 — 需验证 planner 能找到入口路径 |
| **P3** | pyzbar 2s 去重窗口 (简化 qr_decision 冷却) | `qr_detector_node.py` | ~10 行 | 低 |

### 3.10 架构哲学总结

清越队 vs Origincar Pro 代表了嵌入式机器人竞赛中两种根本不同的设计哲学:

```
清越队 (Simple Stack):            Origincar Pro (Nav2 Stack):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
确定性 > 灵活性                   鲁棒性 > 简洁性
800 行 > 3450 行                   每个故障模式都有恢复路径
无外部依赖 > 15+ Nav2 节点        硬件加速感知 (BPU + JPU)
直接控制 > 多层抽象               完整遥测用于事后分析
部署即运行 > 需要 convergence     全局规划 + 重定位能力

两者各有所长: 竞赛最优方案 = 清越队的简洁 (已知路点, 任务编排, 状态输出)
                         + Origincar Pro 的鲁棒性 (动态避障, 定位, 死锁脱困)
```

---

## 4. 多项目交叉对比

### 4.1 控制方案对比

| 维度 | ackermann_car | racing_control | 清越队 | **Origincar Pro (我们)** |
|------|:---:|:---:|:---:|:---:|
| 控制算法 | RPP | 视觉PID | P控制 | RPP |
| 控制频率 | 20Hz | 约14fps | 100Hz | 10Hz |
| 路径来源 | SmacPlannerHybrid | 视觉中线检测 | 硬编码路点 | SmacPlannerHybrid |
| 速度控制 | 固定0.20m/s | 固定1.5m/s | P控制+cap | 曲率自适应 |
| 弯道减速 | RPP内置 | 无 | yaw_error比例 | speed_profile |
| 阿克曼模型 | 完整ros2_control | Twist→Ackermann简化 | Twist直驱 | Twist→Ackermann→STM32 |
| 避障方式 | VoxelLayer+collision | 视觉反比转向 | 左右比较 | ObstacleLayer+keepout |

### 4.2 Nav2 参数空间探索

从 ackermann_car-main 发现的参数调整方向:

| 参数 | 我们 | ackermann_car | 建议方向 | 预期效果 |
|------|------|---------------|----------|----------|
| `controller_frequency` | 10Hz | 20Hz | **↑ 15-20Hz** | 更精确跟线, 减少 overshoot |
| `angle_quantization_bins` | 40 | 72 | **↑ 60** (测试) | 更平滑路径, 可能更多cusp |
| `non_straight_penalty` | 1.8469 | 1.3 | **↓ 1.3-1.5** | 允许更多自然转弯 |
| `cost_penalty` | 6.33 | 3.5 | **↓ 4.0-5.0** | 减少不必要绕行 |
| `retrospective_penalty` | — | 0.015 | **添加 0.01-0.02** | 防止规划器原地绕圈 |
| `lookahead_dist` | 0.678 | 0.45 | — | 我们 ≥2×min_turning_radius=0.60 是硬约束 |
| `max_allowed_time_to_collision` | 0.35 | 2.0 | — | 我们的窄道实战值合理 |
| `speed_lim_angular` | — | true | **添加** | 弯道限制角速度 |
| `approach_velocity_scaling_dist` | — | 0.6 | **添加 0.5-0.8** | 接近目标平滑减速 |
| `alpha1-4` | 0.45 | 0.15-0.2 | **↓ 0.25-0.35** | AMCL 更准确, 测试前提EKF输出可靠 |
| `update_min_a/d` | 0.1 | 0.01 | **↓ 0.03-0.05** | 更频繁定位更新 |

### 4.3 架构设计教训

| 教训 | 来源 | 说明 |
|------|------|------|
| **Watchdog 不可省略** | ackermann_car | 0.5s 无指令自动停车. 我们移除了 cmd_vel_mux 后缺少此保护 |
| **VoxelLayer > ObstacleLayer** | ackermann_car | 3D→2D 投影过滤地面杂波. RDK X5 可能带不动 |
| **ReactiveFallback 用于 GoalUpdated** | ackermann_car BT | GoalUpdated 时立即中止恢复. 我们应在 BT 中采用 |
| **硬编码路点+简单控制是可行的** | 清越队 | 但无法应对动态环境. 我们的 Nav2 方案更通用 |
| **反比避障公式优于固定转向** | racing_control | `ω ∝ 1/横向偏差` 比固定 ω 更平滑 |
| **Dead zone 防抖** | racing_control | ±20px 死区 → 曲率 dead band 概念可移植到 speed_profile |
| **动态参数加载** | racing_control | 每轮 get_parameter() 支持在线调参 |

### 4.4 竞赛规则到工程映射 (补充)

从 rule.md 中提取的关键约束回顾:

| 规则约束 | 工程实现 | 当前状态 |
|----------|----------|----------|
| 180s 总限时 | `competition_master` 全局超时 | ✅ 已实现 |
| 子任务1: P→QR, 不碰锥桶 (+10s/次, max+30s) | NAV_TO_QR + obstacle layer | ✅ |
| 子任务1: 未到QR罚50s | Nav2 NavigateToPose 超时90s | ✅ |
| 子任务2: 只允许黄色通道行驶 (1/2出通道罚10s) | keepout 硬禁区 | ✅ |
| 子任务2: 碰锥桶+10s/次 (max+30s) | costmap obstacle + inflation | ✅ |
| 子任务2: 未完成图生文罚20s | VLM triggers on VLM waypoint | ✅ |
| 子任务2: 驶出通道+10s/次 (max+30s) | keepout 硬禁区 | ✅ |
| 子任务2: 未完成罚50s | CRUISE_CHANNEL 180s超时 | ✅ |
| 子任务3: 回到P点 (2/3在蓝白区域内) | RETURN_P → P精度 0.429m | ✅ |
| 子任务3: 碰锥桶+10s/次 (max+30s) | costmap obstacle | ✅ |
| 子任务3: 未回P罚50s | RETURN_P 120s超时 | ✅ |
| 重启不限次数但计时不停 | respawn=true | ✅ |
| 5分钟准备时间 | — | 足够启动 |
| 禁止高速冲撞场地 | speed limit 0.65m/s | ✅ |

---

## 5. 可采纳优化清单

### 5.1 高优先级 (立即测试)

| # | 优化项 | 来源 | 改动位置 | 预期收益 |
|---|--------|------|----------|----------|
| 1 | `controller_frequency: 10→20Hz` | ackermann_car | nav2_params.yaml | 更精确跟线, 减少 5cm/周期 盲区 |
| 2 | `speed_lim_angular: true` | ackermann_car | nav2_params.yaml | 弯道同时限制ω, 防侧滑 |
| 3 | `approach_velocity_scaling_dist: 0.6` | ackermann_car | nav2_params.yaml | 进场平滑减速 |
| 4 | `retrospective_penalty: 0.015` | ackermann_car | nav2_params.yaml | 防规划绕圈 |
| 5 | `non_straight_penalty: 1.85→1.3` | ackermann_car | nav2_params.yaml | 允许更自然转弯路径 |
| 6 | `cost_penalty: 6.33→4.5` | ackermann_car | nav2_params.yaml | 减少不必要绕行 |
| 7 | `alpha1-4: 0.45→0.30` | ackermann_car | nav2_params.yaml | AMCL 更准确 (需EKF验证) |
| 8 | `update_min_a/d: 0.1→0.05` | ackermann_car | nav2_params.yaml | 更频繁定位更新 |

### 5.2 中优先级 (需代码改动)

| # | 优化项 | 来源 | 说明 |
|---|--------|------|------|
| 9 | ReactiveFallback 替换 RecoveryFallback (GoalUpdated分支) | ackermann_car BT | GoalUpdated时立即中止恢复, 不浪费时间 |
| 10 | speed_profile 加 dead band (κ<0.05→v_max) | racing_control | 微小曲率不减速, 减少不必要速度抖动 |
| 11 | 动态参数支持 (speed_profile β/λ) | racing_control | rqt_reconfigure 在线调参 |
| 12 | YOLO 深度门控 (远处锥桶不触发避障) | racing_control | yolo_costmap_bridge 中过滤 depth>Xm 的检测 |

### 5.3 低优先级 (长期架构)

| # | 优化项 | 来源 | 说明 |
|---|--------|------|------|
| 13 | VoxelLayer 替代 ObstacleLayer (local costmap) | ackermann_car | 需评估 RDK X5 CPU 开销 |
| 14 | local_costmap 3m→5m (或 6m) | ackermann_car | 更大局部视野, 但 CPU ↑ |
| 15 | MPPI 替代 RPP (Jazzy) | research | 有 cusp 检测, 但需 cross-compile |
| 16 | 双 inflation 区域 costmap | research | 环道 0.15 + 大厅 0.55 |

### 5.4 不要采纳的反模式

| # | 反模式 | 来源 | 原因 |
|---|--------|------|------|
| 1 | 硬编码路点 + 无全局规划 | 清越队 | 无法应对动态障碍, 场地变化需重新部署 |
| 2 | YOLOv8n CPU 推理 | 清越队 | RDK X5 CPU 无法承受, 我们有 BPU |
| 3 | `cache_obstacle_heuristic: false` | ackermann_car | 他们仿真不需要, 我们嵌入式必须用 |
| 4 | `max_allowed_time_to_collision: 2.0` | ackermann_car | 仿真值, 窄道实战会撞墙 |
| 5 | `use_fixed_curvature_lookahead: false` | ackermann_car | Iron+ 功能, Humble 不支持. 我们 YAML 中的值静默忽略 |
| 6 | VoxelLayer 同时用于 global costmap | ackermann_car | global 用 static 更好 (他们有) |

---

## 附录: 文件清单

### ackermann_car-main 关键文件
```
src/ackermann_car/
├── config/nav2_params.yaml          ← Nav2 全部参数 (主要参考)
├── config/nav2_slam_params.yaml     ← SLAM 参数
├── config/ros2_control.yaml         ← ros2_control 控制器配置
├── config/slam_toolbox.yaml         ← 离线 SLAM
├── config/slam_toolbox_online.yaml  ← 在线 SLAM
├── behavior_trees/ackermann_navigate.xml ← 行为树
├── ackermann_car/ackermann_controller.py ← 阿克曼运动学解算 (左右轮差速)
├── ackermann_car/nav2_ackermann_bridge.py ← Twist→Ackermann 桥接
├── ackermann_car/twist_to_ackermann.py    ← 同上 (简化版)
├── ackermann_car/odom_publisher.py        ← 里程计发布
├── ackermann_car/keyboard_teleop.py       ← 键盘遥控
├── launch/navigation.launch.py            ← 导航启动
├── launch/slam.launch.py                  ← SLAM 启动
├── launch/slam_nav.launch.py              ← SLAM+Nav 联合启动
├── launch/ignition.launch.py              ← Gazebo 仿真启动
├── launch/display.launch.py               ← RViz 显示
└── urdf/ackermann_car.urdf.xacro          ← 机器人模型 (完整 ros2_control)
```

### racing_control-develop 关键文件
```
├── src/racing_control.cpp           ← 核心控制逻辑 (巡线+避障)
├── include/racing_control/racing_control.h ← 头文件 (参数定义)
├── launch/racing_control.launch.py        ← 实际场景启动
├── launch/racing_control_simulation.launch.py ← 仿真启动
├── CMakeLists.txt
└── README_cn.md
```

### rdkx5-smart-medical-car--main 关键文件
```
ros2_ws/src/
├── task_manager/task_manager/task_manager_node.py  ← 状态机 (竞赛主逻辑)
├── navigation/navigation/path_planner_node.py      ← 硬编码路点规划
├── navigation/navigation/motion_controller_node.py ← P控制
├── navigation/navigation/obstacle_avoidance_node.py ← 简单避障
├── navigation/config/navigation_params.yaml        ← 导航参数
├── qr_detector/qr_detector/qr_detector_node.py     ← pyzbar QR
├── human_detector/human_detector/human_detector_node.py ← YOLOv8n
├── human_detector/human_detector/llm_interface_node.py   ← GPT-4o VLM
├── voice_output/voice_output/voice_output_node.py  ← TTS 语音
└── docs/技术文档.md                                  ← 完整技术文档
```

---

> **下一步**: 将高优先级参数变更在 RDK X5 上测试, 每次只改 1-2 个参数, 用 `plot_trajectory.py` 对比效果.
> **相关**: [[project_racing_vision_ai_paths]], [[project_ackermann_nav2_constraints]], [[project_best_baseline]]
>
> ---
>
> ## 6. EXA MCP 广泛搜索 — 最新研究与实践
>
> > 8 个搜索主题, 40+ 搜索结果, 11 篇深度提取.
> > 完整报告: [ros2_ackermann_racing_latest_techniques.md](ros2_ackermann_racing_latest_techniques.md)
>
> ### 6.1 RPP Cusp Bug 深度剖析
>
> Humble RPP 有两个 cusp 相关 bug:
>
> **#4757 (缺 cusp 检测)**: RPP `path_handler.cpp` 在 Humble 中无 `enforce_path_inversion` 逻辑 (MPPI 有). REEDS_SHEPP cusp 处 RPP 跳过路径段.
>
> **#5098 (固定曲率前视过冲 cusp)**: ★ 此 bug 不适用 Humble — `use_fixed_curvature_lookahead` 是 Iron+ 功能, Humble RPP 根本不支持. 仅在 Iron/Jazzy 中 `use_fixed_curvature_lookahead: true` 时触发.
>
> **修复 (PR #5134, 2行代码, Jazzy 已合入)**:
> ```cpp
> double dist_to_cusp = findVelocitySignChange(transformed_plan);
> if (dist_to_cusp < curv_lookahead_dist) {
>     curv_lookahead_dist = dist_to_cusp;  // 钳位到 cusp!
> }
> ```
>
> **Humble 缓解方案 (无需改源码)**:
> | 方案 | 做法 | 代价 |
> |------|------|------|
> | D | `reverse_penalty: 5.0+` | 强阻换向, 减少 cusp 生成 |
> | B | 手动打 patch (2行) | 需重新编译 Nav2 |
> | C | 切换 DUBIN 替代 REEDS_SHEPP | 失去倒车能力 |
> | A | 用 MPPI 替代 RPP | MPPI 已有 `enforce_path_inversion` |
>
> **推荐**: 方案 D (已在用 `change_penalty=0.20`) + 进一步提高 `reverse_penalty` 到 5.0.
>
> ### 6.2 PP vs MPC — Sim-to-Real 关键发现
>
> Stellenbosch 大学 F1TENTH 物理实验 (2024-2026):
>
> | 指标 | PP | MPC | MPCC |
> |------|:---:|:---:|:---:|
> | 仿真圈速 | 最慢 | 中 | 最快 (-3s) |
> | **物理圈速** | **最好** 🏆 | 中 | **失败** |
> | 物理控制频率 | **8.77 Hz** | 5 Hz | 3.07 Hz |
> | 计算时间 | ~0.1ms | ~50ms | ~200ms |
> | 定位噪声鲁棒性 | 中 | 好 | 差 |
>
> **核心发现**: PP 在物理测试中胜过 MPC! 原因:
> - AMCL 粒子滤波噪声 → MPC 对错误位置做优化 → 灾难性振荡
> - 100ms 延迟 @ 1m/s = 0.1m 位置误差 → MPC 优化错误状态
> - PP 简单 = 高频率 = **更准确的真实世界控制**
>
> **对 RDK X5 的启示**: 不要在 A55 上跑 MPC (OSQP 求解器 <5Hz). PP/RPP 的频率优势比模型预测能力更重要.
>
> ### 6.3 SmacPlannerHybrid 窄通道基准
>
> GitHub #4808 基准 (BriceRenaudeau):
>
> | 优化前 | 优化后 | 路径长度 | 说明 |
> |--------|--------|----------|------|
> | 0.61s | **0.15s (4×)** | 124m | 窄通道 |
> | 0.63s | **0.16s (4×)** | 143m | 窄通道 |
> | 4.51s | 1.58s | 19m | 需 360 bins |
>
> **关键配置**: `angle_quantization_bins: 64-72`, `allow_primitive_interpolation: true`, `retrospective_penalty: 0.015`, `cost_penalty: 1.3-3.5`.
>
> **重要警告**: `angle_quantization_bins=360` 是常见错误 — 在大地图上增加搜索分支因子却未改善路径质量. 72 是 sweet spot.
>
> ### 6.4 Keepout + Inflation 交互陷阱
>
> Nav2 文档确认: **Costmap Filter 不经过 inflation layer!** 这意味着:
> - SE2 footprint 检查可能看不到 keepout 边缘
> - Smac Hybrid 可行规划器的中心点碰撞检查能看到, 但 footprint 边缘可能穿透
>
> **修复**:
> ```yaml
> filters: ["keepout_filter", "keepout_inflation"]
> keepout_inflation:
>   plugin: "nav2_costmap_2d::InflationLayer"
>   inflation_radius: 0.3
>   cost_scaling_factor: 5.0
> ```
>
> ### 6.5 OpenMP Costmap 加速
>
> 2000×2000 栅格 (4M cells) 基准:
> - 无 OpenMP: 48.9 ms
> - 有 OpenMP (16核): **9.11 ms (5.4×)**
>
> RDK X5 的 4×A55 可以从 OpenMP 受益. 编译:
> ```bash
> colcon build --packages-select nav2_costmap_2d --cmake-args -DENABLE_OPENMP=ON
> ```
>
> ### 6.6 PPO 自适应 PP 调参 (前沿)
>
> ICPS-LAB-WVU (IEEE RA-L 2026): PPO 联合在线调节 `L_d` (前视距离) + `g` (转向增益).
> - 状态: 速度 + 3 曲率采样点 (近/中/远)
> - 输出: `[L_d, g]` 控制对
> - 结果: 持续优于固定 PP、速度自适应 PP、运动学 MPC
> - 代码: https://github.com/ICPS-LAB-WVU/Learning-to-Tune-Pure-Pursuit-in-Autonomous-Racing-With-PPO
>
> **实用启示**: PPO 在线训练太重, 但曲率分段 L_d/g 查表法可以手动实现 — 弯道短前视+大增益, 直道长前视+小增益.
>
> ### 6.7 整合建议: 完整参数基线修订
>
> 综合 ackermann_car-main + EXA 搜索 + Smac Planner 论文:
>
> ```yaml
> # === SmacPlannerHybrid ===
> GridBased:
>   minimum_turning_radius: 0.30                 # 我们实测值 (不变)
>   angle_quantization_bins: 64                   # ↑ 40→64 (5.6°/bin, 更平滑)
>   analytic_expansion_max_length: 3.0            # ↑ 1.5→3.0 (>5×min_r)
>   reverse_penalty: 5.0                          # ↑ 4.0→5.0 (强阻换向, 防cusp)
>   non_straight_penalty: 1.30                    # ↓ 1.85→1.30 (接近官方推荐)
>   cost_penalty: 3.5                             # ↓ 6.33→3.5 (减少不必要绕行)
>   retrospective_penalty: 0.015                  # ★ 新增: 防规划绕圈
>   allow_primitive_interpolation: true            # ★ 新增: 减少窄道 zigzag
>   cost_travel_multiplier: 2.0                   # ★ 新增: 速度vs安全权衡
>
> # === RPP Controller ===
> FollowPath:
>   controller_frequency: 20.0                    # ↑ 10→20Hz (每周期2.5cm vs 5cm)
>   speed_lim_angular: true                       # ★ 新增: 弯道限角速度
>   approach_velocity_scaling_dist: 0.6           # ★ 新增: 进场减速
>   max_angular_vel: 1.2                          # ★ 新增: 角速度上限
>
> # === Keepout ===
> global_costmap:
>   filters: ["keepout_filter", "keepout_inflation"]   # ★ keepout 独立 inflation
>   keepout_inflation:
>     plugin: "nav2_costmap_2d::InflationLayer"
>     inflation_radius: 0.3
>     cost_scaling_factor: 5.0
> ```
>
> ### 6.8 不要采纳的 EXA 建议
>
> | 建议 | 原因 |
> |------|------|
> | MPC (OSQP 求解器) | A55 上 ~5Hz, 不如 20Hz RPP |
> | MPPI 替代 RPP | 需 cross-compile C++, Humble MPPI 成熟度低 |
> | `change_penalty: 0.0` (官方推荐) | 我们的 0.20 已验证抑制 cusp 有效 |
> | `use_cost_regulated_linear_velocity_scaling: false` | 窄道场景需要 cost 感知减速 |
>
> ### 6.9 Graceful Controller 曲率公式 (完整)
>
> Nav2 Graceful Controller 实现 Park (2016) "Smooth Control Law":
>
> ```cpp
> // 核心曲率-速度映射
> double v = v_linear_max_ / (1.0 + beta_ * std::pow(fabs(curvature), lambda_));
> // 目标接近减速
> v = std::min(v_linear_max_ * (ego_coords.r / slowdown_radius_), v);
> // 角速度
> double w = curvature * v;
> ```
>
> | 参数 | 默认值 | 说明 |
> |------|--------|------|
> | `beta` | 0.4 | 曲率速度下降因子: 越大弯道越慢 |
> | `lambda` | 2.0 | 曲率锐度: ≥1, 越大弯道响应越陡 |
> | `k_phi` | 0.4 | phi 变化率 / r 变化率. 0=纯路点跟踪 |
> | `k_delta` | 3.0 | 航向误差反馈增益 (快子系统收敛) |
> | `slowdown_radius` | 0.5 | 目标接近减速半径 |
> | `motion_target_dist` | 1.0 | 目标点前视 (~1.0m) |
>
> **对比我们的 speed_profile_node**: `v(κ) = v_max/(1+β·|κ|^λ)` 同公式! β=0.25, λ=1.20. 我们更激进 (弯道更快). Graceful Controller 的 Lyapunov 曲率计算比我们的 Menger 3 点法更数学严谨.
>
> ### 6.10 Ackermann 恢复 BT 完整 XML (参考模板)
>
> ```xml
> <RecoveryNode number_of_retries="6">
>   <PipelineSequence>
>     <RateController hz="1.0">
>       <RecoveryNode number_of_retries="1">
>         <ComputePathToPose goal="{goal}" path="{path}"/>
>         <ClearEntireCostmap service_name="global_costmap/clear_entirely_global_costmap"/>
>       </RecoveryNode>
>     </RateController>
>     <RecoveryNode number_of_retries="1">
>       <FollowPath path="{path}"/>
>       <ClearEntireCostmap service_name="local_costmap/clear_entirely_local_costmap"/>
>     </RecoveryNode>
>   </PipelineSequence>
>   <ReactiveFallback>
>     <GoalUpdated/>
>     <RoundRobin>
>       <Sequence>
>         <ClearEntireCostmap service_name="local_costmap/clear_entirely_local_costmap"/>
>         <ClearEntireCostmap service_name="global_costmap/clear_entirely_global_costmap"/>
>       </Sequence>
>       <!-- ★ 替代 Spin: 多级后退 (阿克曼不可原地旋转) -->
>       <BackUp backup_dist="0.30" backup_speed="0.10"/>
>       <Wait wait_duration="3"/>
>       <BackUp backup_dist="0.50" backup_speed="0.15"/>
>     </RoundRobin>
>   </ReactiveFallback>
> </RecoveryNode>
> ```
>
> ### 6.11 Inflation vs 通道宽度公式
>
> 对于通道宽度 W, 机器人外接圆半径 R:
> - **最小可行**: `inflation_radius < (W/2 - R)` — 否则机器人看不到可通过间隙
> - **最优**: `inflation_radius` 形成梯度在通道中间汇合
> - **Origincar (R≈0.35m) 在 1.0m 通道**: `inflation_radius <= 0.15m` 才能通过, 但理想 0.5-0.8m
> - **我们 0.5m 环道 + inflation 0.55m**: 通道被完全填充 (这正是 §17 中记录的已知问题!)
>
> **Nav2 维护者原话**:
> > "Set your inflation radius to be at MINIMUM half of the robot's largest cross-section." — Steve Macenski
> > "The true value of the inflation layer is creating a consistent potential field around the entire map." — Nav2 Tuning Guide
>
> ---
>
> > **来源**: 本章节整合自 EXA MCP 广泛搜索 (8 topics × 40+ results) + Smac Planner 论文 (Macenski 2024) + Nav2 官方文档 + F1TENTH 社区. 原始 EXA 报告已合并, 无独立文件.
