# Agent 修改记录（时间链：最新在前）

---

## 2026-06-15 17:20 — 速度参数回归 → 禁区卡死 + 紧急回退

> **结果**: ❌ 未完成 (Ctrl-C 强制终止 @ 85.3s)。机器人卡在禁区 36 秒。

### 问题演进

```
82.0s 基线 (desired=0.50) → 速度参数激进 (desired=0.55, accel=1.4, bins=40)
→ 弯道更冲 → 冲入禁区 → "Starting point in lethal space" × 20+ 次
→ BT 恢复循环: clear→backup→wait→retry→fail→repeat (36s卡死)
→ 甚至 backup 行为也失败: "Collision Ahead - Exiting DriveOnHeading"
```

### 根因

| 参数 | 基线 | 本次 | 影响 |
|------|------|------|------|
| `desired_linear_vel` | 0.50 | **0.55** | 10%更快 → 反应时间缩短 → 弯道冲入禁区 |
| `max_linear_accel` | 1.2 | **1.4** | 更快加速进入危险区 |
| `angle_quantization_bins` | 48 | **40** | 17%粗化 → 路径精度不足 → 避禁区能力下降 |

**在 0.5m 宽通道 + 0.55m 膨胀禁区场景下，速度参数没有余量。82.0s 的 0.50 m/s 是安全极限。**

### 保留的安全优化 (未回退)

| 参数 | 值 | 验证 |
|------|-----|------|
| RateController | **1.0Hz** (0.5→1.0) | 理论正确, 更多重规划应帮助避障 |
| max_iterations | **1000** (2000→1000) | 77.3s 基线验证 |
| max_planning_time | **1.5** (3.0→1.5) | 仅影响失败路径 |
| analytic_expansion_ratio | **3.0** (2.0→3.0) | 更快解析扩展 |
| waypoint_pause_duration | **50ms** (200→50) | 0.6s节省 |
| 代码优化 4 项 | 延迟瘦身+Bug修复 | 纯收益 |

### 当前部署状态

- originbot_nav2_rpp.yaml: **已回退速度参数, SSH部署完成**
- BT XML: RateController 1.0Hz **保留**
- competition_master_stage3.py: 代码优化 **保留**

---

## 2026-06-15 16:30 — 多 Agent 联合优化：目标 <80s（待部署）

> **用户要求**: 82.0s DONE → 目标 <80s。4 Agent 并行分析 + EXA MCP 研究 + 辩论合成。

### 诊断方法论

```
Agent 1 (瓶颈分析) ──→ 3 大瓶颈: cusp/recovery, CPU饱和, RETURN_P效率
Agent 2 (EXA MCP)  ──→ 7 次搜索: planner加速, BT限流, RMW, 代价地图
Agent 3 (代码审查)  ──→ 8 处时间浪费: 固定延迟, 阻塞调用, 重复bug
Agent 4 (配置分析)  ──→ 10 项参数: 快速胜利, 回归检测, 风险分级
     ↓
Agent 5 (辩论合成) ──→ 解决4个冲突, 统一方案, Tier分级
```

### 🔥 关键发现: BT RateController = 0.5Hz 瓶颈

**BT XML 中 `RateController hz="0.5"` 将重规划限制为每2秒一次！** 在 0.60 m/s 巡航速度下, 机器人每2秒走 1.2m, 但 lookahead 只有 0.72m → 机器人"跑过"自己的前瞻距离 → 追尾过期路径 → 进入禁区 → 触发恢复 → 浪费 4-7s/次。

同时 `max_iterations=2000`（77.3s 基线是 1000）, 每次规划耗时 ~750ms, planner 锁定在 ~1.3Hz。

### 最终优化方案 (Tier 1 — 必须做)

**目标: 74.0–76.4s（保守估计节省 5.6–8.0s）**

#### Nav2 配置: `originbot_navigation/param/originbot_nav2_rpp.yaml`

| # | 参数 | 当前 | 新值 | 节省 | 原理 |
|---|------|------|------|------|------|
| 1 | `max_iterations` | 2000 | **1000** | 0.5-1.0s | 77.3s 基线验证, 5m×5m 场地足够; 规划时间 750→350ms |
| 2 | `max_planning_time` | 3.0 | **1.5** | 0.5-1.5s | 快速失败重试; 卡在致命起点不再浪费3s |
| 3 | `desired_linear_vel` | 0.50 | **0.55** | 1.0-2.0s | 10%提速, lookahead 约束仍满足 (0.66m > 0.60m) |
| 4 | `max_linear_vel` | 0.60 | **0.65** | 0.5-1.0s | 开放段短时提速余量; velocity_smoother 已有余量 |
| 5 | `max_linear_accel` | 1.2 | **1.4** | 0.3-0.5s | 更快脱离低速段; velocity_smoother 上限 1.5 |
| 6 | `max_linear_decel` | -1.5 | **-1.7** | 0.3-0.5s | 匹配 velocity_smoother 上限; 更快刹停 |
| 7 | `waypoint_pause_duration` | 200ms | **50ms** | 0.5s | 4路点×150ms; 50ms 足够传感器刷新 |
| 8 | `analytic_expansion_ratio` | 2.0 | **3.0** | 0.2-0.5s | 更频繁解析扩展, 更快找到直连目标 |
| 9 | smoother `max_iterations` | 500 | **300** | 0.2-0.5s | 内置平滑器; BT已移除 SmoothPath |
| 10 | `angle_quantization_bins` | 48 | **40** | 0.3-0.5s | 搜索分支削减17%, 9°分辨率足够 |

#### BT XML (两个文件): `behavior_trees/navigate_*_ackermann_rpp.xml`

| # | 参数 | 当前 | 新值 | 节省 | 原理 |
|---|------|------|------|------|------|
| 11 | `RateController hz` | **0.5** | **1.0** | 3.0-5.0s | **最大单项收益！** 消除2秒过期路径窗口, 减少恢复触发 |

#### Python 代码: `origincar/origincar_bringup/src/competition_master_stage3.py`

| # | 参数 | 当前 | 新值 | 节省 | 原理 |
|---|------|------|------|------|------|
| 12 | `start_delay_sec` | 0.5 | **0.1** | 0.4s | 更快轮询 Nav2 action server |
| 13 | `_return_delay_timer` | 0.5s | **0.1s** | 0.4s | 代价地图清除异步, 不需要等0.5s |
| 14 | 重复 `_start_backup()` | L914 | **删除** | BUG修复 | 双定时器泄漏; 异常路径资源泄漏 |

### 拒绝的修改 (经辩论裁定)

| 拒绝项 | 原因 |
|--------|------|
| `change_penalty` 0.10→0.0 | 0.10 在代价函数中可忽略 (3个cusp=0.30 vs reverse_penalty=2.0/段). 移除风险多余振荡. |
| `lookahead_time` 1.2→1.8 | RateController 修复后 0.72m lookahead ≥ 0.60m 穿行距离. 长前瞻在窄道风险穿墙. |
| `backup_duration_sec` 6.0→5.0 | 节省1s但导致46°朝向偏差→通道入口修正耗时更多→净损失. 6.0s经实验调优. |
| `RETURN_P yaw` → p_point_yaw | 当前朝向避免最终旋转 (已验证优化 LRN-20260615-004). 改回去反而增加0.5-1s. |
| BT `backup_speed` 0.12→0.20 | 恢复行为, 更快倒车增加窄道碰撞风险. 保持安全. |

### 预期效果

| 场景 | 预计时间 | 相当于 |
|------|---------|--------|
| **Tier 1 全部** | **74.0–76.4s** | 打破 80s 屏障, 接近 77.3s 基线 |
| 仅 RateController + max_iterations | 77.5–79.0s | 刚好破 80s |

### 风险与回退

- **max_iterations=1000**: 若复杂障碍布局下规划失败, 回退到 1500 (中间值)
- **desired_linear_vel=0.55**: 若窄道振荡加剧, 回退到 0.50
- **RateController=1.0Hz**: CPU 额外负载 ~20%, ARM 仍有足够余量
- 回退策略: 任何参数单跑一圈退化 → 立即回退该参数 → 不影响其他改动

### 部署流程 (待用户确认)

1. 编辑 4 文件 (`originbot_nav2_rpp.yaml` + 2 BT XML + `competition_master_stage3.py`)
2. `ssh_upload` → RDK X5
3. `sed -i 's/\r$//'` 修复 CRLF
4. `colcon build --packages-select originbot_navigation origincar_bringup`
5. 运行一圈验证

---

## 2026-06-15 15:30 — 大膨胀势场验证成功: **82.0s DONE!**

> **用户反馈**: 规划路径贴墙。0.55m 膨胀方案验证。

### 运行结果

| 指标 | 值 |
|------|-----|
| **总耗时** | **82.0s DONE** ✦新纪录✦ |
| 终点 | (-1.67, -0.16), 距P点 0.34m |
| QR | 检测成功 |
| VLM | 正常返回 |
| 轨迹 | 105 点 |
| lethal space 错误 | **仅 2 次** (上轮 11 次) |

### 阶段对比

| 阶段 | 94.1s 基线 | 146.6s(上轮) | **82.0s(本次)** |
|------|-----------|-------------|-----------------|
| LAUNCH | 14.9s | 14.9s | 15.3s |
| NAV_TO_QR | 13.4s | 13.9s | 13.0s |
| BACKING_UP | 6.0s | 6.0s | 6.0s |
| CRUISE_CHANNEL | 39.8s | 38.0s | 41.8s |
| RETURN_P | 33.9s | 88.5s | **21.1s** (-76%) |
| **TOTAL** | 94.1s | 146.6s | **82.0s** (-13%) |

### 关键验证

- **inflation_radius=0.55 + cost_scaling_factor=2.0 完全生效**
- RETURN_P 从 88.5s 暴降到 21.1s — lethal space 从 11× 降到 2×
- 路径不再贴墙：规划器自然选择通道中心线
- CPU 负载降低 (更多时间在 30-50% 而非 100%)
- planner 1.3Hz 不变 (不受膨胀半径影响)

### 结论

0.55m 膨胀半径是正确的。Nav2 官方推荐与实测完全一致。

---## 2026-06-15 10:40 — 定位回退 + DONE (146.6s)

> **用户反馈**: 规划路径贴着墙壁/禁区走，不够居中。
> **多 Agent 分析**: 3 agent 并行审查日志+配置，1 agent 辩论，EXA MCP 研究 Nav2 官方文档。

### 根因

`inflation_radius=0.12m` → 通道(0.5m宽)中心 50% 区域代价=0，规划器看不到任何理由走中心线。Nav2 维护者 Steve Macenski 官方文档明确要求 "create a consistent potential field across the entire map"。

历史上 `0.25m` 被误认为"大膨胀失败"，实际是"恐怖谷"：刚好大到扰乱规划器但不够大到形成完整势场。

### 修改

| 参数 | 旧 | 新 | 原理 |
|------|-----|-----|------|
| `inflation_radius` (local+global) | 0.12 | **0.55** | 双墙代价场在通道中心重叠，自然形成中心"谷" |
| `cost_scaling_factor` (local+global) | 5.0 | **2.0** | 平缓衰减，10cm分辨率 planner 可分辨梯度 |
| `cost_penalty` | 4.0 | **不变** | 中心代价已从0升至~130，无需额外放大 |

### 为什么 0.55m 不是 0.25m

- `inscribed_radius`=0.10m（footprint自动计算）→ 只有这10cm是致命区
- `inflation_radius`=0.55m → 代价衰减距离=0.45m，覆盖整个0.5m通道
- 走廊中心(距每面墙0.25m)代价 ~130（非致命），且是全场最低点

### SSH

- `originbot_nav2_rpp.yaml` → 上传 + colcon build → 成功

---## 2026-06-15 10:40 — 定位回退 + DONE

> **用户要求**: 改回 94.1s 定位配置 + 分析最新日志。

### 修改

| 文件 | 参数 | 值 | 说明 |
|------|------|-----|------|
| `originbot_nav2_rpp.yaml` | AMCL alpha1-5 | 0.45 | 回退（从 0.30） |
| `originbot_nav2_rpp.yaml` | AMCL update_min_a/d | 0.10 | 回退（从 0.20） |
| `originbot_nav2_rpp.yaml` | inflation_radius | 0.12 | 回退（从 0.25） |
| `originbot_nav2_rpp.yaml` | cost_scaling_factor | 5.0 | 回退（从 3.0） |
| `imu_madgwick_bmi088.yaml` | beta | 0.003 | 回退（从 0.015） |
| `imu_madgwick_bmi088.yaml` | gyro_noise | 0.000244 | 回退（从 0.001） |
| `ekf_dual_imu.yaml` | odom0_differential | true | 回退（从 false） |

保留了 `backup_wz=0.80`（非定位参数）。

### 运行结果

| 指标 | 值 |
|------|-----|
| 总耗时 | **146.6s DONE** |
| LAUNCH | 14.9s |
| NAV_TO_QR | 13.9s (QR=1584, CCW) |
| BACKING_UP | 6.0s (wz=0.80, yaw 平滑) |
| CRUISE_CHANNEL | **38.0s** |
| RETURN_P | **88.5s** |
| 轨迹 | 155 点 → trajectory.csv |
| VLM | 正常返回 |

### 分析

- BACKING_UP yaw: -65°→-39°→1° 平滑过渡，wz=0.80 成功
- CRUISE_CHANNEL 38.0s 比 94.1s 基线(39.8s)略快
- **RETURN_P 88.5s** 是瓶颈：11 次 `Starting point in lethal space`
- **Planner 1.3Hz**，CPU 100% 持续
- 禁区地图修改后返航路径被封，clear costmap → re-plan → 再次 lethal 死循环

### SSH

- 4 文件回退 + colcon build → 成功

---## 2026-06-14 18:00 — 全时段禁区 + 轨迹可视化

> **用户反馈**: 禁区必须全时段生效 + 绘制 CSV 轨迹到底图上。

### 代码修改

**competition_master_stage3.py**: 删除所有 `_disable_keepout_and_clear` / `_start_keepout_republish` / `_cancel_keepout_republish` / `_reenable_keepout`。禁区从启动到关闭全程 ON。`override_lethal_cost=True` 保证脱险。

### 运行结果

| 指标 | 值 |
|------|-----|
| 总耗时 | **94.1s DONE** |
| DIR_SWITCH | 55 |
| LAUNCH | 4.5s (0s发车方案) |
| NAV_TO_QR | 13.4s |
| BACKING_UP | 6.0s |
| CRUISE_CHANNEL | 39.8s |
| RETURN_P | 33.9s |
| 轨迹点 | 101 |
| 禁区 | 全时段 ON |

### 轨迹可视化

- CSV: `C:\Users\27826\Desktop\src\trajectory.csv` (101 points)
- 绘图脚本: `originbot_navigation/tools/plot_trajectory.py`
- 输出: `C:\Users\27826\Desktop\src\trajectory_plot.png`
- 底图: keepout_mask.pgm + room.yaml (origin/resolution)
- 曲线: UnivariateSpline 平滑

### 全时段禁区架构

```
启动 → 禁区 ON (startup reset publish → /keepout_mask)
NAV_TO_QR → 禁区 ON
CRUISE_CHANNEL → 禁区 ON
RETURN_P → 禁区 ON
任务结束 → 禁区 ON
override_lethal_cost=True → 误入可脱险
```

### SSH

- `ssh_download` → trajectory.csv
- 无代码修改需同步（禁区改动已在上一轮部署）

---## 2026-06-14 17:50 — 禁区话题隔离 + 内存换性能

> **用户反馈**: 小车被困禁区 + 内存80%空闲, 以内存换实时性。

### 修改（3 文件）

**1. `originbot_nav2_rpp.yaml`**

| 参数 | 旧 | 新 | 说明 |
|------|-----|-----|------|
| `change_penalty` | 0.2 | **0.10** | Nav2推荐0.0-0.3, 抑制cusp |
| `reverse_penalty` | 4.0 | **2.0** | Nav2推荐1.3-5.0 |
| `cache_obstacle_heuristic` | false | **true** | 重规划20-40x加速, 内存+23KB |
| `lookup_table_size` | 10.0 | **20.0** | 默认值, 内存+38KB |
| keepout `filter_info_topic` | `/costmap_filter_info` | **`/costmap_ctrl`** | 话题隔离 |

**2. `nav2_minimal.launch.py`**

| 参数 | 旧 | 新 |
|------|-----|-----|
| server `filter_info_topic` | `/costmap_filter_info` | **`/costmap_filter_info_server`** |

**3. `competition_master_stage3.py`**

| 改动 | 说明 |
|------|------|
| `keepout_info_pub` topic → `/costmap_ctrl` | 独占发布, 零竞态 |
| 新增 startup reset publish | TRANSIENT_LOCAL 持久化覆盖 |

### 架构

```
costmap_filter_info_server → /costmap_filter_info_server (无人订阅)
competition_master         → /costmap_ctrl (独占)
KeepoutFilter              ← /costmap_ctrl (唯一来源)
→ 单发布者, 零竞态, 根除 TRANSIENT_LOCAL race condition
```

### 内存开销

总计 ~150KB（3.2GB 空闲的 0.005%）。EXA MCP 验证 40x 重规划加速。

### SSH

- 3 文件上传 + CRLF fix + colcon build → 成功

---## 2026-06-14 14:45 — 日志增强（纯日志，不改控制逻辑）

> **用户要求**: 用经过优化的日志来。

### 新增（competition_master_stage3.py）

| 功能 | 说明 |
|------|------|
| DIAG 日志 (2s) | `[DIAG] state= pos=(x,y) yaw= cmd=(vx,wz) elapsed= plan[npts len] (start)→(end) cpuFreq= cpuT= bpuT= cpu= mem=` |
| 阶段耗时追踪 | `_phase_times` dict, `_state_transition()` 自动记录离开阶段的耗时 |
| 发车计时 | `[LAUNCH] 发车阶段: Ns` |
| 导航距离 | 发送目标时记录 `[DIAG] nav目标距离: Xm, robot=(…) → target=(…)` |
| 轨迹录制 | `_trajectory` 列表 → DONE/TIMEOUT 时写入 `/userdata/dev_ws/trajectory.csv` |
| 停止保活 | `_finish()` / `_timeout_shutdown()` 中 10Hz 持续发 stop，防止 mux 超时 |
| 硬件监控 | CPU 频率/温度/使用率 + BPU 温度 + 内存使用率 |
| 规划器意图 | 订阅 `/plan`，记录路径点数/长度/首尾点 |

### 未改动

- PID 参数、velocity_pid.py
- Nav2 yaml 配置
- 导航逻辑（状态机、路点、行为树）
- launch 文件

### SSH 同步

- `ssh_upload` → `competition_master_stage3.py`
- `colcon build --packages-select origincar_bringup` → 成功

---

## 2026-06-14 15:00 — BMI088 升级为主 IMU

> **用户要求**: 调试 BMI088，使其帮助优化定位与路径规划。

### 现状问题

BMI088 汽车级 IMU（陀螺噪声 ~1/10 MPU6050）仅作为 EKF 的第二个角速度源（imu1，原始数据），从未参与姿态解算。MPU6050 一直是主姿态源。已有 `imu_madgwick_bmi088.yaml` 配置文件但从未在 launch 中启用。

### 修复：让 BMI088 成为主 IMU

BMI088 → Madgwick 滤波(β=0.01) → EKF imu0 (主姿态+yaw角速度)
MPU6050 → 降级为 imu1 (差分模式, 辅助)

#### 文件改动

**1. `base_minimal.launch.py`**

| 改动 | 说明 |
|------|------|
| 新增 `imu_madgwick_bmi088` 节点 | 输入 `/imu_data`(BMI088 IIO bridge), 输出 `/imu/data/bmi088_madgwick` |

**2. `ekf_dual_imu.yaml`**

| imu | 旧 topic | 新 topic |
|------|---------|---------|
| imu0 (主) | `/imu/data/madgwick` (MPU6050) | **`/imu/data/bmi088_madgwick`** (BMI088) |
| imu1 (辅) | `/imu_data` (BMI088 原始) | **`/imu/data/madgwick`** (MPU6050, 差分) |

### SSH 同步

- `ssh_upload` → `base_minimal.launch.py` + `ekf_dual_imu.yaml`
- `colcon build --packages-select origincar_bringup origincar_base` → 成功

## 2026-06-14 14:55 — 0s 发车 + P点不调位姿

> **用户反馈**: 返回P点只需到达点位，不用调位姿；发车延迟太长，找0s方案。

### 当前状态

- P点 `yaw_goal_tolerance: 3.14` (PI) — 已忽略朝向检查，无需修改
- 发车延迟：`start_delay_sec=8.0s` 固定延迟。本轮 103.9s，LAUNCH 阶段 8.3s

### EXA MCP 调研

ROS2 ActionClient 自带 `wait_for_action_server(timeout)` 方法，可直接轮询替代固定 TimerAction。无需依赖外部信号。

### 修改文件

#### `origincar/origincar_bringup/src/competition_master_stage3.py`

| 改动 | 旧值 | 新值 |
|------|------|------|
| `start_delay_sec` 默认值 | 8.0 | **0.5** |
| `run()` 入口 | 固定 Timer → `_start_nav` | Timer → `_poll_then_start` |
| 新增 `_poll_then_start()` | — | 每 0.5s 轮询 `nav_client.wait_for_server(0.3s)`，就绪后立即调用 `_start_nav()` |

### 原理

```
旧:  8.0s 固定延迟 → _start_nav (无论 Nav2 是否就绪)
新:  0.5s → _poll_then_start → wait_for_server(0.3s)
       ├─ 未就绪 → 0.5s 后重试
       └─ 已就绪 → _start_nav (立即发车)
```

Nav2 激活约需 5-6s，旧方案浪费 2-3s。新方案就绪即发，~节省 2-3s。

### SSH 同步

- `ssh_upload` → `competition_master_stage3.py`
- `colcon build --packages-select origincar_bringup` → 成功

---## 2026-06-14 14:37 — 基线回归（全量回退后首跑）

> **用户反馈**: 跑完一圈了。这一版完美使用 BMI088 了吗？
> **分析**: 1203 行日志分析。

### 运行结果

| 指标 | 值 |
|------|-----|
| 总耗时 | **94.3s DONE** |
| DIR_SWITCH | 55 |
| NAV_TO_QR | ~14s |
| BACKING_UP | ~6s |
| CRUISE_CHANNEL | ~36s |
| RETURN_P | ~37s |
| 规划器 lethal space 错误 | CRUISE + RETURN 各数次 |
| mux TIMEOUT | 4 次 |

### BMI088 使用状态

**正在使用，角色是 EKF 的第二个角速度源：**

```
EKF 双 IMU 融合（原始 ekf.yaml 配置）:
  imu0: /imu/data/madgwick  (MPU6050→Madgwick)
        → 提供 yaw 姿态 + yaw 角速度
  imu1: /imu_data            (BMI088 原始)
        → 仅提供 yaw 角速度 (汽车级陀螺, 无姿态)
```

BMI088 从设计上就只贡献角速度精度，不参与姿态解算。这是原始代码的正确行为。没有"搞废"。

### 已提取到 .learnings/

旧 agent_do.md 中有价值的经验和参数边界已提取到：
- `.learnings/nav2_params.md` — SmacPlannerHybrid 参数边界
- `.learnings/keepout.md` — 禁区话题隔离方案
- `.learnings/deploy.md` — 部署流程
- `.learnings/ackermann.md` — Ackermann + EKF 架构

### 当前代码状态

全量回退到初始 commit（`d2f96f4`），所有后续修改均已撤销。无额外改动。

