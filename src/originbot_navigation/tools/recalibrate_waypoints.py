#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
根据 data/trajectories 里成功(DONE)轨迹, 把 Nav2 巡航航点重新校准到
"车实际跑通的走廊" 上, 并在 room+keepout 底图上叠加 旧/新 航点对比图.

用法:
    python originbot_navigation/tools/recalibrate_waypoints.py

输出:
    trajectories_waypoints_calibrated.png   (仓库根, 保留原 trajectories_overlay.png)
    stdout 打印 旧→新 航点对照表 + 可直接粘贴的参数块
"""
import csv
import json
import math
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from PIL import Image

# ── 路径 ───────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parents[2]          # .../src
MAPS = ROOT / "originbot_navigation" / "maps"
TRAJ = ROOT / "data" / "trajectories"
OUT_PNG = ROOT / "trajectories_waypoints_calibrated.png"

ROOM_PGM = MAPS / "room.pgm"
KEEPOUT_PGM = MAPS / "keepout_mask.pgm"
ROOM_YAML = MAPS / "room.yaml"

# ── 当前航点 (来自 competition_master_stage3.py, 2026-07-08 核对) ────
OLD = {
    "QR":      (0.41, -3.17),
    "Entry":   (0.37, -1.16),
    "P":       (-1.985, -0.014),
    # cruise_ccw (逆时针, even QR): WP1 -> WP2 -> VLM -> PostVLM
    "WP1":     (1.53, -1.51),
    "WP2":     (3.02, -1.06),
    "VLM":     (2.02,  0.94),
    "PostVLM": (1.02, -0.06),
}

# ── 质量过滤: 剔除 CRUISE 异常长(卡死/倒车)的运行, 其环道点是噪声 ──
#   2026-07-08: 20260708_184456 CRUISE=91.8s 在环道反复卡死+倒车,
#   点云不代表可行驶走廊. median跨18条对单outlier鲁棒, 但显式过滤更干净.
MAX_CRUISE_S = 40.0   # 保留 15/18 条干净巡航(<=40s), 丢弃 3 条最差(91.8/45.7/45.0)
# 每个航点用哪个阶段的数据、是否重校准
#   phase: CRUISE_CHANNEL / RETURN_P / None(保持不动)
CALIB_PLAN = {
    "QR":      (None, "车从未到达(检测到即取消), 锚定"),
    "Entry":   ("CRUISE_CHANNEL", "巡航起点"),
    "WP1":     ("CRUISE_CHANNEL", "巡航路点1"),
    "WP2":     ("CRUISE_CHANNEL", "巡航路点2(日志lethal失败点)"),
    "VLM":     (None, "语义拍照点, 环顶已在走廊上, 锚定"),
    "PostVLM": ("RETURN_P",       "返航首段路点3"),
    "P":       (None, "带容差的终点目标, 实际停车天然短~容差, 锚定"),
}


def read_yaml_origin(path):
    d = {}
    for line in Path(path).read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.split("#")[0].strip()
        if line.startswith("resolution:"):
            d["res"] = float(line.split(":", 1)[1])
        elif line.startswith("origin:"):
            vals = line.split(":", 1)[1].strip().strip("[]")
            parts = [float(v) for v in vals.split(",")]
            d["ox"], d["oy"] = parts[0], parts[1]
    return d["res"], d["ox"], d["oy"]


def load_pgm(path):
    return np.asarray(Image.open(path).convert("L"), dtype=np.float32)


def load_runs():
    """返回 list[dict(dir, pts=Nx2, state=list)] 仅 DONE 运行."""
    runs = []
    for csv_path in sorted(TRAJ.glob("trajectory_*.csv")):
        if csv_path.name.endswith("_plans.csv"):
            continue
        sm = csv_path.with_name(csv_path.stem + "_summary.json")
        direction = "CCW"
        final_state = "DONE"
        cruise_s = None
        if sm.exists():
            j = json.loads(sm.read_text(encoding="utf-8", errors="ignore"))
            final_state = j.get("final_state", "?")
            qd = j.get("qr_direction", "")
            direction = "CW" if "顺" in qd else "CCW"
            cruise_s = j.get("phase_times_s", {}).get("CRUISE_CHANNEL")
        if final_state != "DONE":
            continue
        # 质量过滤: CRUISE 异常长 = 环道卡死, 点云是噪声, 排除
        if cruise_s is not None and cruise_s > MAX_CRUISE_S:
            print(f"[跳过] {csv_path.stem} CRUISE={cruise_s:.1f}s > {MAX_CRUISE_S}s (环道卡死, 点云不可信)")
            continue
        xs, ys, st = [], [], []
        with open(csv_path, newline="", encoding="utf-8", errors="ignore") as f:
            for row in csv.DictReader(f):
                try:
                    xs.append(float(row["x_m"])); ys.append(float(row["y_m"]))
                    st.append(row["state"])
                except (KeyError, ValueError):
                    continue
        if xs:
            runs.append({"dir": direction,
                         "pts": np.column_stack([xs, ys]),
                         "state": np.array(st)})
    return runs


def phase_cloud(runs, phase, direction="CCW"):
    """汇总指定方向+阶段的所有轨迹点云."""
    chunks = [r["pts"][r["state"] == phase]
              for r in runs if r["dir"] == direction]
    chunks = [c for c in chunks if len(c)]
    return np.vstack(chunks) if chunks else np.empty((0, 2))


def snap_free(x, y, keepout, res, ox, oy):
    """若 (x,y) 不在可行驶区(kp!=254), 螺旋外推到最近可行驶格."""
    h, w = keepout.shape

    def blocked(px, py):
        col = int((px - ox) / res)
        row = int((py - oy) / res)
        if not (0 <= col < w and 0 <= row < h):
            return True
        return keepout[h - 1 - row, col] != 254    # 254=可行驶; 0=keepout,205=外部

    if not blocked(x, y):
        return x, y, False
    for r_cell in range(1, 25):
        for ang in range(0, 360, 15):
            nx = x + r_cell * res * math.cos(math.radians(ang))
            ny = y + r_cell * res * math.sin(math.radians(ang))
            if not blocked(nx, ny):
                return nx, ny, True
    return x, y, True


def recalibrate(name, phase, runs, keepout, res, ox, oy):
    """逐 run 最近点中位数: 每条轨迹取离原航点最近的实际点, 再componentwise中位数.
    比邻域平均更能贴合弯道顶点, 且对离群走廊质量不敏感."""
    ox0, oy0 = OLD[name]
    closest = []
    for r in runs:
        if r["dir"] != "CCW":
            continue
        pts = r["pts"][r["state"] == phase]
        if len(pts) == 0:
            continue
        d = np.hypot(pts[:, 0] - ox0, pts[:, 1] - oy0)
        closest.append(pts[int(np.argmin(d))])
    if not closest:
        return (ox0, oy0), 0, False
    arr = np.array(closest)
    nx, ny = float(np.median(arr[:, 0])), float(np.median(arr[:, 1]))
    nx, ny, snapped = snap_free(nx, ny, keepout, res, ox, oy)
    return (round(nx, 3), round(ny, 3)), len(arr), snapped


# ═══════════════════════════════════════════════════════════════════
def main():
    res, ox, oy = read_yaml_origin(ROOM_YAML)
    room = load_pgm(ROOM_PGM)
    keepout = load_pgm(KEEPOUT_PGM)
    h, w = room.shape
    extent = [ox, ox + w * res, oy, oy + h * res]

    runs = load_runs()
    n_ccw = sum(r["dir"] == "CCW" for r in runs)
    print(f"[载入] {len(runs)} 条 DONE 轨迹 (CCW={n_ccw}, CW={len(runs)-n_ccw})")

    # ── 重校准 ──
    new = {}
    meta = {}
    for name, (phase, note) in CALIB_PLAN.items():
        if phase is None:
            new[name] = OLD[name]; meta[name] = (0, False, note)
            continue
        pt, nsel, snapped = recalibrate(name, phase, runs, keepout, res, ox, oy)
        new[name] = pt; meta[name] = (nsel, snapped, note)

    # ── 打印对照表 ──
    print("\n{:<9} {:>16} {:>16} {:>8} {}".format(
        "航点", "旧(x,y)", "新(x,y)", "位移m", "依据"))
    print("-" * 78)
    for name in OLD:
        ox0, oy0 = OLD[name]; nx, ny = new[name]
        dist = math.hypot(nx - ox0, ny - oy0)
        nsel, snapped, note = meta[name]
        tag = " [snap]" if snapped else ""
        print("{:<9} {:>16} {:>16} {:>8.3f} {}{}".format(
            name, f"({ox0:.2f},{oy0:.2f})", f"({nx:.2f},{ny:.2f})",
            dist, note, tag))

    # ── 绘图: room + keepout 底图 (复刻 plot_trajectory 配方) ──
    plt.rcParams["font.family"] = "DejaVu Sans"
    fig, ax = plt.subplots(figsize=(13, 11))

    # 可行驶区(kp==254)浅色, 其余(墙/外部)深一点; keepout(kp==0)叠红
    drive_viz = np.where(keepout == 254, 0.0, 0.5)      # 254→白(0), 其余→灰
    ax.imshow(np.flipud(drive_viz), extent=extent, cmap="gray",
              origin="lower", alpha=0.35, vmin=0, vmax=1)
    kp_viz = np.where(keepout == 0, 1.0, np.nan)        # 硬keepout→红
    ax.imshow(np.flipud(kp_viz), extent=extent, cmap="Reds",
              origin="lower", alpha=0.28, vmin=0, vmax=1)

    # 成功轨迹 (context, 压成淡灰)
    for r in runs:
        if r["dir"] != "CCW":
            continue
        ax.plot(r["pts"][:, 0], r["pts"][:, 1], "-", color="#4a90d9",
                lw=0.8, alpha=0.20, zorder=3)
    ax.plot([], [], "-", color="#4a90d9", alpha=0.5, lw=1.2,
            label=f"DONE trajectories (CCW, n={n_ccw})")

    # 新巡航路线顺序 (Entry->WP1->WP2->VLM->PostVLM->P)
    order = ["Entry", "WP1", "WP2", "VLM", "PostVLM", "P"]
    rx = [new[n][0] for n in order]; ry = [new[n][1] for n in order]
    ax.plot(rx, ry, "--", color="#1a5fb4", lw=1.6, alpha=0.7,
            zorder=6, label="New route (CCW)")

    # 旧航点: 中性灰空心星
    for name, (x, y) in OLD.items():
        ax.plot(x, y, "*", ms=15, mfc="none", mec="#888888",
                mew=1.8, zorder=7)
    ax.plot([], [], "*", ms=13, mfc="none", mec="#888888", mew=1.8,
            label="Old waypoints")

    # 旧->新 箭头 + 新航点(强蓝实心)
    for name in OLD:
        ox0, oy0 = OLD[name]; nx, ny = new[name]
        if math.hypot(nx - ox0, ny - oy0) > 0.03:
            ax.add_patch(FancyArrowPatch(
                (ox0, oy0), (nx, ny), arrowstyle="-|>", mutation_scale=13,
                color="#e66100", lw=1.6, alpha=0.9, zorder=8))
        ax.plot(nx, ny, "*", ms=17, mfc="#1c71d8", mec="black",
                mew=1.4, zorder=9)
        ax.annotate(f"{name}\n({nx:.2f},{ny:.2f})", (nx, ny),
                    textcoords="offset points", xytext=(9, 7),
                    fontsize=8.5, fontweight="bold", color="#0b3d66",
                    zorder=10)
    ax.plot([], [], "*", ms=15, mfc="#1c71d8", mec="black", mew=1.4,
            label="New waypoints (data-calibrated)")
    ax.plot([], [], "-", color="#e66100", lw=1.6, label="Shift (old->new)")

    ax.set_xlabel("X (m)"); ax.set_ylabel("Y (m)")
    ax.set_title("Nav2 Waypoints Recalibrated from 15 DONE Trajectories (CCW)")
    ax.set_aspect("equal")
    ax.grid(True, color="#cccccc", lw=0.5, alpha=0.5)
    ax.legend(loc="lower left", fontsize=8, framealpha=0.9)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=200, bbox_inches="tight")
    print(f"\n[输出] {OUT_PNG}")

    # ── 可粘贴参数块 (仅 CCW; CW 无数据保持原值) ──
    print("\n─── cruise_ccw 建议值 (competition_master_stage3.py) ───")
    for n in ["WP1", "WP2", "VLM", "PostVLM"]:
        print(f"    {new[n][0]:.2f}, {new[n][1]:.2f}, 0.0,    # {n}")
    print(f"  entry_point: ({new['Entry'][0]:.2f}, {new['Entry'][1]:.2f})")
    print(f"  p_point:     ({new['P'][0]:.3f}, {new['P'][1]:.3f})")


if __name__ == "__main__":
    main()
