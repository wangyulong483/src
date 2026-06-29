"""
Rosbag2 loader — extract controller & planner metrics without ROS2 runtime.

Parses rosbag2 sqlite3 database directly. No ROS2 imports needed.
Extracts metrics that CSV alone cannot provide: planner frequency,
cross-track error, velocity smoothness.

Topics used:
  /odom  → pose trajectory (high freq ~20Hz)
  /cmd_vel → commanded velocity (high freq ~10Hz)
  /plan   → global plan frequency
  /tf     → base_footprint pose (fallback)
"""
import logging
import sqlite3
import struct
import math
import json
import numpy as np
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass

log = logging.getLogger('Nav2Tuner.Rosbag')


@dataclass
class RosbagMetrics:
    """Controller & planner metrics extracted from rosbag."""
    planner_hz: float = 0.0           # /plan message frequency
    cmd_vel_hz: float = 0.0           # /cmd_vel message frequency
    odom_hz: float = 0.0              # /odom message frequency
    tracking_error_mean: float = 0.0   # mean cross-track error (m)
    tracking_error_max: float = 0.0    # max cross-track error (m)
    velocity_jerk: float = 0.0         # mean jerk |da/dt| from high-freq cmd_vel
    velocity_oscillation: float = 0.0  # std of angular velocity
    avg_speed: float = 0.0             # mean linear velocity
    n_messages: int = 0                # total extracted messages
    obstacle_clearance_min: float = 0.0   # min LiDAR range (m)
    obstacle_clearance_mean: float = 0.0   # mean LiDAR range (m)
    scan_hz: float = 0.0                  # /scan publish frequency


def find_rosbags(directory: str) -> List[str]:
    """Scan directory tree for rosbag2 directories (metadata.yaml + .db3)."""
    bags = []
    root = Path(directory)
    if not root.exists():
        return bags
    for item in root.rglob('metadata.yaml'):
        bag_dir = item.parent
        if list(bag_dir.glob('*.db3')):
            bags.append(str(bag_dir))
    return sorted(bags)


class RosbagLoader:
    """Extract controller metrics from rosbag2 sqlite3 files."""

    def __init__(self):
        pass

    @staticmethod
    def is_rosbag(path: str) -> bool:
        p = Path(path)
        return p.is_dir() and (p / 'metadata.yaml').exists() and bool(list(p.glob('*.db3')))

    def extract_metrics(self, bag_path: str) -> Optional[RosbagMetrics]:
        """Extract controller metrics from a rosbag directory."""
        bag_dir = Path(bag_path)
        db_files = list(bag_dir.glob('*.db3'))
        if not db_files:
            return None

        try:
            conn = sqlite3.connect(str(db_files[0]))
            cursor = conn.cursor()

            # Get topic IDs
            cursor.execute("SELECT id, name, type FROM topics")
            topic_map = {row[0]: (row[1], row[2]) for row in cursor.fetchall()}

            # Find relevant topics
            topic_ids = {}
            for tid, (tname, ttype) in topic_map.items():
                if '/odom' in tname or '/odometry' in tname:
                    topic_ids.setdefault('odom', tid)
                elif tname == '/cmd_vel' or tname == '/cmd_vel_muxed':
                    topic_ids.setdefault('cmd_vel', tid)
                elif tname == '/plan':
                    topic_ids.setdefault('plan', tid)
                elif tname == '/scan':
                    topic_ids.setdefault('scan', tid)

            if not topic_ids:
                log.warning("No relevant topics found in rosbag")
                conn.close()
                return None

            # Extract data for each topic
            odom_data = self._read_topic_messages(cursor, topic_ids.get('odom'))
            cmd_vel_data = self._read_topic_messages(cursor, topic_ids.get('cmd_vel'))
            plan_data = self._read_topic_messages(cursor, topic_ids.get('plan'))
            scan_data = self._read_topic_messages(cursor, topic_ids.get('scan'))
            conn.close()

            metrics = RosbagMetrics()

            # Planner frequency
            if plan_data:
                plan_times = [ts for ts, _ in plan_data]
                if len(plan_times) >= 2:
                    duration = (plan_times[-1] - plan_times[0]) / 1e9
                    metrics.planner_hz = len(plan_times) / max(duration, 0.1)
                    metrics.n_messages += len(plan_times)

            # Cmd_vel frequency + velocity metrics
            if cmd_vel_data:
                vx_vals, wz_vals, cmd_times = [], [], []
                for ts, data in cmd_vel_data:
                    pose = self._parse_cmd_vel_cdr(data)
                    if pose:
                        vx_vals.append(pose['vx'])
                        wz_vals.append(pose['wz'])
                        cmd_times.append(ts)

                if len(cmd_times) >= 2:
                    duration = (cmd_times[-1] - cmd_times[0]) / 1e9
                    metrics.cmd_vel_hz = len(cmd_times) / max(duration, 0.1)
                    metrics.n_messages += len(cmd_times)

                if len(vx_vals) >= 3:
                    vx_arr = np.array(vx_vals, dtype=np.float64)
                    metrics.avg_speed = float(np.mean(np.abs(vx_arr)))
                    # Jerk: |da/dt| from velocity changes
                    dt_vals = np.diff([t / 1e9 for t in cmd_times[:len(vx_arr)]])
                    dvx = np.abs(np.diff(vx_arr[:len(dt_vals)+1]))
                    jerk_vals = dvx[:len(dt_vals)] / np.maximum(dt_vals, 0.01)
                    metrics.velocity_jerk = float(np.mean(jerk_vals)) if len(jerk_vals) > 0 else 0.0

                if len(wz_vals) >= 2:
                    metrics.velocity_oscillation = float(np.std(wz_vals))

            # Odometry frequency
            if odom_data:
                odom_times = [ts for ts, _ in odom_data]
                if len(odom_times) >= 2:
                    duration = (odom_times[-1] - odom_times[0]) / 1e9
                    metrics.odom_hz = len(odom_times) / max(duration, 0.1)
                    metrics.n_messages += len(odom_times)

                # Cross-track error approximation
                if len(odom_data) >= 3:
                    metrics.tracking_error_mean, metrics.tracking_error_max = \
                        self._estimate_tracking_error(odom_data)

            # Extract /scan for obstacle clearance
            if scan_data and len(scan_data) >= 3:
                # Scan frequency
                scan_times = [ts for ts, _ in scan_data]
                if len(scan_times) >= 2:
                    duration = (scan_times[-1] - scan_times[0]) / 1e9
                    metrics.scan_hz = len(scan_times) / max(duration, 0.1)
                    metrics.n_messages += len(scan_times)
                metrics.obstacle_clearance_min, metrics.obstacle_clearance_mean = \
                    self._extract_scan_clearance(scan_data)

            log.info("Rosbag metrics: planner=%.1fHz cmd_vel=%.1fHz odom=%.1fHz "
                     "speed=%.2fm/s jerk=%.2f track_err=%.2fm",
                     metrics.planner_hz, metrics.cmd_vel_hz, metrics.odom_hz,
                     metrics.avg_speed, metrics.velocity_jerk, metrics.tracking_error_mean)

            return metrics

        except Exception as e:
            log.warning("Failed to extract rosbag metrics: %s", e)
            return None

    def _estimate_tracking_error(self, odom_data) -> Tuple[float, float]:
        """Estimate cross-track error from odometry path vs straight-line fit.
        Simple approximation: deviation from smoothed path = tracking error."""
        xy = []
        for ts, data in odom_data:
            pose = self._parse_odom_cdr(data)
            if pose:
                xy.append((pose['x'], pose['y']))

        if len(xy) < 10:
            return 0.0, 0.0

        xs = np.array([p[0] for p in xy], dtype=np.float64)
        ys = np.array([p[1] for p in xy], dtype=np.float64)

        # Fit a smoothed path (moving average) and compute deviation
        window = max(5, len(xs) // 20)
        if window > 2:
            xs_smooth = np.convolve(xs, np.ones(window)/window, mode='same')
            ys_smooth = np.convolve(ys, np.ones(window)/window, mode='same')
            errors = np.hypot(xs - xs_smooth, ys - ys_smooth)
            return float(np.mean(errors)), float(np.max(errors))

        return 0.0, 0.0

    @staticmethod
    def _read_topic_messages(cursor, topic_id) -> List[Tuple[int, bytes]]:
        """Read all messages for a topic. Returns [(timestamp_ns, data_bytes), ...]."""
        if topic_id is None:
            return []
        cursor.execute(
            "SELECT timestamp, data FROM messages WHERE topic_id=? ORDER BY timestamp",
            (topic_id,)
        )
        return [(r[0], r[1]) for r in cursor.fetchall()]

    @staticmethod
    def _parse_cmd_vel_cdr(data: bytes) -> Optional[Dict]:
        """Parse geometry_msgs/Twist from CDR. Returns {'vx':, 'wz':} or None."""
        if len(data) < 48:
            return None
        try:
            # Twist: linear{x,y,z} angular{x,y,z} = 6 doubles
            # Header before it adds ~20-30 bytes
            # Scan for the twist section by looking for reasonable velocity values
            doubles = struct.unpack(f'<{len(data)//8}d', data[:len(data) - len(data) % 8])
            for i in range(len(doubles) - 5):
                vx, vy, vz = doubles[i], doubles[i+1], doubles[i+2]
                wx, wy, wz = doubles[i+3], doubles[i+4], doubles[i+5]
                # vx should be within ±1.0 m/s, vy close to 0 (no lateral motion)
                if abs(vx) < 2.0 and abs(vy) < 0.5 and abs(vz) < 0.5:
                    if abs(wz) < 5.0 and abs(wx) < 1.0 and abs(wy) < 1.0:
                        return {'vx': vx, 'wz': wz}
        except (struct.error, IndexError):
            pass
        return None

    @staticmethod
    def _parse_odom_cdr(data: bytes) -> Optional[Dict]:
        """Parse nav_msgs/Odometry from CDR. Returns {'x':,'y':} or None."""
        if len(data) < 48:
            return None
        try:
            doubles = struct.unpack(f'<{len(data)//8}d', data[:len(data) - len(data) % 8])
            for i in range(len(doubles) - 13):
                x, y, z = doubles[i], doubles[i+1], doubles[i+2]
                if abs(z) > 0.5 or abs(x) > 15 or abs(y) > 15:
                    continue
                qz, qw = doubles[i+5], doubles[i+6]
                if abs(qz*qz + qw*qw - 0.5) > 0.5:
                    continue
                return {'x': x, 'y': y}
        except (struct.error, IndexError):
            pass
        return None

    @staticmethod
    def _extract_scan_clearance(scan_data) -> Tuple[float, float]:
        """Extract obstacle clearance from /scan messages.
        Parses sensor_msgs/LaserScan CDR.
        Returns (min_range, mean_range) in meters.
        """
        ranges_all = []
        for _, data in scan_data:
            if len(data) < 100:
                continue
            try:
                # LaserScan layout: header(~28 bytes) +
                # angle_min(f4) + angle_max(f4) + angle_increment(f4) +
                # time_increment(f4) + scan_time(f4) + range_min(f4) + range_max(f4)
                # Then N x float32 ranges
                floats = struct.unpack(f'<{len(data)//4}f', data[:len(data) - len(data) % 4])
                # Find range_min/range_max section (skip header)
                for i in range(len(floats) - 5):
                    if (0.01 < floats[i] < 0.5 and   # range_min
                        3.0 < floats[i+1] < 50.0):   # range_max
                        # Ranges start at i+2, but we need the count
                        # The number of ranges = (len(data) - offset) / 4
                        # Conservative: take values that look like valid ranges
                        ranges = [f for f in floats[i+2:] if 0.05 < f < 30.0]
                        if ranges:
                            ranges_all.extend(ranges)
                        break
            except (struct.error, IndexError):
                continue

        if ranges_all:
            return float(np.min(ranges_all)), float(np.mean(ranges_all))
        return 0.0, 0.0

    def match_run(self, bag_path: str) -> Optional[Dict]:
        """Match a rosbag to its CSV run. Returns metrics dict or None."""
        metrics = self.extract_metrics(bag_path)
        if metrics is None:
            return None
        return {
            'planner_hz': metrics.planner_hz,
            'cmd_vel_hz': metrics.cmd_vel_hz,
            'odom_hz': metrics.odom_hz,
            'tracking_error_mean': metrics.tracking_error_mean,
            'tracking_error_max': metrics.tracking_error_max,
            'velocity_jerk': metrics.velocity_jerk,
            'velocity_oscillation': metrics.velocity_oscillation,
            'avg_speed': metrics.avg_speed,
        }
