#!/usr/bin/env python3
"""generate_gradient_keepout.py — 将二进制 keepout_mask.pgm 转换为双侧势场加权掩码 + PNG 可视化。

★ 设计原理 (2026-07-11 v3):
  赛场是平面, keepout 是虚拟禁区 (物理空旷). 真实障碍 (外围挡板/锥桶) 由 room.pgm +
  LiDAR obstacle_layer 处理, 保持 LETHAL.

  v2 教训: keepout 全非致命 (max cost 250 < 253 INSCRIBED) → planner 穿越禁区几乎零成本 →
  车不在乎横穿禁区. 梯度生成器实际产出 99% 像素为 250-252(PGM) → costmap cost≈2.5(≈FREE).

  v3 设计: 禁区内部恢复 LETHAL (254) → 规划器绝不穿越; 通道河谷保留梯度引导居中;
  禁区边缘陡峭爬升 (~1.4px) →"悬崖"推回通道; 锥桶绕行是穿越禁区的唯一合法通道.

  - 通道 (channel): 势场河谷, 中心 cost≈0, 向边缘缓升 (preferred lane, 引导居中)
  - 禁区边缘: cost 140→254 在 ~1.4px 内陡升 (RISE_PER_PX=80) → 陡峭"悬崖壁"
  - 禁区内部: cost 254 (LETHAL) → planner 绝不穿越
  - 外围 (arena outside): free (cost 0), 由 room.pgm/LiDAR 处理真实边界

  四个保证:
   1. 优先车道: 通道河谷(0→60) + cost_penalty → planner 沿通道中心行驶
   2. 不穿越:   禁区内部 LETHAL(254) → footprint 判碰撞 → planner 绝不规划穿越路径
   3. 不误入:   陡峭边缘(140→254 在 ~0.07m) → 车触碰前就被推回
   4. 锥桶绕行: cone bypass 禁用 keepout → LiDAR 自然绕行 → 回通道恢复

★ 算法: 八方向 chamfer 距离变换 (纯 Python, 无 numpy/scipy 依赖, 近欧氏)
  正/反两遍传播, 正交邻居 +1.0, 对角邻居 +1.414 → 平滑近圆形势场

★ keepout_mask.yaml 阈值: free_thresh=0.01 / occupied_thresh=1.0
  确保 pixel 0→OccGrid 100→cost 254(LETHAL), pixel 255→OccGrid 1→cost 2.5(FREE).
"""

import os
import math

_MAP_DIR = os.path.join(os.path.dirname(__file__), '..', '..', '..',
                        'src', 'originbot_navigation', 'maps')
KEEPOUT_PGM = os.path.join(_MAP_DIR, 'keepout_mask.pgm')
BINARY_BAK = os.path.join(_MAP_DIR, 'keepout_mask.pgm.binary.bak')
PNG_OUT = os.path.join(_MAP_DIR, 'keepout_mask_gradient.png')

# ── 势场参数 (cost 空间, 0-254) ────────────────────────────────
CHANNEL_EDGE_COST = 60      # 通道边缘 cost (中心→0)
CHANNEL_DECAY_PX = 3.0      # ★ v3: 5.0→3.0, 通道河谷更窄更聚焦
KEEPOUT_EDGE_COST = 140     # 禁区边缘 cost (紧邻通道, ~1.4px 内升至 LETHAL)
KEEPOUT_MAX_COST = 254      # ★ v3: 250→254 (LETHAL), 禁区内部绝不穿越
KEEPOUT_RISE_PER_PX = 80    # ★ v3: 25→80, 边缘→LETHAL 仅 (254-140)/80≈1.4px≈0.07m
SQRT2 = 1.41421356


def load_pgm(path):
    with open(path, 'rb') as f:
        if f.readline().strip() != b'P5':
            raise ValueError("Not P5 PGM")
        line = f.readline()
        while line.startswith(b'#'):
            line = f.readline()
        w, h = map(int, line.split())
        maxval = int(f.readline())
        data = f.read(w * h)
    return bytearray(data), w, h, maxval


def save_pgm(path, data, w, h, maxval=255):
    with open(path, 'wb') as f:
        f.write(f'P5\n{w} {h}\n{maxval}\n'.encode())
        f.write(bytes(data))


def chamfer_edt(seed, w, h):
    """八方向 chamfer 距离变换: 返回每个 cell 到最近 seed=True cell 的近欧氏距离(px)."""
    INF = float(w + h) * 2
    dist = [0.0 if seed[i] else INF for i in range(w * h)]

    # 正向遍历 (左上→右下): 检查 上/左 及两个上对角
    for y in range(h):
        for x in range(w):
            i = y * w + x
            if dist[i] == 0.0:
                continue
            best = dist[i]
            if x > 0:
                best = min(best, dist[i - 1] + 1.0)
            if y > 0:
                best = min(best, dist[i - w] + 1.0)
                if x > 0:
                    best = min(best, dist[i - w - 1] + SQRT2)
                if x < w - 1:
                    best = min(best, dist[i - w + 1] + SQRT2)
            dist[i] = best

    # 反向遍历 (右下→左上): 检查 下/右 及两个下对角
    for y in range(h - 1, -1, -1):
        for x in range(w - 1, -1, -1):
            i = y * w + x
            best = dist[i]
            if x < w - 1:
                best = min(best, dist[i + 1] + 1.0)
            if y < h - 1:
                best = min(best, dist[i + w] + 1.0)
                if x < w - 1:
                    best = min(best, dist[i + w + 1] + SQRT2)
                if x > 0:
                    best = min(best, dist[i + w - 1] + SQRT2)
            dist[i] = best

    return dist


def cost_to_pixel(cost):
    """cost (0-254) → PGM pixel (0=black→LETHAL, 255=white→FREE).

    ★ v3: 配合 free_thresh=0.01 / occupied_thresh=1.0:
      pixel 0   → OccGrid 100 → costmap cost 254 (LETHAL)
      pixel 255 → OccGrid 1   → costmap cost 2.5 (FREE)
      中间值线性插值.
    """
    occ = cost / 254.0 * 100.0
    darkness = 0.01 + occ / 100.0 * (1.0 - 0.01)
    pixel = int(round(255 * (1.0 - darkness)))
    return max(0, min(255, pixel))


def main():
    # 优先从原始二进制备份读取 (防止在已生成的梯度上重复运行)
    src = BINARY_BAK if os.path.isfile(BINARY_BAK) else KEEPOUT_PGM
    print(f"Loading: {src}")
    data, w, h, maxval = load_pgm(src)
    print(f"  Size: {w}x{h}, maxval={maxval}")

    # 备份原始二进制 (仅首次, 不覆盖真原始)
    if not os.path.isfile(BINARY_BAK):
        save_pgm(BINARY_BAK, data, w, h, maxval)
        print(f"  Backup saved: {BINARY_BAK}")

    # 分类: channel=通道(orig≥250), keepout=禁区(orig<100), outside=外围(其余, orig~205)
    is_channel = [data[i] >= 250 for i in range(w * h)]
    is_keepout = [data[i] < 100 for i in range(w * h)]
    n_ch = sum(is_channel); n_kp = sum(is_keepout)
    n_out = w * h - n_ch - n_kp
    print(f"  channel={n_ch}  keepout={n_kp}  outside={n_out}")

    # 双距离场: 到最近 keepout (给通道河谷) + 到最近 channel (给禁区斜坡)
    print("  Computing chamfer distance transforms (2x)...")
    d_to_keepout = chamfer_edt(is_keepout, w, h)
    d_to_channel = chamfer_edt(is_channel, w, h)

    # 计算 cost → pixel
    out = bytearray(w * h)
    for i in range(w * h):
        if is_keepout[i]:
            # 禁区: 边缘140 → 内部250, 随深入线性升, 封顶 250 (非致命)
            depth = d_to_channel[i]
            cost = min(KEEPOUT_MAX_COST, KEEPOUT_EDGE_COST + depth * KEEPOUT_RISE_PER_PX)
        elif is_channel[i]:
            # 通道: 河谷, 边缘60 → 中心0, 随远离禁区衰减
            d = d_to_keepout[i]
            cost = CHANNEL_EDGE_COST * max(0.0, 1.0 - d / CHANNEL_DECAY_PX)
        else:
            # 外围: free (room.pgm/LiDAR 处理真实边界)
            cost = 0.0
        out[i] = cost_to_pixel(cost)

    save_pgm(KEEPOUT_PGM, out, w, h)

    # 统计
    from collections import Counter
    hist = Counter(out)
    lethal = sum(1 for v in out if v <= 2)
    print(f"\n  输出直方图 (cost 分组):")
    buckets = {'free(cost0-10)': 0, 'low(10-80)': 0, 'mid(80-160)': 0,
               'high(160-249)': 0, 'near-max(250-252)': 0, 'lethal(253+)': 0}
    for v in out:
        c = (255 - v) / 255.0 * 254
        if c <= 10: buckets['free(cost0-10)'] += 1
        elif c <= 80: buckets['low(10-80)'] += 1
        elif c <= 160: buckets['mid(80-160)'] += 1
        elif c <= 249: buckets['high(160-249)'] += 1
        elif c <= 252: buckets['near-max(250-252)'] += 1
        else: buckets['lethal(253+)'] += 1
    for k, n in buckets.items():
        print(f"    {k:22s}: {n:6d} px ({n/(w*h)*100:.1f}%)")
    print(f"  致命像素 (cost≥253): {lethal}  ← 应为 0 (keepout 全非致命)")

    # PNG 可视化
    _write_png(out, w, h)

    print(f"\n  ★ 梯度 keepout v3: {KEEPOUT_PGM}")
    print(f"  ★ PNG 可视化:     {PNG_OUT}")
    print(f"  ★ keepout_mask.yaml 阈值: free_thresh=0.01 occupied_thresh=1.0")
    print(f"  ★ KEEPOUT_MAX_COST=254(LETHAL) RISE={KEEPOUT_RISE_PER_PX}px DECAY={CHANNEL_DECAY_PX}px")


def _write_png(pgm_data, w, h, scale=5):
    """用 PIL 生成 cost 彩色映射 PNG (放大 scale 倍便于查看)."""
    try:
        from PIL import Image
    except ImportError:
        print("  [PNG] PIL 不可用, 跳过可视化")
        return

    def colormap(pixel):
        """pixel(0-255) → cost → RGB. 绿(free)→黄→橙→红(high)→暗红(near-lethal)."""
        cost = (255 - pixel) / 255.0 * 254
        if cost <= 5:
            return (235, 245, 235)          # 近白绿 = 通道中心 (free)
        t = min(1.0, cost / 250.0)
        if t < 0.33:                        # free→黄
            f = t / 0.33
            return (int(120 + 135 * f), int(200 + 55 * f), int(90 * (1 - f)))
        elif t < 0.66:                      # 黄→橙
            f = (t - 0.33) / 0.33
            return (255, int(255 - 100 * f), 0)
        else:                               # 橙→暗红
            f = (t - 0.66) / 0.34
            return (int(255 - 100 * f), int(155 - 155 * f), 0)

    img = Image.new('RGB', (w, h))
    px = img.load()
    for y in range(h):
        for x in range(w):
            px[x, y] = colormap(pgm_data[y * w + x])
    img = img.resize((w * scale, h * scale), Image.NEAREST)
    img.save(PNG_OUT)
    print(f"  [PNG] 已保存 {w*scale}x{h*scale} 彩色 cost 图")


if __name__ == '__main__':
    main()
