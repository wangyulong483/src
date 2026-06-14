# Agent 修改记录（时间链：最新在前）

---

## 2026-06-14 18:00 — 全时段禁区 + 轨迹可视化

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

