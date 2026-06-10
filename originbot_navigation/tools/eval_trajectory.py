#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
eval_trajectory.py — 定位精度验证工具

交互流程:
  1. PGM 窗口: 鼠标拖框选择有效地图区域 (左下→右上)
  2. PNG 窗口: 鼠标拖框选择同一有效区域
  3. 对齐窗口: 拖动旋转滑块使 PGM 与 PNG 方向一致
  4. 自动生成三子图 + 评估报告

用法:
  python eval_trajectory.py --bag ./trajectory_logs/
  python eval_trajectory.py --bag ./data/ --calib png_calib.json --headless

依赖: pip install rosbags matplotlib numpy Pillow PyYAML
"""

import os, sys, json, csv, math, argparse
from pathlib import Path
from datetime import datetime

import numpy as np
import yaml as _yaml
from PIL import Image

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector
from matplotlib.patches import Rectangle as MplRect

# ---- 固定参考点 ----
GT_POINTS = {
    'Ch Entry':  (2.0, 1.8),
    'Ch Exit':   (2.0, 2.5),
    'Task Post': (4.5, 1.5),
}

# ---- 透视变换 (4点对齐) ----
def four_point_warp(src_img, src_pts, dst_pts):
    """将 src_img 中 src_pts 定义的四边形区域, 透视变换到 dst_pts 定义的矩形.

    src_pts: [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]  顺序: TL, TR, BR, BL
    dst_pts: [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]  顺序: TL, TR, BR, BL
    返回 warped 图像, 尺寸由 dst_pts 决定.
    """
    try:
        import cv2
        src = np.float32(src_pts)
        dst = np.float32(dst_pts)
        M = cv2.getPerspectiveTransform(src, dst)
        w = int(max(p[0] for p in dst_pts)); h = int(max(p[1] for p in dst_pts))
        warped = cv2.warpPerspective(np.array(src_img), M, (w, h))
        return warped, M
    except ImportError:
        # fallback: Pillow quad transform (less accurate but no cv2 needed)
        from PIL import Image as PILImage
        w = int(max(p[0] for p in dst_pts)); h = int(max(p[1] for p in dst_pts))
        coeffs = _find_coeffs(dst_pts, src_pts)
        img = PILImage.fromarray(src_img)
        warped = img.transform((w, h), PILImage.PERSPECTIVE, coeffs, PILImage.BICUBIC)
        return np.array(warped), None


def _find_coeffs(pa, pb):
    """计算 Pillow perspective transform 系数."""
    matrix = []
    for p1, p2 in zip(pa, pb):
        matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0]*p1[0], -p2[0]*p1[1]])
        matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1]*p1[0], -p2[1]*p1[1]])
    A = np.array(matrix, dtype=float)
    B = np.array([p[0] for p in pb] + [p[1] for p in pb], dtype=float)
    # 只取前8个方程
    A8 = A[:8, :8]; B8 = B[:8]
    res = np.linalg.solve(A8, B8)
    return res.tolist()

# ===================================================================
# Bag 解析
# ===================================================================
def parse_bag(bag_path):
    try:
        from rosbags.rosbag2 import Reader
        from rosbags.typesys import Stores, get_typestore
        return _parse_rosbags(bag_path)
    except Exception:
        pass
    try:
        from rosbag2_py import SequentialReader, StorageOptions, ConverterOptions
        from rclpy.serialization import deserialize_message
        from rosidl_runtime_py.utilities import get_message
        return _parse_rosbag2_py(bag_path)
    except Exception:
        pass
    return {'amcl': [], 'odom': [], 'initial_pose': None}


def _parse_rosbags(bag_path):
    from rosbags.rosbag2 import Reader
    from rosbags.typesys import Stores, get_typestore
    ts = get_typestore(Stores.ROS2_HUMBLE)
    amcl, init_pose = [], None
    with Reader(bag_path) as reader:
        for conn, timestamp, raw in reader.messages():
            try: msg = ts.deserialize_cdr(raw, conn.msgtype)
            except Exception: continue
            try:
                t = max(0.0, timestamp / 1e9)
                if conn.topic == '/amcl_pose':
                    p = msg.pose.pose.position; q = msg.pose.pose.orientation
                    siny = 2*(q.w*q.z+q.x*q.y); cosy = 1-2*(q.y*q.y+q.z*q.z)
                    cov = msg.pose.covariance
                    amcl.append((p.x, p.y, math.atan2(siny,cosy), math.sqrt(max(cov[0],cov[7])), t))
                elif conn.topic == '/initialpose':
                    p = msg.pose.pose.position; q = msg.pose.pose.orientation
                    siny = 2*(q.w*q.z+q.x*q.y); cosy = 1-2*(q.y*q.y+q.z*q.z)
                    init_pose = (p.x, p.y, math.atan2(siny,cosy))
            except Exception: continue
    return {'amcl': amcl, 'initial_pose': init_pose}


def _parse_rosbag2_py(bag_path):
    from rosbag2_py import SequentialReader, StorageOptions, ConverterOptions
    from rclpy.serialization import deserialize_message
    from rosidl_runtime_py.utilities import get_message
    reader = SequentialReader()
    for sid in ['sqlite3', 'mcap']:
        try:
            s = StorageOptions(uri=str(bag_path), storage_id=sid)
            c = ConverterOptions(input_serialization_format='cdr', output_serialization_format='cdr')
            reader.open(s, c); break
        except Exception: continue
    else: raise RuntimeError('cannot open bag')
    tmap = {t.name: t.type for t in reader.get_all_topics_and_types()}
    amcl, init_pose = [], None
    while reader.has_next():
        topic, data, ts = reader.read_next()
        mt = tmap.get(topic)
        if not mt: continue
        try: msg = deserialize_message(data, get_message(mt))
        except Exception: continue
        t = ts / 1e9
        if topic == '/amcl_pose':
            p = msg.pose.pose.position; q = msg.pose.pose.orientation
            siny = 2*(q.w*q.z+q.x*q.y); cosy = 1-2*(q.y*q.y+q.z*q.z)
            cov = msg.pose.covariance
            amcl.append((p.x, p.y, math.atan2(siny,cosy), math.sqrt(max(cov[0],cov[7])), t))
        elif topic == '/initialpose':
            p = msg.pose.pose.position; q = msg.pose.pose.orientation
            siny = 2*(q.w*q.z+q.x*q.y); cosy = 1-2*(q.y*q.y+q.z*q.z)
            init_pose = (p.x, p.y, math.atan2(siny,cosy))
    return {'amcl': amcl, 'initial_pose': init_pose}

# ===================================================================
# 标定: PGM 4角点 → 透视变换 → 对齐 PNG
# ===================================================================
def _click_quad(ax, title, n=4):
    """在 ax 上用 ginput 点 n 个点, 按顺序连线显示四边形. 返回 [(x,y),...]"""
    ax.figure.canvas.manager.set_window_title(title)
    pts = []
    lines = []

    def onclick(event):
        if event.inaxes != ax or event.button != 1: return
        if event.xdata is None: return
        pts.append((event.xdata, event.ydata))
        x, y = event.xdata, event.ydata
        ax.plot(x, y, 'ro', ms=6)
        if len(pts) >= 2:
            (l,) = ax.plot([pts[-2][0], pts[-1][0]], [pts[-2][1], pts[-1][1]], 'r-', lw=2)
            lines.append(l)
        if len(pts) == n:
            # close the quadrilateral
            (l,) = ax.plot([pts[-1][0], pts[0][0]], [pts[-1][1], pts[0][1]], 'r-', lw=2)
            lines.append(l)
            ax.figure.canvas.draw_idle()
            plt.close(ax.figure)
        ax.figure.canvas.draw_idle()

    cid = ax.figure.canvas.mpl_connect('button_press_event', onclick)
    plt.show(block=True)
    ax.figure.canvas.mpl_disconnect(cid)
    return pts if len(pts) == n else None


def run_calibration(pgm_img, png_img, map_cfg):
    """交互标定: PGM点4角 → PNG点4角 → 透视变换对齐 → 返回 calib."""
    ox, oy = map_cfg['origin'][0], map_cfg['origin'][1]
    res = map_cfg['resolution']

    # ---- Step 1: PGM 4 corner points (slanted quadrilateral) ----
    fig1, ax1 = plt.subplots(figsize=(10, 9))
    ax1.imshow(pgm_img, cmap='gray', origin='lower')
    ax1.set_title('PGM: click 4 corners of the slanted map (TL->TR->BR->BL)')

    pgm_pts = _click_quad(ax1, 'PGM 4 Corners', 4)
    if pgm_pts is None:
        print('[ERROR] need 4 PGM points'); return None

    # PGM pixel → World (origin='lower', no Y-flip)
    pgm_world = []
    for px, py in pgm_pts:
        pgm_world.append((ox + px*res, oy + py*res))
    print('PGM corners (World):')
    for i, (wx, wy) in enumerate(pgm_world):
        print(f'  {i}: ({pgm_pts[i][0]:.0f},{pgm_pts[i][1]:.0f})px -> ({wx:.3f},{wy:.3f})m')

    # ---- Step 2: PNG 4 corner points ----
    fig2, ax2 = plt.subplots(figsize=(10, 9))
    ax2.imshow(png_img, origin='upper')
    ax2.set_title('PNG: click same 4 corners (TL->TR->BR->BL)')

    png_pts = _click_quad(ax2, 'PNG 4 Corners', 4)
    if png_pts is None:
        print('[ERROR] need 4 PNG points'); return None
    print('PNG corners:')
    for i, (px, py) in enumerate(png_pts):
        print(f'  {i}: ({px:.0f},{py:.0f})px')

    # ---- Step 3: 透视变换 PGM, 对齐到 PNG 裁剪矩形 ----
    try: import cv2
    except ImportError: cv2 = None

    pu = [p[0] for p in png_pts]; pv = [p[1] for p in png_pts]
    qu_lo, qu_hi = int(min(pu)), int(max(pu))
    qv_lo, qv_hi = int(min(pv)), int(max(pv))
    png_crop = png_img[qv_lo:qv_hi, qu_lo:qu_hi]
    pw, ph = png_crop.shape[1], png_crop.shape[0]

    # PNG 四个角在裁剪图中的像素
    png_crop_pts = [(px-qu_lo, py-qv_lo) for px, py in png_pts]

    # PGM→裁剪PNG透视矩阵
    if cv2:
        M = cv2.getPerspectiveTransform(np.float32(pgm_pts), np.float32(png_crop_pts))
        pgm_warped = cv2.warpPerspective(pgm_img, M, (pw, ph))
    else:
        from PIL import Image as PILImage
        w = int(max(p[0] for p in png_crop_pts)); h = int(max(p[1] for p in png_crop_pts))
        # Pillow perspective via 8-coeff
        coeffs_data = []
        for (px,py), (qx,qy) in zip(png_crop_pts, pgm_pts):
            coeffs_data.extend([qx, qy, px, py])
        # Solve 8-coeff from 4 point pairs
        mat = []; bb = []
        for i in range(4):
            px, py = png_crop_pts[i]; qx, qy = pgm_pts[i]
            mat.append([px, py, 1, 0, 0, 0, -qx*px, -qx*py])
            mat.append([0, 0, 0, px, py, 1, -qy*px, -qy*py])
            bb.extend([qx, qy])
        A8, B8 = np.array(mat[:8], float), np.array(bb[:8], float)
        coeffs = np.linalg.solve(A8, B8).tolist()
        pgm_warped = np.array(PILImage.fromarray(pgm_img).transform((pw, ph), PILImage.PERSPECTIVE, coeffs, PILImage.BICUBIC))
        M = coeffs  # 8-element for Pillow fallback

    # Warped PGM 的 World 坐标:
    # 四个角在 warped 图中的像素 → 逆透视 → 原PGM像素 → World
    corners_warped = [(0,0), (pw-1,0), (pw-1,ph-1), (0,ph-1)]
    if cv2:
        M_inv = np.linalg.inv(M)
        world_corners = []
        for cx, cy in corners_warped:
            d = cv2.perspectiveTransform(np.float32([[[cx, cy]]]), M_inv)
            wx = ox + d[0][0][0]*res; wy = oy + d[0][0][1]*res
            world_corners.append((wx, wy))
    else:
        # Inverse 8-coeff
        a,b,c,d,e,f,g,h = M[:8]
        world_corners = []
        for cx, cy in corners_warped:
            qx, qy = cx, cy
            # Solve for px, py: qx = (a*px+b*py+c)/(g*px+h*py+1)
            mm = [[a-g*qx, b-h*qx], [d-g*qy, e-h*qy]]
            bb2 = [qx-c, qy-f]
            try:
                px, py = np.linalg.solve(np.array(mm, float), np.array(bb2, float))
                world_corners.append((ox+px*res, oy+py*res))
            except np.linalg.LinAlgError:
                world_corners.append((ox, oy))
    wx_vals = [c[0] for c in world_corners]; wy_vals = [c[1] for c in world_corners]
    extent_warped = [min(wx_vals), max(wx_vals), min(wy_vals), max(wy_vals)]

    # 函数: World → warped PGM pixel (直接画在 warped PGM 上)
    def world_to_warped_pgm(wx, wy):
        ppx = (wx - ox) / res; ppy = (wy - oy) / res
        if cv2:
            dst = cv2.perspectiveTransform(np.float32([[[ppx, ppy]]]), M)
            return dst[0][0][0], dst[0][0][1]
        else:
            a,b,c,d,e,f,g,h = M[:8]
            denom = g*ppx + h*ppy + 1
            return (a*ppx + b*ppy + c)/denom, (d*ppx + e*ppy + f)/denom

    # 反向: warped PGM pixel → World
    def warped_pgm_to_world(cx, cy):
        if cv2:
            d = cv2.perspectiveTransform(np.float32([[[cx, cy]]]), M_inv)
            return ox + d[0][0][0]*res, oy + d[0][0][1]*res
        else:
            a,b,c,d,e,f,g,h = M[:8]
            mm = [[a-g*cx, b-h*cx], [d-g*cy, e-h*cy]]
            bb2 = [cx-c, cy-f]
            try:
                px, py = np.linalg.solve(np.array(mm,float), np.array(bb2,float))
                return ox+px*res, oy+py*res
            except: return ox, oy

    # 同时计算 World → PNG裁剪像素 (用于PNG子图)
    # PGM pixel → PNG crop pixel via M (same as world_to_warped_pgm since M maps to crop coords)
    world_to_png_cropped = world_to_warped_pgm

    calib = {
        'pgm_crop': pgm_warped,
        'png_crop': png_crop,
        'extent_pgm': extent_warped,
        'pgm_pts': pgm_pts, 'png_pts': png_pts,
        'M': M.tolist() if cv2 else M,
        'use_cv2': cv2 is not None,
        'ox': ox, 'oy': oy, 'res': res,
        'world_to_png_fn': world_to_png_cropped,
        'world_to_warped_fn': world_to_warped_pgm,
        'warped_to_world_fn': warped_pgm_to_world,
    }

    # ---- Step 4: Draw keepout zones on PNG crop, map to PGM ----
    keepout_rects = []  # list of (x1,y1,x2,y2) in PNG crop pixels
    fig4, ax4 = plt.subplots(figsize=(10, 9))
    ax4.imshow(png_crop, origin='upper')
    ax4.set_title('Step 4: drag rectangles for keepout zones. Press D when done')
    rects_artists = []

    def on_keepout(eclick, erelease):
        x1, y1 = eclick.xdata, eclick.ydata
        x2, y2 = erelease.xdata, erelease.ydata
        if None in (x1,y1,x2,y2): return
        rx1, ry1 = min(x1,x2), min(y1,y2)
        rx2, ry2 = max(x1,x2), max(y1,y2)
        keepout_rects.append((rx1, ry1, rx2, ry2))
        r = MplRect((rx1, ry1), rx2-rx1, ry2-ry1, fill=True, facecolor='red', alpha=0.3, edgecolor='red')
        ax4.add_patch(r); rects_artists.append(r)
        fig4.canvas.draw_idle()
        print(f'  Keepout #{len(keepout_rects)}: ({rx1:.0f},{ry1:.0f})-({rx2:.0f},{ry2:.0f})')

    rs_ko = RectangleSelector(ax4, on_keepout, useblit=True, button=[1],
                              minspanx=10, minspany=10, spancoords='data',
                              props=dict(facecolor='red', alpha=0.3, edgecolor='red'))

    def on_key(event):
        if event.key == 'd':
            plt.close(fig4)

    fig4.canvas.mpl_connect('key_press_event', on_key)
    plt.show(block=True)
    print(f'  Total keepout zones: {len(keepout_rects)}')

    # Convert keepout rects: PNG crop pixel → World → PGM mast
    if keepout_rects:
        oh, ow = pgm_img.shape
        mask = np.full((oh, ow), 254, dtype=np.uint8)  # white = free
        for rx1, ry1, rx2, ry2 in keepout_rects:
            # 4 corners of each rect → inverse perspective → PGM pixel
            cnrs = [(rx1, ry1), (rx2, ry1), (rx2, ry2), (rx1, ry2)]
            pgm_cnrs = []
            for cx, cy in cnrs:
                wx, wy = warped_pgm_to_world(cx, cy)
                ppx = (wx - ox) / res; ppy = (wy - oy) / res
                pgm_cnrs.append((ppx, ppy))
            # Fill polygon or bounding box in PGM mask
            pxs = [p[0] for p in pgm_cnrs]; pys = [p[1] for p in pgm_cnrs]
            min_px, max_px = int(min(pxs)), int(max(pxs))
            min_py, max_py = int(min(pys)), int(max(pys))
            min_px = max(0, min(ow-1, min_px)); max_px = max(0, min(ow-1, max_px))
            min_py = max(0, min(oh-1, min_py)); max_py = max(0, min(oh-1, max_py))
            # PGM origin='lower', so y needs flip: row = oh-1-y
            py_lo = oh - 1 - max_py; py_hi = oh - 1 - min_py
            mask[py_lo:py_hi+1, min_px:max_px+1] = 0  # black = keepout

        calib['keepout_mask'] = mask
        calib['keepout_rects'] = keepout_rects

    # ---- Step 5: click P-point on PNG crop ----
    fig3, ax3 = plt.subplots(figsize=(10, 9))
    ax3.imshow(png_crop, origin='upper')
    ax3.set_title('Click P-point on cropped PNG (or close to skip)')
    pp = ax3.figure.ginput(1, timeout=30, show_clicks=True)
    plt.close('all')
    if pp:
        pwx, pwy = warped_pgm_to_world(*pp[0])
        if pwx is not None:
            calib['p_field'] = (pwx - ox, pwy - oy)
            print(f'P-point: World({pwx:.3f},{pwy:.3f}) Field({pwx-ox:.3f},{pwy-oy:.3f})')

    return calib


def load_calib(path):
    with open(path) as f: d = json.load(f)
    for k in ('pgm_crop', 'png_crop'):
        if k in d and isinstance(d[k], list): d[k] = np.array(d[k])
    if 'M' in d and 'ox' in d:
        ox, oy, res = d['ox'], d['oy'], d['res']
        M = d['M']; cv2_ok = d.get('use_cv2', True)
        def _make_w2p():
            if cv2_ok:
                import cv2; _M = np.float32(M)
                return lambda wx,wy: cv2.perspectiveTransform(
                    np.float32([[[(wx-ox)/res, (wy-oy)/res]]]), _M)[0][0]
            else:
                a,b,c,e,f,g,h,i = M[:9]
                return lambda wx,wy: (
                    (a*(wx-ox)/res + b*(wy-oy)/res + c)/(g*(wx-ox)/res + h*(wy-oy)/res + 1),
                    (e*(wx-ox)/res + f*(wy-oy)/res + i)/(g*(wx-ox)/res + h*(wy-oy)/res + 1))
        d['world_to_png_fn'] = _make_w2p()
    return d

# ===================================================================
# 绘图
# ===================================================================
def plot_results(calib, data, map_cfg):
    ox, oy = map_cfg['origin'][0], map_cfg['origin'][1]
    gt = dict(GT_POINTS)
    if calib and calib.get('p_field'): gt['P (start)'] = calib['p_field']
    elif data['initial_pose']:
        ip = data['initial_pose']; gt['P (start)'] = (ip[0]-ox, ip[1]-oy)

    amcl = np.array([(p[0],p[1]) for p in data['amcl']]) if data['amcl'] else np.empty((0,2))
    fig, axes = plt.subplots(1, 3, figsize=(20, 7))
    ax1, ax2, ax3 = axes

    # --- PGM (warped, aligned with PNG) ---
    # warped 图像 origin='upper', extent 已正确映射像素到 World
    if calib and 'pgm_crop' in calib:
        ax1.imshow(calib['pgm_crop'], cmap='gray', origin='upper', extent=calib['extent_pgm'])
    if amcl.size: ax1.plot(amcl[:,0], amcl[:,1], 'r-', lw=1.5, alpha=0.8, label='AMCL')
    for n,(fx,fy) in gt.items():
        wx=fx+ox; wy=fy+oy; ax1.plot(wx,wy,'gx',ms=10,mew=2)
        ax1.annotate(n,(wx,wy),textcoords='offset points',xytext=(5,5),fontsize=7,color='green')
    if amcl.size: ax1.plot(amcl[0,0], amcl[0,1], 'go', ms=8, label='Start')
    ax1.set_title('PGM (warped) + AMCL'); ax1.set_aspect('equal'); ax1.grid(alpha=0.3)
    if amcl.size: ax1.legend(fontsize=7)
    if amcl.size: ax1.plot(amcl[:,0], amcl[:,1], 'r-', lw=1.5, alpha=0.8, label='AMCL')
    for n,(fx,fy) in gt.items():
        wx=fx+ox; wy=fy+oy; ax1.plot(wx,wy,'gx',ms=10,mew=2)
        ax1.annotate(n,(wx,wy),textcoords='offset points',xytext=(5,5),fontsize=7,color='green')
    if amcl.size: ax1.plot(amcl[0,0], amcl[0,1], 'go', ms=8, label='Start')
    ax1.set_title('PGM (cropped+rotated) + AMCL'); ax1.set_aspect('equal'); ax1.grid(alpha=0.3)
    if amcl.size: ax1.legend(fontsize=7)

    # --- PNG (cropped) ---
    if calib and 'png_crop' in calib:
        ax2.imshow(calib['png_crop'], origin='upper')
        w2p = calib.get('world_to_png_fn')
        if amcl.size and w2p:
            pxs, pys = [], []
            for i in range(len(amcl)):
                px, py = w2p(float(amcl[i,0]), float(amcl[i,1]))
                pxs.append(px); pys.append(py)
            ax2.plot(pxs, pys, 'r-', lw=1.5, alpha=0.8, label='AMCL')
        for n,(fx,fy) in gt.items():
            if w2p:
                wx=fx+ox; wy=fy+oy
                gpx, gpy = w2p(wx, wy)
                ax2.plot(gpx,gpy,'gx',ms=10,mew=2)
                ax2.annotate(n,(gpx,gpy),textcoords='offset points',xytext=(5,5),fontsize=7,color='green')
    ax2.set_title('PNG (cropped) + AMCL')
    if amcl.size: ax2.legend(fontsize=7)

    # --- P-point zoom ---
    wp_x, wp_y = gt['P (start)'][0]+ox, gt['P (start)'][1]+oy
    if calib and 'pgm_crop' in calib:
        ax3.imshow(calib['pgm_crop'], cmap='gray', origin='upper', extent=calib['extent_pgm'])
    ax3.set_xlim(wp_x-0.5, wp_x+0.5); ax3.set_ylim(wp_y-0.5, wp_y+0.5)
    if amcl.size: ax3.plot(amcl[:,0], amcl[:,1], 'r-', lw=1.5)
    ax3.plot(wp_x, wp_y, 'g*', ms=15, label='P')
    if amcl.size:
        ln = max(1, min(len(amcl)//10, 50))
        ex = np.mean(amcl[-ln:,0]); ey = np.mean(amcl[-ln:,1])
        ax3.plot(ex, ey, 'r*', ms=15, label=f'End({ln})')
        err = math.hypot(ex-wp_x, ey-wp_y)*100
        ax3.set_title(f'P zoom 1m | err={err:.1f}cm')
    ax3.legend(fontsize=7); ax3.set_aspect('equal'); ax3.grid(alpha=0.3)

    fig.tight_layout(); return fig

# ===================================================================
# 报告
# ===================================================================
def gen_report(data, map_cfg, out_dir, calib=None):
    amcl = data['amcl']; ox, oy = map_cfg['origin'][0], map_cfg['origin'][1]
    gt = dict(GT_POINTS)
    if calib and calib.get('p_field'): gt['P (start)'] = calib['p_field']
    elif data['initial_pose']:
        ip = data['initial_pose']; gt['P (start)'] = (ip[0]-ox, ip[1]-oy)

    lines = ['='*50, '  AMCL Localization Report',
             f'  {datetime.now():%Y-%m-%d %H:%M:%S}',
             f'  AMCL samples: {len(amcl)}', '='*50, '']

    gx, gy = gt['P (start)'][0]+ox, gt['P (start)'][1]+oy
    if amcl:
        ln = max(1, min(len(amcl)//10, 50))
        ex = np.mean([p[0] for p in amcl[-ln:]]); ey = np.mean([p[1] for p in amcl[-ln:]])
        err = math.hypot(ex-gx, ey-gy)*100
        lines.append(f'[1] P-point end error (last {ln} avg): {err:.1f} cm')
        if err > 15: lines.append('    [WARN] > 15cm, check AMCL params!')
    lines.append('')
    covs = []
    for ax, ay, _, c, _ in amcl:
        fx, fy = ax-ox, ay-oy
        if 1.5 <= fx <= 2.5 and 1.8 <= fy <= 2.5: covs.append(c)
    if covs: lines.append(f'[2] Channel avg cov: {np.mean(covs)*100:.1f} cm ({len(covs)} samples)')
    lines.append('')
    if amcl:
        xs=[p[0] for p in amcl]; ys=[p[1] for p in amcl]
        d = sum(math.hypot(xs[i]-xs[i-1],ys[i]-ys[i-1]) for i in range(1,len(xs)))
        lines.append(f'[3] Total distance: {d:.2f} m')

    r = '\n'.join(lines); print(r)
    with open(os.path.join(out_dir, 'eval_report.txt'), 'w') as f: f.write(r)

# ===================================================================
# main
# ===================================================================
def main():
    p = argparse.ArgumentParser()
    p.add_argument('--bag', required=True)
    p.add_argument('--map', default=None)
    p.add_argument('--png', default=None)
    p.add_argument('--out', default=None)
    p.add_argument('--calib', default=None)
    p.add_argument('--headless', action='store_true')
    args = p.parse_args()

    # paths
    pgm_path = Path(args.map) if args.map else None
    if pgm_path is None:
        for c in [Path('originbot_navigation/maps/room.pgm'), Path('room.pgm')]:
            if c.exists(): pgm_path = c; break
    png_path = Path(args.png) if args.png else (pgm_path.with_suffix('.png') if pgm_path else None)
    out_dir = args.out or str(Path(args.bag))

    # clean old
    for f in ['eval_plot.png','eval_report.txt','amcl_pose.csv','png_calib.json']:
        fp = os.path.join(out_dir, f)
        if os.path.exists(fp): os.remove(fp)
    os.makedirs(out_dir, exist_ok=True)

    # load images
    pgm_img = np.array(Image.open(pgm_path).convert('L'))
    yml = pgm_path.with_suffix('.yaml')
    cfg = _yaml.safe_load(open(yml)) if yml.exists() else {'resolution':0.05,'origin':[-2.65,-4.5,0]}
    png_img = np.array(Image.open(png_path)) if png_path and png_path.exists() else None

    # parse bag
    print(f'[INFO] parse bag: {args.bag}')
    data = parse_bag(args.bag)
    print(f'  AMCL: {len(data["amcl"])} samples')

    # calibrate or load
    calib = None
    if args.headless and args.calib:
        calib = load_calib(args.calib)
    elif not args.headless:
        calib = run_calibration(pgm_img, png_img, cfg)
        if calib:
            save = {}
            for k, v in calib.items():
                if isinstance(v, np.ndarray):
                    save[k] = v.tolist()
                elif callable(v):
                    continue  # skip functions
                elif isinstance(v, (list, tuple)):
                    save[k] = [float(x) if hasattr(x, 'item') else x for x in v]
                elif hasattr(v, 'item'):  # numpy scalar
                    save[k] = float(v)
                else:
                    save[k] = v
            with open(os.path.join(out_dir, 'png_calib.json'), 'w') as f:
                json.dump(save, f, indent=2)
            print('[INFO] calib saved: png_calib.json')

    # plot
    fig = plot_results(calib, data, cfg)
    fig.savefig(os.path.join(out_dir, 'eval_plot.png'), dpi=150, bbox_inches='tight')
    if not args.headless: plt.show()
    else: plt.close('all')

    # report
    gen_report(data, cfg, out_dir, calib)

    # save keepout mask if drawn
    if calib and 'keepout_mask' in calib:
        ts = datetime.now().strftime('%Y%m%d_%H%M%S')
        mask_pgm = os.path.join(out_dir, f'keepout_{ts}.pgm')
        mask_yaml = os.path.join(out_dir, f'keepout_{ts}.yaml')
        Image.fromarray(calib['keepout_mask']).save(mask_pgm)
        cfg_copy = dict(cfg)
        cfg_copy['image'] = os.path.basename(mask_pgm)
        cfg_copy['mode'] = 'scale'
        cfg_copy['occupied_thresh'] = 0.5
        cfg_copy['free_thresh'] = 0.5
        with open(mask_yaml, 'w') as f:
            _yaml.dump(cfg_copy, f)
        print(f'[INFO] keepout saved: {mask_pgm} + {mask_yaml}')

    # save CSV
    with open(os.path.join(out_dir, 'amcl_pose.csv'), 'w', newline='') as f:
        w = csv.writer(f); w.writerow(['x','y','yaw','cov_xy','t'])
        for x,y,yaw,cov,t in data['amcl']:
            w.writerow([f'{x:.4f}',f'{y:.4f}',f'{yaw:.4f}',f'{cov:.4f}',f'{t:.3f}'])

if __name__ == '__main__':
    main()
