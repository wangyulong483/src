#!/usr/bin/env python3
"""
竞赛场地一键标定 — 全自动, 无需手动操作

Phase 1: P 点定位 (Cartographer 纯定位, 120s)
Phase 2: 锥桶分析 (LiDAR 聚类 + 深度相机精测宽/高, 15s)

输出: maps/p_point.yaml  config/cone_params.yaml
"""
import math, yaml, numpy as np
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, DurabilityPolicy
import tf2_ros
from sensor_msgs.msg import LaserScan, PointCloud2
from sensor_msgs_py import point_cloud2
from nav_msgs.msg import OccupancyGrid

PHASE1_SEC = 120
PHASE2_SEC = 15
CONE_LIDAR_RANGE, CONE_CLUSTER_DIST, CONE_MIN_POINTS = 3.0, 0.06, 8


class FieldCalibrator(Node):
    def __init__(self):
        super().__init__('field_calibrator')

        self._tf_buffer = tf2_ros.Buffer()
        self._tf_listener = tf2_ros.TransformListener(self._tf_buffer, self)

        self._scan_buf, self._pc_buf = [], []
        self._scan_sub = self.create_subscription(LaserScan, '/scan', self._scan_cb, 10)
        self._pc_sub = self.create_subscription(PointCloud2, '/aurora/points2', self._pc_cb, 10)
        latched = QoSProfile(depth=1, durability=DurabilityPolicy.TRANSIENT_LOCAL)
        self._map_sub = self.create_subscription(OccupancyGrid, '/map', self._map_cb, latched)
        self._map_data = None

        self._phase = 1
        self._samples, self._start_time = [], self.get_clock().now()

        self.get_logger().info("=" * 70)
        self.get_logger().info(f"  全自动标定 — {PHASE1_SEC}s P点 → {PHASE2_SEC}s 锥桶 → 退出")
        self.get_logger().info("=" * 70)
        self._timer = self.create_timer(0.1, self._tick)

    # ══════════════════════ Phase 1 ══════════════════════

    def _tick(self):
        if self._phase != 1: return
        elapsed = (self.get_clock().now() - self._start_time).nanoseconds / 1e9
        try:
            tf = self._tf_buffer.lookup_transform('map', 'base_footprint', rclpy.time.Time())
        except Exception:
            return
        x, y = tf.transform.translation.x, tf.transform.translation.y
        q = tf.transform.rotation
        siny, cosy = 2.0*(q.w*q.z+q.x*q.y), 1.0-2.0*(q.y*q.y+q.z*q.z)
        yaw = math.atan2(siny, cosy)
        self._samples.append({'x': x, 'y': y, 'yaw': yaw})
        n = len(self._samples)

        if n % 50 == 0 and n > 0:
            xs = [s['x'] for s in self._samples]; ys = [s['y'] for s in self._samples]
            yaws_ = [s['yaw'] for s in self._samples]
            myaw = math.atan2(sum(math.sin(y) for y in yaws_), sum(math.cos(y) for y in yaws_))
            self.get_logger().info(
                f"  [{n:4d}帧 {elapsed:3.0f}s] "
                f"x={float(np.mean(xs)):.4f}±{float(np.std(xs))*1000:.1f}mm  "
                f"y={float(np.mean(ys)):.4f}±{float(np.std(ys))*1000:.1f}mm  "
                f"yaw={float(myaw)*180/math.pi:.1f}±{float(np.std(yaws_))*180/math.pi:.1f}°")

        if elapsed > PHASE1_SEC:
            self._timer.cancel()
            self._finish_p1()

    def _scan_cb(self, msg): self._scan_buf.append(msg)
    def _pc_cb(self, msg):   self._pc_buf.append(msg)
    def _map_cb(self, msg):  self._map_data = msg

    # ══════════════════════ Phase 1 结果 ══════════════════════

    def _finish_p1(self):
        if not self._samples: return
        xs = [s['x'] for s in self._samples]; ys = [s['y'] for s in self._samples]
        yaws_ = [s['yaw'] for s in self._samples]
        x_m = float(np.mean(xs)); y_m = float(np.mean(ys))
        yaw_m = float(math.atan2(sum(math.sin(y) for y in yaws_), sum(math.cos(y) for y in yaws_)))
        self._px, self._py, self._pyaw = x_m, y_m, yaw_m
        ir = self._calc_inflation()
        ck = self._check_map(x_m, y_m)

        self.get_logger().info("\n" + "=" * 70)
        self.get_logger().info(f"  ★ P 点 ({len(self._samples)} 帧)")
        self.get_logger().info(f"    x={x_m:.4f}  y={y_m:.4f}  yaw={yaw_m:.4f}({yaw_m*180/math.pi:.1f}°)")
        self.get_logger().info(f"    σ_x={float(np.std(xs))*1000:.1f}mm  σ_y={float(np.std(ys))*1000:.1f}mm  σ_yaw={float(np.std(yaws_))*180/math.pi:.1f}°")
        self.get_logger().info(f"    inflation: {ir:.3f}m  |  map P点: {'FREE' if ck else 'WARN'}")
        self.get_logger().info("=" * 70)

        with open('/userdata/dev_ws/src/originbot_navigation/maps/p_point.yaml', 'w') as f:
            yaml.dump({
                'p_point': {'x': round(x_m,4), 'y': round(y_m,4), 'yaw': round(yaw_m,4)},
                'precision': {'std_x_mm': round(float(np.std(xs))*1000,1),
                              'std_y_mm': round(float(np.std(ys))*1000,1),
                              'std_yaw_deg': round(float(np.std(yaws_))*180/math.pi,2),
                              'samples': len(self._samples)},
                'inflation_radius_m': round(float(ir),3),
                'map_p_point_free': bool(ck),
            }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

        # → Phase 2
        self._phase = 2
        self._scan_buf.clear(); self._pc_buf.clear()
        self._p2_start = self.get_clock().now()
        self.get_logger().info(f"\n>>> Phase 2: 锥桶采集 ({PHASE2_SEC}s)...")
        self._timer = self.create_timer(0.3, self._p2_tick)

    # ══════════════════════ Phase 2 ══════════════════════

    def _p2_tick(self):
        elapsed = (self.get_clock().now() - self._p2_start).nanoseconds / 1e9
        if elapsed % 3 < 0.5:
            self.get_logger().info(f"  {elapsed:.0f}s  LiDAR:{len(self._scan_buf)}  PC2:{len(self._pc_buf)}")
        if elapsed > PHASE2_SEC:
            self._timer.cancel()
            self._analyze_cones()

    def _analyze_cones(self):
        clusters = self._cluster_scans()
        if not clusters:
            self.get_logger().warn("  未检测到锥桶 — 使用默认参数")
            self._print_result({}, {})
            return

        pc_ws, pc_hs, dists = [], [], []
        for i, cl in enumerate(clusters):
            cx, cy, lw = cl['center'][0], cl['center'][1], cl['width']
            dw, dh = self._measure_cone_pc(cx, cy)
            self.get_logger().info(f"  锥桶 #{i+1}: {math.hypot(cx,cy):.2f}m  LiDAR{lw*100:.0f}cm  深度{dw*100:.0f}cm  H{dh*100:.0f}cm")
            dists.append(math.hypot(cx, cy))
            if dw > 0.05: pc_ws.append(dw)
            if dh > 0: pc_hs.append(dh)

        widths = [c['width'] for c in clusters]
        max_w = max(widths)
        eff_w = max(max_w, max(pc_ws)) if pc_ws else max_w

        params = {
            'inflation_radius_m':    round(float(eff_w/2 + 0.05), 3),
            'cost_scaling_gain':     round(float(1.5 + eff_w*3), 1),
            'observation_persistence_s': 0.7,
            'min_obstacle_height_m': max(0.03, round(float(min(pc_hs))*0.3, 2)) if pc_hs else 0.05,
            'max_obstacle_height_m': round(float(max(pc_hs))*1.5, 2) if pc_hs else 0.50,
            'obstacle_range_m':      round(float(max(dists))*1.3, 1),
            'raytrace_range_m':      round(float(max(dists))*1.3 + 0.5, 1),
        }
        dpc = max(pc_ws)*100 if pc_ws else 0
        self.get_logger().info(f"\n  有效锥宽: {eff_w*100:.1f}cm (LiDAR {max_w*100:.1f} / 深度 {dpc:.1f})")
        self._print_result(params, {
            'num_cones': len(clusters),
            'lidar_width_cm': [round(float(w)*100,1) for w in widths],
            'depth_width_cm': [round(float(w)*100,1) for w in pc_ws],
            'depth_height_cm': [round(float(h)*100,0) for h in pc_hs],
            'effective_width_cm': round(float(eff_w)*100,1),
            'distances_m': [round(float(d),2) for d in dists],
        })

    # ══════════════════════ LiDAR 聚类 ══════════════════════

    def _cluster_scans(self):
        frames = self._scan_buf[-30:] if len(self._scan_buf) >= 30 else self._scan_buf
        pts = []
        for scan in frames:
            for i, r in enumerate(scan.ranges):
                if not (0.2 < r < CONE_LIDAR_RANGE): continue
                angle = scan.angle_min + i*scan.angle_increment
                if abs(angle) > math.radians(60): continue
                pts.append((r*math.cos(angle), r*math.sin(angle)))
        if not pts: return []
        pts_s = sorted(pts, key=lambda p: p[0])
        clusters, used = [], set()
        for i, p in enumerate(pts_s):
            if i in used: continue
            cl = [p]; used.add(i)
            for j, q in enumerate(pts_s):
                if j in used: continue
                if math.hypot(p[0]-q[0], p[1]-q[1]) < CONE_CLUSTER_DIST:
                    cl.append(q); used.add(j)
            if len(cl) >= CONE_MIN_POINTS:
                xs_ = [q[0] for q in cl]; ys_ = [q[1] for q in cl]
                cx, cy = float(np.mean(xs_)), float(np.mean(ys_))
                w = max(math.hypot(q[0]-cx, q[1]-cy) for q in cl)*2
                clusters.append({'center': (cx, cy), 'width': float(w), 'n_points': len(cl)})
        clusters.sort(key=lambda c: c['center'][0])
        return clusters[:2]

    def _measure_cone_pc(self, cx, cy):
        if not self._pc_buf: return (0.0, 0.0)
        xs, ys, zs = [], [], []
        for pc in self._pc_buf[-10:]:
            for pt in point_cloud2.read_points(pc, field_names=('x','y','z'), skip_nans=True):
                px, py, pz = float(pt[0]), float(pt[1]), float(pt[2])
                if abs(px-cx) < 0.25 and abs(py-cy) < 0.25 and 0.02 < pz < 1.0:
                    xs.append(px); ys.append(py); zs.append(pz)
        if len(xs) < 10: return (0.0, 0.0)
        return (float(max(max(xs)-min(xs), max(ys)-min(ys))), float(max(zs)-min(zs)))

    def _calc_inflation(self):
        w, l = 0.189, 0.276
        return round(max(math.sqrt(w*w+l*l)/2, min(w,l)/2+0.01)+0.005, 3)

    def _check_map(self, x, y):
        if not self._map_data: return False
        cx = int((x-self._map_data.info.origin.position.x)/self._map_data.info.resolution)
        cy = int((y-self._map_data.info.origin.position.y)/self._map_data.info.resolution)
        if 0 <= cx < self._map_data.info.width and 0 <= cy < self._map_data.info.height:
            return self._map_data.data[cy*self._map_data.info.width+cx] == 0
        return False

    def _print_result(self, params, measured):
        PR = params or {'inflation_radius_m': 0.18, 'cost_scaling_gain': 2.0,
                        'observation_persistence_s': 0.5, 'min_obstacle_height_m': 0.05,
                        'max_obstacle_height_m': 0.35, 'obstacle_range_m': 2.5, 'raytrace_range_m': 3.0}
        self.get_logger().info("\n● 全部标定结果 (写入 originbot_nav2_rpp.yaml)")
        self.get_logger().info(f"  amcl.initial_pose:       x={self._px:.4f} y={self._py:.4f} yaw={self._pyaw:.4f}")
        self.get_logger().info(f"  inflation_radius:        {PR['inflation_radius_m']}")
        self.get_logger().info(f"  cost_scaling_gain:        {PR['cost_scaling_gain']}")
        self.get_logger().info(f"  observation_persistence:  {PR['observation_persistence_s']}")
        self.get_logger().info(f"  min_obstacle_height:      {PR['min_obstacle_height_m']}")
        self.get_logger().info(f"  max_obstacle_height:      {PR['max_obstacle_height_m']}")
        self.get_logger().info(f"  obstacle_range:           {PR['obstacle_range_m']}")
        self.get_logger().info(f"  raytrace_range:           {PR['raytrace_range_m']}")

        with open('/userdata/dev_ws/src/originbot_navigation/config/cone_params.yaml', 'w') as f:
            yaml.dump({
                'costmap': {
                    'inflation_radius': float(PR['inflation_radius_m']),
                    'cost_scaling_factor': 5.0,
                    'observation_persistence': float(PR['observation_persistence_s']),
                    'min_obstacle_height': float(PR['min_obstacle_height_m']),
                    'max_obstacle_height': float(PR['max_obstacle_height_m']),
                    'obstacle_range': float(PR['obstacle_range_m']),
                    'raytrace_range': float(PR['raytrace_range_m']),
                },
                'controller': {
                    'cost_scaling_dist': float(PR['inflation_radius_m']),
                    'cost_scaling_gain': float(PR['cost_scaling_gain']),
                },
                'amcl': {
                    'set_initial_pose': True,
                    'initial_pose': {
                        'x': round(self._px, 4), 'y': round(self._py, 4),
                        'z': 0.0, 'yaw': round(self._pyaw, 4),
                    },
                },
                'measured': measured,
            }, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

        self.get_logger().info(f"\n  结果: maps/p_point.yaml  config/cone_params.yaml")
        self.get_logger().info(f"  5 秒后自动退出")
        self.create_timer(5.0, lambda: (self.destroy_node(), rclpy.shutdown()), 1)


def main():
    rclpy.init()
    rclpy.spin(FieldCalibrator())


if __name__ == '__main__':
    main()
