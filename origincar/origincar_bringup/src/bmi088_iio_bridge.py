#!/usr/bin/env python3
"""
bmi088_iio_bridge.py -- BMI088 IIO -> ROS2 /imu_data bridge
==========================================================
通过 srpi-config 配置 BMI088-I2C-Interface 后, 内核 IIO 驱动将
BMI088 暴露为 /sys/bus/iio/devices/iio:deviceX/

不同内核/平台的 IIO 设备命名可能不同:
  - NVIDIA Jetson 定制驱动:  name="accelerometer" / "gyroscope"
                              属性: gyr_val_x / accel_val_x (已转 SI 单位)
  - Mainline Linux 驱动:     name="bmi088-accel" / "bmi088-gyro" (或 "bmg160")
                              属性: in_accel_x_raw / in_anglvel_x_raw (原始值)
  - RDK X5 / Sunrise 5:      可能是上述之一或自定义命名

本节点:
  1. 扫描所有 IIO 设备, 打印所有名称用于调试
  2. 多策略匹配: 按 name (多模式) -> 按 part 文件 -> 按可用属性
  3. 多属性名探测: gyr_val_x / in_anglvel_x_raw / anglvel_x 等
  4. 通过 ROS 参数可手动指定设备路径 (跳过自动检测)
  5. 未找到设备时发布零数据, 不崩溃 (EKF 可优雅降级)

依赖: 仅 Python 标准库 + rclpy + sensor_msgs, 无需任何外部包.
"""

import os
import math
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu


IIO_BASE = "/sys/bus/iio/devices"

# ---------------------------------------------------------------------------
# 已知的 IIO 设备 name 模式 (按优先级)
# ---------------------------------------------------------------------------
KNOWN_GYRO_NAMES = [
    "gyroscope",        # NVIDIA Jetson 定制驱动
    "bmi088-gyro",      # Mainline Linux 可能命名
    "bmg160",           # Mainline gyro 驱动 (BMG160 兼容 BMI088 gyro 部分)
    "bmi08x_gyroscope", # 某些变体
    "bmi08x",           # RDK X5 srpi-config 单设备模式 (gyro+accel 合一)
]
KNOWN_ACCEL_NAMES = [
    "accelerometer",    # NVIDIA Jetson 定制驱动
    "bmi088-accel",     # Mainline Linux (v8+)
    "bmi088a",          # Mainline Linux (旧版, v7 之前)
    "bmi085-accel",     # 兼容芯片
    "bmi090l-accel",    # 兼容芯片
    "bmi08x",           # RDK X5 srpi-config 单设备模式 (gyro+accel 合一)
]

# ---------------------------------------------------------------------------
# 已知的 IIO 属性名模式 (按优先级), 每个元素为 (三轴基础名, 已是SI?)
# ---------------------------------------------------------------------------
GYRO_ATTR_CANDIDATES = [
    ("gyr_val",      True),   # NVIDIA Jetson: 已转 rad/s
    ("in_anglvel",   False),  # Mainline raw: 需要 scale
    ("anglvel",      False),  # Mainline raw 变体
]
ACCEL_ATTR_CANDIDATES = [
    ("accel_val",    True),   # NVIDIA Jetson: 已转 m/s^2
    ("in_accel",     False),  # Mainline raw: 需要 scale
]


# ---------------------------------------------------------------------------
# 工具函数
# ---------------------------------------------------------------------------

def _list_all_iio_devices() -> list[dict]:
    """扫描 /sys/bus/iio/devices/, 返回所有设备的 {name, path, part, attrs} 列表."""
    devices = []
    if not os.path.isdir(IIO_BASE):
        return devices

    for entry in sorted(os.listdir(IIO_BASE)):
        dev_path = os.path.join(IIO_BASE, entry)
        if not os.path.isdir(dev_path):
            continue

        name = _read_str(dev_path, "name")
        part = _read_str(dev_path, "part")  # NVIDIA 定制驱动有 part 文件

        # 收集该设备下的所有属性文件名
        try:
            attrs = set(os.listdir(dev_path))
        except OSError:
            attrs = set()

        devices.append({
            "path": dev_path,
            "entry": entry,
            "name": name,
            "part": part,
            "attrs": attrs,
        })

    return devices


def _read_str(dev_path: str, filename: str) -> str | None:
    """读取 sysfs 文件内容为 strip 后的字符串, 失败返回 None."""
    try:
        with open(os.path.join(dev_path, filename)) as f:
            return f.read().strip()
    except (OSError, UnicodeDecodeError):
        return None


def _read_float(dev_path: str, filename: str) -> float | None:
    """读取 sysfs 文件内容为 float, 失败返回 None."""
    try:
        with open(os.path.join(dev_path, filename)) as f:
            return float(f.read().strip())
    except (OSError, ValueError, UnicodeDecodeError):
        return None


def _read_vec3(dev_path: str, base_attr: str, is_si: bool,
               scale: float = 1.0) -> tuple[float, float, float]:
    """读取三轴属性 (base_attr + _x/_y/_z).
    如果 is_si=False, 返回值乘以 scale.
    个别属性失败时该轴返回 0.0."""
    x = _read_float(dev_path, f"{base_attr}_x")
    y = _read_float(dev_path, f"{base_attr}_y")
    z = _read_float(dev_path, f"{base_attr}_z")

    # 如果 base 本身不带轴后缀 (比如 in_anglvel_x_raw, base="in_anglvel", 则实际文件是 in_anglvel_x_raw)
    # 我们已经尝试了 base_attr + _x, 如果全部是 None, 尝试 base_attr + _x_raw
    if x is None and y is None and z is None:
        x = _read_float(dev_path, f"{base_attr}_x_raw")
        y = _read_float(dev_path, f"{base_attr}_y_raw")
        z = _read_float(dev_path, f"{base_attr}_z_raw")

    vx = (x or 0.0) * (1.0 if is_si else scale)
    vy = (y or 0.0) * (1.0 if is_si else scale)
    vz = (z or 0.0) * (1.0 if is_si else scale)
    return (vx, vy, vz)


def _detect_attr_base(dev_path: str, candidates: list[tuple[str, bool]]) -> tuple[str, bool, float] | None:
    """探测设备使用哪套属性命名.
    返回 (base_attr, is_si, scale) 或 None.
    """
    for base_attr, is_si in candidates:
        # 尝试 base_attr_x 或 base_attr_x_raw
        if os.path.isfile(os.path.join(dev_path, f"{base_attr}_x")):
            scale = 1.0
            if not is_si:
                s = _read_float(dev_path, f"{base_attr}_scale")
                scale = s if s is not None and s > 0 else 1.0
            return (base_attr, is_si, scale)
        if os.path.isfile(os.path.join(dev_path, f"{base_attr}_x_raw")):
            scale = 1.0
            if not is_si:
                s = _read_float(dev_path, f"{base_attr}_scale")
                scale = s if s is not None and s > 0 else 1.0
            return (base_attr, is_si, scale)
    return None


def _find_device_by_name_attr(candidates: list[str], all_devices: list[dict],
                               part_keywords: list[str],
                               attr_keywords: list[str]) -> tuple[str | None, dict | None]:
    """多策略匹配 IIO 设备.
    优先级: name 精确匹配 -> name 模糊匹配 -> part 匹配 -> 属性探测
    返回 (匹配策略描述, device_dict) 或 (None, None).
    """
    # 策略 1: name 精确匹配已知模式
    for dev in all_devices:
        if dev["name"] in candidates:
            return (f"name==\"{dev['name']}\"", dev)

    # 策略 2: name 包含 "bmi" 且包含匹配关键字
    for dev in all_devices:
        if dev["name"] and "bmi" in dev["name"].lower():
            if any(kw in dev["name"].lower() for kw in part_keywords):
                return (f"name=~\"{dev['name']}\" (contains bmi+{part_keywords})", dev)

    # 策略 3: part 文件匹配 (NVIDIA 定制驱动有 "bmi08x accelerometer" / "bmi08x gyroscope")
    for dev in all_devices:
        if dev["part"] and "bmi08x" in dev["part"].lower():
            if any(kw in dev["part"].lower() for kw in part_keywords):
                return (f"part==\"{dev['part']}\"", dev)

    # 策略 4: 按属性文件探测 (属性名包含关键字并以 _x 或 _x_raw 结尾)
    for dev in all_devices:
        for attr_name in dev["attrs"]:
            for kw in attr_keywords:
                if kw in attr_name and (attr_name.endswith("_x") or attr_name.endswith("_x_raw")):
                    return (f"attr \"{attr_name}\" contains \"{kw}\"", dev)

    return (None, None)


# ---------------------------------------------------------------------------
# ROS2 Node
# ---------------------------------------------------------------------------

class Bmi088IioBridge(Node):
    def __init__(self):
        super().__init__("bmi088_iio_bridge")

        # ── 参数 ──────────────────────────────────────────────
        self.declare_parameter("rate", 100.0)
        self.declare_parameter("frame_id", "bmi088_link")

        # 手动指定设备路径 (可选): 设置后将跳过自动检测
        self.declare_parameter("gyro_device_path", "")
        self.declare_parameter("accel_device_path", "")

        # 手动指定属性基础名 (可选): e.g. "gyr_val" 或 "in_anglvel"
        self.declare_parameter("gyro_attr_base", "")
        self.declare_parameter("accel_attr_base", "")
        # 是否已为 SI 单位 (NVIDIA 驱动已转换, mainline 需 scale)
        self.declare_parameter("gyro_attr_is_si", True)
        self.declare_parameter("accel_attr_is_si", True)
        # scale override: RDK X5 IIO 驱动不提供 scale 文件, 需手动指定
        # BMI088 @ ±1000°/s → 1 LSB = 0.00053 rad/s
        # BMI088 @ ±3g     → 1 LSB = 0.00341 m/s²
        self.declare_parameter("gyro_scale_override", 0.0)
        self.declare_parameter("accel_scale_override", 0.0)

        rate = self.get_parameter("rate").value
        self._frame_id = self.get_parameter("frame_id").value
        self._gyro_scale_override = self.get_parameter("gyro_scale_override").value or None
        self._accel_scale_override = self.get_parameter("accel_scale_override").value or None

        # ── 诊断: 扫描所有 IIO 设备并打印 name 文件内容 ────────
        # 等效于: ls /sys/bus/iio/devices/*/name; cat /sys/bus/iio/devices/*/name
        all_devices = _list_all_iio_devices()

        self.get_logger().info(f"=================================================================")
        self.get_logger().info(f"  DIAGNOSTIC: Scanning IIO devices under {IIO_BASE}/")
        self.get_logger().info(f"  Equivalent to: ls {IIO_BASE}/*/name")
        self.get_logger().info(f"=================================================================")

        if not all_devices:
            self.get_logger().error(f"  IIO base directory is empty or absent!")
            self.get_logger().error(f"  Run:  ls {IIO_BASE}/")
        else:
            # Print every device's name file content (equivalent to cat each name file)
            bmi_device_names = []
            for dev in all_devices:
                name_str = dev["name"] or "(name file missing or unreadable)"
                self.get_logger().info(
                    f"  {dev['entry']}/name = \"{name_str}\""
                )
                if dev["name"] and "bmi" in dev["name"].lower():
                    bmi_device_names.append(dev["name"])

            self.get_logger().info(f"  Total IIO devices found: {len(all_devices)}")

            # ── BMI088 专项检查 ──────────────────────────────────
            if bmi_device_names:
                self.get_logger().info(
                    f"  BMI088 kernel module APPEARS LOADED: {len(bmi_device_names)} BMI device(s) detected"
                )
                self.get_logger().info(f"  BMI device names: {bmi_device_names}")
            else:
                self.get_logger().error(f"")
                self.get_logger().error(f"  *** NO BMI088 DEVICES DETECTED ***")
                self.get_logger().error(f"  The BMI088 IIO kernel driver is NOT loaded.")
                self.get_logger().error(f"")
                self.get_logger().error(f"  To enable the BMI088 IMU on RDK X5 / Sunrise 5:")
                self.get_logger().error(f"    1. Run:  sudo srpi-config")
                self.get_logger().error(f"    2. Navigate:  3 Interface Options")
                self.get_logger().error(f"                  -> I6 IMU")
                self.get_logger().error(f"                  -> BMI088-I2C-Interface  (select with Space, then Enter)")
                self.get_logger().error(f"    3. Select <Finish> and reboot:  sudo reboot")
                self.get_logger().error(f"    4. After reboot, verify:  ls /sys/bus/iio/devices/*/name")
                self.get_logger().error(f"       You should see entries like 'bmi088-accel' and 'bmi088-gyro'")
                self.get_logger().error(f"    5. Relaunch bmi088_iio_bridge")
                self.get_logger().error(f"")
                self.get_logger().error(f"  Alternative: check I2C wiring")
                self.get_logger().error(f"    sudo i2cdetect -y 5    # RDK X5 I2C bus 5")
                self.get_logger().error(f"    dmesg | grep -i bmi    # kernel messages")
                self.get_logger().error(f"=================================================================")

        # ── 定位 gyro / accel 设备 ────────────────────────────
        gyro_path = self.get_parameter("gyro_device_path").value or ""
        accel_path = self.get_parameter("accel_device_path").value or ""
        gyro_attr_base = self.get_parameter("gyro_attr_base").value or ""
        accel_attr_base = self.get_parameter("accel_attr_base").value or ""
        gyro_is_si = self.get_parameter("gyro_attr_is_si").value
        accel_is_si = self.get_parameter("accel_attr_is_si").value

        self._gyro_info: dict | None = None   # {path, base_attr, is_si, scale}
        self._accel_info: dict | None = None

        # 路径+属性都已手动指定
        if gyro_path and gyro_attr_base:
            self._gyro_info = {
                "path": gyro_path,
                "base_attr": gyro_attr_base,
                "is_si": gyro_is_si,
                "scale": 1.0 if gyro_is_si else (_read_float(gyro_path, f"{gyro_attr_base}_scale") or 1.0),
            }
            self.get_logger().info(f"  gyro (manual): path={gyro_path} attr={gyro_attr_base}")

        if accel_path and accel_attr_base:
            self._accel_info = {
                "path": accel_path,
                "base_attr": accel_attr_base,
                "is_si": accel_is_si,
                "scale": 1.0 if accel_is_si else (_read_float(accel_path, f"{accel_attr_base}_scale") or 1.0),
            }
            self.get_logger().info(f"  accel (manual): path={accel_path} attr={accel_attr_base}")

        # 自动检测 gyro
        if self._gyro_info is None:
            reason, dev = _find_device_by_name_attr(
                KNOWN_GYRO_NAMES, all_devices,
                part_keywords=["gyro", "gyroscope"],
                attr_keywords=["anglvel", "gyr_val"],
            )
            if dev:
                attr_info = _detect_attr_base(dev["path"], GYRO_ATTR_CANDIDATES)
                if attr_info:
                    base_attr, is_si, scale = attr_info
                    if not is_si and self._gyro_scale_override:
                        scale = self._gyro_scale_override
                    self._gyro_info = {
                        "path": dev["path"],
                        "base_attr": base_attr,
                        "is_si": is_si,
                        "scale": scale,
                    }
                    self.get_logger().info(
                        f"  gyro:  {dev['path']} ({reason}) attr={base_attr} is_si={is_si}"
                        f"{' scale_override=' + str(scale) if self._gyro_scale_override else ''}"
                    )
                else:
                    self.get_logger().warn(
                        f"  gyro:  设备找到 ({dev['path']}, {reason}) 但无可识别的数据属性"
                    )
            else:
                self.get_logger().warn(
                    f"  gyro:  未找到 (tried names={KNOWN_GYRO_NAMES}). "
                    f"角速度将为零. 用 'gyro_device_path'+'gyro_attr_base' 参数手动指定."
                )

        # 自动检测 accel
        if self._accel_info is None:
            reason, dev = _find_device_by_name_attr(
                KNOWN_ACCEL_NAMES, all_devices,
                part_keywords=["accel", "accelerometer"],
                attr_keywords=["accel"],
            )
            if dev:
                attr_info = _detect_attr_base(dev["path"], ACCEL_ATTR_CANDIDATES)
                if attr_info:
                    base_attr, is_si, scale = attr_info
                    if not is_si and self._accel_scale_override:
                        scale = self._accel_scale_override
                    self._accel_info = {
                        "path": dev["path"],
                        "base_attr": base_attr,
                        "is_si": is_si,
                        "scale": scale,
                    }
                    self.get_logger().info(
                        f"  accel: {dev['path']} ({reason}) attr={base_attr} is_si={is_si}"
                        f"{' scale_override=' + str(scale) if self._accel_scale_override else ''}"
                    )
                else:
                    self.get_logger().warn(
                        f"  accel: 设备找到 ({dev['path']}, {reason}) 但无可识别的数据属性"
                    )
            else:
                self.get_logger().warn(
                    f"  accel: 未找到 (tried names={KNOWN_ACCEL_NAMES}). "
                    f"加速度将为零. 用 'accel_device_path'+'accel_attr_base' 参数手动指定."
                )

        # ── 发布者 ────────────────────────────────────────────
        self._pub = self.create_publisher(Imu, "/imu_data", 10)

        # ── 定时器 ────────────────────────────────────────────
        period = 1.0 / max(rate, 1.0)
        self._timer = self.create_timer(period, self._publish)

        # ── 陀螺零偏校准 (Bosch 建议: 静止时采样取均值) ────
        self._gyro_bias = (0.0, 0.0, 0.0)
        self._bias_samples = []
        self._bias_calibrated = False
        self._bias_timer = self.create_timer(0.01, self._collect_bias_sample)

        status = "OK" if (self._gyro_info or self._accel_info) else "DEGRADED (zero data)"
        self.get_logger().info(f"BMI088 IIO Bridge 启动 @ {rate:.0f}Hz -> /imu_data  [{status}]")

        if self._gyro_info is None and self._accel_info is None:
            self.get_logger().warn(
                "=================================================================\n"
                "  BMI088 IIO bridge -- both gyro AND accel devices unresolved.\n"
                "  Publishing zero IMU data (EKF will use process_noise_covariance).\n"
                "=================================================================\n"
                "  See the DIAGNOSTIC section above for detailed findings.\n"
                "=================================================================\n"
                "  Manual override (if devices exist but auto-detection fails):\n"
                "    ros2 run origincar_bringup bmi088_iio_bridge --ros-args -p\n"
                "      gyro_device_path:=/sys/bus/iio/devices/iio:device0\n"
                "      accel_device_path:=/sys/bus/iio/devices/iio:device1\n"
                "      gyro_attr_base:=gyr_val  accel_attr_base:=accel_val\n"
                "================================================================="
            )

    def _collect_bias_sample(self):
        """开机后 2 秒内采集陀螺样本用于零偏校准 (Bosch datasheet 建议)"""
        if self._bias_calibrated or self._gyro_info is None:
            if hasattr(self, '_bias_timer') and self._bias_timer:
                self._bias_timer.cancel()
                self._bias_timer = None
            return
        gx, gy, gz = _read_vec3(
            self._gyro_info["path"], self._gyro_info["base_attr"],
            self._gyro_info["is_si"], self._gyro_info["scale"])
        self._bias_samples.append((gx, gy, gz))
        if len(self._bias_samples) >= 200:  # 2s @ 100Hz
            n = len(self._bias_samples)
            self._gyro_bias = (
                sum(s[0] for s in self._bias_samples) / n,
                sum(s[1] for s in self._bias_samples) / n,
                sum(s[2] for s in self._bias_samples) / n,
            )
            self._bias_calibrated = True
            self._bias_timer.cancel()
            self._bias_timer = None
            self.get_logger().info(
                f"  gyro bias calibrated: ({self._gyro_bias[0]:.6f}, "
                f"{self._gyro_bias[1]:.6f}, {self._gyro_bias[2]:.6f}) rad/s")

    def _publish(self):
        now = self.get_clock().now()
        msg = Imu()
        msg.header.stamp = now.to_msg()
        msg.header.frame_id = self._frame_id

        # 角速度 (rad/s) — 减去静止零偏
        if self._gyro_info:
            gx, gy, gz = _read_vec3(
                self._gyro_info["path"],
                self._gyro_info["base_attr"],
                self._gyro_info["is_si"],
                self._gyro_info["scale"],
            )
            if self._bias_calibrated:
                gx -= self._gyro_bias[0]
                gy -= self._gyro_bias[1]
                gz -= self._gyro_bias[2]
            msg.angular_velocity.x = gx
            msg.angular_velocity.y = gy
            msg.angular_velocity.z = gz

        # 加速度 (m/s^2)
        if self._accel_info:
            ax, ay, az = _read_vec3(
                self._accel_info["path"],
                self._accel_info["base_attr"],
                self._accel_info["is_si"],
                self._accel_info["scale"],
            )
            msg.linear_acceleration.x = ax
            msg.linear_acceleration.y = ay
            msg.linear_acceleration.z = az

        # 协方差: -1 表示未设置 (EKF 将使用 process_noise_covariance)
        for i in range(9):
            msg.orientation_covariance[i] = -1.0
            msg.angular_velocity_covariance[i] = (
                -1.0 if i % 4 != 0 else 1e-5   # BMI088 ~0.005 deg/s/rtHz
            )
            msg.linear_acceleration_covariance[i] = (
                -1.0 if i % 4 != 0 else 0.05    # ~230 ug/rtHz
            )

        self._pub.publish(msg)


def main():
    rclpy.init()
    try:
        node = Bmi088IioBridge()
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.shutdown()


if __name__ == '__main__':
    main()
