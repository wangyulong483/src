# 知识库 Wiki — object-detector-fusion 引入研究

> **日期**: 2026-06-29 | **源项目**: `object-detector-fusion-master` (ROS1 Melodic)
> **目标**: 将源项目的感知-跟踪-融合技术迁移到当前 RDK X5 + ROS2 Humble 竞赛项目

---

## 1. 源项目架构总览

### 1.1 定位

`object-detector-fusion-master` 是一个 ROS1 Melodic 包，实现了 **2D LiDAR + 深度相机双传感器融合 → 多目标粒子滤波跟踪** 的完整 pipeline。

### 1.2 核心文件清单

| 文件 | 行数 | 功能 |
|------|------|------|
| [src/multi_particle_filter_a.py](src/object-detector-fusion-master/src/multi_particle_filter_a.py) | 90 | **纯数学库**：7个函数，零 ROS 依赖 |
| [src/multipf.py](src/object-detector-fusion-master/src/multipf.py) | 382 | **主 PF 节点**：N=1000 粒子、7D 状态、3 目标跟踪、匈牙利关联、多元高斯融合 |
| [src/obstacle_pf.py](src/object-detector-fusion-master/src/obstacle_pf.py) | ~430 | 轻量版 PF (N=10 粒子) |
| [src/pf_analysis.py](src/object-detector-fusion-master/src/pf_analysis.py) | ~190 | RViz OverlayText 可视化 + CSV 导出 |
| [src/pf_analysis_fusion.py](src/object-detector-fusion-master/src/pf_analysis_fusion.py) | ~190 | 融合版可视化（含 LiDAR 数据） |
| [launch/fusion.launch](src/object-detector-fusion-master/launch/fusion.launch) | 194 | 完整 pipeline：相机→深度→激光扫描→障碍提取→PF 跟踪→RViz |

### 1.3 数据流

```
[RealSense D435]                    [RPLiDAR A1]
      |                                   |
depth image (/camera/depth/image_rect_raw)   laserscan (/laserscan)
      |                                   |
[depthimage_to_laserscan]             [laser_filters (angular bounds)]
      |                                   |
/camera/depth/laserscan               /scan_filtered
      |                                   |
[camera_obstacle_extractor]           [lidar_obstacle_extractor]
(obstacle_detector 密度聚类)          (obstacle_detector 密度聚类)
      |                                   |
/raw_obstacles/camera_obstacles       /raw_obstacles/lidar_obstacles
      \_________________________________/
                    |
          [particle_filter node]
          (multipf.py — ParticleFilter class)
          ├─ 线性校准 (camera + lidar)
          ├─ 匈牙利数据关联 (时序 + 跨传感器)
          ├─ 数据门控 (camera cost >5 拒绝, lidar cost <0.5 融合)
          ├─ 多元高斯传感器融合
          ├─ 恒加速度运动模型预测
          ├─ 多元高斯似然更新
          ├─ 系统重采样 (Neff < N/2)
          └─ 周期性重初始化 (10s 或 发散>2m)
                    |
         /estimate/viz/mean          (Marker: CUBE_LIST 品红框)
         /estimate/viz/particles     (Marker: POINTS 黑点)
         /estimate/values/mean       (Float32MultiArray: 3×7 状态矩阵)
         /runtime                    (Float32: 处理时间 ms)
```

### 1.4 核心算法

#### 状态向量 (7D)
```
[x, y, vx, vy, ax, ay, true_radius]
 0  1   2   3   4   5       6
```

#### 运动模型 — 恒加速度 (CA)
```python
# predict() — multi_particle_filter_a.py:32-49
a += noise              # 加速度随机游走
v += a*dt + noise       # 速度 + 加速度积分
x += v*dt + 0.5*a*dt² + noise  # 位置 + 速度积分 + 加速度积分
radius += noise         # 半径随机游走
```

#### 观测模型 — 多元高斯似然
```python
# update_multivariate() — multi_particle_filter_a.py:62-69
weights *= scipy.stats.multivariate_normal.pdf(x=particles[:, [0,1,6]], mean=z, cov=R)
```
观测为 `[x, y, radius]`，协方差矩阵 R 为对角阵。

#### 传感器融合 — 多元高斯乘积
```python
# 当 LiDAR 可用 + 关联代价 < 0.5 时
zs, sigma = multivariate_multiply(camera, cam_cov, lidar, lid_cov)
# cam_cov  = diag([0.35², 0.25², 0.1²])  — 相机不确定性
# lid_cov   = diag([0.05², 0.05², 0.05²])  — LiDAR 不确定性 (7x 更精确)
# 融合后 LiDAR 权重自然占主导
```

#### 数据关联 — 匈牙利算法
```python
# cost_function() — multipf.py:151-155
cost = sqrt((x_i - x_j)² + (y_i - y_j)² + (r_i - r_j)²)
row_idx, col_idx = linear_sum_assignment(cost_matrix)
```

#### 传感器线性校准
```python
# multipf.py:157-158
camera: x_cal = 0.7485*x_raw + 0.2889,  y_cal = 0.9955*y_raw - 0.0108
lidar:  x_cal = 1.0124*x_raw - 0.0401,  y_cal = 0.9982*y_raw - 0.0215
```

---

## 2. 分级借用以鉴清单

### 2.1 🟢 绿色 — 低投入 / 高收益 (直接复制)

#### G1. 纯粒子滤波数学库 ✦最高优先级✦

**文件**: `multi_particle_filter_a.py` (90 行)

**零 ROS 依赖** — 仅使用 `numpy` + `scipy.stats`。7 个函数可直接复制到新 ROS2 包：

| 函数 | 用途 |
|------|------|
| `create_gaussian_particles(mean, std, N)` | 初始化 N 个 7D 高斯粒子 |
| `predict(particles, std, dt)` | CA 运动模型预测 |
| `update_multivariate(particles, weights, z, R)` | 多元高斯似然加权 |
| `estimate(particles, weights)` | 加权均值 + 方差 |
| `neff(weights)` | 有效样本量 (触发重采样) |
| `resample_from_index(particles, weights, indexes)` | 系统重采样 |
| `create_initial_weights(N)` | 均匀权重初始化 |

**需替换的依赖**:
- `filterpy.monte_carlo.systematic_resample` → numpy 实现 (~10 行)
- `filterpy.stats.multivariate_multiply` → 直接高斯乘积公式 (~5 行 numpy)

**竞赛影响**: 提供跟踪所需的所有数学基础。即使只做单目标跟踪，这也是必须的核心。

#### G2. 匈牙利算法代价函数

**文件**: `multipf.py:151-155` + `objects_assigner()` (lines 160-171, ~20 行)

3D 代价函数 `cost = sqrt((Δx)² + (Δy)² + (Δr)²)` 可用于：
- 新检测→已有跟踪的分配
- 多传感器数据关联
- 误检过滤 (cost > 阈值 → 拒绝)

**竞赛影响**: 在窄道环境中 (最多 1-2 个障碍物)，匈牙利算法的开销几乎为零，但能可靠防止 track-swapping。

#### G3. 多元高斯传感器融合公式

**文件**: `multipf.py:108-116` (~10 行)

核心逻辑：
```python
if lidar_available and cost < 0.5:
    zs, sigma = gaussian_product(camera, cam_cov, lidar, lid_cov)
else:
    zs = camera  # 回退到相机
```
LiDAR 协方差比相机小 7 倍 → 融合后 LiDAR 自然主导 → 更精确的障碍物位置。

**竞赛影响**: Aurora930 深度相机在远距离噪声大，N10 LiDAR 稀疏但精确。融合两者结合密集覆盖 + 精确定位。

#### G4. 角度滤波配置

**文件**: `my_laser_config.yaml` (5 行)

```
angular_bounds: [-0.69, +0.69] rad  (~80° 前向 FOV)
```

N10 LiDAR 每圈 2000 点。限制到前向 80° → ~380 点 → AMCL + costmap 处理负载降低 80%。

**竞赛影响**: 直接节省 Cortex-A55 的 CPU 周期。已有 `laser_filters` ROS2 包可用。

---

### 2.2 🟡 黄色 — 中等投入 / 高收益 (需 ROS2 移植)

#### Y1. 轻量单目标粒子滤波跟踪器 ✦最高优先级✦

**来源**: `obstacle_pf.py` + `multipf.py` 算法

**新建文件**: `object_tracker/tracker_node.py` (~200 行)

关键适配：

| 方面 | 源 (ROS1) | 目标 (ROS2) |
|------|-----------|-------------|
| 粒子数 | N=1000 (3 目标) | **N=50** (1 目标) |
| 状态维度 | 7D [x,y,vx,vy,ax,ay,r] | **5D** [x,y,vx,vy,r] (去掉加速度) |
| 更新频率 | 60Hz (外部 rate 节点) | **5Hz** (内部 Timer) |
| 消息类型 | `obstacle_detector/Obstacles` | `geometry_msgs/Point` 数组 |
| 依赖 | `filterpy` | **仅 scipy + numpy** |
| 重采样触发 | Neff < N/2 | Neff < N/2 (同) |
| 重初始化 | 10s 或 发散>2m | 10s 或 发散>1.5m (更小环境) |
| LiDAR 超时 | 80ms (10Hz RPLiDAR) | **400ms** (5Hz N10, 允许丢 2 帧) |

**竞赛影响 (量化)**:
- 估计障碍物速度 → 预测碰撞 → 提前 1-2s 反应
- 单帧噪声检测被过滤 → 减少误减速
- 障碍物在接近还是远离 → 决定加速/减速策略

#### Y2. 深度相机障碍物检测节点

**新建文件**: `object_tracker/depth_detector.py` (~150 行)

替代 `obstacle_detector` C++ 包 (~2000行) 的方式：
1. 订阅 `/aurora/depth/image_raw` (15fps)
2. 提取水平中心行 (row 200, 640px → 640 深度值)
3. 投影到 3D 相机坐标 (使用 Aurora930 内参: fx=421.3, fy=422.3, cx=320.3, cy=197.0)
4. 丢弃 Z 轴 → 2D 障碍物点
5. `sklearn.cluster.DBSCAN` 聚类 (eps=0.3m, min_samples=5)
6. 发布聚类中心 `geometry_msgs/Point` 数组

**竞赛影响**:
- Aurora930 点云首次被用于导航感知 (目前完全闲置)
- 深度相机检测范围补充 LiDAR 稀疏区域
- ~150 行 Python 替换 ~2000 行 C++ 移植

#### Y3. Costmap 动态障碍物集成

**新建文件**: `object_tracker/costmap_publisher.py` (~80 行)

将跟踪结果发布为 `sensor_msgs/PointCloud2`，通过 Nav2 已有的 `obstacle_layer` 观察源机制自动集成。

**修改文件**: `originbot_navigation/param/originbot_nav2_rpp.yaml`
```yaml
obstacle_layer:
  observation_sources: scan tracked_obstacles  # ← 新增
  tracked_obstacles:
    topic: /tracked_obstacles_cloud
    data_type: PointCloud2
    marking: true
    clearing: false
    obstacle_range: 3.5
    min_obstacle_height: 0.05
    max_obstacle_height: 2.0
```

**竞赛影响**: 零规划器/控制器改动 → Nav2 自动避让跟踪到的障碍物。这是从"检测到障碍物"到"避开障碍物"的最短路径。

#### Y4. RViz2 可视化

修改 `originbot_navigation/rviz/nav.rviz` 添加：
- Marker 显示 `/tracked_objects/mean` (品红框, CUBE_LIST)
- Marker 显示 `/tracked_objects/particles` (黑点, POINTS)
- Float32MultiArray 显示状态值 (用于调试)

**竞赛影响**: 调试和参数调优的关键工具。当前完全没有障碍物感知的可视化。

---

### 2.3 🔴 红色 — 高投入 / 高收益 (需架构变更)

#### R2. 完整多目标多传感器融合管线

移植完整的 `multipf.py` (382 行)，支持 3 目标同时跟踪 + 匈牙利跨传感器关联 + 完整融合门控。

**前提条件**: Phase 1-2 (Y1-Y4) 完成 + CPU 预算验证。

**风险**: N=1000×3 目标 的 PF 在 Cortex-A55 上可能导致 CPU 过载。需要先用 N=200 测试。

---

### 2.4 ⬜ 灰色 — 低优先级或不必要

| 编号 | 内容 | 原因 |
|------|------|------|
| N1 | CSV 数据导出 | `competition_master_stage3.py` 已有 14 列 CSV + plans CSV |
| N2 | TF Broadcaster | URDF + `robot_state_publisher` 已处理 |
| N3 | jsk_rviz_plugins OverlayText | ROS2 无直接等效，用 Marker 文字替代 |
| N4 | 传感器线性校准节点 | Aurora930 + N10 已有 TF 外参标定；源项目的每轴 y=ax+b 是 D435 特定修正 |
| N5 | obstacle_detector C++ 包移植 | ~2000 行 C++，Y2 方案的 Python DBSCAN 替代更轻量 |

---

## 3. 分阶段实施路线图

### Phase 1: 基础 (Day 1, ~6h) — 🟢 绿色项

**目标**: 基本障碍物检测 + 跟踪工作，CPU 增量 <3%

| 步骤 | 产出 | 预计 |
|------|------|------|
| 1.1 | 创建 `object_tracker` ROS2 Python 包骨架 | 30min |
| 1.2 | 复制并适配 `pf_math.py` (去掉 filterpy 依赖) | 1h |
| 1.3 | `pytest` 单元测试 pf_math 7 个函数 | 30min |
| 1.4 | 实现 `depth_detector.py` (深度切片→DBSCAN→中心) | 2h |
| 1.5 | 实现 `tracker_node.py` (PF 包装节点, N=50, 5Hz) | 2h |

**创建的文件**:
```
object_tracker/
├── package.xml
├── setup.py
├── setup.cfg
├── launch/tracker.launch.py
└── object_tracker/
    ├── __init__.py
    ├── pf_math.py          ← G1 (来自 multi_particle_filter_a.py)
    ├── depth_detector.py   ← Y2
    └── tracker_node.py     ← Y1
```

### Phase 2: 集成 (Day 2, ~4h) — 🟡 黄色项

**目标**: 跟踪结果进入 Nav2 costmap → 自动避让

| 步骤 | 产出 | 预计 |
|------|------|------|
| 2.1 | 实现 `costmap_publisher.py` | 1h |
| 2.2 | 修改 `originbot_nav2_rpp.yaml` 添加观察源 | 30min |
| 2.3 | 修改 `stage3_bringup.launch.py` 添加 tracker 节点 | 30min |
| 2.4 | 修改 `nav.rviz` 添加可视化 | 30min |
| 2.5 | 在 RDK X5 上测试完整流程 | 1.5h |

### Phase 3: 调优 (Day 3, ~3h)

**目标**: 在实机上调优参数，测量 CPU 影响

| 步骤 | 产出 | 预计 |
|------|------|------|
| 3.1 | 添加 CPU 监控到 tracker 节点 | 30min |
| 3.2 | 参数调优 (粒子数, DBSCAN eps, 过程噪声) | 1.5h |
| 3.3 | 5 轮带/不带 tracker 的完整 stage3 对比 | 1h |

---

## 4. 竞赛影响分析

### 4.1 直接圈速节省

| 改进 | 机制 | 预计节省 | 可信度 |
|------|------|---------|--------|
| 动态障碍物跟踪 | 避免碰撞停车/重启 | 15-50s | 中 |
| 更智能的 costmap | 仅在被跟踪障碍物周围标记，而非全面膨胀 | 2-5s | 低 |
| RETURN_P 可靠性 | 障碍物感知 → 减少窄道规划失败 | 10-50s | 中 |

### 4.2 可靠性提升 (难量化)

- **障碍物速度估计**: 知道障碍物在接近 → 可主动加速或减速
- **误检过滤**: 跟踪滤除单帧噪声 → 减少不必要减速
- **多传感器冗余**: LiDAR 丢失 → 深度相机兜底，反之亦然
- **可视化**: 操作员可看到机器人"看到"什么 → 更快调试

### 4.3 单项最大收益

**Phase 1 基础跟踪器 + Phase 2 costmap 集成** 提供最大收益：

1. 赋予当前完全没有的障碍物检测能力
2. 直接融入 Nav2 (通过已有的 costmap 基础设施)
3. CPU 影响极小 (N=50 PF @ 5Hz ≈ 0.1ms 更新时间)
4. 立即改善 RETURN_P (最容易失败的阶段)

---

## 5. CPU 预算分析

### 5.1 每帧 CPU 成本估算

| 组件 | 操作 | 预估 CPU @ 5Hz | 备注 |
|------|------|----------------|------|
| 深度切片提取 | 640 float 读取 + numpy 数组 | ~0.5ms | 向量化 |
| DBSCAN 聚类 | sklearn C 实现 | ~1-2ms | ~50 点 (阈值过滤后) |
| PF predict (N=50) | 50 × 5D numpy | ~0.2ms | 向量化 |
| PF update (N=50) | 50 × multivariate_normal.pdf | ~0.5ms | scipy C 实现 |
| 重采样 (N=50) | O(N) systematic | ~0.1ms | 纯 numpy |
| PointCloud2 发布 | 序列化 + DDS | ~0.3ms | 小消息 |
| **每帧总计** | | **~2-3ms** | |
| **每秒 @ 5Hz** | | **~10-15ms** | = 1-1.5% CPU 单核 |

### 5.2 回退策略

| 触发条件 | 措施 | 预期 CPU |
|----------|------|---------|
| 当前基线 (75-100%) | 2Hz 更新 + N=20 粒子 | ~0.4% |
| 仍不够 | 关闭深度检测, 仅 PF 预测 | ~0.2% |

---

## 6. ROS1 → ROS2 消息类型映射

| ROS1 (源) | ROS2 (目标) | 说明 |
|-----------|-------------|------|
| `obstacle_detector/Obstacles` | `visualization_msgs/msg/MarkerArray` | 障碍物圆可视化 |
| `obstacle_detector/CircleObstacle` | `geometry_msgs/msg/Point` + `Float32` (radius) | 简化，标准类型 |
| `std_msgs/Float32MultiArray` (via `numpy_msg`) | `std_msgs/msg/Float32MultiArray` | 直接等价 |
| `geometry_msgs/Point` | `geometry_msgs/msg/Point` | 直接等价 |
| `visualization_msgs/Marker` | `visualization_msgs/msg/Marker` | 直接等价 |
| `sensor_msgs/LaserScan` | `sensor_msgs/msg/LaserScan` | 直接等价 |
| `jsk_rviz_plugins/OverlayText` | `std_msgs/msg/String` / Marker TEXT_VIEW_FACING | 无 ROS2 直接等效 |
| `nav_msgs/Odometry` | `nav_msgs/msg/Odometry` | 直接等价 |

---

## 7. 关键参数参考表

| 参数 | 源值 | 建议目标值 | 调优方向 |
|------|------|-----------|---------|
| 相机 sigma x | 0.35m | 0.30m | Aurora930 深度噪声待实测；从保守开始 |
| 相机 sigma y | 0.25m | 0.25m | 同 |
| 相机 sigma radius | 0.10m | 0.10m | 同 |
| LiDAR sigma x | 0.05m | 0.05m | N10 精度与 RPLiDAR A1 相似 |
| LiDAR sigma y | 0.05m | 0.05m | 同 |
| LiDAR sigma radius | 0.05m | 0.05m | 同 |
| predict std (位置) | 0.02m | 0.02m | CA 模型过程噪声 |
| predict std (速度) | 0.04 m/s | 0.04 m/s | 同 |
| predict std (半径) | 0.04m | 0.04m | 同 |
| 相机时域关联门控 | 5.0 | **3.0** | 更窄通道 → 更小预期位移 |
| 传感器融合门控 | 0.5 | 0.5 | 同 |
| LiDAR 超时 | 80ms | **400ms** | N10 5Hz = 200ms 周期；允许 2 帧丢 |
| 重初始化周期 | 10s | 10s | 同 |
| 重初始化发散阈值 | 2m | **1.5m** | 更小比赛区域 |
| DBSCAN eps | 0.3m | 0.3m | 从源值开始，在 Aurora930 上调 |
| DBSCAN min_samples | 5 | 5 | 同 |
| 角度滤波下界 | -0.69 rad | -0.69 rad | ~80° 前向 FOV |
| 角度滤波上界 | +0.69 rad | +0.69 rad | 同 |
| 粒子数 N | 1000 | **50** | 3 目标 → 1 目标；乘 20x 减少 |
| 状态维度 | 7D | **5D** | 去掉 ax, ay (不可靠) |

---

## 8. 算法决策：保持 / 修改 / 替换

### 保持 (原样复制或纯 numpy 适配)

1. **PF 数学库** (`multi_particle_filter_a.py`) — 全部 7 个函数
2. **恒加速度运动模型** — 标准运动学，无需改动
3. **系统重采样** — Neff < N/2 触发条件不变
4. **数据门控模式** — 阈值需要重新调优，但门控逻辑不变
5. **LiDAR 超时回退** — 模式不变，超时时长适配 N10

### 修改 (保留概念，改变实现)

1. **7D → 5D 状态** — 去掉 ax, ay (从噪声数据估计的加速度不可靠，没有可操作性)
2. **N=1000 → N=50** — 单目标替代 3 目标，20x 更少 CPU
3. **obstacle_detector → DBSCAN** — Python `sklearn.cluster.DBSCAN` 替代 ~2000 行 C++
4. **jsk_viz → ROS2 Marker** — 标准 ROS2 Marker 替代自定义 RViz 插件
5. **外部 rate 控制 → 内部 Timer** — ROS2 `create_timer()` 替代独立 rate 节点

### 替换 (完全不同的方案)

1. **filterpy → scipy + numpy** — 消除外部依赖
2. **自定义 Obstacles 消息 → 标准 ROS2 消息** — `Point`, `Marker`, `PointCloud2`
3. **D435 特定校准 → 通用 pipeline** — 先用 TF 外参，需要时再加每轴校准

---

## 9. 风险与缓解

| 风险 | 概率 | 影响 | 缓解方案 |
|------|------|------|---------|
| Tracker 增加 CPU 负载降低 Nav2 性能 | 中 | 高 | 从 2Hz + N=20 开始；launch arg 可禁用 tracker |
| Aurora930 深度数据质量不足以做 DBSCAN | 中 | 中 | 降低聚类灵敏度 (增大 eps)；或改用 LiDAR-only 检测 |
| Costmap 集成导致规划器性能下降 | 低 | 中 | 新观察源只增加 1-3 点到 costmap；YAML 移除即恢复 |
| scipy 在 RDK X5 上不可用 | 低 | 高 | `python3-scipy` apt 包或 `pip install`；offline_tuner 已用 |
| N10 5Hz 太慢不适合跟踪 | 低 | 中 | 相机 (15fps) 提供高频更新；LiDAR 提供精度修正 |

---

## 10. 与当前项目架构的契合点

### 10.1 可以复用的现有基础设施

- **Aurora930**: 深度图 + RGB 已发布 (`/aurora/depth/image_raw`, `/aurora/rgb/image_raw`)
- **N10 LiDAR**: 扫描已发布 (`/scan`)，已用于 costmap
- **Nav2 costmap**: 已有多观察源框架，只需加一个 `observation_source`
- **轨迹系统**: `competition_master_stage3.py` 14 列 CSV 已含 CPU/内存/温度
- **EKF 融合模式**: 双 IMU 融合可作为传感器融合的已有参考

### 10.2 需要新增的

- 深度相机 → 障碍物检测 pipeline
- 障碍物跟踪节点 (PF)
- 跟踪结果 → costmap 桥接节点

### 10.3 不需要改动的

- Nav2 规划器/控制器 (costmap 自动处理)
- 阿克曼运动模型
- AMCL 定位
- 状态机 (competition_master)
- 禁区系统
- QR 检测
- VLM 推理

---

## 11. 验收标准

| 指标 | 当前基线 | 目标 |
|------|---------|------|
| 障碍物检测延迟 | N/A (无检测) | <200ms 传感器→costmap |
| 静态障碍物跟踪精度 | N/A | 位置误差 <0.1m (2s 收敛后) |
| Tracker CPU 开销 | 0% | <3% 单核 |
| RETURN_P 成功率 | ~80% | >95% (10 次统计) |
| 带 tracker 圈速 | 77.3s | <80s (基线 3% 以内) |
| 误检率 | N/A | <1 次/分钟 |

---

## 12. 参考链接

- 源项目 [multipf.py](src/object-detector-fusion-master/src/multipf.py) — 主 PF 节点 (382 行)
- 源项目 [multi_particle_filter_a.py](src/object-detector-fusion-master/src/multi_particle_filter_a.py) — 纯数学库 (90 行)
- 源项目 [fusion.launch](src/object-detector-fusion-master/launch/fusion.launch) — 完整 pipeline 配置 (194 行)
- 本项目 [competition_master_stage3.py](src/origincar/origincar_bringup/src/competition_master_stage3.py) — 状态机参考
- 本项目 [originbot_nav2_rpp.yaml](src/originbot_navigation/param/originbot_nav2_rpp.yaml) — Nav2 配置 (需修改)
- 本项目 [agent_do.md](src/Z_MD/agent_do.md) — 全部运行历史与根因分析
- 本项目 [.learnings/](src/.learnings/) — 结构化经验库 (30+ 条)
