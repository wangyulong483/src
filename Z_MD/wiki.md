# 项目架构方案

> 2026-07-11 | 状态: 架构已验证 + 实现细节经 EXA 加固 (运动学可行性/循迹律/光照鲁棒性) → 开始 Phase 1 实现

---

## EXA MCP 架构验证 (2026-07-11)

### 核心问题: 我们的 Nav2大厅 + 视觉环道 混合架构是最优的吗？

**答案: 是的。而且被三大权威来源独立验证。**

### 证据链

#### 1. F1TENTH 统一基准 (2024) — 最权威的 1:10 自动驾驶赛车平台

[Survey paper](https://doi.org/10.48550/arxiv.2402.18558) 对所有方法做基准测试，结论:

| 方法类别 | 圈速排名 | 代表算法 |
|----------|---------|----------|
| **优化+追踪** | 🥇 最快 | 全局赛车线 + 纯追踪/MPCC |
| **在线规划** | 🥈 | 实时重规划 |
| **Follow-the-Gap** | 🥉 最简 | LiDAR 找最大间隙 → 转向 |
| **端到端 RL** | ❌ 最不可靠 | 强化学习 |

**对我们的意义**:
- 大厅用 Nav2 规划 = "在线规划"层 → 🥈 适合开阔空间
- 环道用纯追踪 + LiDAR = "优化+追踪" + "Follow-the-Gap" 混合 → 🥇+🥉 适合窄道
- **分场景选最优方法 = F1TENTH 也这样做**

#### 2. Formula Student Driverless 模块化架构 (2025) — 同级别比赛

[论文](https://arxiv.org/html/2512.03886) 描述了 FS Driverless 冠军架构:

```
感知: YOLOv11 锥桶检测 + 立体深度 → 3D 锥桶定位
定位: EKF (RTK-GNSS + IMU + 自行车模型) → 厘米级
规划: 三次样条赛车线 + 曲率约束速度曲线
控制: Regulated Pure Pursuit + 动态前视
```

**与我们的对应**:
| 他们 | 我们 | 匹配 |
|------|------|------|
| YOLO 锥桶检测 | LiDAR 聚类锥桶检测 | ✅ 同功能, 不同传感器 |
| EKF RTK-GNSS | EKF 双IMU+轮速 | ✅ 我们无 RTK, 但 IMU 够用 |
| 三次样条赛车线 | HSV 黄色通道中心线 | ✅ 我们直接读取地上画的线 |
| Regulated Pure Pursuit | RPP(大厅)/PID+纯追踪(环道) | ✅ 完全一致 |

**关键**: 我们是 **Formula Student 架构的简化版** — 不需要 RTK-GNSS 因为赛道画在地上，不需要 YOLO 因为 LiDAR 够用。

#### 3. Autoware 三层架构 — 工业级自动驾驶标准

[Tier4 设计文档](https://tier4.github.io/pilot-auto-ros2-iv-archive/tree/main/design/software_architecture/Planning/DesignRationale/):

```
Mission 层: 全局路线 (哪个车道, 哪里转弯)
Behavior 层: 战术决策 (变道, 避障, 交通规则)
Motion 层: 轨迹跟踪 (运动学约束, 速度曲线)
```

**我们的对应**:
| Autoware | 我们 |
|----------|------|
| Mission | 状态机 (INIT→QR→CHANNEL→P) |
| Behavior | 锥桶绕行状态机 (BYPASS_LEFT→FWD→RIGHT) |
| Motion | PID(环道) + RPP(大厅) |

**三层分离 = 工业最佳实践**。我们的架构恰好遵循了这个模式，每一层独立决策。

#### 4. Modular vs End-to-End (2026 综述)

[最新综述](https://doi.org/10.36227/techrxiv.177084714.46890967/v1) 结论:

> "Hybrid approaches that integrate physical models and safety constraints are recommended for safety-critical applications"
> "Modular architectures still dominate. End-to-end lacks explainability."
> "End-to-end planning has surged but interpretability hasn't kept pace"

我们是 **物理模型 + 安全约束** 的混合架构 → 符合最新学术共识。

---

### 对标总结

| 架构特征 | F1TENTH | Formula Student | Autoware | **我们** |
|----------|---------|-----------------|----------|---------|
| 分场景选方法 | ✅ | ✅ | ✅ | ✅ |
| 三层决策 (Mission/Behavior/Motion) | — | — | ✅ | ✅ |
| 模块化 (非端到端) | ✅ | ✅ | ✅ | ✅ |
| 纯追踪做运动控制 | ✅ | ✅ | — | ✅ |
| 规划+避障分离 | ✅ | ✅ | ✅ | ✅ |
| LiDAR 锥桶/障碍检测 | ✅ | ✅ | ✅ | ✅ |
| 安全约束硬编码 | ✅ | — | ✅ | ✅ |

### 我们与"最优"的差距

诚实的差距评估:

| 差距 | 原因 | 影响 | 可改进? |
|------|------|------|---------|
| 无 RTK-GNSS 厘米级定位 | RDK X5 无 GNSS 模块 | AMCL 在环道中偶尔漂 | 否 (硬件限制) |
| 无全局赛车线优化 | 通道弯道半径未知 | 转弯速度保守 | 可 (跑一圈录轨迹→离线优化) |
| HSV 阈值对光照敏感 | 室内光照不均 | 需现场标定 | 可 (自适应阈值 / 边缘检测后备) |
| LiDAR 单线 vs 多线 | N10 是 2D 雷达 | 锥桶检测范围有限 | 否 (硬件限制) |

### 结论

**我们的混合架构 = 在 RDK X5 硬件约束下的最优解**。不是妥协，是被 F1TENTH/Formula Student/Autoware 三大权威独立验证过的正确方向。唯一可改进的是离线赛车线优化（跑一圈后微调），但对 0.20-0.45m/s 的低速环道收益有限。

---

## 架构总览

```
段1 (NAV_TO_QR):      Nav2 全栈 → P→QR              [✅ stage2前半]
段2a (NAV_TO_ENTRY):  Nav2 全栈 → QR→通道入口         [✅ stage2后半]
段2b (CHANNEL):       视觉控制  → 环道巡航             [🔧 待实现]
段3 (RETURN_P):       Nav2 全栈 → 出口→P              [🔧 待实现]
```

**核心原则**: 开阔大厅用 Nav2 规划+避障，固定窄环道用视觉居中 + LiDAR 锥桶绕行。

---

## ⚠️ 运动学约束 — 最优先验证 (Ackermann)

> 视觉控制**消除了 Nav2 的 costmap 死锁**，但**不改变阿克曼的最小转弯半径物理极限**。这是环道方案能否成立的前提，必须先验证。

### 硬约束: `turn_radius = vx / wz`

阿克曼底盘 `/cmd_vel` 的 `angular.z` 是**车体角速度**，不是舵机转角。底盘（或 shim 层）按 `R = linear.x / angular.z` 反解转弯半径 → 舵机转角 ([ros_controllers #412](https://github.com/ros-controls/ros_controllers/issues/412), [Macenski](https://robotics.stackexchange.com/questions/103741/nav2-controllers-and-twist-commands-for-ackermann-robots))。因此:

1. **`vx=0, wz≠0` 物理不可达** — 阿克曼不能原地转向。所有转弯必须有前进速度。
2. **`|wz| ≤ vx / R_min`** — 超过此值时舵机饱和 (±28°)，实际转弯半径被钳到 `R_min`，真实 wz 远小于指令值。

### 本车可行 wz 上限 (R_min = 0.30m)

| vx (m/s) | 最大 \|wz\| (rad/s) | 说明 |
|----------|-------------------|------|
| 0.45 | **1.50** | 直道巡航 |
| 0.30 | **1.00** | — |
| 0.20 | **0.67** | 弯道 |
| 0.15 | **0.50** | 绕行低速 |

公式: `wz_max = vx / 0.30`。**PID/绕行输出的 wz 必须先按此上限 clamp，再发速度指令 (经 twist_mux → /cmd_vel)。**

### 🔴 首要风险: 环道中心线曲率半径

若黄色环道任一拐弯的**中心线转弯半径 < 0.30m**，阿克曼车用纯转向**无解**（这正是旧 Nav2 方案切内角进禁区的物理根因，视觉控制同样受限）。

**验证方法** (Phase 1 前必做): 手动推车沿环道中心走一圈，用 `plot_trajectory.py` 拟合各拐弯半径。若最小半径 < 0.30m → 需在该拐弯降速 + 提前入弯（占用外侧车道宽度），或评估多点掉头。

---

## 段2b 视觉环道 — 详细设计

### 传感器分工

| 传感器 | 作用 | 频率 |
|--------|------|------|
| **RGB 相机** | HSV 黄色分割 → 前视点追踪；出口检测（黄色+map 帧 TF） | 15fps → **目标 30fps** |
| **N10 LiDAR** | AMCL 定位；前方锥桶聚类检测 | 5Hz |
| **MPU6050+BMI088** | EKF 里程计（yaw 不漂） | 100Hz/50Hz |
| **深度相机** | 环道不需要（RGB 就够了） | 提高帧率给 QR/VLM 用 |

### 控制模式

| 场景 | 方式 | vx | wz 上限 (=vx/0.30) | 说明 |
|------|------|-----|-------------------|------|
| **直道** | 前视点追踪 | 0.45 | ≤1.50 | HSV 黄色分割 → 前视点横向误差 → 转向 |
| **弯道** | 前视点追踪 | 0.20 | ≤0.67 | 同方式。前视点自然过弯，wz 必 clamp |
| **锥桶** | 绕行（见下） | 0.20 | ≤0.67 | ⚠️ 旧参数 vx=0.15/wz=1.2 不可达，已重算 |
| **出口** | 切段3 | — | — | 摄像头黄色<20% **且** map 帧在出口区域 |

> **控制律说明**: 原计划用「画面中心 − 质心」的纯 PID。对比研究显示纯 PID 是三种循迹法中**跟踪误差最大、转向抖动最强**的 ([PID vs Pure-Pursuit vs Stanley, EPJ 2025](https://doi.org/10.1051/epjconf/202533006001))。改进为**前视点追踪**: 在 ROI 上方取一个前视行的车道中心作为目标点，横向误差输入 PID（而非底部质心），弯道超前响应、比底部 PID 更稳。保留 Kd 项抑制抖动。控制器本身仍是 PID，参考点向前移了。

### 视觉居中 (前视点追踪)

```
Aurora930 RGB (BGR8)
    │
    ▼
高斯模糊 (5×5) — 去噪, 提升 HSV 分割稳定性 (Duckietown 推荐)
    │
    ▼
ROI 裁剪 (下1/3, 去掉远处无用区域)
    │
    ▼
BGR → HSV
    │
    ▼
黄色分割: cv2.inRange(hsv, [15,80,50], [45,255,255])  ← 加宽范围
    │
    ▼
形态学: 开运算去噪 → 闭运算填洞
    │
    ▼
取前视行 (ROI 底部上方 lookahead_rows 行) 的黄色像素中心 = 前视点
  └ 而非整块最大轮廓质心 — 前视点更接近 pure-pursuit 目标点, 弯道超前响应
    │
    ▼
横向误差 err = 画面中心.x − 前视点.x  (可归一化到 [-1,1])
    │
    ▼
wz = Kp·err + Kd·(err − prev_err)
    │
    ▼
★ clamp: wz = clip(wz, −vx/0.30, +vx/0.30)   ← 阿克曼可行性硬约束
    │
    ▼
→ channel_vel: vx=0.45(直道)/0.20(弯道), wz=clamp后输出
```

**光照鲁棒性** (室内光照不均, HSV 固定阈值易失效 — [Duckietown](https://docs.duckietown.com/ente/opmanual-duckiebot/03-demonstrations/lane-following-lf.html), [MFC 自适应阈值 2021](https://doi.org/10.1016/j.ifacol.2021.11.167)):
- **高斯模糊 + 加宽 H/S 下界** — H 用 15-45 (黄色在 HSV 中 Hue 稳定, 主要受 V 影响)。
- **现场标定必做** — 提供 `calibrate_hsv.py` 交互拖条工具, 对着实际通道调阈值。
- **无黄色兜底**: 单帧黄色像素 < 阈值时 → 保持上一帧 wz + 减速; 连续 N 帧 (~1s) 丢失 → 停车报警, 防止盲走冲出通道 (罚时 10s)。

### LiDAR 锥桶检测 + 绕行

```
/scan (5Hz)
    │
    ▼
前方 90° 扇形, 0.3-1.5m
    │
    ▼
聚类: 相邻点 < 0.15m → 同簇
    │
    ▼
簇宽 0.05-0.20m, 2-5个点 → 锥桶候选
    │
    ▼
≥3帧/1.5s 持续 → 确认锥桶
    │
    ▼
BYPASS_LEFT (vx=0.20, wz=+0.60)   ← R=0.33m ≥ 0.30m 可行 (原 wz=1.2 不可达)
    │                                    (CCW 绕行: 左=外侧. CW 改为 BYPASS_RIGHT 先)
    ▼
BYPASS_FWD  (vx=0.20, wz=0)
    │
    ▼
BYPASS_RIGHT(vx=0.20, wz=−0.60)   ← 对称回正
    │                                    (CCW 绕行: 右=回通道. CW 改为 BYPASS_LEFT)
    ▼
回通道 → 恢复视觉居中
```

> **⚠️ 开环定时绕行的两个陷阱**:
> 1. **可行性**: 原参数 `vx=0.15, wz=1.2` → R=0.125m，远小于 0.30m 最小半径 → 舵机饱和，实际走出的弧线远比预期平缓 → 3s 计时下**横移量严重不足**，撞上锥桶。已按 `wz ≤ vx/0.30` 重算为 `vx=0.20, wz=0.60` (R=0.33m)。
> 2. **开环脆弱**: 定时死算 (dead-reckoning) 假设「指令 wz = 实际 wz」，但舵机响应、地面打滑、电压变化都会使实际弧线偏离 → 8s 后位置累积误差大。**优先改闭环**: 绕行中持续用 LiDAR 跟踪锥桶侧向距离，锥桶脱离前方扇区 (角度 > 阈值) 即触发 BYPASS_RIGHT，而非固定 3s。计时仅作超时兜底。

**绕行时长标定**: 摆放实际锥桶，用重算后的 `vx/wz` 实测左转到锥桶侧移所需时间，替换默认值。切勿沿用理论计算的开环时长。

### 出口判定

```
条件1: 摄像头 ROI 内黄色像素占比 < 20% (通道结束)
条件2: map 帧位姿在出口矩形区域内（辅助校验, 环道内 AMCL 纵向弱可观）
       ↓
  两个条件同时满足 → 切段3（视觉为主, map 帧为辅）
```

### VLM 触发

```
位置: 从黄色通道入口开始, 第 4 个拐弯处
触发: 拐弯计数到达 vlm_turn_index → 发布 /sign4return=100 (环道内 AMCL 纵向弱可观, 用计数代替定位判断)
方式: 发后立即继续 (不等 VLM 结果, 异步)
```

**拐弯计数机制** (角度积分法, [El-Gohary IMU 转弯检测](https://mobgap.readthedocs.io/en/stable/modules/generated/turning/mobgap.turning.TdElGohary.html)):

```
积分: 进入弯道模式 (CENTERING 内 vx=0.20) 起累加 turn_angle += ωz·dt
判定: 退出弯道模式 (回到 vx=0.45) 时, 若 |turn_angle| ≥ turn_count_min_angle(60°) → 计数 +1
去重: 距上次计数 < turn_count_min_gap_s(3.0s) 的候选合并 (防同一弯抖动重复计数)
门控: BYPASS 状态期间冻结计数 (双保险)
```

> **★ 为什么不能只数 ωz 越阈值**: `bypass_wz(0.60) > turn_wz_threshold(0.50)` — 锥桶绕行的 ωz 也超弯道阈值。但绕行是 **左弧(+)→右弧(−) 的 S 形, 净转角≈0°**, 且每段远小于 60° → 角度积分法自动过滤, 不会误计为拐弯。若简单数阈值越界, 一次绕行会被误计 1-2 个弯 → VLM 提前触发 → 错位拍照漏图生文 (罚时 20s)。

---

## 段间切换

```
段1  → 段2a: QR 检测 → cancel Nav2 → backup → Nav2 NavigateToPose(入口)
段2a → 段2b: 到达入口 → /channel_lock=true (屏蔽 Nav2) → /channel_enable=1|2 (启动+方向)
段2b → 段3:  出口判定 → /channel_enable=0 → /channel_lock=false (放行 Nav2) → Nav2 NavigateToPose(P)
段3  → DONE: 到达 P 点 → 停车
```

**切换机制**: 所有速度经 **twist_mux** 仲裁 (见 M14)，无节点直接发 `/cmd_vel`。段2b: master 发 `/channel_lock=true` 屏蔽 Nav2 (`nav_vel`) + `/channel_enable=1|2` (方向+启动) 令 channel_controller 发 `channel_vel`。段3: 反向 (enable=0→unlock)。不修改 lifecycle。

> **✅ /cmd_vel 竞争已解**: 原设计让 master 直接发 `/cmd_vel` 覆盖 Nav2 会产生总线竞争。改为 twist_mux 优先级 (channel_vel 50 > nav_vel 10) + Bool lock 双保险；切换空档由 twist_mux `timeout` 自动补 0 速。保活参见 memory `cmd_vel_mux_keepalive`。

---

## 已知风险与缓解

| # | 风险 | 严重度 | 缓解 | 来源 |
|---|------|--------|------|------|
| 1 | 环道拐弯中心线半径 < 0.30m → 阿克曼纯转向无解 | 🔴 阻断 | Phase 1 前手推实测各拐弯半径；不足则降速+提前入弯 | 运动学 |
| 2 | wz 指令超 `vx/0.30` → 舵机饱和, 实际弧线偏离 | 🔴 高 | 所有 wz 输出统一 clamp；绕行参数已重算 | [#412](https://github.com/ros-controls/ros_controllers/issues/412) |
| 3 | HSV 固定阈值受室内光照不均影响 → 分割失败 | 🟠 中 | 高斯模糊+加宽阈值+现场标定+丢失兜底停车 | [Duckietown](https://docs.duckietown.com/ente/opmanual-duckiebot/03-demonstrations/lane-following-lf.html) |
| 4 | 开环定时绕行累积误差 → 撞锥桶/偏出通道 | 🟠 中 | 改 LiDAR 闭环触发, 计时仅兜底 | robotics 通识 |
| 5 | 纯 PID 循迹抖动大、弯道跟踪差 | 🟡 低 | 改前视点追踪 (pure-pursuit 思路) + Kd 抑抖 | [EPJ 2025](https://doi.org/10.1051/epjconf/202533006001) |
| 6 | AMCL 在环道内纵向弱可观 → 出口/VLM 判定漂移 | 🟠 中 | 出口用「视觉黄色<20%」为主, AMCL 为辅; VLM 拐弯计数为主 | memory `map_physical_vs_virtual` |
| 7 | 段2b 与 Nav2 抢 `/cmd_vel` | ✅ 已解 | twist_mux 优先级+lock 仲裁 (M14), 无节点直发 /cmd_vel | [twist_mux](https://docs.ros.org/en/rolling/p/twist_mux/) |
| 8 | 相机/雷达 QoS 不匹配 → 订阅静默收不到数据 | 🟠 中 | 传感器话题统一用 SensorDataQoS (BEST_EFFORT) | [Nav2 AMCL 源码](https://github.com/ros-planning/navigation2/blob/main/nav2_amcl/src/amcl_node.cpp) |
| 9 | channel_controller 用 /odom 做区域判定 → 里程漂移误判出口/VLM | 🟠 中 | 改 TF map→base_footprint (AMCL 修正), 回退 /amcl_pose | REP-105 / Nav2 TF 文档 |

---

## 节点与接口设计

> 段2b 引入 **2 个自写节点** (`channel_controller` 控制 + `calibrate_hsv` 标定工具) + **1 个现成包** (`twist_mux` 仲裁)，修改 **1 个现有节点** (`competition_master_stage2`)，其余全部复用。接口设计按 README.md 的 M 模块格式。
>
> **接口设计三原则** (本次 EXA 加固): (1) 段切换用**信号握手** (enable/lock/state) 而非直发 /cmd_vel 抢占; (2) 全局区域判定用 **map 帧 TF** 而非漂移的 /odom; (3) 传感器话题统一 **SensorDataQoS**，控制/信号话题 **Reliable**，跨启动信号 **TRANSIENT_LOCAL**。

### 新增节点

#### M12: channel_controller.py (段2b 视觉环道控制)

| 项目 | 值 |
|------|-----|
| **包** | `origincar_bringup` |
| **节点** | `channel_controller` (Python) |
| **执行模型** | **图像回调驱动** (每帧 RGB 触发一次控制, ~30Hz)；scan/pose/imu 缓存最新值 |
| **生命周期** | 常驻 (t+5s 启动)，收到 `/channel_enable=1|2` 存方向→接管控制，`=0` 回 IDLE |

**输入**:

| Topic | 类型 | QoS | 用途 |
|-------|------|-----|------|
| `/aurora/rgb/image_raw` | Image (BGR8) | **SensorData** (BEST_EFFORT) | HSV 黄色分割 → 前视点追踪 |
| `/scan` | LaserScan | **SensorData** (BEST_EFFORT) | 前方锥桶聚类检测 (缓存最新帧) |
| `/imu/data/bmi088_madgwick` | Imu | SensorData | ωz 弯道判定 (缓存最新帧) |
| `/channel_enable` | **Int32** | **Reliable, TRANSIENT_LOCAL** | ★ master→本节点: `0=disable`, `1=CW`, `2=CCW` (方向+接管合一, 解决 /qr_event 不可达) |
| **TF** `map→base_footprint` | tf2 | — | ★ 机器人 map 帧位姿 (出口/VLM 区域判定, 取代 /odom) |

> **位姿来源**: 出口/VLM 判定是**全局区域**判断，必须用 map 帧。`/odom` 是 odom 帧且随里程漂移 → 用 tf2 查 `map→base_footprint` (AMCL 实时修正)；TF 查不到时回退 `/amcl_pose` (latched)。**不订阅 /odom 做区域判定**。

**输出**:

| Topic | 类型 | QoS | 用途 |
|-------|------|-----|------|
| `channel_vel` | Twist | Reliable | ★ 速度指令 (wz 已 clamp) → twist_mux. **全局话题, launch 中 remap 到 `/channel_vel`** |
| `/channel_state` | String | Reliable, TRANSIENT_LOCAL | ★ 本节点→master: 状态 + 出口事件 (CENTERING/BYPASS_*/EXIT) |
| `/sign4return` | Int32 | Reliable | VLM 触发 (第4拐弯, 值=100, 须匹配 VLM 节点订阅) |
| `/channel_debug_mask` | Image | SensorData | 调试: HSV 分割二值图 (10Hz 抽帧) |
| `/channel_lateral_error` | Float32 | Reliable | 调试: 归一化横向误差 (rqt_plot 调 PID) |

**参数**: 见下方参数表 (视觉车道 / LiDAR锥桶 / 绕行 / 出口 / VLM 五组)

**状态机**:

```
IDLE ──(/channel_enable=1|2, 存方向)──→ CENTERING
                                         │
CENTERING (前视点追踪, 发 channel_vel)
    │
    ├── 锥桶确认 (≥3帧/1.5s) → BYPASS_LEFT → BYPASS_FWD → BYPASS_RIGHT → CENTERING
    │                          (绕行侧=环道外侧: CW→右绕, CCW→左绕, 远离中心禁区; LiDAR闭环触发, 计时兜底)
    │
    ├── 拐弯计数(角度积分, 见 VLM 触发)到达 vlm_turn_index → 发 /sign4return=100 (异步)
    │
    └── 出口判定 (黄色<20% AND map 帧在出口区域) → 发 /channel_state=EXIT → IDLE
                                                    (master 收 EXIT 后切段3, 发 /channel_enable=0)
```

**控制输出约束**:

```
err = (画面中心.x − 前视点.x) / (画面宽/2)     # 归一化到 [-1,1]
wz_raw = Kp·err + Kd·(err − prev_err)
wz = clip(wz_raw, −vx/min_turn_radius, +vx/min_turn_radius)   ← 阿克曼可行性硬约束
publish channel_vel = (vx, 0, wz)              # twist_mux 转发到 /cmd_vel
```

#### M13: calibrate_hsv.py (HSV 标定工具)

| 项目 | 值 |
|------|-----|
| **包** | `origincar_bringup` (tools/) |
| **节点** | `calibrate_hsv` (Python, 独立运行) |
| **职责** | 离线交互式 HSV 阈值标定 |

**输入**: 静态图像文件 (对着黄色通道截图) 或实时 `/aurora/rgb/image_raw`
**输出**: 终端打印 `hsv_lower / hsv_upper` 推荐值 (可复制到 channel_controller 参数)
**UI**: OpenCV trackbar 拖条实时调 H/S/V 上下界 + 二值图预览

#### M14: twist_mux (cmd_vel 仲裁, 现成包)

| 项目 | 值 |
|------|-----|
| **包** | `twist_mux` (apt 安装, 无需自写) |
| **节点** | `twist_mux` |
| **职责** | 按优先级仲裁多个速度源 → 输出唯一 `/cmd_vel` 给 STM32 |

> 消除段2b 与 Nav2 抢 `/cmd_vel` 的竞态 ([twist_mux 官方](https://docs.ros.org/en/rolling/p/twist_mux/))。Nav2 的输出重定向到 `nav_vel`，channel_controller 发 `channel_vel`，twist_mux 汇聚后发 `/cmd_vel`。高优先级源有数据时压制低优先级；源静默 `timeout` 后自动回退。

**配置** (`config/twist_mux.yaml`):

| 输入源 | topic | 优先级 | timeout | 段 |
|--------|-------|--------|---------|-----|
| Nav2 | `nav_vel` | 10 | 0.5s | 段1/2a/3 |
| 视觉环道 | `channel_vel` | 50 | 0.5s | 段2b |
| 急停 (可选) | `estop_vel` | 100 | — | 全段 |

**锁 (lock)**: master 发 `/channel_lock` (Bool) — 段2b 期间 `true` → 强制屏蔽 `nav_vel` 残留指令，双保险 (优先级 + 锁)。

> **改动代价**: Nav2 输出话题从 `/cmd_vel` 改为 `nav_vel` (controller_server `cmd_vel` remap, 1 行 launch)；STM32 驱动订阅不变 (仍收 `/cmd_vel`，现在由 twist_mux 发)。

---

### 修改节点

#### M10': competition_master_stage2.py (修改)

| 方法 | 改动 | 说明 |
|------|------|------|
| 状态机 | `NAV_TO_ENTRY` → `DONE` 之间插入 `CHANNEL` 状态 | 段2b 入口 → 出口 |
| `_enter_channel_control()` | 🆕 新增 | 到达入口: cancel Nav2 导航 → `/channel_lock=true` (屏蔽 nav_vel) → `/channel_enable=1(CW) or 2(CCW)` (启动+方向) |
| `_exit_channel_control()` | 🆕 新增 | 收到 EXIT: `/channel_enable=0` → `/channel_lock=false` (放行 Nav2) → Nav2 NavigateToPose(P) → `RETURN_P` |
| `/cmd_vel` 发布 | **删除** | master 不再直接发 `/cmd_vel`；速度全部经 twist_mux。段切换用 enable/lock 信号, 无 cmd_vel 竞争 |

**新增输出** (master → 其他节点):

| Topic | 类型 | QoS | 用途 |
|-------|------|-----|------|
| `/channel_enable` | Int32 | Reliable, TRANSIENT_LOCAL | 令 channel_controller 接管: `0=disable`, `1=CW`, `2=CCW` |
| `/channel_lock` | Bool | Reliable, TRANSIENT_LOCAL | 令 twist_mux 屏蔽/放行 nav_vel |

**新增输入**:

| Topic | 类型 | QoS | 用途 |
|-------|------|-----|------|
| `/channel_state` | String | Reliable, TRANSIENT_LOCAL | 监听 channel_controller; 收到 `EXIT` → 触发切段3 |

> **握手时序** (无 /cmd_vel 竞争的关键): 进段2b 先 lock 屏蔽 Nav2 → 再 enable 接管；出段2b 先 disable → 再 unlock → 再发 Nav2 目标。twist_mux 在两次切换的空档用 `timeout` 自动输出 0 速，无指令真空。

> **已知副作用**: disable 后 channel_vel 约 33ms 停止（下帧回调不发），mux `timeout=0.5s` 内输出 0 → 段切换有 <0.5s 减速。对 0.45m/s 低速运动影响可忽略（<0.1m 滑行）。

**修改的状态机**:

```
INIT → NAV_TO_QR → BACKING_UP → NAV_TO_ENTRY
                                       │
                          ┌────────────┘
                          ▼
                      CHANNEL (新)  ── enable+lock ──→ channel_controller 接管
                          │
                          ▼ (收到 /channel_state=EXIT)
                      RETURN_P → DONE
```

---

### 复用节点 (不改动)

| 节点 | 段 | 用途 |
|------|-----|------|
| `origincar_base_node` (M1) | 全段 | STM32 驱动, 收 `/cmd_vel` (唯一发布者: twist_mux) |
| `lslidar_driver_node` (M2) | 全段 | `/scan` → channel_controller (锥桶) + AMCL (定位) |
| Aurora930 (M3) | 全段 | `/aurora/rgb/image_raw` → channel_controller (车道) + QR (段1) |
| Madgwick ×2 (M4) | 全段 | IMU 姿态 → EKF; BMI088 ωz → channel_controller 弯道判定 |
| EKF (M5) | 全段 | 发布 `odom→base_footprint` TF (channel_controller 经 map→base_footprint 用) |
| AMCL (M6) | 全段 | map→odom TF (channel_controller 区域判定用), `/amcl_pose` 回退源 |
| QR decoder (M7) | 段1 | 二维码解码; 方向由 master 中转至 channel_controller (经 /channel_enable Int32) |
| Nav2 全栈 (M8) | 段1/2a/3 | 大厅规划+控制, 输出改发 `nav_vel`; 段2b 期间被 lock 屏蔽 |
| Keepout (M9) | 段1/2a/3 | 禁区, 段2b 不参与 (环道无 keepout) |
| `stage2_bringup.launch.py` | 全段 | 启动时序新增 channel_controller + twist_mux |

### 启动时序 (stage2_bringup)

```
t=0s:  base_minimal (STM32 + LiDAR + IMU + EKF) + camera_all (Aurora930 + QR)
t=0s:  twist_mux                                   ← 🆕 汇聚 nav_vel/channel_vel → /cmd_vel
t=1s:  nav2_minimal (keepout + Nav2, 输出 nav_vel)  ← 段1/2a/3 用
t=4s:  competition_master_stage2                   ← 状态机
t=5s:  channel_controller                          ← 🆕 段2b 用 (常驻 IDLE, 等 enable)
t=8s:  RViz2
```

> **twist_mux 必须最先起**: 它是 `/cmd_vel` 的唯一发布者，须先于 Nav2/channel_controller 就绪，否则早期指令丢失。
> **channel_controller 提前启动**: 常驻 IDLE 不发 `channel_vel`，收到 master `/channel_enable=1|2` 才接管。提前启动避免段切换时的节点发现延迟。

---

### 全段数据流

`/cmd_vel` 的唯一发布者是 **twist_mux**；Nav2 与 channel_controller 各发自己的输入话题，由优先级+lock 仲裁：

```
                Nav2 ──nav_vel (prio 10)──┐
                                          ├──→ twist_mux ──/cmd_vel──→ STM32
   channel_controller ──channel_vel (prio 50)─┘        ▲
                                                       │
                          master ──/channel_lock (Bool)┘   (段2b=true, 屏蔽 nav_vel)


段1+2a (Nav2 大厅)                     段2b (视觉环道)
═══════════════                       ════════════
Aurora930 ─RGB─→ QR解码 ─→ master      Aurora930 ─RGB─→ channel_controller ─channel_vel─→ mux
N10 ─/scan─→ AMCL ─→ Nav2 ─nav_vel→mux N10 ─/scan─→ ├ AMCL (map→odom TF)
master ─/costmap_ctrl→ keepout                      └ channel_controller (锥桶聚类)
                                       TF map→base_footprint ─→ channel_controller (区域判定)
   master ─enable+lock→ channel_controller / twist_mux
   master ◄─/channel_state (EXIT)─ channel_controller
```

| 段 | 控制源 | 速度话题 | `/cmd_vel` 来自 | 感知 | 避障 |
|----|--------|---------|----------------|------|------|
| 段1 (P→QR) | Nav2 | `nav_vel` | twist_mux | LiDAR + 深度点云 + keepout | costmap 全局 |
| 段2a (QR→入口) | Nav2 | `nav_vel` | twist_mux | 同上 | costmap 全局 |
| **段2b (环道)** | **channel_controller** | **`channel_vel`** | **twist_mux (lock 屏蔽 Nav2)** | **RGB(车道) + LiDAR(锥桶)** | **绕行状态机** |
| 段3 (出口→P) | Nav2 | `nav_vel` | twist_mux | LiDAR + 深度点云 + keepout | costmap 全局 |

---

## 实现计划

### Phase 1: channel_controller.py

| 功能 | 依赖 | 行数估 |
|------|------|--------|
| 高斯模糊 + HSV 黄色分割 + ROI + 丢失兜底 | OpenCV | ~60 |
| 前视点提取 + 追踪控制 + wz clamp | 无 | ~50 |
| LiDAR 锥桶聚类 | sensor_msgs/LaserScan | ~40 |
| 绕行状态机 (LiDAR 闭环 + 计时兜底) | 无 | ~70 |
| 出口判定 (视觉主 + map 帧辅) | 无 | ~30 |
| channel_vel 发布 (30Hz 回调驱动, twist_mux timeout 兜底) | 无 | ~25 |
| 调试话题 (debug_mask, error, state, wz) | 无 | ~40 |
| **合计** | | **~315** |

### Phase 2: 集成

- **twist_mux 接入** (M14): 新增 `config/twist_mux.yaml`；Nav2 controller_server `cmd_vel` remap 到 `nav_vel`；stage2_bringup 最先启动 twist_mux
- competition_master_stage2 增加 `_enter_channel_control()` / `_exit_channel_control()` + `/channel_enable` `/channel_lock` 发布 + `/channel_state` 订阅
- stage2_bringup 启动 channel_controller (t+5s, 常驻 IDLE)
- 深度相机帧率调到 30fps
- **验证握手**: 手动发 `/channel_enable=1` (CW) 确认 channel_vel 压过 nav_vel; `=0` 确认 Nav2 恢复

### Phase 3: VLM + 段3

- VLM 在 channel_controller 中触发（第4拐弯）
- 段3 出口→P 用 Nav2 NavigateToPose
- 端到端联调

---

## 参数表

### 视觉车道

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `hsv_lower` | [15, 80, 50] | 黄色下界（加宽, 需现场标定） |
| `hsv_upper` | [45, 255, 255] | 黄色上界 |
| `gaussian_ksize` | 5 | 高斯模糊核（去噪, 提升分割稳定性） |
| `roi_v_ratio` | 0.33 | ROI 高度比例（下1/3） |
| `Kp` | 0.008 | 比例增益（作用于归一化横向误差） |
| `Kd` | 0.004 | 微分增益（抑制转向抖动） |
| `lookahead_rows` | 10 | 前视行数（从 ROI 底部向上数, 越大越超前但越抖） |
| `min_turn_radius` | 0.30 | ★ 阿克曼最小转弯半径, 用于 wz clamp |
| `turn_wz_threshold` | 0.50 | ★ \|IMU ωz\| 超此值进入弯道模式 (对应 R≈0.90m, 比直道更急的弯) |
| `turn_wz_hysteresis` | 0.15 | 滞后: ωz 需降至 `threshold − hysteresis` 以下才退出弯道模式 |
| `turn_confirm_frames` | 5 | 连续 N 帧满足条件才切换 (防 ωz 噪声误触发, ~0.17s@30Hz) |
| `yellow_lost_frames` | 30 | 连续丢失黄色帧数阈值 → 停车报警（~1s@30fps） |

> **弯道判定**: 不从 HSV 分割结果判弯（前视点横向偏移受光照/遮挡影响大），用 IMU ωz 直接测量车体转动——车已经在转弯了，IMU 不会骗人。判定逻辑: `|ωz| > turn_wz_threshold` 持续 `turn_confirm_frames` → TURNING(vx=0.20)；`|ωz| < turn_wz_threshold − turn_wz_hysteresis` 持续同等帧数 → CENTERING(vx=0.45)。

### LiDAR 锥桶

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `cone_fov_deg` | 90 | 检测扇形角度 |
| `cone_range_min` | 0.3 | 最近检测距离 (m) |
| `cone_range_max` | 1.5 | 最远检测距离 (m) |
| `cone_cluster_tol` | 0.15 | 聚类容差 (m) |
| `cone_width_min` | 0.05 | 最小簇宽 (m) |
| `cone_width_max` | 0.20 | 最大簇宽 (m) |
| `cone_confirm_frames` | 3 | 确认帧数 |
| `cone_confirm_window` | 1.5 | 确认时间窗 (s) |

### 绕行

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `bypass_speed` | 0.20 | 绕行速度 (m/s)，原 0.15 提高以满足可行 wz |
| `bypass_wz` | 0.60 | 绕行转向 (rad/s)，R=0.33m ≥ 0.30m 可行（原 1.2 不可达） |
| `bypass_left_dur` | 待实测 | 左转时长 (s)，实测标定，勿用开环理论值 |
| `bypass_fwd_dur` | 待实测 | 直行时长 (s) |
| `bypass_right_dur` | 待实测 | 右转时长 (s) |
| `bypass_clear_angle` | 60 | ★ 闭环触发: 锥桶偏离前方扇区角度 (°) → 转 BYPASS_RIGHT |
| `bypass_timeout` | 8.0 | 绕行超时兜底 (s) → 停车 |

### 出口

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `exit_yellow_ratio` | 0.20 | ROI 黄色占比阈值 |
| `exit_region_x_min/max` | 待标定 | 出口 map 帧矩形 |
| `exit_region_y_min/max` | 待标定 | 出口 map 帧矩形 |

### VLM

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `vlm_turn_index` | 4 | 从入口起第几个拐弯 (方向由 /channel_enable 1=CW / 2=CCW 决定计数序) |
| `vlm_sign_id` | 100 | 发 /sign4return 的值 |
| `turn_count_min_angle` | 60 | ★ 计数阈值: TURNING 累积转角 ≥ 此值(°)才计 1 个弯 (滤除绕行 S 形净转角≈0) |
| `turn_count_min_gap_s` | 3.0 | 两次计数最小间隔 (s), 防同一弯抖动重复计数 |

### twist_mux (config/twist_mux.yaml)

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `nav_vel` priority | 10 | Nav2 输出优先级 (段1/2a/3) |
| `channel_vel` priority | 50 | 视觉环道优先级 (段2b, 高于 Nav2) |
| `timeout` | 0.5 | 源静默超时 → 输出 0 速 (s) |
| `/channel_lock` priority | 100 | Bool 锁, master 段2b 置 true 屏蔽 nav_vel |

---

## 待标定项

| 项 | 方法 | 工具 |
|----|------|------|
| HSV 阈值 | 对着黄色通道截图, 手动调 | `calibrate_hsv.py`（待写） |
| 出口区域 | 跑一圈, 记录出口 map 帧坐标 | plot_trajectory.py |
| VLM 拐弯点 | 跑一圈, 确认拐弯计数在第4个拐弯触发 /sign4return | plot_trajectory.py + /channel_state 日志 |
| PID 增益 | 实际跑, 观察振荡/响应 | rqt_plot /lateral_error |
| 绕行轨迹参数 | 摆锥桶, 实测 vx=0.20/wz=0.60 下时长 | 手动调 |
| 深度相机帧率 | 改 Aurora930 配置 | 厂商 SDK |
| **★ 环道拐弯半径** | **手推一圈, 确认各拐弯中心线 R ≥ 0.30m** | plot_trajectory.py |

---

## 参考文献 (EXA MCP, 2026-07-11)

**架构对标** (见「EXA MCP 架构验证」章):
- F1TENTH 统一基准 · Formula Student Driverless · Autoware 三层架构 · Modular vs E2E 综述

**实现加固** (本次新增):
| 来源 | 用途 |
|------|------|
| [ros_controllers #412 — angular velocity vs steering angle](https://github.com/ros-controls/ros_controllers/issues/412) | 阿克曼 `R = vx/wz` 约束依据 |
| [Nav2 Twist for Ackermann (Macenski)](https://robotics.stackexchange.com/questions/103741/nav2-controllers-and-twist-commands-for-ackermann-robots) | `angular.z` 是车体角速度, 需 shim 反解转角 |
| [PID vs Pure-Pursuit vs Stanley (EPJ Web Conf 2025)](https://doi.org/10.1051/epjconf/202533006001) | 纯 PID 循迹误差最大 → 改前视点追踪 |
| [Duckietown Lane Following](https://docs.duckietown.com/ente/opmanual-duckiebot/03-demonstrations/lane-following-lf.html) | 高斯模糊 + 黄色 HSV [15,80,50]-[45,255,255] + 需标定 |
| [Real-Time Adaptive HSV Threshold (IFAC 2021)](https://doi.org/10.1016/j.ifacol.2021.11.167) | 光照变化下固定阈值失效, 自适应阈值 |
| [twist_mux 官方文档](https://docs.ros.org/en/rolling/p/twist_mux/) | cmd_vel 多源仲裁, 优先级+lock 机制, yaml 配置 |
| [El-Gohary IMU 转弯检测 (mobgap)](https://mobgap.readthedocs.io/en/stable/modules/generated/turning/mobgap.turning.TdElGohary.html) | 拐弯计数: ωz 积分转角 + 最小转角过滤 + 合并去重, 滤除绕行误计 |
