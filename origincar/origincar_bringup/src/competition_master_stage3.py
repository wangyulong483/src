#!/usr/bin/env python3
"""
competition_master_stage3 — Stage 3 管理层节点

完整 Stage 3 流程:
1. NAV_TO_QR:       导航到 QR 发布点 (停靠, 扫码获取方向 CW/CCW)
2. BACKING_UP:      右后退摆正车头, 使车头对准通道入口 (阿克曼无法原地旋转)
3. CRUISE_CHANNEL:  NavigateThroughPoses 穿全部路点 (途经+停靠)
                    规划器自动处理通道内路由, 入口为途经点不停
                    CW  (顺时针) → cruise_cw[-1], CCW (逆时针) → cruise_ccw[-1]
4. VLM_TRIGGER:     发布 100 到 /sign4return, 立即返航不等AI结果
5. RETURN_P:        导航返回 P 点 (停靠)

架构说明:
  - NavigateToPose action client 用于全部导航 (NAV_TO_QR, NAV_TO_ENTRY, CRUISE_CHANNEL, RETURN_P)
  - cruise_cw / cruise_ccw 数组保留全部路点以备后用, 实际仅取最后一个作为 VLM 停靠点
  - 沿用 stage2 的 QR 拦截→cancel-wait-for-BT→backup→entry-nav 模式
  - 180s 全局超时 + 各阶段独立超时
"""

import math
import os
import subprocess
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from std_msgs.msg import String, Int32, Empty
from geometry_msgs.msg import Twist, PoseStamped, PoseWithCovarianceStamped
from nav2_msgs.action import NavigateToPose, NavigateThroughPoses
from nav2_msgs.srv import ClearCostmapAroundRobot
from nav2_msgs.msg import CostmapFilterInfo
from nav_msgs.msg import Path, OccupancyGrid
from rclpy.qos import QoSProfile, QoSDurabilityPolicy, QoSHistoryPolicy, QoSReliabilityPolicy
from action_msgs.msg import GoalStatus

try:
    import psutil
    _HAS_PSUTIL = True
except ImportError:
    _HAS_PSUTIL = False


def _flat_to_waypoints(arr, stride=3):
    """将 flat double array 转为 [[x, y, yaw], ...]"""
    return [arr[i:i + stride] for i in range(0, len(arr), stride)]


class CompetitionMasterStage3(Node):
    def __init__(self):
        super().__init__('competition_master_stage3')

        # ═══════════════════════════════════════════════════════════
        # ── 声明参数: 路点 ──────────────────────────────────────
        # ═══════════════════════════════════════════════════════════
        self.declare_parameter('qr_point_x', 0.41)
        self.declare_parameter('qr_point_y', -3.17)
        self.declare_parameter('qr_point_yaw', 0.0)
        self.declare_parameter('entry_point_x', 0.38)
        self.declare_parameter('entry_point_y', -1.10)
        self.declare_parameter('entry_point_yaw', 0.0)
        self.declare_parameter('p_point_x', -1.985)
        self.declare_parameter('p_point_y', -0.014)
        self.declare_parameter('p_point_yaw', 0.262)

        # cruise_cw: 顺时针 (odd QR) — 途经点 + VLM 停靠点
        #            仅最后一个路点 (VLM 停靠点) 用于 NavigateToPose
        # 2026-06-28: 手动驾驶重标定 (stage2 RViz 逐点导航)
        self.declare_parameter('cruise_cw', [
            0.93, 0.11, 0.0,   2.19, 0.77, 0.0,   3.01, -1.16, 0.0,
        ])
        # cruise_ccw: 逆时针 (even QR) — 途经点 + VLM 停靠点
        #             仅最后一个路点 (VLM 停靠点) 用于 NavigateToPose
        # 2026-06-12: 手动驾驶标定路径
        self.declare_parameter('cruise_ccw', [
            0.25, -1.17, 0.0,   1.66, -1.50, 0.0,   2.90, -0.90, 0.0,   2.17, 0.69, 0.80,  # 手动驾驶标定
        ])

        # ═══════════════════════════════════════════════════════════
        # ── 声明参数: 超时 ──────────────────────────────────────
        # ═══════════════════════════════════════════════════════════
        self.declare_parameter('total_timeout', 180.0)
        self.declare_parameter('nav_to_qr_timeout', 90.0)
        self.declare_parameter('nav_to_entry_timeout', 60.0)
        self.declare_parameter('cruise_timeout', 180.0)  # 不重试, 一次走完
        self.declare_parameter('vlm_timeout', 30.0)
        self.declare_parameter('return_timeout', 120.0)
        self.declare_parameter('default_qr_direction', '逆时针')  # 未扫到 QR 时的回退方向

        # ═══════════════════════════════════════════════════════════
        # ── 声明参数: 其他 ──────────────────────────────────────
        # ═══════════════════════════════════════════════════════════
        self.declare_parameter('backup_duration_sec', 6.0)
        self.declare_parameter('keepout_disable_duration_sec', 30.0)
        self.declare_parameter('backup_linear_x', -0.15)     # 慢速=更小转弯半径
        self.declare_parameter('backup_angular_z', 0.80)    # 2.80→0.80: 降低转速防止IMU/AMCL跟丢
        self.declare_parameter('start_delay_sec', 0.1)       # 0.5→0.1: 更快轮询Nav2 action server
        self.declare_parameter('cancel_wait_timeout_sec', 3.0)  # 等待 BT 取消确认
        self.declare_parameter('qr_decision_kill_timeout_sec', 2.0)  # 等待 qr_decision 返回方向
        self.declare_parameter('vlm_result_topic', 'vlm_result')

        # ═══════════════════════════════════════════════════════════
        # ── 读取参数 ────────────────────────────────────────────
        # ═══════════════════════════════════════════════════════════
        self.qr_point_x = self.get_parameter('qr_point_x').value
        self.qr_point_y = self.get_parameter('qr_point_y').value
        self.qr_point_yaw = self.get_parameter('qr_point_yaw').value
        self.entry_point_x = self.get_parameter('entry_point_x').value
        self.entry_point_y = self.get_parameter('entry_point_y').value
        self.entry_point_yaw = self.get_parameter('entry_point_yaw').value
        self.p_point_x = self.get_parameter('p_point_x').value
        self.p_point_y = self.get_parameter('p_point_y').value
        self.p_point_yaw = self.get_parameter('p_point_yaw').value
        self.cruise_cw = self.get_parameter('cruise_cw').value
        self.cruise_ccw = self.get_parameter('cruise_ccw').value
        self.total_timeout = self.get_parameter('total_timeout').value
        self.nav_to_qr_timeout = self.get_parameter('nav_to_qr_timeout').value
        self.nav_to_entry_timeout = self.get_parameter('nav_to_entry_timeout').value
        self.cruise_timeout = self.get_parameter('cruise_timeout').value
        self.vlm_timeout = self.get_parameter('vlm_timeout').value
        self.return_timeout = self.get_parameter('return_timeout').value
        self.default_qr_direction = self.get_parameter('default_qr_direction').value
        self.backup_duration_sec = self.get_parameter('backup_duration_sec').value
        self.keepout_disable_duration_sec = self.get_parameter('keepout_disable_duration_sec').value
        self.backup_linear_x = self.get_parameter('backup_linear_x').value
        self.backup_angular_z = self.get_parameter('backup_angular_z').value
        self.start_delay_sec = self.get_parameter('start_delay_sec').value
        self.cancel_wait_timeout_sec = self.get_parameter('cancel_wait_timeout_sec').value
        self.qr_decision_kill_timeout_sec = self.get_parameter('qr_decision_kill_timeout_sec').value
        self.vlm_result_topic = self.get_parameter('vlm_result_topic').value

        # ═══════════════════════════════════════════════════════════
        # ── 状态变量 ────────────────────────────────────────────
        # ═══════════════════════════════════════════════════════════
        # 状态机: INIT → NAV_TO_QR → BACKING_UP → CRUISE_CHANNEL
        #         → (VLM触发,不等结果) → RETURN_P → DONE
        self.state = 'INIT'
        self.qr_data = None               # QR 原始解码文本
        self._qr_direction = None         # qr_decision 输出: "顺时针" / "逆时针"
        self._qr_event_received = False   # 是否已收到 /qr_event
        self._vlm_result = None           # VLM 推理结果
        self._vlm_received = False        # 是否已收到 VLM 结果

        # ── NavigateToPose (全部导航使用单一 action client) ─────
        self._goal_handle = None
        self._retry_timer = None
        self._nav_start_time = None       # 当前段导航目标发送时间 (用于段超时)

        # ── QR 拦截取消等待 (沿用 stage2 模式) ──────────────────
        self._pending_entry_nav = False             # True=等待BT取消确认
        self._pending_entry_nav_timeout = None      # 取消确认超时定时器

        # ── 后退序列变量 ────────────────────────────────────────
        self._backup_timer = None
        self._backup_keepalive = None      # 10Hz 保活定时器
        self._backup_twist = None          # 后退速度缓存

        # ── Keepout 临时禁用 ────────────────────────────────────
        self._keepout_reenable_timer = None

        # ── VLM 触发 ────────────────────────────────────────────
        self._vlm_triggered = False
        self._vlm_trigger_time = None

        # ── 全局计时 ────────────────────────────────────────────
        self._clock_start = None           # 全局计时起点 (首次发送导航目标时记录)

        # ═══════════════════════════════════════════════════════════
        # ── ROS 接口 ────────────────────────────────────────────
        # ═══════════════════════════════════════════════════════════
        # Action Clients
        self.nav_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')
        self.through_client = ActionClient(
            self, NavigateThroughPoses, 'navigate_through_poses')

        # ClearCostmapAroundRobot service clients (返航时清除障碍物标记)
        self._clear_around_local = self.create_client(
            ClearCostmapAroundRobot, 'local_costmap/clear_around_local_costmap')
        self._clear_around_global = self.create_client(
            ClearCostmapAroundRobot, 'global_costmap/clear_around_global_costmap')

        # Subscribers
        self.qr_sub = self.create_subscription(
            String, '/sign', self.qr_callback, 10)
        self.qr_event_sub = self.create_subscription(
            String, '/qr_event', self._on_qr_event, 10)
        self.vlm_result_sub = self.create_subscription(
            String, self.vlm_result_topic, self._on_vlm_result, 10)

        # ── 诊断订阅 ──────────────────────────────────────────
        self._robot_pose = None
        self._amcl_sub = self.create_subscription(
            PoseWithCovarianceStamped, '/amcl_pose', self._on_amcl_pose, 10)
        self._plan_info = None
        self._plan_sub = self.create_subscription(Path, '/plan', self._on_plan, 10)
        self._cmd_vx = 0.0; self._cmd_wz = 0.0
        self._cmd_diag_sub = self.create_subscription(
            Twist, '/cmd_vel', self._on_cmd_diag, 10)
        self._trajectory = []  # [(elapsed, x, y, yaw, state, cmd_vx, cmd_wz, plan_n, plan_len, plan_ex, plan_ey, cpu, mem, cputemp), ...]
        self._plan_history = []  # [(elapsed, state, n_pts, len_m, sx, sy, ex, ey), ...] 每次规划记录

        # ── 障碍物录制: 缓存global_costmap, 退出时保存为PGM ──
        self._costmap_msg = None  # 最新的 OccupancyGrid
        self._costmap_sub = self.create_subscription(
            OccupancyGrid, '/global_costmap/costmap', self._on_costmap, 10)
        self._nav_goal_pos = None       # (x, y) current nav target for dist-to-goal
        self._hw_cache = {'cpu': -1, 'mem': -1, 'cpu_temp': -1}
        self._exit_reason = 'unknown'
        self._timeout_handled = False   # 防止 _timeout_shutdown 重复触发

        # Publishers
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.sign4return_pub = self.create_publisher(Int32, '/sign4return', 10)
        self.costmap_clear_pub = self.create_publisher(
            Empty, '/global_costmap/clear_entirely_global_costmap', 10)
        self.local_costmap_clear_pub = self.create_publisher(
            Empty, '/local_costmap/clear_entirely_local_costmap', 10)
        _fi_qos = QoSProfile(depth=10, reliability=QoSReliabilityPolicy.RELIABLE,
                             durability=QoSDurabilityPolicy.TRANSIENT_LOCAL,
                             history=QoSHistoryPolicy.KEEP_LAST)
        self.keepout_info_pub = self.create_publisher(
            CostmapFilterInfo, '/costmap_ctrl', _fi_qos)
        # ★ 启动时重置: 覆盖上轮运行的禁用残留
        _reset_msg = CostmapFilterInfo()
        _reset_msg.type = 0
        _reset_msg.filter_mask_topic = "/keepout_mask"
        _reset_msg.base = 0.0; _reset_msg.multiplier = 1.0
        self.keepout_info_pub.publish(_reset_msg)

        # ── rosbag 录制 ───────────────────────────────────────
        self._bag_process = None

        # ── 定时器 ──────────────────────────────────────────────
        self._timeout_timer = self.create_timer(1.0, self._check_timeouts)
        self._diag_timer = self.create_timer(2.0, self._diagnostic_log)

        # ── 阶段计时 ──────────────────────────────────────────
        self._phase_times = {}
        self._phase_start_time = None
        self._launch_time = self.get_clock().now()

        # ★ 清理上轮残留 CSV/JSON (防止堆积)
        self._cleanup_old_trajectories()

        # ═══════════════════════════════════════════════════════════
        # ── 启动日志 ────────────────────────────────────────────
        # ═══════════════════════════════════════════════════════════
        self.get_logger().info("=" * 60)
        self.get_logger().info("=== [Stage 3] 总控节点初始化 ===")
        self.get_logger().info(
            f"  QR点:    ({self.qr_point_x:.2f}, {self.qr_point_y:.2f}, yaw={self.qr_point_yaw:.2f})")
        self.get_logger().info(
            f"  通道入口: ({self.entry_point_x:.2f}, {self.entry_point_y:.2f}, yaw={self.entry_point_yaw:.2f})")
        self.get_logger().info(
            f"  P点:     ({self.p_point_x:.2f}, {self.p_point_y:.2f}, yaw={self.p_point_yaw:.2f})")
        wps_cw = _flat_to_waypoints(self.cruise_cw)
        wps_ccw = _flat_to_waypoints(self.cruise_ccw)
        self.get_logger().info(
            f"  cruise_cw: {len(wps_cw)} 路点 → VLM=({wps_cw[-1][0]:.2f}, {wps_cw[-1][1]:.2f})")
        self.get_logger().info(
            f"  cruise_ccw: {len(wps_ccw)} 路点 → VLM=({wps_ccw[-1][0]:.2f}, {wps_ccw[-1][1]:.2f})")
        self.get_logger().info(
            f"  超时: total={self.total_timeout}s QR={self.nav_to_qr_timeout}s "
            f"entry={self.nav_to_entry_timeout}s cruise={self.cruise_timeout}s "
            f"vlm={self.vlm_timeout}s return={self.return_timeout}s")
        self.get_logger().info(
            f"  回退QR方向: {self.default_qr_direction}")
        self.get_logger().info(
            f"  VLM结果话题: {self.vlm_result_topic}")
        self.get_logger().info("=" * 60)

    # ═══════════════════════════════════════════════════════════════
    # ── 工具方法 ────────────────────────────────────────────────
    # ═══════════════════════════════════════════════════════════════

    def _kill_process(self, name):
        """安全终止进程 (subprocess.Popen 非阻塞)"""
        try:
            subprocess.Popen(
                ['pkill', '-f', name],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
            self.get_logger().info(f"[KILL] 已发送终止信号: {name}")
        except FileNotFoundError:
            self.get_logger().error(f"[KILL] 命令 pkill 未找到，跳过终止 {name}")
        except Exception as e:
            self.get_logger().error(f"[KILL] 终止进程 {name} 异常: {e}")

    def _state_transition(self, new_state):
        """统一状态转换, 带诊断日志 + 阶段耗时追踪"""
        if self.state == new_state:
            return
        now = self._get_current_raw_time()
        old = self.state
        if self._phase_start_time is not None and old != 'INIT':
            self._phase_times[old] = now - self._phase_start_time
        self.state = new_state
        self._phase_start_time = now
        self.get_logger().info(
            f"[状态机] {old} → {new_state}"
        )

    def send_stop(self):
        """发布停止指令 — 直接写入 /cmd_vel 到达 STM32"""
        self.cmd_vel_pub.publish(Twist())

    def _get_current_raw_time(self):
        """获取当前时钟的原始秒数 (用于全局计时)"""
        return self.get_clock().now().nanoseconds / 1e9

    def _get_cruise_waypoints(self):
        """根据 QR 方向返回完整巡航路点列表 (途经点+停靠点)

        Returns:
            [[x, y, yaw], ...]: 全部路点, 最后一个为 VLM 停靠点
        """
        if self._qr_direction and '逆时针' in self._qr_direction:
            wps = _flat_to_waypoints(self.cruise_ccw)
            label = 'CCW (逆时针, even QR)'
        elif self._qr_direction and '顺时针' in self._qr_direction:
            wps = _flat_to_waypoints(self.cruise_cw)
            label = 'CW (顺时针, odd QR)'
        else:
            wps = _flat_to_waypoints(self.cruise_cw)
            label = 'CW (回退默认)'
        pts = ", ".join(f"({w[0]:.2f},{w[1]:.2f})" for w in wps)
        self.get_logger().info(f"[CRUISE] 方向: {label}, 路点: {pts}")
        return wps

    # ═══════════════════════════════════════════════════════════════
    # ── QR 回调 ─────────────────────────────────────────────────
    # ═══════════════════════════════════════════════════════════════

    def qr_callback(self, msg):
        """QR 解码回调 (/sign): 仅在 NAV_TO_QR 阶段拦截"""
        if not msg.data or self.state != 'NAV_TO_QR':
            return
        self.qr_data = msg.data
        self.get_logger().info(f"[QR检测] 内容: {msg.data}")
        self._nav_start_time = None   # QR 拦截终止第一段导航，清除段超时计时

        # 关闭 ZBar 解码节点 (CPU密集), 保留 qr_decision 以获取 /qr_event (方向)
        self._kill_process('qr_decoder_zbar')
        # qr_decision 将在收到 /qr_event 后关闭 (见 _on_qr_event)
        # 如果超时未收到 /qr_event, 也强制关闭
        self._qr_kill_timer = self.create_timer(
            self.qr_decision_kill_timeout_sec, self._kill_qr_decision_on_timeout)
        self.get_logger().info(">>> QR 解码已关闭, 等待方向判断 (/qr_event)...")

        if self._goal_handle is not None:
            # ★ 关键: 取消第一个目标后, 必须等待 BT navigator 完成 follow_path halt
            # 否则立即发送第二个目标会导致 race condition
            self.get_logger().info(
                "[QR检测] 取消当前导航目标, 等待BT完成 cancel/halt 清理..."
            )
            self._goal_handle.cancel_goal_async()
            # 设置等待标志: get_result_callback 收到 STATUS_CANCELED 后再发送第二个目标
            self._pending_entry_nav = True
            self._pending_entry_nav_timeout = self.create_timer(
                self.cancel_wait_timeout_sec, self._entry_nav_on_cancel_timeout)
        else:
            # goal_handle 不存在 (异常/边界情况), 直接发送第二个目标
            self.get_logger().warn(
                "[QR检测] goal_handle 为空，直接发送通道入口目标")
            self._transition_to_cruise()

    def _on_qr_event(self, msg):
        """qr_decision 结构化输出: {num},{direction},{x},{y}

        解析方向用于通道巡航。收到有效方向后立即关闭 qr_decision 释放资源。
        """
        # 仅在 NAV_TO_ENTRY 或等待取消确认期间接收 qr_event
        if (self.state != 'NAV_TO_ENTRY' and not self._pending_entry_nav) \
                or self._qr_event_received:
            return
        parts = msg.data.split(',') if msg.data else []
        if len(parts) < 2:
            return
        self._qr_direction = parts[1]  # "顺时针" 或 "逆时针"
        self._qr_event_received = True
        self.get_logger().info(
            f"[QR事件] 方向: {self._qr_direction} (通道巡航阶段使用)")
        # 收到方向后立即关闭 qr_decision
        self._kill_process('qr_decision')
        # 取消超时定时器
        if hasattr(self, '_qr_kill_timer') and self._qr_kill_timer is not None:
            self._qr_kill_timer.cancel()
            self._qr_kill_timer = None

    def _kill_qr_decision_on_timeout(self):
        """如果超时未收到 /qr_event, 强制关闭 qr_decision 防止资源泄漏"""
        if self._qr_event_received:
            return
        self.get_logger().warn(
            f"[QR] qr_decision {self.qr_decision_kill_timeout_sec}s "
            f"内未返回 /qr_event, 强制关闭, 使用回退方向")
        self._kill_process('qr_decision')
        if hasattr(self, '_qr_kill_timer') and self._qr_kill_timer is not None:
            self._qr_kill_timer.cancel()
            self._qr_kill_timer = None

    # ═══════════════════════════════════════════════════════════════
    # ── VLM 回调 ─────────────────────────────────────────────────
    # ═══════════════════════════════════════════════════════════════

    def _on_vlm_result(self, msg):
        """VLM 推理结果回调 (后台接收, 不阻塞导航)"""
        if self._vlm_received:
            return
        self._vlm_result = msg.data
        self._vlm_received = True
        self.get_logger().info(f"[VLM] 后台收到推理结果: {msg.data[:120]}...")

    # ═══════════════════════════════════════════════════════════════
    # ── 诊断回调 ─────────────────────────────────────────────────
    # ═══════════════════════════════════════════════════════════════

    def _on_amcl_pose(self, msg):
        q = msg.pose.pose.orientation
        siny = 2.0 * (q.w * q.z + q.x * q.y)
        cosy = 1.0 - 2.0 * (q.y * q.y + q.z * q.z)
        yaw = math.atan2(siny, cosy)
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y
        self._robot_pose = {'x': x, 'y': y, 'yaw': yaw}

        # ── 丰富轨迹记录 (每 ~10Hz) ─────────────────────────
        elapsed = self._get_current_raw_time() - self._clock_start if self._clock_start else 0.0

        # plan info snapshot
        plan_n = 0; plan_len = 0.0; plan_ex = 0.0; plan_ey = 0.0
        if self._plan_info:
            pi = self._plan_info
            plan_n = pi['n']; plan_len = pi['len']
            plan_ex = pi['end'][0]; plan_ey = pi['end'][1]

        # HW snapshot (from cache, refreshed at 2Hz by _diagnostic_log)
        hw = self._hw_cache

        self._trajectory.append((
            elapsed, x, y, yaw,
            self.state,
            self._cmd_vx, self._cmd_wz,
            plan_n, plan_len, plan_ex, plan_ey,
            hw.get('cpu', -1), hw.get('mem', -1), hw.get('cpu_temp', -1)
        ))

    def _on_plan(self, msg):
        if not msg.poses:
            self._plan_info = None; return
        pts = [(p.pose.position.x, p.pose.position.y) for p in msg.poses]
        total_len = sum(math.hypot(pts[i][0]-pts[i-1][0], pts[i][1]-pts[i-1][1])
                       for i in range(1, len(pts)))
        mid = pts[len(pts)//2]
        self._plan_info = {'n': len(pts), 'len': total_len,
                          'start': pts[0], 'mid': mid, 'end': pts[-1]}
        # ★ 记录每次规划: 用于评估planner质量
        elapsed = self._get_current_raw_time() - self._clock_start if self._clock_start else 0.0
        self._plan_history.append((
            elapsed, self.state, len(pts), total_len,
            pts[0][0], pts[0][1], pts[-1][0], pts[-1][1]
        ))

    def _on_cmd_diag(self, msg):
        self._cmd_vx = msg.linear.x; self._cmd_wz = msg.angular.z

    def _on_costmap(self, msg):
        """缓存最新 global_costmap, 退出时保存为PGM供可视化障碍物"""
        self._costmap_msg = msg

    # ── 硬件监控 ──────────────────────────────────────────────
    @staticmethod
    def _read_sysfs(path):
        try:
            with open(path, 'r') as f: return f.read().strip()
        except Exception: return None

    def _refresh_hw_cache(self):
        """刷新硬件监控缓存 (供 _diagnostic_log 和 CSV 轨迹使用)"""
        hw = {'cpu': -1, 'mem': -1, 'cpu_temp': -1, 'bpu_temp': -1, 'cpu_freq': -1}
        freq_raw = self._read_sysfs('/sys/devices/system/cpu/cpufreq/policy0/cpuinfo_cur_freq')
        if freq_raw: hw['cpu_freq'] = int(freq_raw) // 1000
        cpu_temp = self._read_sysfs('/sys/class/hwmon/hwmon0/temp3_input')
        if cpu_temp: hw['cpu_temp'] = int(cpu_temp) // 1000
        bpu_temp = self._read_sysfs('/sys/class/hwmon/hwmon0/temp2_input')
        if bpu_temp: hw['bpu_temp'] = int(bpu_temp) // 1000
        if _HAS_PSUTIL:
            try:
                hw['cpu'] = int(psutil.cpu_percent(interval=0.01))
                hw['mem'] = int(psutil.virtual_memory().percent)
            except Exception: pass
        self._hw_cache = hw
        return hw

    def _get_hw_stats(self):
        hw = self._refresh_hw_cache()  # 刷新缓存
        parts = []
        if hw['cpu_freq'] > 0: parts.append(f"cpuFreq={hw['cpu_freq']}MHz")
        if hw['cpu_temp'] >= 0: parts.append(f"cpuT={hw['cpu_temp']}C")
        if hw['bpu_temp'] >= 0: parts.append(f"bpuT={hw['bpu_temp']}C")
        if hw['cpu'] >= 0: parts.append(f"cpu={hw['cpu']}%")
        if hw['mem'] >= 0: parts.append(f"mem={hw['mem']}%")
        return ' '.join(parts) if parts else 'hw=N/A'

    def _diagnostic_log(self):
        if self._robot_pose is None: return
        p = self._robot_pose
        elapsed = self._get_current_raw_time() - self._clock_start if self._clock_start else 0.0
        plan_str = ""
        if self._plan_info:
            pi = self._plan_info
            plan_str = (f" plan[{pi['n']}pts {pi['len']:.1f}m] "
                       f"({pi['start'][0]:.2f},{pi['start'][1]:.2f})"
                       f"→({pi['end'][0]:.2f},{pi['end'][1]:.2f})")
        self.get_logger().info(
            f"[DIAG] state={self.state} "
            f"pos=({p['x']:.2f},{p['y']:.2f}) yaw={math.degrees(p['yaw']):.0f}deg "
            f"cmd=(vx={self._cmd_vx:.2f} wz={self._cmd_wz:.2f}) "
            f"elapsed={elapsed:.1f}s{plan_str} {self._get_hw_stats()}")

    def _get_nav2_params_snapshot(self):
        """读取当前 Nav2 YAML 中的关键参数, 用于离线分析关联参数与效果."""
        import yaml as _yaml
        nav2_yaml = '/userdata/dev_ws/src/originbot_navigation/param/originbot_nav2_rpp.yaml'
        flat = {}
        try:
            with open(nav2_yaml, 'r') as f:
                cfg = _yaml.safe_load(f) or {}

            # RPP controller params
            ctrl = cfg.get('controller_server', {}).get('ros__parameters', {})
            fp = ctrl.get('FollowPath', {})
            gc = ctrl.get('goal_checker', {})
            pc = ctrl.get('progress_checker', {})

            for k in ['desired_linear_vel', 'lookahead_dist', 'min_lookahead_dist',
                       'max_lookahead_dist', 'lookahead_time', 'cost_scaling_gain',
                       'cost_scaling_dist', 'min_approach_linear_velocity',
                       'approach_velocity_scaling_dist', 'max_linear_vel',
                       'max_angular_vel', 'max_linear_accel',
                       'regulated_linear_scaling_min_radius',
                       'regulated_linear_scaling_min_speed']:
                if k in fp:
                    flat[f'controller.{k}'] = fp[k]

            for k in ['xy_goal_tolerance', 'yaw_goal_tolerance']:
                if k in gc:
                    flat[f'controller.{k}'] = gc[k]

            for k in ['required_movement_radius', 'movement_time_allowance']:
                if k in pc:
                    flat[f'controller.{k}'] = pc[k]

            # Planner params
            planner = cfg.get('planner_server', {}).get('ros__parameters', {})
            gb = planner.get('GridBased', {})
            for k in ['reverse_penalty', 'change_penalty', 'non_straight_penalty',
                       'analytic_expansion_ratio', 'max_iterations',
                       'max_planning_time', 'angle_quantization_bins',
                       'cost_penalty', 'minimum_turning_radius']:
                if k in gb:
                    flat[f'planner.{k}'] = gb[k]

            # Costmap params (local + global)
            for scope, key in [('local_costmap', 'local'), ('global_costmap', 'global')]:
                cm = cfg.get(scope, {}).get(f'{scope}', {}).get('ros__parameters', {})
                infl = cm.get('inflation_layer', {})
                if 'inflation_radius' in infl:
                    flat[f'planner.inflation_radius.{key}'] = infl['inflation_radius']
                if 'cost_scaling_factor' in infl:
                    flat[f'planner.cost_scaling_factor.{key}'] = infl['cost_scaling_factor']

            self.get_logger().info(f'[TRAJ] Nav2 params snapshot: {len(flat)} keys')
        except Exception as e:
            self.get_logger().warn(f'[TRAJ] Failed to read Nav2 params: {e}')
        return flat

    def _cleanup_old_trajectories(self):
        """启动时删除上轮残留的所有 trajectory 文件, 防止堆积."""
        import glob as _glob
        try:
            for pat in ['/userdata/dev_ws/trajectory_*.csv',
                        '/userdata/dev_ws/trajectory_*.json',
                        '/userdata/dev_ws/trajectory_*.pgm']:
                for f in _glob.glob(pat):
                    os.remove(f)
            # 清理旧 rosbag (保留最近2个)
            bag_dir = '/userdata/dev_ws/bags'
            if os.path.isdir(bag_dir):
                bags = sorted(os.listdir(bag_dir))
                for old in bags[:-2]:
                    import shutil as _shutil
                    _shutil.rmtree(os.path.join(bag_dir, old), ignore_errors=True)
        except Exception as e:
            self.get_logger().warn(f'[CLEANUP] failed: {e}')

    def _start_bag_record(self):
        """启动 rosbag 录制 (后台进程)."""
        from datetime import datetime
        bag_dir = '/userdata/dev_ws/bags'
        os.makedirs(bag_dir, exist_ok=True)
        bag_name = f"stage3_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        bag_path = os.path.join(bag_dir, bag_name)
        topics = '/tf /tf_static /scan /odom /amcl_pose /plan /local_plan ' \
                 '/cmd_vel ' \
                 '/global_costmap/costmap /local_costmap/costmap ' \
                 '/sign /qr_event /vlm_result /robotvel'
        try:
            self._bag_process = subprocess.Popen(
                ['ros2', 'bag', 'record', '-o', bag_path] + topics.split(),
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            self.get_logger().info(f'[BAG] 录制开始: {bag_name}')
        except Exception as e:
            self.get_logger().error(f'[BAG] 启动失败: {e}')

    def _stop_bag_record(self):
        """停止 rosbag 录制."""
        if self._bag_process is None:
            return
        try:
            self._bag_process.send_signal(subprocess.signal.SIGINT)
            self._bag_process.wait(timeout=5)
            self.get_logger().info('[BAG] 录制已停止')
        except subprocess.TimeoutExpired:
            self._bag_process.kill()
            self.get_logger().warn('[BAG] 录制强制终止')
        except Exception as e:
            self.get_logger().warn(f'[BAG] 停止异常: {e}')
        self._bag_process = None

    def _save_trajectory(self):
        """保存全程 CSV + 摘要 JSON，无论退出原因都调用。"""
        if not self._trajectory:
            self.get_logger().warn('[TRAJ] 无轨迹数据, 跳过保存')
            return
        import json
        from datetime import datetime

        run_ts = datetime.now().strftime('%Y%m%d_%H%M%S')
        csv_path = f'/userdata/dev_ws/trajectory_{run_ts}.csv'
        json_path = f'/userdata/dev_ws/trajectory_{run_ts}_summary.json'

        # ── 写入 CSV ─────────────────────────────────────────
        try:
            with open(csv_path, 'w') as f:
                f.write('elapsed_s,x_m,y_m,yaw_rad,state,'
                        'cmd_vx,cmd_wz,'
                        'plan_pts,plan_len_m,plan_end_x,plan_end_y,'
                        'cpu_pct,mem_pct,cpu_temp_c\n')
                for row in self._trajectory:
                    elapsed, x, y, yaw, state, cvx, cwz, pn, pl, pex, pey, cpu, mem, cput = row
                    f.write(f'{elapsed:.3f},{x:.4f},{y:.4f},{yaw:.4f},{state},'
                            f'{cvx:.3f},{cwz:.3f},'
                            f'{pn},{pl:.3f},{pex:.3f},{pey:.3f},'
                            f'{cpu},{mem},{cput}\n')
            self.get_logger().info(
                f'[TRAJ] CSV已保存: {csv_path} ({len(self._trajectory)} 点)')
        except Exception as e:
            self.get_logger().error(f'[TRAJ] CSV保存失败: {e}')

        # ── 写入摘要 JSON ─────────────────────────────────────
        try:
            elapsed_total = 0.0
            if self._clock_start is not None:
                elapsed_total = self._get_current_raw_time() - self._clock_start

            # 收集各阶段耗时
            phase_order = ['LAUNCH', 'NAV_TO_QR', 'NAV_TO_ENTRY',
                           'BACKING_UP', 'CRUISE_CHANNEL', 'RETURN_P']
            phases = {}
            for ph in phase_order:
                if ph in self._phase_times:
                    phases[ph] = round(self._phase_times[ph], 2)

            # 最后已知位置
            last_pos = None
            if self._robot_pose:
                last_pos = {'x': round(self._robot_pose['x'], 4),
                            'y': round(self._robot_pose['y'], 4),
                            'yaw': round(self._robot_pose['yaw'], 4)}

            # 轨迹统计
            n_pts = len(self._trajectory)
            traj_stats = {}
            if n_pts > 0:
                xs = [r[1] for r in self._trajectory]
                ys = [r[2] for r in self._trajectory]
                dx = max(xs) - min(xs)
                dy = max(ys) - min(ys)
                # 按状态统计
                state_counts = {}
                for r in self._trajectory:
                    st = r[4]
                    state_counts[st] = state_counts.get(st, 0) + 1
                traj_stats = {
                    'n_points': n_pts,
                    'x_range': round(dx, 3),
                    'y_range': round(dy, 3),
                    'state_distribution': {s: c for s, c in
                                           sorted(state_counts.items(),
                                                  key=lambda x: -x[1])}
                }

            summary = {
                'run_ts': run_ts,
                'final_state': self.state,
                'exit_reason': getattr(self, '_exit_reason', 'unknown'),
                'elapsed_total_s': round(elapsed_total, 2),
                'phase_times_s': phases,
                'last_position': last_pos,
                'trajectory_stats': traj_stats,
                'qr_raw': self.qr_data,
                'qr_direction': self._qr_direction,
                'vlm_received': self._vlm_received,
                'vlm_result': self._vlm_result[:300] if self._vlm_result else None,
                'params': {
                    'total_timeout': self.total_timeout,
                    'backup_linear_x': self.backup_linear_x,
                    'backup_angular_z': self.backup_angular_z,
                    'nav2_config': self._get_nav2_params_snapshot(),
                }
            }
            with open(json_path, 'w') as f:
                json.dump(summary, f, indent=2, ensure_ascii=False)
            self.get_logger().info(
                f'[TRAJ] 摘要JSON已保存: {json_path}')
        except Exception as e:
            self.get_logger().error(f'[TRAJ] JSON保存失败: {e}')

        # ── 保存规划历史 CSV ──────────────────────────────────
        if self._plan_history:
            try:
                plans_path = csv_path.replace('.csv', '_plans.csv')
                with open(plans_path, 'w') as f:
                    f.write('elapsed_s,state,n_pts,len_m,start_x,start_y,end_x,end_y\n')
                    for p in self._plan_history:
                        f.write(f'{p[0]:.3f},{p[1]},{p[2]},{p[3]:.3f},{p[4]:.3f},{p[5]:.3f},{p[6]:.3f},{p[7]:.3f}\n')
                self.get_logger().info(
                    f'[TRAJ] 规划历史已保存: {plans_path} ({len(self._plan_history)} 次规划)')
            except Exception as e:
                self.get_logger().error(f'[TRAJ] 规划历史保存失败: {e}')

        # ── 保存 costmap PGM (障碍物可视化) ────────────────────
        if self._costmap_msg is not None:
            try:
                self._save_costmap_pgm(csv_path.replace('.csv', '_costmap.pgm'))
            except Exception as e:
                self.get_logger().error(f'[TRAJ] costmap PGM保存失败: {e}')

    def _save_costmap_pgm(self, path):
        """OccupancyGrid → PGM P5 (binary) 用于障碍物叠加可视化"""
        msg = self._costmap_msg
        w, h = msg.info.width, msg.info.height
        # OccupancyGrid: -1=unknown, 0=free, 100=occupied
        # PGM: 0=black(obstacle), 255=white(free), 127=unknown
        pgm_data = bytearray(w * h)
        for i, val in enumerate(msg.data):
            if val < 0:
                pgm_data[i] = 127  # unknown → gray
            elif val > 90:
                pgm_data[i] = 0    # lethal obstacle → black
            elif val > 50:
                pgm_data[i] = 60   # likely obstacle → dark gray
            else:
                pgm_data[i] = 255  # free → white (transparent in overlay)
        with open(path, 'wb') as f:
            f.write(f'P5\n{w} {h}\n255\n'.encode())
            f.write(pgm_data)
        self.get_logger().info(f'[TRAJ] costmap PGM已保存: {path}')

    # ═══════════════════════════════════════════════════════════════
    # ── NAV_TO_QR → NAV_TO_ENTRY 转换 (沿用 stage2 模式) ────────
    # ═══════════════════════════════════════════════════════════════

    def _transition_to_cruise(self):
        """BT cancel 后右后退摆正车头, 然后前进进入通道。

        阿克曼无法原地旋转, 必须先后退+转向让车头对准通道入口,
        再前进进入。这是标准三点调头的一部分。
        """
        self._pending_entry_nav = False
        if self._pending_entry_nav_timeout is not None:
            self._pending_entry_nav_timeout.cancel()
            self._pending_entry_nav_timeout = None
        if self._retry_timer is not None:
            self._retry_timer.cancel()
            self._retry_timer = None
        self._goal_handle = None
        self._state_transition('BACKING_UP')
        self.get_logger().info(">>> BT取消完成, 右后退摆正车头→前进进通道...")
        self._start_backup()

    def _entry_nav_on_cancel_timeout(self):
        """fallback: 如果超时未收到 STATUS_CANCELED, 直接发送第二个目标。

        可能原因: goal_handle 在 cancel 前已完成 (STATUS_SUCCEEDED), 或 BT 状态异常。
        """
        if not self._pending_entry_nav:
            return
        self.get_logger().warn(
            f"[超时] 等待 BT 取消确认超时 ({self.cancel_wait_timeout_sec}s), "
            f"直接发送通道入口目标 (fallback)"
        )
        self._transition_to_cruise()

    # ═══════════════════════════════════════════════════════════════
    # ── 后退序列 (沿用 stage2 模式) ─────────────────────────────
    # ═══════════════════════════════════════════════════════════════

    def _start_backup(self):
        """右后后退: 10Hz 持续发布, 防止 mux nav_timeout(0.5s) 超时断开。"""
        self._backup_twist = Twist()
        self._backup_twist.linear.x = self.backup_linear_x
        self._backup_twist.angular.z = self.backup_angular_z
        self.cmd_vel_pub.publish(self._backup_twist)
        # 100ms 定时器: 持续保活 mux nav 通道 (> 0.1s < 0.5s timeout)
        self._backup_keepalive = self.create_timer(0.1, self._backup_republish)
        self._backup_timer = self.create_timer(
            self.backup_duration_sec, self._backup_stop)
        self.get_logger().info(
            f"[BACKUP] 右后退中: vx={self.backup_linear_x:.2f} "
            f"wz={self.backup_angular_z:.2f}, "
            f"持续 {self.backup_duration_sec:.1f}s..."
        )

    def _backup_republish(self):
        """10Hz 保活: 重新发布后退指令, 防止 mux nav_timeout(0.5s) 超时"""
        if self._backup_twist is not None and self.state == 'BACKING_UP':
            self.cmd_vel_pub.publish(self._backup_twist)

    def _backup_stop(self):
        if self._backup_keepalive is not None:
            self._backup_keepalive.cancel()
            self._backup_keepalive = None
        """后退完成: 进入巡航, 使用 NavigateThroughPoses 穿全部路点"""
        if self._backup_timer is not None:
            self._backup_timer.cancel()
            self._backup_timer = None
        self.cmd_vel_pub.publish(Twist())

        self._state_transition('CRUISE_CHANNEL')
        self._start_cruise()

    def _disable_keepout_and_clear(self):
        """禁用 keepout (空 mask) + 清除双 costmap. 巡航/返航时允许穿过禁区."""
        disable_msg = CostmapFilterInfo()
        disable_msg.type = 0
        disable_msg.filter_mask_topic = "/keepout_disabled"  # 不存在的topic → filter订阅但无数据 → no-op
        disable_msg.base = 0.0
        disable_msg.multiplier = 1.0
        self.keepout_info_pub.publish(disable_msg)
        self.costmap_clear_pub.publish(Empty())
        self.local_costmap_clear_pub.publish(Empty())
        self.get_logger().info("[KEEPOUT] keepout disabled + costmaps cleared")

    def _cancel_keepout_republish(self):
        if hasattr(self, '_keepout_repub_timer') and self._keepout_repub_timer is not None:
            self._keepout_repub_timer.cancel()
            self._keepout_repub_timer = None

    def _start_keepout_republish(self):
        """每2秒重新发布keepout禁用, 防止BT恢复时costmap_filter_info_server覆盖."""
        if self.state in ('CRUISE_CHANNEL', 'RETURN_P'):
            disable_msg = CostmapFilterInfo()
            disable_msg.type = 0
            disable_msg.filter_mask_topic = "/keepout_disabled"
            disable_msg.base = 0.0
            disable_msg.multiplier = 1.0
            self.keepout_info_pub.publish(disable_msg)
        else:
            self._keepout_repub_timer.cancel()
            self._keepout_repub_timer = None

    def _start_cruise(self):
        """发送 NavigateThroughPoses: 通道入口(安全起点)→途经点→VLM停靠点"""
        # 通道入口作为第一个路点: 确保机器人先离开 keepout 边界再开始巡航
        entry_wp = [self.entry_point_x, self.entry_point_y, self.entry_point_yaw]
        wps = [entry_wp] + self._get_cruise_waypoints()

        if not self.through_client.wait_for_server(timeout_sec=3.0):
            self.get_logger().error("navigate_through_poses server 未就绪!")
            return

        goal = NavigateThroughPoses.Goal()
        for wp in wps:
            pose = PoseStamped()
            pose.header.frame_id = 'map'
            pose.header.stamp = self.get_clock().now().to_msg()
            pose.pose.position.x = wp[0]
            pose.pose.position.y = wp[1]
            pose.pose.orientation.z = math.sin(wp[2] / 2.0)
            pose.pose.orientation.w = math.cos(wp[2] / 2.0)
            goal.poses.append(pose)

        pts = ", ".join(f"({w[0]:.2f},{w[1]:.2f})" for w in wps)
        self.get_logger().info(f"[CRUISE] NavigateThroughPoses: {pts}")
        self._nav_start_time = self.get_clock().now()
        self._through_future = self.through_client.send_goal_async(goal)
        self._through_future.add_done_callback(self._through_response_cb)

    def _reenable_keepout(self):
        """恢复 keepout filter: 重新发布指向 /keepout_mask 的 CostmapFilterInfo"""
        enable_msg = CostmapFilterInfo()
        enable_msg.type = 0
        enable_msg.filter_mask_topic = "/keepout_mask"
        enable_msg.base = 0.0
        enable_msg.multiplier = 1.0      # 匹配 launch 文件配置
        self.get_logger().info("[KEEPOUT] 恢复 keepout filter (mask_topic=/keepout_mask)")
        self.keepout_info_pub.publish(enable_msg)
        if self._keepout_reenable_timer is not None:
            self._keepout_reenable_timer.cancel()
            self._keepout_reenable_timer = None

    def _through_response_cb(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().warn("NavigateThroughPoses 被拒绝, 3s后重试")
            if self._retry_timer is not None:
                self._retry_timer.cancel()
            if self.state == 'RETURN_P':
                self._retry_timer = self.create_timer(3.0, self._start_return)
            else:
                self._retry_timer = self.create_timer(3.0, lambda: self._start_cruise())
            return
        self.get_logger().info("NavigateThroughPoses 已接受, 巡航中...")
        self._through_result_future = goal_handle.get_result_async()
        self._through_result_future.add_done_callback(self._through_result_cb)

    def _through_result_cb(self, future):
        status = future.result().status
        if status == GoalStatus.STATUS_SUCCEEDED:
            self._nav_start_time = None
            if self.state == 'RETURN_P':
                self.get_logger().info("[结果回调] 返航完成, 已回到P点!")
                self._finish()
            else:
                self.get_logger().info("[结果回调] 巡航完成, 触发VLM推理...")
                self._trigger_vlm()
        else:
            self.get_logger().warn(f"NavigateThroughPoses 失败 status={status}")

    # ═══════════════════════════════════════════════════════════════
    # ── NavigateToPose (统一导航接口) ────────────────────────────
    # ═══════════════════════════════════════════════════════════════

    def send_nav_goal(self, x, y, yaw, description):
        """发送单个 NavigateToPose 导航目标"""
        # 生命周期检查: 确保 navigate_to_pose action server 可用
        if not self.nav_client.wait_for_server(timeout_sec=3.0):
            self.get_logger().warn(
                f"navigate_to_pose action server 未就绪 (3s 超时), "
                f"跳过导航目标 [{description}]. 3s 后重试."
            )
            if self._retry_timer is not None:
                self._retry_timer.cancel()
            self._retry_timer = self.create_timer(3.0, self._retry_nav)
            return

        goal_msg = NavigateToPose.Goal()
        goal_msg.pose.header.frame_id = 'map'
        goal_msg.pose.header.stamp = self.get_clock().now().to_msg()
        goal_msg.pose.pose.position.x = x
        goal_msg.pose.pose.position.y = y
        goal_msg.pose.pose.orientation.x = 0.0
        goal_msg.pose.pose.orientation.y = 0.0
        goal_msg.pose.pose.orientation.z = math.sin(yaw / 2.0)
        goal_msg.pose.pose.orientation.w = math.cos(yaw / 2.0)

        if self._robot_pose:
            dist = math.hypot(x - self._robot_pose['x'], y - self._robot_pose['y'])
            self.get_logger().info(
                f"[DIAG] nav目标距离: {dist:.2f}m, "
                f"robot=({self._robot_pose['x']:.2f},{self._robot_pose['y']:.2f}) → target=({x:.2f},{y:.2f})")
        self.get_logger().info(
            f">>> 发送导航目标 [{description}]: "
            f"({x:.2f}, {y:.2f}, yaw={yaw:.2f})"
        )
        self._nav_start_time = self.get_clock().now()   # 记录发送时间，启动段超时
        self._nav_goal_pos = (x, y)                     # 记录目标位置，用于 CSV 距离计算
        self._send_goal_future = self.nav_client.send_goal_async(goal_msg)
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        """NavigateToPose 目标响应回调"""
        goal_handle = future.result()
        if not goal_handle.accepted:
            if self.state in ('NAV_TO_QR', 'NAV_TO_ENTRY'):
                self.get_logger().warn("导航目标被拒绝, 3s 后重试...")
                if self._retry_timer is not None:
                    self._retry_timer.cancel()
                self._retry_timer = self.create_timer(3.0, self._retry_nav)
            return
        if self._retry_timer is not None:
            self._retry_timer.cancel()
            self._retry_timer = None
        self._goal_handle = goal_handle
        self.get_logger().info("导航目标已接受，车辆出发...")
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def _retry_nav(self):
        """重试当前状态的导航目标"""
        if self.state == 'NAV_TO_QR':
            self.get_logger().info("重试发送导航目标 (QR点)...")
            self.send_nav_goal(
                self.qr_point_x, self.qr_point_y,
                self.qr_point_yaw, "任务发布点"
            )
        elif self.state == 'NAV_TO_ENTRY':
            self.get_logger().info("重试发送导航目标 (通道入口)...")
            self.send_nav_goal(
                self.entry_point_x, self.entry_point_y,
                self.entry_point_yaw, "通道入口"
            )
        elif self.state == 'CRUISE_CHANNEL':
            self.get_logger().info("重试 NavigateThroughPoses...")
            self._start_cruise()
        elif self.state == 'RETURN_P':
            self.get_logger().info("重试返航 (P点)...")
            self.send_nav_goal(
                self.p_point_x, self.p_point_y,
                self.p_point_yaw, "P点返航"
            )

    def get_result_callback(self, future):
        """NavigateToPose 结果回调"""
        status = future.result().status
        if status == GoalStatus.STATUS_SUCCEEDED:
            self._nav_start_time = None
            if self.state == 'NAV_TO_QR':
                if self._pending_entry_nav:
                    # QR 已检测, 但 goal 在 cancel 前已成功完成 (race)
                    self.get_logger().info(
                        "[结果回调] QR导航目标在cancel前已完成, 直接过渡到通道入口"
                    )
                    self._transition_to_cruise()
                else:
                    self.get_logger().warn(
                        "[结果回调] 已到达任务发布点，但全程未检测到 QR 码！"
                    )
                    # 使用回退方向, 继续流程
                    if not self._qr_event_received:
                        self._qr_direction = self.default_qr_direction
                        self._qr_event_received = True
                        self.get_logger().warn(
                            f"[结果回调] 使用回退QR方向: {self._qr_direction}"
                        )
                    # 直接发送通道入口目标 (无需备份, 因为是从QR点正常导航过来的)
                    self._state_transition('NAV_TO_ENTRY')
                    self.send_nav_goal(
                        self.entry_point_x, self.entry_point_y,
                        self.entry_point_yaw, "通道入口"
                    )
            elif self.state == 'NAV_TO_ENTRY':
                self.get_logger().info(
                    "[结果回调] 已到达通道入口, 准备通道巡航..."
                )
                self._start_cruise()
            elif self.state == 'CRUISE_CHANNEL':
                self.get_logger().info(
                    "[结果回调] 已到达VLM路点 (人形立牌), 触发VLM推理..."
                )
                self._trigger_vlm()
            elif self.state == 'RETURN_P':
                self.get_logger().info("[结果回调] 已回到P点, 任务完成!")
                self._finish()
        elif status == GoalStatus.STATUS_CANCELED:
            self._nav_start_time = None
            if self._pending_entry_nav:
                # ★ BT 已确认 cancel/halt 完成, 安全发送第二个目标
                self.get_logger().info(
                    "[结果回调] BT取消确认完成 (STATUS_CANCELED), "
                    "准备发送通道入口目标..."
                )
                self._transition_to_cruise()
            else:
                self.get_logger().info(
                    "[结果回调] 导航任务已取消 (QR 拦截成功)"
                )
        else:
            self._nav_start_time = None
            self.get_logger().error(
                f"[结果回调] 导航异常结束, status={status}"
            )

    # ═══════════════════════════════════════════════════════════════
    # ── VLM 触发 ─────────────────────────────────────────────────
    # ═══════════════════════════════════════════════════════════════

    def _trigger_vlm(self):
        """VLM路点拍照, 后台推理, 结果在P点显示."""
        if self._vlm_triggered:
            return  # 防重入: 巡航结果回调可能多次触发
        self._vlm_triggered = True
        self.get_logger().info("[VLM] 发布 sign4return=100, 拍照推理中...")
        self.sign4return_pub.publish(Int32(data=100))
        self._start_return()

    def _on_return_delay(self):
        """返航延迟回调: NavigateToPose 直接回P点."""
        if self._return_sent:
            return
        self._return_sent = True
        if self._return_delay_timer is not None:
            self._return_delay_timer.cancel()
            self._return_delay_timer = None
        approach_yaw = self._robot_pose['yaw'] if self._robot_pose else self.p_point_yaw
        self.send_nav_goal(self.p_point_x, self.p_point_y,
                           approach_yaw, "P点返航")

    def _start_return(self):
        """从 VLM 路点 NavigateThroughPoses 经通道入口回 P 点.
        复用通道入口 (entry_point) 作为中间路点: 进得来就出得去."""
        self._state_transition('RETURN_P')

        if not self.through_client.wait_for_server(timeout_sec=3.0):
            self.get_logger().error("navigate_through_poses server 未就绪!")
            return

        # 构造路点: VLM→第3环路点→P点
        goal = NavigateThroughPoses.Goal()
        for (wx, wy, wyaw) in [
            (1.07, -0.73, 0.0),                                    # 第3环路点
            (self.p_point_x, self.p_point_y, self.p_point_yaw),
        ]:
            pose = PoseStamped()
            pose.header.frame_id = 'map'
            pose.header.stamp = self.get_clock().now().to_msg()
            pose.pose.position.x = wx
            pose.pose.position.y = wy
            pose.pose.orientation.z = math.sin(wyaw / 2.0)
            pose.pose.orientation.w = math.cos(wyaw / 2.0)
            goal.poses.append(pose)

        self.get_logger().info(
            f"[RETURN] NavigateThroughPoses: 通道入口→P点 "
            f"({self.entry_point_x:.2f},{self.entry_point_y:.2f})→"
            f"({self.p_point_x:.2f},{self.p_point_y:.2f})")
        self._nav_start_time = self.get_clock().now()
        self._through_future = self.through_client.send_goal_async(goal)
        self._through_future.add_done_callback(self._through_response_cb)

    # ═══════════════════════════════════════════════════════════════
    # ── 超时检查 ─────────────────────────────────────────────────
    # ═══════════════════════════════════════════════════════════════

    def _check_timeouts(self):
        """1Hz 定时器: 同时检查段超时和全局超时"""
        # ── 全局超时检查 ──────────────────────────────────────
        if self._clock_start is not None:
            elapsed_total = self._get_current_raw_time() - self._clock_start
            if elapsed_total > self.total_timeout and not self._timeout_handled:
                self._timeout_handled = True
                self.get_logger().error(
                    f">>> [TIMEOUT] 全局超时! 已运行 {elapsed_total:.1f}s "
                    f"> {self.total_timeout}s, 当前状态={self.state}"
                )
                self._timeout_shutdown()
                return

        # ── 段超时检查 ────────────────────────────────────────
        if self._nav_start_time is None:
            return

        elapsed = (self.get_clock().now() - self._nav_start_time).nanoseconds / 1e9

        if self.state == 'NAV_TO_QR':
            if elapsed > self.nav_to_qr_timeout:
                self.get_logger().error(
                    f">>> [TIMEOUT] NAV_TO_QR 段超时! "
                    f"{elapsed:.1f}s > {self.nav_to_qr_timeout}s"
                )
                self._handle_segment_timeout('NAV_TO_QR')
        elif self.state == 'NAV_TO_ENTRY':
            if elapsed > self.nav_to_entry_timeout:
                self.get_logger().error(
                    f">>> [TIMEOUT] NAV_TO_ENTRY 段超时! "
                    f"{elapsed:.1f}s > {self.nav_to_entry_timeout}s"
                )
                self._handle_segment_timeout('NAV_TO_ENTRY')
        elif self.state == 'CRUISE_CHANNEL':
            if elapsed > self.cruise_timeout:
                self.get_logger().error(
                    f">>> [TIMEOUT] CRUISE_CHANNEL 段超时! "
                    f"{elapsed:.1f}s > {self.cruise_timeout}s"
                )
                self._handle_segment_timeout('CRUISE_CHANNEL')
        elif self.state == 'RETURN_P':
            if elapsed > self.return_timeout:
                self.get_logger().error(
                    f">>> [TIMEOUT] RETURN_P 段超时! "
                    f"{elapsed:.1f}s > {self.return_timeout}s"
                )
                self._handle_segment_timeout('RETURN_P')

    def _handle_segment_timeout(self, state):
        """处理段超时: 取消当前目标, 根据状态决定下一步"""
        self._nav_start_time = None

        # 取消当前活动的目标 (统一使用 NavigateToPose action client)
        if self._goal_handle is not None:
            self._goal_handle.cancel_goal_async()
            self._goal_handle = None

        self.send_stop()

        # 根据段超时决定下一步
        if state == 'NAV_TO_QR':
            # QR 段超时: 使用回退方向, 直接尝试进入通道入口
            if not self._qr_event_received:
                self._qr_direction = self.default_qr_direction
                self._qr_event_received = True
                self._pending_entry_nav = False
                if self._pending_entry_nav_timeout is not None:
                    self._pending_entry_nav_timeout.cancel()
                    self._pending_entry_nav_timeout = None
                self.get_logger().warn(
                    f"[TIMEOUT] NAV_TO_QR 超时, 使用回退方向: {self._qr_direction}"
                )
            self._state_transition('BACKING_UP')
            self._start_backup()
        elif state == 'NAV_TO_ENTRY':
            # 入口段超时: 仍然尝试巡航
            self.get_logger().warn(
                "[TIMEOUT] NAV_TO_ENTRY 超时, 尝试直接进入巡航..."
            )
            self._start_cruise()
        elif state == 'CRUISE_CHANNEL':
            # 巡航段超时: 仍然尝试触发 VLM
            self.get_logger().warn(
                "[TIMEOUT] CRUISE_CHANNEL 超时, 尝试触发 VLM..."
            )
            self._trigger_vlm()
        elif state == 'RETURN_P':
            # 返航段超时: 视为失败, 但保存轨迹
            self.get_logger().error(
                "[TIMEOUT] RETURN_P 超时, 任务终止!"
            )
            self._exit_reason = 'return_timeout'
            self._state_transition('TIMEOUT')
            self._log_summary()
            self._save_trajectory()

    def _timeout_shutdown(self):
        """全局超时处理"""
        self._exit_reason = 'total_timeout'
        self._stop_bag_record()
        if self._goal_handle is not None:
            self._goal_handle.cancel_goal_async()
            self._goal_handle = None
        self.send_stop()
        self._stop_keepalive = self.create_timer(0.1, lambda: self.cmd_vel_pub.publish(Twist()))
        self._state_transition('TIMEOUT')
        self._log_summary()
        self._save_trajectory()

    # ═══════════════════════════════════════════════════════════════
    # ── 启动 & 完成 ──────────────────────────────────────────────
    # ═══════════════════════════════════════════════════════════════

    def _start_nav(self):
        """延迟启动: 等待 BT 激活后开始第一阶段导航"""
        if self.state != 'INIT':
            return
        launch_dur = self._get_current_raw_time() - self._launch_time.nanoseconds / 1e9
        self._phase_times['LAUNCH'] = launch_dur
        self.get_logger().info(f"[LAUNCH] 发车阶段: {launch_dur:.1f}s")
        self.get_logger().info(">>> 系统就绪, 开始 Stage 3 导航")
        self._start_bag_record()          # ★ 开始录制 rosbag
        self._clock_start = self._get_current_raw_time()
        self._state_transition('NAV_TO_QR')
        self.send_nav_goal(
            self.qr_point_x, self.qr_point_y,
            self.qr_point_yaw, "任务发布点"
        )

    def _finish(self):
        """任务完成: 停车, 打印VLM结果, 保存轨迹"""
        self._exit_reason = 'done'
        self._stop_bag_record()
        self.send_stop()
        self._stop_keepalive = self.create_timer(0.1, lambda: self.cmd_vel_pub.publish(Twist()))
        self._state_transition('DONE')
        self._log_summary()
        self._save_trajectory()

    def _log_summary(self):
        """打印任务摘要"""
        elapsed = 0.0
        if self._clock_start is not None:
            elapsed = self._get_current_raw_time() - self._clock_start
        self.get_logger().info("")
        self.get_logger().info("=" * 60)
        self.get_logger().info(f">>> [Stage 3] 任务结束 <<<")
        self.get_logger().info(f"  最终状态: {self.state}")
        self.get_logger().info(f"  总耗时:   {elapsed:.1f}s")
        # 各阶段耗时
        phase_order = ['LAUNCH', 'NAV_TO_QR', 'NAV_TO_ENTRY', 'BACKING_UP',
                       'CRUISE_CHANNEL', 'RETURN_P']
        self.get_logger().info(f"  --- 各阶段耗时 ---")
        total_phases = 0.0
        for ph in phase_order:
            if ph in self._phase_times:
                t = self._phase_times[ph]; total_phases += t
                self.get_logger().info(f"  {ph:.<22s} {t:.1f}s")
        for ph, t in sorted(self._phase_times.items()):
            if ph not in phase_order:
                total_phases += t
                self.get_logger().info(f"  {ph:.<22s} {t:.1f}s")
        other = elapsed - total_phases
        if abs(other) > 0.5:
            self.get_logger().info(f"  {'(transition/overhead)':.<22s} {other:.1f}s")
        self.get_logger().info(f"  --- ---")
        self.get_logger().info(f"  QR 原始数据: {self.qr_data}")
        if self._qr_direction:
            self.get_logger().info(
                f"  QR 方向:   {self._qr_direction} "
                f"(CW=顺时针/odd, CCW=逆时针/even)"
            )
        else:
            self.get_logger().warn("  QR 方向:   未获取")
        if self._vlm_received:
            self.get_logger().info(
                f"  VLM 结果:  {self._vlm_result[:200] if self._vlm_result else 'N/A'}"
            )
        else:
            self.get_logger().warn("  VLM 结果:  未收到")
        self.get_logger().info(
            f"  超时限制:  {self.total_timeout}s (全局)"
        )
        self.get_logger().info("=" * 60)

    def run(self):
        """主入口: 轮询 Nav2 action server, 就绪后立即发车 (0s 延迟方案)"""
        self._start_timer = self.create_timer(
            self.start_delay_sec, self._poll_then_start)
        rclpy.spin(self)

    def _poll_then_start(self):
        """轮询 Nav2 action server, 就绪后调用 _start_nav"""
        if self.state != 'INIT':
            return
        if not self.nav_client.wait_for_server(timeout_sec=0.3):
            self._start_timer = self.create_timer(0.5, self._poll_then_start)
            return
        self._start_nav()


def main(args=None):
    rclpy.init(args=args)
    node = CompetitionMasterStage3()
    try:
        node.run()
    except KeyboardInterrupt:
        node.get_logger().info('[MAIN] 收到 Ctrl+C, 停止录制 + 保存轨迹...')
        node._stop_bag_record()
        node._exit_reason = 'keyboard_interrupt'
        node._log_summary()
    except Exception as e:
        node.get_logger().error(f'[MAIN] 异常退出: {e}')
        node._exit_reason = f'exception:{e}'
    finally:
        # ★ 无论何种退出, 停止录制 + 保存全程 CSV
        try:
            node._stop_bag_record()
        except Exception:
            pass
        try:
            node._save_trajectory()
        except Exception as e:
            node.get_logger().error(f'[MAIN] 最终保存失败: {e}')
        try:
            node.destroy_node()
        except Exception:
            pass
        try:
            rclpy.shutdown()
        except RuntimeError:
            pass


if __name__ == '__main__':
    main()
