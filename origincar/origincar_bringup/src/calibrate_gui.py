#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
calibrate.py — Nav2 路径标定工具 (单文件, matplotlib, 无需 PyQt5)

用法:
  1. RDK X5: ros2 launch originbot_navigation nav_bringup.launch.py
  2. PC:    python3 calibrate.py

  PC 上只需: pip install matplotlib numpy Pillow PyYAML
  ROS2 rclpy 可选 — 没有也能打开地图标路径点/禁行区/保存, 只是无实时轨迹

功能:
  - 显示地图 + PNG 彩色叠加, 左键点路径点 → 绿色参考线
  - 右键拖拽框选禁行区 → 蓝色半透明
  - 红色实时轨迹 (需 ROS2 /amcl_pose)
  - 滑块调参 + 按钮: 发送目标 | 保存全部 | 清除
  - 保存: trajectory.csv + waypoints.csv + keepout.pgm/yaml + params.txt
"""

import os, sys, csv, math, time, re
from datetime import datetime
from pathlib import Path
from threading import Lock

import numpy as np
from PIL import Image
import yaml as _yaml

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RectangleSelector
from matplotlib.patches import Rectangle as MplRect

# ROS2 — 可选导入, 没有也能打开 GUI
_ROS2_OK = False
try:
    import rclpy
    from rclpy.node import Node
    from rclpy.qos import QoSProfile, ReliabilityPolicy
    from geometry_msgs.msg import PoseWithCovarianceStamped, PoseStamped
    _ROS2_OK = True
except ModuleNotFoundError:
    print('[WARN] rclpy 不可用 — 实时轨迹 & 发送目标功能禁用')
    print('       安装: pip install rclpy (或使用 ROS2 Humble 环境)')

# ===================================================================
# ROS2 桥接 (仅在 rclpy 可用时加载)
# ===================================================================
if _ROS2_OK:
    class Bridge(Node):
        def __init__(self):
            super().__init__('calibrate')
            qos = QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT)
            self.create_subscription(PoseWithCovarianceStamped, '/amcl_pose', self._cb, qos)
            self._pub = self.create_publisher(PoseStamped, '/goal_pose', 10)
            self.pose = None  # (x, y, yaw)
            self.traj = []    # [(x, y), ...]
            self.lock = Lock()

        def _cb(self, m):
            p = m.pose.pose.position
            q = m.pose.pose.orientation
            siny = 2*(q.w*q.z + q.x*q.y)
            cosy = 1 - 2*(q.y*q.y + q.z*q.z)
            with self.lock:
                self.pose = (p.x, p.y, math.atan2(siny, cosy))
                self.traj.append((p.x, p.y))

        def send_goal(self, x, y, yaw=0.0):
            m = PoseStamped()
            m.header.frame_id = 'map'
            m.header.stamp = self.get_clock().now().to_msg()
            m.pose.position.x = x; m.pose.position.y = y
            m.pose.orientation.w = math.cos(yaw/2)
            m.pose.orientation.z = math.sin(yaw/2)
            self._pub.publish(m)

else:
    # 空壳 Bridge — 所有操作无害
    class Bridge:
        def __init__(self): self.pose = None; self.traj = []; self.lock = Lock()
        def send_goal(self, *a, **kw): pass

# ===================================================================
# 主程序
# ===================================================================
def main():
    # ---- 初始化 ROS2 (可选) ----
    if _ROS2_OK:
        rclpy.init(args=[])
    bridge = Bridge()

    # ---- 查找地图 ----
    script_dir = Path(__file__).resolve().parent
    for root in [script_dir, script_dir.parent]:
        for sub in ['originbot_navigation', 'originbot_navigation/maps']:
            pgm = root / sub / 'maps' / 'room.pgm' if 'maps' not in sub else root / sub / 'room.pgm'
            if pgm.exists():
                map_path = pgm
                break
        else:
            continue
        break
    else:
        map_path = Path('room.pgm')

    yaml_path = map_path.with_suffix('.yaml')
    if yaml_path.exists():
        with open(yaml_path) as f:
            cfg = _yaml.safe_load(f)
    else:
        cfg = {'resolution': 0.05, 'origin': [-2.65, -4.5, 0]}

    # ---- 加载地图 ----
    img = np.array(Image.open(map_path).convert('L'))
    H, W = img.shape
    ox, oy = cfg['origin'][0], cfg['origin'][1]
    res = cfg['resolution']
    extent = [ox, ox + W*res, oy, oy + H*res]
    save_dir = map_path.parent

    # 加载官方 PNG 彩色地图 (保持原始比例，用 extent 控制缩放和偏移)
    png_path = map_path.with_suffix('.png')
    png_rgba = None       # RGBA 0-1 float 全尺寸
    png_offset_x = 0.0    # PNG 在 X 方向的额外偏移 (m)
    png_offset_y = 0.0    # PNG 在 Y 方向的额外偏移 (m)
    png_alpha = 0.35      # PNG 透明度
    if png_path.exists():
        png_raw = np.array(Image.open(png_path)) / 255.0
        # 假设 PNG 覆盖相同世界范围，用 extent 缩放 (保留 PNG 自身宽高比)
        png_rgba = png_raw
        print(f'PNG 叠加: {png_path} ({png_raw.shape[1]}x{png_raw.shape[0]})')

    # ---- 创建界面 ----
    fig = plt.figure('Nav2 Path Calibration', figsize=(14, 9))
    fig.subplots_adjust(left=0.06, right=0.98, bottom=0.08, top=0.97)

    # 地图区域
    ax = fig.add_subplot(111)
    pgm_layer = ax.imshow(img, cmap='gray', origin='upper', extent=extent)
    png_layer = None
    if png_rgba is not None:
        # PNG 用自己的 extent 映射到世界坐标 (保留原始宽高比)
        png_ext = [ox + png_offset_x, ox + W*res + png_offset_x,
                   oy + png_offset_y, oy + H*res + png_offset_y]
        png_layer = ax.imshow(png_rgba, origin='upper', extent=png_ext,
                              alpha=png_alpha)
    ax.set_xlabel('X (m)'); ax.set_ylabel('Y (m)')
    ax.set_title('L-click=waypoint | R-drag=keepout | M-click=del last')
    ax.grid(True, alpha=0.3, linestyle='--')

    # 数据
    waypoints = []
    (wp_line,) = ax.plot([], [], 'g-', lw=2.5, label='Ref Path')
    (wp_dots,) = ax.plot([], [], 'go', ms=8, mec='darkgreen')
    (traj_line,) = ax.plot([], [], 'r-', lw=1.5, alpha=0.7, label='Actual Traj')
    (robot_dot,) = ax.plot([], [], 'ro', ms=10, zorder=10)
    (robot_hdg,) = ax.plot([], [], 'r-', lw=2, zorder=10)
    keepout_rects = []   # [(x1,y1,x2,y2), ...]
    keepout_patches = []
    ax.legend(loc='lower right')

    def redraw_waypoints():
        if len(waypoints) >= 2:
            xs = [p[0] for p in waypoints]; ys = [p[1] for p in waypoints]
            wp_line.set_data(xs, ys)
        else:
            wp_line.set_data([], [])
        if waypoints:
            xs = [p[0] for p in waypoints]; ys = [p[1] for p in waypoints]
            wp_dots.set_data(xs, ys)
        else:
            wp_dots.set_data([], [])
        fig.canvas.draw_idle()

    # ---- 交互: 路径点 ----
    def on_click(event):
        if event.inaxes != ax or event.button != 1: return
        if event.xdata is None: return
        waypoints.append((event.xdata, event.ydata))
        redraw_waypoints()

    def on_middle(event):
        if event.button == 2 and waypoints:
            waypoints.pop()
            redraw_waypoints()

    # ---- 交互: 禁行区 ----
    def on_select(eclick, erelease):
        x1, y1 = eclick.xdata, eclick.ydata
        x2, y2 = erelease.xdata, erelease.ydata
        if None in (x1, y1, x2, y2): return
        dx, dy = abs(x2-x1), abs(y2-y1)
        if dx < 0.1 or dy < 0.1: return  # 太小忽略
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        keepout_rects.append((x1, y1, x2, y2))
        rect = MplRect((x1, y1), x2-x1, y2-y1, lw=2, ec='blue', fc='blue', alpha=0.25)
        ax.add_patch(rect)
        keepout_patches.append(rect)
        fig.canvas.draw_idle()

    rs = RectangleSelector(ax, on_select, button=[3],
                           useblit=True, interactive=False,
                           props=dict(facecolor='blue', alpha=0.2, edgecolor='blue'))

    fig.canvas.mpl_connect('button_press_event', on_click)
    fig.canvas.mpl_connect('button_press_event', on_middle)

    # ---- 发送目标按钮 ----
    def send_goal(event):
        if not waypoints: return
        wx, wy = waypoints[-1]
        yaw = 0.0
        if len(waypoints) >= 2:
            dx = waypoints[-1][0] - waypoints[0][0]
            dy = waypoints[-1][1] - waypoints[0][1]
            yaw = math.atan2(dy, dx)
        bridge.send_goal(wx, wy, yaw)
        print(f'[goal] → ({wx:.2f}, {wy:.2f}, {math.degrees(yaw):.1f}deg)')

    ax_go = fig.add_axes([0.77, 0.01, 0.08, 0.04])
    btn_go = Button(ax_go, 'Go')
    btn_go.on_clicked(send_goal)

    # ---- 保存按钮 ----
    def save_all(event):
        ts = datetime.now().strftime('%Y%m%d_%H%M%S')
        # 轨迹
        with bridge.lock:
            traj_data = list(bridge.traj)
        with open(save_dir / f'trajectory_{ts}.csv', 'w', newline='') as f:
            w = csv.writer(f); w.writerow(['x', 'y'])
            for x, y in traj_data: w.writerow([f'{x:.4f}', f'{y:.4f}'])
        # 路径点
        with open(save_dir / f'waypoints_{ts}.csv', 'w', newline='') as f:
            w = csv.writer(f); w.writerow(['x', 'y'])
            for x, y in waypoints: w.writerow([f'{x:.4f}', f'{y:.4f}'])
        # 禁行区 → PGM mask
        if keepout_rects:
            mask = np.full((H, W), 254, dtype=np.uint8)
            for x1, y1, x2, y2 in keepout_rects:
                px1 = max(0, min(W-1, int((x1-ox)/res)))
                py1 = max(0, min(H-1, H-1-int((y1-oy)/res)))
                px2 = max(0, min(W-1, int((x2-ox)/res)))
                py2 = max(0, min(H-1, H-1-int((y2-oy)/res)))
                xa, xb = min(px1,px2), max(px1,px2)
                ya, yb = min(py1,py2), max(py1,py2)
                mask[ya:yb+1, xa:xb+1] = 0
            Image.fromarray(mask).save(save_dir / f'keepout_{ts}.pgm')
            with open(save_dir / f'keepout_{ts}.yaml', 'w') as f:
                f.write(f'image: keepout_{ts}.pgm\nmode: scale\n'
                        f'resolution: {res}\norigin: [{ox}, {oy}, 0]\n'
                        f'occupied_thresh: 0.5\nfree_thresh: 0.5\nnegate: 0\n')
        print(f'[save] trajectory_{ts}.csv + waypoints_{ts}.csv'
              + (f' + keepout_{ts}.pgm' if keepout_rects else ''))

    ax_save = fig.add_axes([0.86, 0.01, 0.08, 0.04])
    btn_save = Button(ax_save, 'Save All')
    btn_save.on_clicked(save_all)

    # ---- 清除按钮 ----
    def clear_all(event):
        waypoints.clear(); redraw_waypoints()
        with bridge.lock: bridge.traj.clear()
        traj_line.set_data([], [])
        for p in keepout_patches: p.remove()
        keepout_patches.clear(); keepout_rects.clear()
        fig.canvas.draw_idle()

    ax_clr = fig.add_axes([0.68, 0.01, 0.08, 0.04])
    btn_clr = Button(ax_clr, 'Clear')
    btn_clr.on_clicked(clear_all)

    # ---- PNG 叠加控制 (仅在 PNG 存在时显示) ----
    png_ctrl_y = 0.96
    if png_layer is not None:
        # 透明度滑块
        ax_alpha = fig.add_axes([0.02, png_ctrl_y, 0.14, 0.015])
        sl_alpha = Slider(ax_alpha, 'PNG Alpha', 0.0, 1.0, valinit=0.35, valstep=0.05)
        def on_alpha(v):
            png_layer.set_alpha(v)
            fig.canvas.draw_idle()
        sl_alpha.on_changed(on_alpha)
        png_ctrl_y -= 0.025

        # X 偏移滑块
        ax_dx = fig.add_axes([0.02, png_ctrl_y, 0.14, 0.015])
        sl_dx = Slider(ax_dx, 'PNG X(m)', -2.0, 2.0, valinit=0.0, valstep=0.05)
        def on_dx(v):
            nonlocal png_offset_x; png_offset_x = v
            _update_png_transform()
        sl_dx.on_changed(on_dx)
        png_ctrl_y -= 0.025

        # Y 偏移滑块
        ax_dy = fig.add_axes([0.02, png_ctrl_y, 0.14, 0.015])
        sl_dy = Slider(ax_dy, 'PNG Y(m)', -2.0, 2.0, valinit=0.0, valstep=0.05)
        def on_dy(v):
            nonlocal png_offset_y; png_offset_y = v
            _update_png_transform()
        sl_dy.on_changed(on_dy)
        png_ctrl_y -= 0.025

        # 旋转滑块 (绕地图中心)
        png_angle = 0.0
        ax_rot = fig.add_axes([0.02, png_ctrl_y, 0.14, 0.015])
        sl_rot = Slider(ax_rot, 'PNG Rot(deg)', -10.0, 10.0, valinit=0.0, valstep=0.1)
        def on_rot(v):
            nonlocal png_angle; png_angle = v
            _update_png_transform()
        sl_rot.on_changed(on_rot)

        import matplotlib.transforms as mtransforms
        def _update_png_transform():
            cx = ox + W*res/2 + png_offset_x
            cy = oy + H*res/2 + png_offset_y
            t = (mtransforms.Affine2D()
                 .translate(-cx, -cy)
                 .rotate_deg(png_angle)
                 .translate(cx, cy)
                 + ax.transData)
            png_layer.set_transform(t)
            fig.canvas.draw_idle()
        png_ctrl_y -= 0.04

    # ---- 参数滑块 ----
    slider_widgets = {}
    params_def = [
        ('inflation_radius', 0.05, 0.50, 0.15),
        ('cost_scaling_factor', 1.0, 20.0, 5.0),
        ('max_angular_vel', 0.5, 2.5, 1.5),
        ('desired_linear_vel', 0.1, 0.8, 0.5),
        ('lookahead_dist', 0.2, 1.5, 0.55),
        ('goal_tolerance', 0.05, 0.5, 0.2),
    ]
    for i, (name, vmin, vmax, vdef) in enumerate(params_def):
        y = png_ctrl_y - i * 0.025
        ax_sl = fig.add_axes([0.02, y, 0.14, 0.018])
        sl = Slider(ax_sl, name, vmin, vmax, valinit=vdef, valstep=0.01)
        slider_widgets[name] = sl

    def on_slider(val, name):
        pass  # 可通过 ros2 param set 实时下发

    for name, sl in slider_widgets.items():
        sl.on_changed(lambda v, n=name: on_slider(v, n))

    info_text = fig.text(0.02, 0.03, 'Ready', fontsize=9, color='gray',
                         family='monospace')

    # ---- 主循环 ----
    timer = fig.canvas.new_timer(interval=100)  # 10Hz
    last_traj_len = 0

    def update():
        nonlocal last_traj_len
        if _ROS2_OK:
            rclpy.spin_once(bridge, timeout_sec=0.001)
        with bridge.lock:
            pose = bridge.pose
            traj_len = len(bridge.traj)
            traj_copy = list(bridge.traj)
        if pose:
            x, y, yaw = pose
            robot_dot.set_data([x], [y])
            hx = x + 0.2*math.cos(yaw); hy = y + 0.2*math.sin(yaw)
            robot_hdg.set_data([x, hx], [y, hy])
            info_text.set_text(
                f'pos=({x:.3f},{y:.3f}) yaw={math.degrees(yaw):.1f}deg | '
                f'traj={traj_len} | wp={len(waypoints)} | keepout={len(keepout_rects)}')
        if traj_len != last_traj_len and traj_copy:
            xs = [p[0] for p in traj_copy]; ys = [p[1] for p in traj_copy]
            traj_line.set_data(xs, ys)
            last_traj_len = traj_len
        fig.canvas.draw_idle()

    timer.add_callback(update)
    timer.start()

    print(f'\n=== Nav2 标定工具 ===')
    print(f'地图: {map_path} ({W}x{H}, {res:.2f}m/pix)')
    print(f'保存: {save_dir}/')
    print(f'左键=路径点 | 右键拖拽=禁行区 | 中键=删除最后点 | 按钮在窗口底部\n')

    plt.show()

    if _ROS2_OK:
        bridge.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
