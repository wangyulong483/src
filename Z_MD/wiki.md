我来帮你系统梳理阿克曼转向的运动学原理，并给出可直接引用的论文和工程资料。


阿克曼小车过弯的本质是**几何约束下的非完整运动**：四个轮子必须绕同一个瞬时中心做圆周运动，且内侧前轮转角大于外侧，以避免轮胎侧滑。下面从原理、模型、控制算法到论文资料系统梳理。

---

## 1. 阿克曼过弯的核心原理

### 1.1 几何约束（Ackermann Steering Geometry）
车辆转向时，四个车轮的轴线延长线必须交于后轴延长线上的**瞬时转向中心 O**。这是阿克曼转向的根本约束：

- **内侧轮转角 α > 外侧轮转角 β**
- 核心几何关系：
  $$\cot\beta - \cot\alpha = \frac{K}{L}$$
  其中 $K$ 为轮距（track width），$L$ 为轴距（wheelbase）。

### 1.2 运动学模型（自行车模型 / Bicycle Model）
工程上通常将四轮简化为"单车模型"：用前后轴中点的两个等效轮子代替实际四轮，以后轴中心 $(x,y)$ 为参考点。

**连续时间微分方程**：
$$
\begin{aligned}
\dot{x} &= v \cos\theta \\
\dot{y} &= v \sin\theta \\
\dot{\theta} &= \frac{v \tan\delta}{L}
\end{aligned}
$$

**离散化位姿更新**（用于里程计推算和路径规划）：
$$
\theta_{k+1} = \theta_k + \frac{v_k}{L} \tan(\delta_k) \cdot \Delta t
$$

**最小转弯半径**：
$$R_{\min} = \frac{L}{\tan\delta_{\max}}$$

这个 $R_{\min}$ 是路径规划中最关键的硬约束——任何小于此半径的圆弧，阿克曼小车物理上无法完成。

---

## 2. 阿克曼路径跟踪的经典论文

### 2.1 基础运动学建模
| 论文 | 作者/来源 | 核心贡献 |
|------|-----------|----------|
| **Using the Ackerman principle for kinematic modeling of wheeled mobile robots** | 任孝平, 蔡自兴 / 《智能系统学报》2009 | 国内最早系统推导阿克曼移动机器人运动学模型的论文之一，给出了转向角、航向角、转弯半径的完整数学公式，并仿真验证了模型正确性 |
| **Kinematic Model of a Logistic Train with a Double Ackermann Steering System** | IJSIMM | 双阿克曼转向系统的 Jacobian 运动学建模，适用于多节车厢/拖车场景 |

### 2.2 路径跟踪控制算法（必读）
| 论文 | 来源 | 核心贡献 |
|------|------|----------|
| **Simulation Performance Evaluation of Pure Pursuit, Stanley, LQR, MPC Controller for Autonomous Vehicles** | IEEE, 2021 (被引79次) | 在阿克曼模型下系统对比了四种主流跟踪器：Pure Pursuit、Stanley、LQR、MPC，给出了各算法的精度与鲁棒性量化评估 |
| **New control model for autonomous vehicles using integration of Model Predictive and Stanley based controllers** | PMC/NIH | 提出 MPC + Stanley 的混合控制架构，用 MPC 做纵向速度/制动控制，Stanley 做横向转向控制，在阿克曼转向约束下实现了更平滑的过弯 |
| **Driving Fast but Safe: On Enforcing Operational Limits of a NMPC System** | SciTePress 2020 | 针对阿克曼车辆的 NMPC 实时控制，讨论了模型精度与加速度约束的边界，适合高速场景下的过弯安全控制 |
| **Predictive Active Steering Control for Autonomous Vehicle Systems** | ResearchGate (经典) | 早期 MPC 主动转向控制论文，将车辆动力学嵌入 LPV 系统，实现了侧风抑制和湿滑路面双车道保持 |
| **Stanley: The Robot that Won the DARPA Grand Challenge** | Thrun et al. | 虽然侧重 AI 感知，但 Stanley 赛车的横向控制正是基于几何路径跟踪，其阿克曼底盘的高速沙漠驾驶经验是路径跟踪的工程标杆 |

---

## 3. 可直接运行的工程资料

### 3.1 开源仿真项目
- **CoppeliaSim + Python 路径跟踪仿真**：GitHub 项目 `pangy9/Path-Planning-and-Control-for-CoppeliaSim`，内含**差速与阿克曼小车模型文件**，以及 Pure Pursuit、Stanley、MPC 的完整 Python 实现。你可以直接下载 `.ttt` 场景文件，在 CoppeliaSim 中验证不同控制器的过弯表现。

### 3.2 Simulink 建模教程
- CSDN 上的《基于阿克曼转向的车辆运动学模型》系列：提供了 Simulink 2018b 的完整模型文件和说明文档，包含转向梯形机构的三角函数实现：
  ```matlab
  phi_R = atan(L/(L/tan(alpha) + W/2));  % 外侧轮
  phi_L = atan(L/(L/tan(alpha) - W/2));  % 内侧轮
  ```
  以及运动学方程的 MATLAB Function 模块，适合作为路径规划算法的验证平台。

### 3.3 中文入门资料
- **Yahboom 阿克曼运动学分析**：从最小转弯半径推导到位姿预测，公式完整且配有图示，适合快速建立直觉。
- **CSDN 车辆运动学模型(阿克曼模型)**：详细解释了单车模型假设、圆弧轨迹近似、以及离散化位姿更新公式。

---

## 4. 与你当前 Nav2 项目的直接关联

你正在用 **Regulated Pure Pursuit Controller** 做 Nav2 导航，这个控制器本质上就是**阿克曼运动学模型的路径跟踪实现**：

| 概念 | 论文/源码对应 | 你的项目中的体现 |
|------|---------------|------------------|
| **转弯半径约束** | $R = L/\tan\delta$ | Nav2 参数 `min_turning_radius`（若你用的是 SmacPlannerHybrid，它会用 Reeds-Shepp 模型，但控制器层面仍需约束） |
| **速度-曲率调节** | Regulated Pure Pursuit 论文 | `use_velocity_scaled_lookahead_dist` 参数，根据当前速度动态调整前视距离 |
| **航向角漂移** | 运动学模型依赖 $\theta$ 的精度 | 你日志中 BMI088 Madgwick 的 `beta=0.0030` 导致快速旋转后航向丢失，直接破坏了 $\theta$ 的估计，使控制器算出的 $\delta$ 完全错误 |

**一个关键建议**：在 OriginCar Pro 的 `nav2_params.yaml` 中，确认 `controller_server` 的 `min_turning_radius` 是否与你小车的物理参数匹配。OriginCar Pro 的轴距 $L$ 约 0.2m 左右，若最大前轮转角 $\delta_{\max} \approx 30°$，则：
$$R_{\min} = \frac{0.2}{\tan(30°)} \approx 0.35\text{m}$$

如果 Nav2 中设置的最小转弯半径小于这个值，规划器会生成小车**物理上无法执行**的轨迹，导致原地震荡或撞墙。

---

## 5. 推荐阅读顺序

如果你要深入理解并优化 OriginCar 的过弯性能，建议按这个顺序阅读：

1. **先看**：《智能系统学报》任孝平/蔡自兴的论文（建立运动学直觉）
2. **再读**：Yahboom 或 CSDN 的 Simulink 教程（动手验证公式）
3. **然后**：IEEE 2021 的 Pure Pursuit vs Stanley vs MPC 对比论文（理解控制器差异）
4. **最后**：PMC 那篇 MPC + Stanley 混合控制（如果你后续想换掉 Regulated Pure Pursuit，用更高级的 MPC）

需要我把这些论文中的核心公式整理成一份可以直接插入你项目文档的 Markdown 笔记吗？或者针对 OriginCar Pro 的具体轴距参数，帮你算一份最小转弯半径和最大曲率的对照表？