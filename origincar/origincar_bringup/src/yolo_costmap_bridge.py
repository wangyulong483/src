#!/usr/bin/env python3
"""
yolo_costmap_bridge.py — YOLO PerceptionTargets → PointCloud2 for Nav2 costmap.

Subscribes to /racing_obstacle_detection (ai_msgs/PerceptionTargets) from
the BPU YOLO node, samples depth at each detection center, projects to 3D,
and publishes PointCloud2 to /tracked_obstacles_cloud for the costmap.

Also publishes /detected_obstacle (PointStamped) for backward compat with
the tracker_node → costmap_publisher pipeline.
"""

import struct
import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, PointCloud2, PointField
from geometry_msgs.msg import PointStamped
from std_msgs.msg import Header


# Aurora930 RGB intrinsics
FX = 416.49
FY = 417.38
CX = 316.83
CY = 188.75
IMG_W = 640
IMG_H = 400


class YoloCostmapBridge(Node):
    """Converts YOLO detection boxes → 3D points for Nav2 costmap."""

    def __init__(self):
        super().__init__('yolo_costmap_bridge')

        # Latest data
        self._latest_depth = None  # (H, W) float32 array in meters
        self._depth_header = None

        # Try ai_msgs import
        try:
            from ai_msgs.msg import PerceptionTargets
            self._PerceptionTargets = PerceptionTargets
        except ImportError:
            self.get_logger().fatal(
                'ai_msgs not available. Install: sudo apt install ros-humble-ai-msgs')
            raise

        # Subscribers
        self._det_sub = self.create_subscription(
            self._PerceptionTargets, '/racing_obstacle_detection',
            self._on_detection, 10)
        self._depth_sub = self.create_subscription(
            Image, '/aurora/depth/image_raw', self._on_depth, 10)

        # Publishers
        self._cloud_pub = self.create_publisher(
            PointCloud2, '/tracked_obstacles_cloud', 10)
        self._obstacle_pub = self.create_publisher(
            PointStamped, '/detected_obstacle', 10)

        self.get_logger().info('YoloCostmapBridge ready')

    def _on_depth(self, msg: Image):
        if msg.encoding not in ('16UC1', 'mono16'):
            return
        try:
            data = np.frombuffer(msg.data, dtype=np.uint16).reshape(
                (msg.height, msg.width)).astype(np.float32) / 1000.0  # mm→m
        except Exception:
            return
        self._latest_depth = data
        self._depth_header = msg.header

    def _on_detection(self, msg):
        if self._latest_depth is None:
            return

        points = []
        for target in msg.targets:
            for roi in target.rois:
                # ROI center in pixel coords
                cx = roi.rect.x_offset + roi.rect.width / 2
                cy = roi.rect.y_offset + roi.rect.height / 2

                # Clamp to image bounds
                u = int(np.clip(cx, 0, IMG_W - 1))
                v = int(np.clip(cy, 0, IMG_H - 1))

                # Sample depth in a 3×3 window around center, take median
                r0 = max(0, v - 1)
                r1 = min(IMG_H, v + 2)
                c0 = max(0, u - 1)
                c1 = min(IMG_W, u + 2)
                patch = self._latest_depth[r0:r1, c0:c1]
                z_val = float(np.median(patch[patch > 0])) if np.any(patch > 0) else 0.0

                if z_val < 0.1 or z_val > 5.0:
                    continue

                # Project to camera 3D
                x_cam = (cx - CX) * z_val / FX
                y_cam = (cy - CY) * z_val / FY

                points.append((float(x_cam), float(y_cam), float(z_val)))

        # Publish PointCloud2
        if points:
            self._publish_cloud(self._depth_header, points)
            # Publish closest obstacle for tracker compat
            closest = min(points, key=lambda p: p[2])
            obs = PointStamped()
            obs.header = self._depth_header
            obs.header.frame_id = 'depth_camera_link'
            obs.point.x = closest[0]
            obs.point.y = closest[1]
            obs.point.z = closest[2]
            self._obstacle_pub.publish(obs)

    def _publish_cloud(self, header, points):
        cloud = PointCloud2()
        cloud.header = header
        cloud.header.frame_id = 'depth_camera_link'
        cloud.fields = [
            PointField(name='x', offset=0, datatype=PointField.FLOAT32, count=1),
            PointField(name='y', offset=4, datatype=PointField.FLOAT32, count=1),
            PointField(name='z', offset=8, datatype=PointField.FLOAT32, count=1),
        ]
        cloud.point_step = 12
        cloud.height = 1
        cloud.width = len(points)
        cloud.is_bigendian = False
        cloud.is_dense = True
        cloud.row_step = cloud.point_step * cloud.width

        buf = bytearray()
        for x, y, z in points:
            buf.extend(struct.pack('<fff', x, y, z))
        cloud.data = bytes(buf)
        self._cloud_pub.publish(cloud)


def main(args=None):
    rclpy.init(args=args)
    node = YoloCostmapBridge()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
