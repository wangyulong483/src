#!/usr/bin/env python3
"""
Plot trajectory CSV on top of room.pgm + keepout overlay.
ROS map_server convention: PGM pixel(0,0)=top-left, origin=world_xy of bottom-left pixel.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from pathlib import Path
import csv

HERE = Path(__file__).parent.parent
MAP_ROOM_PGM = HERE / "maps" / "room.pgm"
MAP_KEEPOUT_PGM = HERE / "maps" / "keepout_mask.pgm"
MAP_ROOM_YAML = HERE / "maps" / "room.yaml"
MAP_KEEPOUT_YAML = HERE / "maps" / "keepout_mask.yaml"
TRAJ_CSV = Path("C:/Users/27826/Desktop/src/trajectory.csv")
OUT = Path("C:/Users/27826/Desktop/src/trajectory_plot.png")


def read_pgm(path):
    with open(path, 'rb') as f:
        assert f.readline().strip() == b'P5'
        w, h = map(int, f.readline().split())
        maxval = int(f.readline().strip())
        data = np.frombuffer(f.read(), dtype=np.uint8 if maxval < 256 else np.uint16)
        return data.reshape(h, w)  # row-major: rows=height, cols=width


def read_yaml_origin(path):
    """Return (resolution_m, origin_x_m, origin_y_m)."""
    import yaml
    with open(path) as f:
        d = yaml.safe_load(f)
    return float(d['resolution']), float(d['origin'][0]), float(d['origin'][1])


def world_to_pixel(x, y, res, ox, oy, img_h):
    """World (x,y) -> PGM pixel (col, row). row=0 is top of image."""
    col = int(round((x - ox) / res))
    row = img_h - 1 - int(round((y - oy) / res))
    return col, row


def main():
    # ======== load maps ========
    room_img = read_pgm(MAP_ROOM_PGM).astype(float)
    kp_img = read_pgm(MAP_KEEPOUT_PGM).astype(float)
    res, ox, oy = read_yaml_origin(MAP_ROOM_YAML)

    h, w = room_img.shape  # h=141, w=163
    # extent for origin='lower': [xmin, xmax, ymin, ymax]
    extent = [ox, ox + w * res, oy, oy + h * res]

    # ======== load trajectory ========
    pts = []
    if TRAJ_CSV.exists():
        with open(TRAJ_CSV) as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                pts.append((float(row[1]), float(row[2])))
    pts = np.array(pts) if pts else np.empty((0, 2))
    n = len(pts)

    # ======== smooth spline if enough points ========
    if n > 4:
        t = np.linspace(0, 1, n)
        try:
            spl_x = UnivariateSpline(t, pts[:, 0], s=0.3)
            spl_y = UnivariateSpline(t, pts[:, 1], s=0.3)
            td = np.linspace(0, 1, n * 8)
            smooth = np.column_stack([spl_x(td), spl_y(td)])
        except Exception:
            smooth = pts
    else:
        smooth = pts

    # ======== plot ========
    fig, ax = plt.subplots(figsize=(12, 10))

    # Room map background (trinary: 0=free, 100=occupied, -1=unknown)
    # occupied=dark, free=white
    room_viz = np.where(room_img <= 25, 1.0,  # free
               np.where(room_img >= 65, 0.0, 0.5))  # occupied / unknown
    ax.imshow(np.flipud(room_viz), extent=extent, cmap='gray', origin='lower',
              alpha=0.45, vmin=0, vmax=1)

    # Keepout mask overlay (red): occupied cells are white (255) in this PGM
    kp_viz = np.where(kp_img >= 128, 1.0, np.nan)
    ax.imshow(np.flipud(kp_viz), extent=extent, cmap='Reds', origin='lower',
              alpha=0.35, vmin=0, vmax=1)

    # Trajectory
    if len(smooth) > 0:
        ax.plot(smooth[:, 0], smooth[:, 1], '-', color='#1f77b4',
                linewidth=2.1, label=f'Trajectory ({n} poses)', zorder=5)
        ax.plot(pts[:, 0], pts[:, 1], '.', color='#1f77b4',
                markersize=3, alpha=0.5, zorder=4)
        # Start / end markers
        ax.plot(pts[0, 0], pts[0, 1], 'o', color='lime',
                markersize=10, markeredgecolor='black', zorder=6,
                label=f'Start P ({pts[0,0]:.2f},{pts[0,1]:.2f})')
        ax.plot(pts[-1, 0], pts[-1, 1], 's', color='red',
                markersize=10, markeredgecolor='black', zorder=6,
                label=f'End ({pts[-1,0]:.2f},{pts[-1,1]:.2f})')

    # Key waypoints
    kw = {'QR (0.41,-3.17)': (0.41, -3.17),
          'Entry (0.38,-1.10)': (0.38, -1.10),
          'P (-1.99,-0.01)': (-1.99, -0.01)}
    for name, (kx, ky) in kw.items():
        ax.plot(kx, ky, '*', markersize=14, markeredgecolor='black',
                markerfacecolor='yellow', zorder=7)
    # Annotate only P point to avoid clutter
    ax.annotate('P', (-1.99, -0.01), textcoords="offset points",
                xytext=(8, -12), fontsize=10, weight='bold')
    ax.annotate('QR', (0.41, -3.17), textcoords="offset points",
                xytext=(8, -12), fontsize=10, weight='bold')
    ax.annotate('Entry', (0.38, -1.10), textcoords="offset points",
                xytext=(8, -12), fontsize=10, weight='bold')

    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_title(f'Stage3 Trajectory — 94.1s DONE ({n} poses)')
    ax.legend(loc='lower left', fontsize=8)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.25)
    ax.set_xlim(ox, ox + w * res)
    ax.set_ylim(oy, oy + h * res)

    fig.savefig(OUT, dpi=180, bbox_inches='tight')
    plt.close()
    print(f"Saved: {OUT}  ({n} trajectory points)")


if __name__ == '__main__':
    main()
