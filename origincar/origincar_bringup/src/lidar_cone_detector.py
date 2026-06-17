#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
lidar_cone_detector.py — 地图背景减法 + 几何聚类锥桶检测

Subscribes: /scan (LaserScan), /map (OccupancyGrid), /keepout_mask (OccupancyGrid)
Publishes:  /cone_in_channel (Bool)

两阶段检测:
  1. 地图减法: LiDAR 点 → map 坐标 → 查 room.pgm(墙?) + keepout_mask(禁区?) → 都不是? 未知物体
  2. 几何聚类: 未知物体点按扫描线间距聚类 → ≥2 点成簇 → 锥桶

只用地图减法: 单点 LiDAR 噪点可能被误判
只用聚类:    墙壁反射可能被当成锥桶
两者结合:     地图清掉已知几何, 聚类清掉残余噪点 → 只有真锥桶
"""

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import OccupancyGrid
from std_msgs.msg import Bool
import tf2_ros
import math


class LidarConeDetector(Node):
    def __init__(self):
        super().__init__('lidar_cone_detector')

        # ── 通道区域 (map 坐标系) ────────────────────────
        self.ch_x_min, self.ch_x_max = 0.3, 3.5
        self.ch_y_min, self.ch_y_max = -2.5, 1.5

        # ── LiDAR 参数 ───────────────────────────────────
        self.min_range, self.max_range = 0.5, 3.5
        self.angle_half = math.radians(60)

        # ── 聚类参数 ─────────────────────────────────────
        self.cluster_dist = 0.3        # 相邻点最大间距 (m)
        self.min_cluster_pts = 2       # 最小簇点数 (过滤单点噪点)

        # ── 去抖 ─────────────────────────────────────────
        self.debounce_frames = 5
        self._seen, self._lost = 0, 0
        self._active = False

        # ── 地图缓存 ─────────────────────────────────────
        self._static_map = None
        self._keepout_mask = None

        # ── TF2 ──────────────────────────────────────────
        self._tf_buf = tf2_ros.Buffer()
        self._tf_lis = tf2_ros.TransformListener(self._tf_buf, self)

        # ── Pub/Sub ──────────────────────────────────────
        self._pub = self.create_publisher(Bool, '/cone_in_channel', 10)
        self.create_subscription(LaserScan, '/scan', self._on_scan, 10)
        self.create_subscription(
            OccupancyGrid, '/map', self._on_map,
            rclpy.qos.QoSProfile(depth=1,
                durability=rclpy.qos.QoSDurabilityPolicy.TRANSIENT_LOCAL,
                reliability=rclpy.qos.QoSReliabilityPolicy.RELIABLE))
        self.create_subscription(
            OccupancyGrid, '/keepout_mask', self._on_keepout,
            rclpy.qos.QoSProfile(depth=1,
                durability=rclpy.qos.QoSDurabilityPolicy.TRANSIENT_LOCAL,
                reliability=rclpy.qos.QoSReliabilityPolicy.RELIABLE))

        self.get_logger().info(
            f'[lidar_cone] map+cluster mode: '
            f'channel=[{self.ch_x_min},{self.ch_x_max}]x'
            f'[{self.ch_y_min},{self.ch_y_max}] '
            f'cluster={self.cluster_dist}m min={self.min_cluster_pts}pts '
            f'debounce={self.debounce_frames}')

    # ═══════════════════════════════════════════════════════════════
    # ── 地图缓存 ──────────────────────────────────────────────────
    # ═══════════════════════════════════════════════════════════════

    def _on_map(self, msg):   self._static_map = msg
    def _on_keepout(self, msg): self._keepout_mask = msg

    # ═══════════════════════════════════════════════════════════════
    # ── 主逻辑 ────────────────────────────────────────────────────
    # ═══════════════════════════════════════════════════════════════

    def _on_scan(self, msg: LaserScan):
        # tf: laser → map
        try:
            tf = self._tf_buf.lookup_transform(
                'map', msg.header.frame_id, rclpy.time.Time())
        except Exception:
            return
        yaw = 2 * math.atan2(tf.transform.rotation.z, tf.transform.rotation.w)
        c, s = math.cos(yaw), math.sin(yaw)
        tx, ty = tf.transform.translation.x, tf.transform.translation.y

        # Step 1: 地图减法 → 收集未知物体点
        unknown = []  # [(lx, ly), ...]  in laser frame for clustering
        ang = msg.angle_min
        for r in msg.ranges:
            if self.min_range < r < self.max_range and -self.angle_half < ang < self.angle_half:
                lx = r * math.cos(ang)
                ly = r * math.sin(ang)
                mx = tx + c * lx - s * ly
                my = ty + s * lx + c * ly

                if not self._on_map_cell(mx, my) and not self._on_keepout_cell(mx, my):
                    unknown.append((lx, ly))
            ang += msg.angle_increment

        # Step 2: 几何聚类 → 锥桶 = ≥min_cluster_pts 的簇
        clusters = self._cluster(unknown)
        cones = any(len(c) >= self.min_cluster_pts for c in clusters)

        self._debounce(cones)

    # ═══════════════════════════════════════════════════════════════
    # ── 地图查表 ──────────────────────────────────────────────────
    # ═══════════════════════════════════════════════════════════════

    def _on_map_cell(self, mx, my):
        """True = 静态地图上是墙/挡板"""
        return self._lookup(self._static_map, mx, my) > 65

    def _on_keepout_cell(self, mx, my):
        """True = 在禁区 mask 内"""
        return self._lookup(self._keepout_mask, mx, my) > 10

    @staticmethod
    def _lookup(grid, wx, wy):
        if grid is None:
            return -1
        gx = int((wx - grid.info.origin.position.x) / grid.info.resolution)
        gy = int((wy - grid.info.origin.position.y) / grid.info.resolution)
        if 0 <= gx < grid.info.width and 0 <= gy < grid.info.height:
            return grid.data[gy * grid.info.width + gx]
        return -1

    # ═══════════════════════════════════════════════════════════════
    # ── 几何聚类 ──────────────────────────────────────────────────
    # ═══════════════════════════════════════════════════════════════

    def _cluster(self, points):
        """按扫描线相邻点间距分簇"""
        if len(points) < 2:
            return [points]
        clusters, cur = [], [points[0]]
        d2 = self.cluster_dist ** 2
        for i in range(1, len(points)):
            dx = points[i][0] - points[i-1][0]
            dy = points[i][1] - points[i-1][1]
            if dx*dx + dy*dy < d2:
                cur.append(points[i])
            else:
                clusters.append(cur)
                cur = [points[i]]
        clusters.append(cur)
        return clusters

    # ═══════════════════════════════════════════════════════════════
    # ── 去抖 ──────────────────────────────────────────────────────
    # ═══════════════════════════════════════════════════════════════

    def _debounce(self, cones_found):
        if cones_found:
            self._seen += 1; self._lost = 0
        else:
            self._lost += 1; self._seen = 0

        new = self._active
        if self._seen >= self.debounce_frames:
            new = True
        elif self._lost >= self.debounce_frames:
            new = False

        if new != self._active:
            self._active = new
            label = ("no_cone→CLEAR", "cone→CONE_DETECTED")[self._active]
            self.get_logger().info(f'[lidar_cone] {label}')
            self._pub.publish(Bool(data=self._active))


def main():
    rclpy.init()
    rclpy.spin(LidarConeDetector())
    rclpy.shutdown()


if __name__ == '__main__':
    main()
