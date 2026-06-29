# Nav2 Offline Auto Tuner 重构方案（Claude Code 执行指南）

## 项目背景

当前平台：

- ROS2 Humble
- SmacPlannerHybrid (REEDS_SHEPP)
- RegulatedPurePursuit Controller
- Ackermann 小车
- wheelbase = 0.143 m
- min_turning_radius = 0.30 m

当前成绩：

- 真车最佳：
    DONE
    73.1 s

目标：

- 尽可能逼近 70.1 s

约束：

- 不允许改 MPPI
- 不允许改 DUBIN
- 不增加新的 ROS2 依赖
- 不需要 Gazebo
- 不依赖 WSL2

目前已有：

_analyze_plans.py

但是目前仅属于：

Heuristic Parameter Search

而不是：

Offline Data-driven Auto Tuner

需要彻底升级。

---

# 总体目标

将 _analyze_plans.py 改造成：

Offline Nav2 Auto Tuner

要求：

✔ 能持续学习历史 rosbag / trajectory CSV

✔ 能自动建立真实评分模型

✔ 能生成可直接使用的 YAML

✔ 能利用 RTX 5060 做高速搜索

✔ 每次新增 rosbag 后评分都会越来越准确

最终形成：

Trajectory
↓

Feature Extraction

↓

Metric Database

↓

Offline Evaluator

↓

Optuna / GPU Search

↓

Top Parameters

↓

YAML Patch

---

# 第一部分：评分函数（最高优先级）

目前 compute_score()

基本属于：

人为经验

例如：

desired_linear_vel

接近

0.48

就是好。

这是不可接受的。

应该改成：

Data-driven Score

即：

score =
Σ wi * metric_i

其中：

metric 包括：

Total Time

Phase Time

Path Length

Average Speed

DIR_SWITCH

Replan Count

Average Curvature

Curvature Variance

Heading Error

Cross Track Error

CPU

Planner Frequency

Goal Reach Success

Smoothness

Jerk

Angular Oscillation

其中：

weight

不能写死。

应自动根据历史数据学习。

例如：

corr(metric,time)

得到：

DIR_SWITCH

0.87

Jerk

0.81

CPU

0.04

则：

weight=

normalize(|corr|)

CSV 越多，

评分越准确。

如果没有 CSV：

再退回 heuristic。

---

# 第二部分：建立 Metrics Database

不要分析一个 CSV。

应该分析：

logs/

目录。

例如：

trajectory_70.csv

trajectory_71.csv

trajectory_73.csv

...

全部导入。

自动生成：

metrics_database.json

例如：

{

baseline:

{

CRUISE:

{

mean_time

best_time

std

},

RETURN_P:

...

},

feature_statistics:

...

}

以后：

compute_score()

全部读取这里。

不要硬编码。

---

# 第三部分：支持 rosbag

CSV 信息太少。

建议支持：

rosbag2

自动读取：

odom

tf

cmd_vel

plan

global_costmap

local_costmap

planner_server

controller_server

behavior_tree_log

diagnostics

如果存在：

自动提取：

Planner Frequency

Controller Frequency

Planning Delay

Path Curvature

Heading Error

Tracking Error

Goal Error

Obstacle Clearance

CPU

Memory

Temperature

Planner Failures

Behavior Transition

Recoveries

DIR_SWITCH

重新规划次数

如果只有 CSV：

自动降级。

要求：

不新增 ROS2 依赖。

直接调用：

ros2 bag info

ros2 bag play

或解析 sqlite3 bag。

---

# 第四部分：GPU 利用（RTX 5060）

当前 GPU 基本没发挥作用。

要求：

GPU 负责：

① Batch Score

例如：

一次：

100000

组参数

GPU

同时评分。

不要：

一个 Trial

一个 Trial

算。

建议：

CuPy

Numba CUDA

Torch

任选一种。

要求：

Score Evaluation

GPU 化。

---

② Sobol Sampling

不要：

Random。

建议：

Sobol

Latin Hypercube

GPU

生成：

几十万参数。

一次筛掉：

90%

再交：

Optuna。

---

③ Pareto Ranking

不要：

单目标。

建立：

Pareto

目标：

Time

DIR_SWITCH

CPU

Smoothness

Path Length

Planner Hz

输出：

Pareto Front

---

第四部分：

Optuna

只负责：

局部搜索。

GPU：

负责：

大规模初筛。

---

# 第五部分：搜索空间分层

Tier1

7个

必须搜索：

desired_linear_vel

lookahead_dist

inflation_radius

cost_scaling_gain

cost_scaling_factor

reverse_penalty

change_penalty

Tier2

12个

默认开启。

Tier3

固定。

只有：

--full

搜索。

另外：

增加：

--freeze

例如：

--freeze planner.*

或者：

--freeze controller.lookahead_dist

---

# 第六部分：参数敏感性分析

搜索结束：

自动：

每个重要参数：

±20%

扫描。

生成：

Sensitivity

例如：

lookahead

↓

Score

形成：

曲线。

自动输出：

High Sensitive

Medium Sensitive

Low Sensitive

方便真车调试。

---

# 第七部分：YAML Patch

不要：

#

planner.change_penalty

0.1→0.08

而是真正生成：

controller_server:

ros__parameters:

FollowPath:

desired_linear_vel:

planner_server:

ros__parameters:

GridBased:

reverse_penalty:

change_penalty:

要求：

可直接：

ros2 param load

或者：

diff

原 YAML。

---

# 第八部分：Compare

compare

输出：

Markdown Table

例如：

| File | Status | Total | Cruise | Return | Backing | DIR_SWITCH | Replan | Planner Hz | Trend |

Trend：

自动：

↑

↓

≈

不要：

只输出：

文件名。

---

# 第九部分：输出

不要：

每100 Trial

打印。

改：

500

一次。

新最优：

打印：

一行。

最后：

Top10

Parameter Importance

Sensitivity

Pareto

即可。

---

# 第十部分：新增 Machine Learning Baseline（可选）

如果：

CSV

>30

建议：

训练：

LightGBM

XGBoost

RandomForest

预测：

Time

而不是：

人工 Score。

要求：

离线。

不增加 ROS2 依赖。

如果：

CSV

不足：

自动退回：

Correlation Score。

---

# 第十一部分：建议新增目录结构

_analyze_plans.py

只保留入口。

新增：

offline_tuner/

feature_extractor.py

phase_metrics.py

score_model.py

gpu_search.py

optuna_search.py

yaml_patch.py

compare.py

rosbag_loader.py

visualizer.py

这样：

以后维护成本低。

---

# 第十二部分：Agent 执行原则

Agent 不允许：

修改导航算法。

不能：

改：

Smac

RPP

BT

Recovery

Collision Monitor

MPPI

只能：

升级：

Offline Auto Tuner。

所有新增功能：

必须：

向下兼容。

即：

只有 CSV

仍然可运行。

有 rosbag

自动增强。

没有 GPU

自动 CPU。

有 RTX

自动 GPU。

---

# 最终目标

最终得到的 Offline Auto Tuner 应满足：

✓ 利用 RTX 5060 大规模并行评分与筛选参数。

✓ 自动分析多个 trajectory CSV 与 rosbag2，建立 Metrics Database。

✓ 使用真实历史数据构建评分模型，而不是固定启发式。

✓ 默认搜索 Tier1+Tier2，支持 --full 与 --freeze。

✓ 输出 Pareto 最优参数集合，而不仅是单一最优。

✓ 自动生成可直接用于 Nav2 的 YAML Patch。

✓ 输出参数敏感性分析、重要性排序、阶段性能统计和趋势分析。

✓ 新增历史数据后无需修改代码即可自动提升评分准确性。

目标不是生成一个"参数搜索脚本"，而是建立一个能够长期服务于该 Ackermann Nav2 项目的离线自动调参平台。

另外，我还有一个建议：如果你的目标是70 秒以内，仅靠目前 CSV 中的字段（位置、速度、plan_len 等）是不够的。我建议额外录制一批 rosbag（10~30 次真车运行即可），至少包含：

/odom

/tf

/cmd_vel

/plan（全局路径）

/local_plan（如果有）

/scan

/planner_server/transition_event（如果有）

/controller_server/transition_event（如果有）

/behavior_tree_log

/diagnostics

/parameter_events

有了这些数据，就能计算横向误差、路径曲率、规划频率、重规划延迟、控制器振荡、障碍物净空等真正影响比赛成绩的指标。这样离线评分与真车表现的一致性会比单纯依赖 CSV 高得多，也是最有希望帮助你进一步逼近 70.1 秒的方法。