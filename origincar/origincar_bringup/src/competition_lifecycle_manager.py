#!/usr/bin/env python3
"""
competition_lifecycle_manager — 竞赛模式管理节点
参考 amphibious_analysis.md §2.4: Lifecycle 手动管理 → 竞赛模式切换

接收 task_manager 模式指令, 动态切换 Nav2 costmap 参数 + 速度配置 + 感知激活。
紧急情况可重置整个 Nav2 导航栈 (deactivate→cleanup→configure→activate).
"""

import math
import time
import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from lifecycle_msgs.srv import ChangeState, GetState
from lifecycle_msgs.msg import Transition
from rcl_interfaces.srv import SetParameters
from rcl_interfaces.msg import Parameter as ParamMsg, ParameterValue


# Nav2 受管节点列表 (用于 emergency 栈重置)
NAV2_LIFECYCLE_NODES = [
    'controller_server',
    'planner_server',
    'bt_navigator',
    'recoveries_server',
    'global_costmap/global_costmap',
    'local_costmap/local_costmap',
    'velocity_smoother',
    'smoother_server',
    'waypoint_follower',
]

# costmap 可动态调参的节点
COSTMAP_NODES = [
    'global_costmap/global_costmap',
    'local_costmap/local_costmap',
]

# ── 模式→costmap 参数映射 (§2.4) ──
MODE_COSTMAP_PARAMS = {
    # 模式名: { inflation_radius, cost_scaling_dist, cost_scaling_gain, obstacle_range }
    'task1': {'inflation_radius': 0.18, 'cost_scaling_dist': 0.18, 'cost_scaling_gain': 1.5,
              'obstacle_range': 5.0},
    'task2': {'inflation_radius': 0.12, 'cost_scaling_dist': 0.12, 'cost_scaling_gain': 2.0,
              'obstacle_range': 1.5},
    'task3': {'inflation_radius': 0.18, 'cost_scaling_dist': 0.18, 'cost_scaling_gain': 1.5,
              'obstacle_range': 5.0},
}

# ── 模式→速度参数映射 ──
MODE_SPEED_PARAMS = {
    'task1': {'desired_linear_vel': 0.70, 'max_linear_vel': 0.80},
    'task2': {'desired_linear_vel': 0.40, 'max_linear_vel': 0.50},
    'task3': {'desired_linear_vel': 0.70, 'max_linear_vel': 0.80},
}


class CompetitionLifecycleManager(Node):
    def __init__(self):
        super().__init__('competition_lifecycle_manager')

        self.declare_parameter('task1_activate_vlm', False)
        self.declare_parameter('task2_activate_vlm', True)
        self.declare_parameter('task3_activate_vlm', False)
        self.declare_parameter('verify_position', True)
        self.declare_parameter('position_tolerance', 1.0)
        self.declare_parameter('task1_expected_x', 1.5)
        self.declare_parameter('task1_expected_y', 0.0)
        self.declare_parameter('task2_expected_x', 2.0)
        self.declare_parameter('task2_expected_y', 0.0)
        self.declare_parameter('task3_expected_x', 0.0)
        self.declare_parameter('task3_expected_y', 0.0)

        self._current_mode = 'idle'
        self._mode_lock = False
        self._odom_x = 0.0
        self._odom_y = 0.0

        # ── 订阅 ──────────────────────────────────────────
        self._mode_sub = self.create_subscription(
            String, '/competition_mode', self._on_mode_cmd, 10)
        self._odom_sub = self.create_subscription(
            Odometry, '/odom', self._odom_callback, 10)

        # ── 发布 ──────────────────────────────────────────
        self._mode_active_pub = self.create_publisher(
            String, '/competition_mode_active', 10)

        # ── 客户端缓存 (lazy init) ────────────────────────
        self._lifecycle_clients = {}
        self._param_clients = {}

        self.get_logger().info("CompetitionLifecycleManager 就绪: /competition_mode")

    # ═══════════════════════════════════════════════════════════
    # 回调
    # ═══════════════════════════════════════════════════════════

    def _odom_callback(self, msg):
        self._odom_x = msg.pose.pose.position.x
        self._odom_y = msg.pose.pose.position.y

    def _on_mode_cmd(self, msg):
        mode = msg.data.strip()
        if not mode or mode == self._current_mode:
            return
        if self._mode_lock:
            self.get_logger().warn(f"模式切换进行中, 忽略: {mode}")
            return

        self.get_logger().info(f"收到模式切换指令: {self._current_mode} → {mode}")

        if mode == 'emergency':
            self._handle_emergency()
            return

        if mode in MODE_COSTMAP_PARAMS:
            self._apply_mode(mode)
        else:
            self.get_logger().error(f"未知模式: {mode}")

    # ═══════════════════════════════════════════════════════════
    # 模式应用
    # ═══════════════════════════════════════════════════════════

    def _apply_mode(self, mode):
        self._mode_lock = True
        self.get_logger().info(
            f"应用模式 {mode} @ 位置 (x={self._odom_x:.2f}, y={self._odom_y:.2f})")

        if self.get_parameter('verify_position').value:
            self._verify_mode_position(mode)

        # 1. 切换 costmap 参数
        if mode in MODE_COSTMAP_PARAMS:
            self._reconfigure_costmaps(MODE_COSTMAP_PARAMS[mode])

        # 2. 切换速度参数
        if mode in MODE_SPEED_PARAMS:
            self._reconfigure_controller(MODE_SPEED_PARAMS[mode])

        # 3. VLM 激活已移至 task_manager→mission_controller 编排链路
        # competition_lifecycle_mgr 仅负责 Nav2 参数, 不直接发控制信号

        self._current_mode = mode
        self._publish_mode_active(mode)
        self._mode_lock = False
        self.get_logger().info(f"模式切换完成: {mode}")

    # ── 位置验证 (§§ 控制调度: 模式切换前检查位置) ──────

    def _verify_mode_position(self, mode):
        expected_x = self.get_parameter(f'{mode}_expected_x').value
        expected_y = self.get_parameter(f'{mode}_expected_y').value
        tolerance = self.get_parameter('position_tolerance').value
        dx = self._odom_x - expected_x
        dy = self._odom_y - expected_y
        dist = math.sqrt(dx * dx + dy * dy)
        if dist > tolerance:
            self.get_logger().warn(
                f"模式 {mode} 位置偏差较大: 当前({self._odom_x:.2f},{self._odom_y:.2f}) "
                f"期望({expected_x:.2f},{expected_y:.2f}) 偏差{dist:.2f}m > {tolerance:.1f}m",
                throttle_duration_sec=5.0)
        else:
            self.get_logger().info(
                f"模式 {mode} 位置验证通过 (偏差{dist:.2f}m ≤ {tolerance:.1f}m)")

    # ── costmap 参数重配置 ────────────────────────────────

    def _reconfigure_costmaps(self, params_dict):
        for node_name in COSTMAP_NODES:
            param_list = []
            for key, value in params_dict.items():
                pv = ParamValue()
                pv.type = Parameter.Type.DOUBLE.value
                pv.double_value = float(value)
                param_list.append(ParamMsg(name=key, value=pv))

            ok = self._set_node_params(node_name, param_list)
            if ok:
                self.get_logger().info(
                    f"  costmap [{node_name}]: {params_dict}")
            else:
                self.get_logger().error(
                    f"  costmap [{node_name}]: 参数设置失败")

    # ── controller 参数重配置 ─────────────────────────────

    def _reconfigure_controller(self, params_dict):
        param_list = []
        for key, value in params_dict.items():
            pv = ParamValue()
            pv.type = Parameter.Type.DOUBLE.value
            pv.double_value = float(value)
            param_list.append(ParamMsg(name=key, value=pv))

        self._set_node_params('controller_server', param_list)
        self.get_logger().info(f"  controller_server: {params_dict}")

    # ═══════════════════════════════════════════════════════════
    # §2.4: emergency → Nav2 栈完全重置
    # deactivate(4) → cleanup(5) → configure(1) → activate(3)
    # ═══════════════════════════════════════════════════════════

    def _handle_emergency(self):
        self._mode_lock = True
        self.get_logger().error("EMERGENCY: 开始 Nav2 栈重置...")

        TRANSITION_DEACTIVATE = Transition(label='deactivate', id=4)
        TRANSITION_CLEANUP = Transition(label='cleanup', id=5)
        TRANSITION_CONFIGURE = Transition(label='configure', id=1)
        TRANSITION_ACTIVATE = Transition(label='activate', id=3)

        # 依次对每个受管节点执行: deactivate → cleanup → configure → activate
        for node_name in NAV2_LIFECYCLE_NODES:
            ok = True
            for tr in [TRANSITION_DEACTIVATE, TRANSITION_CLEANUP,
                       TRANSITION_CONFIGURE, TRANSITION_ACTIVATE]:
                ok = self._transition_node(node_name, tr)
                if not ok:
                    self.get_logger().warn(
                        f"  [{node_name}] {tr.label} 失败, 跳过后续步骤")
                    break
                time.sleep(0.15)  # Nav2 需要时间完成状态转换

        if ok:
            self.get_logger().info("EMERGENCY: Nav2 栈重置完成")
        else:
            self.get_logger().error("EMERGENCY: Nav2 栈重置部分失败")

        self._current_mode = 'emergency_recovered'
        self._publish_mode_active(self._current_mode)
        self._mode_lock = False

    # ═══════════════════════════════════════════════════════════
    # 底层: lifecycle 状态转换
    # ═══════════════════════════════════════════════════════════

    def _get_lifecycle_client(self, node_name):
        if node_name not in self._lifecycle_clients:
            client = self.create_client(
                ChangeState, f'/{node_name}/change_state')
            self._lifecycle_clients[node_name] = client
        return self._lifecycle_clients[node_name]

    def _transition_node(self, node_name, transition):
        client = self._get_lifecycle_client(node_name)
        if not client.wait_for_service(timeout_sec=2.0):
            self.get_logger().warn(
                f"  [{node_name}] change_state 服务未就绪")
            return False

        req = ChangeState.Request()
        req.transition = transition
        future = client.call_async(req)

        # 同步等待 (异步请求 + spin, 不阻塞全局)
        start = time.time()
        while not future.done():
            rclpy.spin_once(self, timeout_sec=0.05)
            if time.time() - start > 5.0:
                self.get_logger().error(
                    f"  [{node_name}] {transition.label} 超时")
                return False

        if future.result() is not None and future.result().success:
            return True
        self.get_logger().warn(
            f"  [{node_name}] {transition.label} 失败")
        return False

    # ═══════════════════════════════════════════════════════════
    # 底层: 动态参数设置
    # ═══════════════════════════════════════════════════════════

    def _get_param_client(self, node_name):
        if node_name not in self._param_clients:
            client = self.create_client(
                SetParameters, f'/{node_name}/set_parameters')
            self._param_clients[node_name] = client
        return self._param_clients[node_name]

    def _set_node_params(self, node_name, param_list):
        client = self._get_param_client(node_name)
        if not client.wait_for_service(timeout_sec=2.0):
            self.get_logger().warn(
                f"  [{node_name}] set_parameters 服务未就绪")
            return False

        req = SetParameters.Request()
        req.parameters = param_list
        future = client.call_async(req)

        start = time.time()
        while not future.done():
            rclpy.spin_once(self, timeout_sec=0.05)
            if time.time() - start > 3.0:
                self.get_logger().error(f"  [{node_name}] 参数设置超时")
                return False

        if future.result() is not None:
            for res in future.result().results:
                if not res.successful:
                    self.get_logger().warn(
                        f"  [{node_name}] 参数被拒绝: {res.reason}")
                    return False
            return True
        return False

    # ═══════════════════════════════════════════════════════════

    def _publish_mode_active(self, mode):
        msg = String()
        msg.data = mode
        self._mode_active_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = CompetitionLifecycleManager()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
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
