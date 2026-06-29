# Stage 3 工作交接文档

> 写于 2026-06-12，最后更新 2026-06-27
> 新对话开始时应先读此文件。

---

## 工作流程规范

### 每次修改代码后的标准操作
1. 上传到机器人：`ssh_upload` → `192.168.31.59:/userdata/dev_ws/src/`
2. **修复 CRLF**：`sed -i 's/\r$//'` 每个上传的 .py 文件
3. 构建：`bash -c 'source /opt/ros/humble/setup.bash && cd /userdata/dev_ws && colcon build --packages-select <pkg>'`
4. C++ 包（qr_decoder, lslidar_driver 等）构建需 ~90 秒，Python 包 ~3 秒

### 禁止操作
- **禁止 `git checkout` 覆盖用户文件**——用户可能已编辑但未告知
- **禁止 `git reset --hard`** 等破坏性 git 操作
- **禁止删除 `/userdata/ros_ws/`**——那是深度相机驱动的工作空间
- **禁止动 keepout_mask.pgm 的像素内容**——用户自己管理禁区地图

### 日志分析规范
- 日志路径：`C:\Users\27826\Desktop\src\Z_MD\log.md`
- 遇到复杂问题用多 Agent 并行分析（EXA MCP + 代码审查 + 日志分析）

---

## 机器人环境

| 项目 | 值 |
|------|-----|
| IP | 192.168.31.59 |
| 用户 | root |
| 平台 | RDK X5 (ARM Cortex-A55) |
| ROS2 | Humble |
| 工作空间 | `/userdata/dev_ws/` |
| 深度相机工作空间 | `/userdata/ros_ws/` (不动) |
| SSH MCP 服务器名 | `myserver` |

---

## 文件对应关系

| 本地路径 (Windows) | 机器人路径 (Linux) |
|---|---|
| `origincar/origincar_bringup/src/competition_master_stage3.py` | `src/origincar/origincar_bringup/src/` |
| `origincar/origincar_bringup/src/velocity_pid.py` | 同上 |
| `originbot_navigation/param/originbot_nav2_rpp.yaml` | `src/originbot_navigation/param/` |
| `originbot_navigation/behavior_trees/*.xml` | `src/originbot_navigation/behavior_trees/` |
| `originbot_navigation/maps/keepout_mask.pgm` | `src/originbot_navigation/maps/` |
| `qr_decoder/src/qr_decoder.cpp` | `src/qr_decoder/src/` |
| `origincar_qr/origincar_qr/qr_decision.py` | `src/origincar_qr/origincar_qr/` |

---

## 关键陷阱（反复踩过的坑）

### 1. CRLF 行尾
Windows 编辑的 .py 上传到 Linux 后 shebang 变成 `python3\r` → 进程崩溃（exit 127）。
**每次上传后必须**：`sed -i 's/\r$//' <file>`

### 2. CostmapFilterInfo QoS 不匹配
- 发布者（competition_master）默认 QoS 是 VOLATILE
- 订阅者（KeepoutFilter）要求 TRANSIENT_LOCAL
- ROS2 拒绝匹配 → 消息被静默丢弃
- 日志中会出现：`"requesting incompatible QoS... DURABILITY"`
- **修复**：发布者必须用 `QoSDurabilityPolicy.TRANSIENT_LOCAL`

---

## 当前代码状态（2026-06-12 最终版）

### competition_master_stage3.py
- 基于 git 初始版本，只做了 3 处最小改动：
  1. `keepout_info_pub` QoS → TRANSIENT_LOCAL
  2. `_disable_keepout_and_clear()` 发布空 mask 禁用禁区
  3. `_finish()` / `_timeout_shutdown()` 调用 `_reenable_keepout()` 恢复禁区
- **没有** toggle_filter、空间门、odom 订阅、backup settle
- 状态机：`INIT → NAV_TO_QR → BACKING_UP → CRUISE_CHANNEL → RETURN_P → DONE`

### originbot_nav2_rpp.yaml
- `use_collision_detection: false`
- `yaw_goal_tolerance: 3.14` (PI，跳过朝向检查)
- `lookahead_time: 1.8`, `max_robot_pose_search_dist: -1.0`
- `regulated_linear_scaling_min_radius: 0.20`
- 规划器：`cost_penalty=4.0`, `reverse_penalty=4.0`, `change_penalty=0.2`, `non_straight_penalty=1.3`
- 代价图：`inflation_radius=0.20`, `cost_scaling_factor=2.0`, `allow_unknown=false`

### qr_decoder.cpp
- ZBar 仅扫描 QR 码制（`ZBAR_QRCODE`），禁用其他码制
- 深度过滤 advisory（只记录不拦截）
- 内容长度检查：`min_qr_length=1`

### qr_decision.py
- 格式验证：`1 <= len <= 4` 且纯数字，范围 `[1, 9999]`

### navigate_through_poses_ackermann_rpp.xml
- Recovery Fallback 中 ClearCostmap 后加了 `Wait wait_duration="0.5"`
- 系统级恢复中 ClearCostmap 后加了 `Wait wait_duration="0.5"`

---

## 常用命令

```bash
# 查看日志
grep -n "关键词" C:\Users\27826\Desktop\src\Z_MD\log.md

# SSH 执行（通过 MCP ssh-manager，server=myserver）
bash -c 'source /opt/ros/humble/setup.bash && cd /userdata/dev_ws && colcon build --packages-select <pkg>'

# 修复 CRLF
sed -i 's/\r$//' <file.py>

# 清理 ROS 日志
rm -rf /root/.ros/log/*

# 清理构建缓存
rm -rf /userdata/dev_ws/build/* /userdata/dev_ws/log/*
```

---

# Offline Nav2 Auto Tuner v3 (2026-06-27 新增)

## 概述

基于 wiki.md 需求实现的离线自动调参平台。从单文件脚本重构为模块化 `offline_tuner/` 包。

## 项目目录结构（2026-06-27 整理后）

```
src/
  _analyze_plans.py              ← CLI 入口（279行）
  offline_tuner/                 ← 核心包（11 文件, 2751行）
    __init__.py                  ← 包初始化 + 懒加载
    config.py                    ← PARAM_SPACE(27参数), DEFAULTS, TIERS, YAML映射
    feature_extractor.py         ← CSV加载 → PhaseMetrics/RunMetrics (曲率/平滑度)
    phase_metrics.py             ← metrics_database.json → corr(metric, time)
    score_model.py               ← ★ 核心: heuristic→correlation→path_based 自动升级
    costmap_generator.py         ← PGM加载 + Nav2 inflation → 代价地图
    astar_planner.py             ← A* 8连接搜索 + 路径特征提取
    optuna_search.py             ← 分层搜索 (tier1/7, default/19, full/27) + --freeze
    gpu_search.py                ← Sobol采样 + 批量评分 + Pareto (桩代码)
    yaml_patch.py                ← 参数→Nav2嵌套YAML, ros2 param load兼容
    compare.py                   ← Markdown对比表 + 趋势检测
    rosbag_loader.py             ← 纯sqlite3解析rosbag2, 无ROS2依赖
    visualizer.py                ← 敏感性曲线/Pareto图/参数重要性/收敛图
  data/                          ← 所有数据集中
    trajectories/                ← 2组真车CSV (2026-06-27 11:22/11:23)
    rosbags/                     ← 3个rosbag (11:14/11:16/11:21)
  tuning_results/                ← 自动生成
    metrics_database.json        ← 共享历史数据库
    out1/ out2/ out3/ ...        ← 每次运行独立目录
      tune_*.log                 ← 运行日志
      best_params_*.json         ← 最佳参数JSON
      nav2_patch_*.yaml          ← ★ 可部署的YAML补丁
      importance_*.png           ← 参数重要性图
      convergence_*.png          ← 收敛曲线
      sensitivity_matrix_*.png   ← 敏感性矩阵
```

## 评分策略升级路径

```
0 CSV                 → heuristic (硬编码公式, 15项加权)
1+ CSV, 无地图         → correlation (corr(metric, time) 自动权重)
1+ CSV + 地图          → ★ path_based (A* 真实路径特征 → 评分)
30+ CSV + 地图         → path_based + LightGBM 代替 Ridge
```

## path_based 评分验证 (2026-06-27)

| inflation | path_based | heuristic | 真车效果 |
|-----------|-----------|-----------|---------|
| 0.55 | **0.42** ✅ | 0.33 ❌ | 82.0s DONE |
| 0.25 | 0.66 | 0.12 ❌ | 175.4s |
| 0.12 | 0.63 | — | 贴墙 |

**path_based 评分方向正确**：正确识别 0.55 比 0.25 好（heuristic 给反了）。

## 已知限制

- **当前无 per-run 参数记录**：历史 CSV 不含当时用的 Nav2 配置，Ridge 路径模型无法训练 → 使用 raw path-feature 公式降级
- **controller 参数无法评估**：`desired_linear_vel`/`cost_scaling_gain` 等不影响路径几何 → 需 CSV 相关性补充
- **GPU 未实现**：CuPy/Numba 桩代码，评分函数太轻量不需 GPU
- **单次 A* 评分 ≈7ms**：10000 次 ≈70秒（可接受，不需 GPU）

## 常用命令 (Auto Tuner)

```bash
# 默认搜索: 10000 trials, tier=default (19参数)
python _analyze_plans.py

# 仅分析不搜索
python _analyze_plans.py --analyze-only

# Tier1 (7核心参数)
python _analyze_plans.py --tier tier1

# 冻结全部 planner 参数
python _analyze_plans.py --freeze "planner.*"

# 对比所有历史跑
python _analyze_plans.py --compare

# 含 rosbag 增强
python _analyze_plans.py --rosbag-dir data/rosbags/

# 生成单参数敏感性曲线
python _analyze_plans.py --sensitivity controller.desired_linear_vel
```

## 数据获取流程

```bash
# 从小车下载最新数据
ssh_download → trajectory_*.csv → data/trajectories/
ssh_download → rosbag *.db3 + metadata.yaml → data/rosbags/

# 放到对应目录后自动扫描
python _analyze_plans.py  # 自动加载 data/trajectories/ + data/rosbags/
```
