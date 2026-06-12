# Stage 3 工作交接文档

> 写于 2026-06-12，总结多轮调试中反复出现的规范、陷阱和约定。新对话开始时应先读此文件。

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
