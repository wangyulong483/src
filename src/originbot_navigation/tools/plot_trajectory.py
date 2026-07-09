#!/usr/bin/env python3
"""
Plot trajectory CSV on room.pgm + multi-panel analysis charts.

Usage:
    python plot_trajectory.py                          # auto-find latest CSV
    python plot_trajectory.py trajectory.csv           # specific file
    python plot_trajectory.py trajectory.csv --nodpi   # skip high-DPI
    python plot_trajectory.py --list                   # list available CSVs

Supports:
  - Old format:  timestamp,x,y,yaw
  - New format:  elapsed_s,x_m,y_m,yaw_rad,state,cmd_vx,cmd_wz,
                 plan_pts,plan_len_m,plan_end_x,plan_end_y,
                 cpu_pct,mem_pct,cpu_temp_c

Outputs:
  - trajectory_analysis.png   (4-panel analysis)
  - trajectory_map.png        (standalone map overlay)
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from pathlib import Path
import csv
import sys
import json
import os

# ── Paths ─────────────────────────────────────────────────────
HERE = Path(__file__).parent.parent
MAP_ROOM_PGM = HERE / "maps" / "room.pgm"
MAP_KEEPOUT_PGM = HERE / "maps" / "keepout_mask.pgm"
MAP_ROOM_YAML = HERE / "maps" / "room.yaml"

# Search dirs for CSV files
SEARCH_DIRS = [
    Path("/userdata/dev_ws"),
    Path("C:/Users/27826/Desktop/src"),
    Path("."),
]

# ── State color map ───────────────────────────────────────────
STATE_COLORS = {
    'INIT':           '#999999',
    'NAV_TO_QR':      '#1f77b4',
    'NAV_TO_ENTRY':   '#ff7f0e',
    'BACKING_UP':     '#9467bd',
    'CRUISE_CHANNEL': '#2ca02c',
    'RETURN_P':       '#d62728',
    'DONE':           '#17becf',
    'TIMEOUT':        '#7f7f7f',
}
FALLBACK_COLORS = ['#e377c2','#bcbd22','#8c564b','#7b4173','#a5512e',
                   '#5254a3','#637939','#8ca252','#b5cf6b','#cedb9c']


# ═══════════════════════════════════════════════════════════════
# Map helpers
# ═══════════════════════════════════════════════════════════════

def read_pgm(path):
    with open(path, 'rb') as f:
        assert f.readline().strip() == b'P5'
        w, h = map(int, f.readline().split())
        maxval = int(f.readline().strip())
        data = np.frombuffer(f.read(), dtype=np.uint8 if maxval < 256 else np.uint16)
        return data.reshape(h, w)


def read_yaml_origin(path):
    import yaml
    with open(path) as f:
        d = yaml.safe_load(f)
    return float(d['resolution']), float(d['origin'][0]), float(d['origin'][1])


def find_latest_csv():
    """Find the most recent trajectory CSV across search dirs."""
    candidates = []
    for d in SEARCH_DIRS:
        if not d.exists():
            continue
        for p in d.glob('trajectory_*.csv'):
            candidates.append((p.stat().st_mtime, p))
        # also check legacy name
        legacy = d / 'trajectory.csv'
        if legacy.exists():
            candidates.append((legacy.stat().st_mtime, legacy))
    if not candidates:
        # try local dir
        for p in Path('.').glob('trajectory*.csv'):
            candidates.append((p.stat().st_mtime, p))
    if not candidates:
        print("ERROR: No trajectory CSV found. Searched:", [str(d) for d in SEARCH_DIRS])
        return None
    candidates.sort(reverse=True)
    return candidates[0][1]


def list_csvs():
    """List all available trajectory CSV files."""
    found = []
    for d in SEARCH_DIRS:
        if not d.exists():
            continue
        for p in sorted(d.glob('trajectory*.csv')):
            mtime = p.stat().st_mtime
            size_kb = p.stat().st_size / 1024
            found.append((mtime, p, size_kb))
    if not found:
        print("No trajectory CSV files found.")
        return
    found.sort(reverse=True)
    print(f"{'Age':>12s}  {'Size':>8s}  Path")
    print("-" * 60)
    now = os.path.getmtime(__file__) if False else max(f[0] for f in found)
    for mtime, p, size_kb in found:
        age = now - mtime
        if age < 3600:
            age_str = f"{age/60:.0f}m ago"
        elif age < 86400:
            age_str = f"{age/3600:.1f}h ago"
        else:
            age_str = f"{age/86400:.0f}d ago"
        print(f"{age_str:>12s}  {size_kb:>6.1f}KB  {p}")


# ═══════════════════════════════════════════════════════════════
# CSV parsing
# ═══════════════════════════════════════════════════════════════

def parse_csv(path):
    """Parse trajectory CSV. Returns (is_rich, data_dict).
    data_dict keys: elapsed, x, y, yaw, [state, cmd_vx, cmd_wz,
                     plan_pts, plan_len, plan_ex, plan_ey,
                     cpu, mem, cpu_temp]
    """
    rows = []
    with open(path, newline='') as f:
        reader = csv.reader(f)
        header = next(reader, None)
        if header is None:
            return False, _empty_data()

        # detect format
        is_rich = 'elapsed_s' in header[0] or 'state' in (h.lower() for h in header)

        for row in reader:
            if not row or row[0].startswith('#'):
                continue
            rows.append(row)

    if not rows:
        return is_rich, _empty_data()

    if is_rich:
        return True, _parse_rich(rows)
    else:
        return False, _parse_old(rows)


def _empty_data():
    return {'elapsed': np.array([]), 'x': np.array([]), 'y': np.array([]),
            'yaw': np.array([]), 'state': [], 'cmd_vx': np.array([]),
            'cmd_wz': np.array([]), 'plan_pts': np.array([]),
            'plan_len': np.array([]), 'plan_ex': np.array([]),
            'plan_ey': np.array([]), 'cpu': np.array([]),
            'mem': np.array([]), 'cpu_temp': np.array([])}


def _parse_old(rows):
    """Old format: timestamp,x,y,yaw"""
    n = len(rows)
    elapsed = np.zeros(n); x = np.zeros(n); y = np.zeros(n); yaw = np.zeros(n)
    t0 = float(rows[0][0])
    for i, row in enumerate(rows):
        ts = float(row[0])
        elapsed[i] = ts - t0
        x[i] = float(row[1])
        y[i] = float(row[2])
        yaw[i] = float(row[3])

    d = _empty_data()
    d['elapsed'] = elapsed; d['x'] = x; d['y'] = y; d['yaw'] = yaw
    d['state'] = ['UNKNOWN'] * n
    return d


def _parse_rich(rows):
    """New format: elapsed_s,x_m,y_m,yaw_rad,state,cmd_vx,cmd_wz,
       plan_pts,plan_len_m,plan_end_x,plan_end_y,cpu_pct,mem_pct,cpu_temp_c"""
    n = len(rows)
    d = {
        'elapsed':  np.zeros(n), 'x': np.zeros(n), 'y': np.zeros(n),
        'yaw': np.zeros(n), 'state': [''] * n,
        'cmd_vx': np.zeros(n), 'cmd_wz': np.zeros(n),
        'plan_pts': np.zeros(n, dtype=int), 'plan_len': np.zeros(n),
        'plan_ex': np.zeros(n), 'plan_ey': np.zeros(n),
        'cpu': np.zeros(n, dtype=int), 'mem': np.zeros(n, dtype=int),
        'cpu_temp': np.zeros(n, dtype=int),
    }
    for i, row in enumerate(rows):
        d['elapsed'][i] = float(row[0])
        d['x'][i] = float(row[1])
        d['y'][i] = float(row[2])
        d['yaw'][i] = float(row[3])
        d['state'][i] = row[4]
        d['cmd_vx'][i] = float(row[5])
        d['cmd_wz'][i] = float(row[6])
        d['plan_pts'][i] = int(row[7])
        d['plan_len'][i] = float(row[8])
        d['plan_ex'][i] = float(row[9])
        d['plan_ey'][i] = float(row[10])
        d['cpu'][i] = int(float(row[11]))
        d['mem'][i] = int(float(row[12]))
        d['cpu_temp'][i] = int(float(row[13]))
    return d


# ═══════════════════════════════════════════════════════════════
# State segment helpers
# ═══════════════════════════════════════════════════════════════

def state_segments(elapsed, state_list):
    """Yield (state_name, start_idx, end_idx, color) for each contiguous segment."""
    if not state_list:
        return
    states = np.array(state_list)
    boundaries = np.where(states[:-1] != states[1:])[0] + 1
    seg_starts = np.concatenate([[0], boundaries])
    seg_ends = np.concatenate([boundaries, [len(states)]])

    for start, end in zip(seg_starts, seg_ends):
        sname = states[start]
        color = STATE_COLORS.get(sname, FALLBACK_COLORS[
            hash(sname) % len(FALLBACK_COLORS)])
        yield sname, start, end, color


def state_transitions(elapsed, state_list):
    """Return list of (elapsed, old_state, new_state) for each transition."""
    if len(state_list) < 2:
        return []
    transitions = []
    prev = state_list[0]
    for i in range(1, len(state_list)):
        cur = state_list[i]
        if cur != prev:
            transitions.append((elapsed[i], prev, cur))
            prev = cur
    return transitions


# ═══════════════════════════════════════════════════════════════
# Summary info
# ═══════════════════════════════════════════════════════════════

def load_summary(csv_path):
    """Try to load matching summary JSON."""
    stem = str(csv_path).replace('.csv', '')
    json_path = Path(stem + '_summary.json')
    if json_path.exists():
        with open(json_path, encoding='utf-8') as f:
            return json.load(f)
    return None


# ═══════════════════════════════════════════════════════════════
# Plotting
# ═══════════════════════════════════════════════════════════════

def plot_map_overlay(ax, data, room_img, kp_img, res, ox, oy, w, h,
                     is_rich, n, csv_path):
    """Plot trajectory on map background."""
    extent = [ox, ox + w * res, oy, oy + h * res]

    # room background
    room_viz = np.where(room_img <= 25, 1.0,
               np.where(room_img >= 65, 0.0, 0.5))
    ax.imshow(np.flipud(room_viz), extent=extent, cmap='gray', origin='lower',
              alpha=0.45, vmin=0, vmax=1)

    # keepout overlay
    kp_viz = np.where(kp_img >= 128, 1.0, np.nan)
    ax.imshow(np.flipud(kp_viz), extent=extent, cmap='Reds', origin='lower',
              alpha=0.35, vmin=0, vmax=1)


    x_vals = data['x']; y_vals = data['y']

    if is_rich and len(x_vals) > 0:
        # color by state
        for sname, start, end, color in state_segments(
                data['elapsed'], data['state']):
            seg_x = x_vals[start:end+1]
            seg_y = y_vals[start:end+1]
            if len(seg_x) < 2:
                continue
            ax.plot(seg_x, seg_y, '-', color=color, linewidth=2.1,
                    alpha=0.9, label=sname, zorder=5)
        # deduplicate legend
        handles, labels = ax.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        ax.legend(by_label.values(), by_label.keys(),
                  loc='lower left', fontsize=7, ncol=2)
    elif len(x_vals) > 1:
        ax.plot(x_vals, y_vals, '-', color='#1f77b4', linewidth=2.1,
                label=f'Trajectory ({n} poses)', zorder=5)
        ax.plot(x_vals, y_vals, '.', color='#1f77b4',
                markersize=3, alpha=0.5, zorder=4)

    # start/end markers
    if len(x_vals) > 0:
        ax.plot(x_vals[0], y_vals[0], 'o', color='lime',
                markersize=10, markeredgecolor='black', zorder=6,
                label=f'Start ({x_vals[0]:.2f},{y_vals[0]:.2f})')
        ax.plot(x_vals[-1], y_vals[-1], 's', color='red',
                markersize=10, markeredgecolor='black', zorder=6,
                label=f'End ({x_vals[-1]:.2f},{y_vals[-1]:.2f})')

    # Waypoints
    kw = [('QR', 0.41, -3.17), ('Entry', 0.38, -1.10), ('P', -1.99, -0.01)]
    for name, kx, ky in kw:
        ax.plot(kx, ky, '*', markersize=14, markeredgecolor='black',
                markerfacecolor='yellow', zorder=7)
        ax.annotate(name, (kx, ky), textcoords="offset points",
                    xytext=(8, -12), fontsize=10, weight='bold')

    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.25)
    ax.set_xlim(ox, ox + w * res)
    ax.set_ylim(oy, oy + h * res)

    # title
    title = f'Trajectory — {csv_path.name} ({n} pts)'
    summary = load_summary(csv_path)
    if summary:
        title = (f"Trajectory — {summary.get('final_state','?')} "
                 f"in {summary.get('elapsed_total_s','?')}s "
                 f"({summary.get('exit_reason','?')})  [{n} pts]")
    ax.set_title(title, fontsize=10)


def plot_velocity(ax, data, transitions):
    """Plot cmd_vx and cmd_wz vs elapsed time."""
    t = data['elapsed']
    ax.plot(t, data['cmd_vx'], '-', color='#1f77b4', linewidth=0.8,
            alpha=0.8, label='cmd_vx (m/s)')
    ax.plot(t, data['cmd_wz'], '-', color='#d62728', linewidth=0.8,
            alpha=0.8, label='cmd_wz (rad/s)')
    ax.axhline(y=0, color='gray', linewidth=0.5, linestyle='--')
    ax.set_ylabel('Velocity')
    ax.legend(loc='upper right', fontsize=7, ncol=2)
    ax.grid(True, alpha=0.2)

    # state transitions as vertical lines
    for et, _old_s, _new_s in transitions:
        ax.axvline(x=et, color='gray', linewidth=0.5, linestyle=':',
                   alpha=0.5)

    # state background bands
    _add_state_bands(ax, data, alpha=0.06)


def plot_plan(ax, data, transitions):
    """Plot plan metrics vs elapsed time."""
    t = data['elapsed']
    ax2 = ax.twinx()
    ax.fill_between(t, 0, data['plan_pts'], alpha=0.2, color='#2ca02c',
                    label='plan_pts')
    ax.plot(t, data['plan_pts'], '-', color='#2ca02c', linewidth=0.8,
            alpha=0.7, label='plan pts')
    ax2.plot(t, data['plan_len'], '-', color='#9467bd', linewidth=1.2,
             alpha=0.8, label='plan_len (m)')

    ax.set_ylabel('Plan points', color='#2ca02c')
    ax2.set_ylabel('Plan length (m)', color='#9467bd')
    ax.tick_params(axis='y', labelcolor='#2ca02c')
    ax2.tick_params(axis='y', labelcolor='#9467bd')

    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, loc='upper right',
              fontsize=7)
    ax.grid(True, alpha=0.2)

    for et, _old_s, _new_s in transitions:
        ax.axvline(x=et, color='gray', linewidth=0.5, linestyle=':',
                   alpha=0.5)
    _add_state_bands(ax, data, alpha=0.06)


def plot_resources(ax, data, transitions):
    """Plot CPU, memory, temperature vs elapsed time."""
    t = data['elapsed']

    # CPU usage
    cpu_valid = data['cpu'] >= 0
    if cpu_valid.any():
        ax.plot(t[cpu_valid], data['cpu'][cpu_valid], '-',
                color='#1f77b4', linewidth=1.0, alpha=0.8, label='CPU %')

    # Memory
    mem_valid = data['mem'] >= 0
    if mem_valid.any():
        ax.plot(t[mem_valid], data['mem'][mem_valid], '-',
                color='#ff7f0e', linewidth=1.0, alpha=0.8, label='MEM %')

    # CPU Temp
    temp_valid = data['cpu_temp'] >= 0
    if temp_valid.any():
        ax.plot(t[temp_valid], data['cpu_temp'][temp_valid], '-',
                color='#d62728', linewidth=1.0, alpha=0.8, label='CPU Temp °C')

    ax.set_ylabel('Value')
    ax.legend(loc='upper right', fontsize=7)
    ax.grid(True, alpha=0.2)

    for et, _old_s, _new_s in transitions:
        ax.axvline(x=et, color='gray', linewidth=0.5, linestyle=':',
                   alpha=0.5)
    _add_state_bands(ax, data, alpha=0.06)


def _add_state_bands(ax, data, alpha=0.06):
    """Add light background bands for state regions."""
    for sname, start, end, color in state_segments(
            data['elapsed'], data['state']):
        t0 = data['elapsed'][start]
        t1 = data['elapsed'][min(end, len(data['elapsed']) - 1)]
        ax.axvspan(t0, t1, facecolor=color, alpha=alpha, zorder=0)


def plot_analysis(data, is_rich, csv_path, out_dir, no_dpi=False):
    """Generate 4-panel analysis figure."""
    n = len(data['elapsed'])
    if n == 0:
        print("ERROR: No data points to plot.")
        return

    transitions = state_transitions(data['elapsed'], data['state']) if is_rich else []

    # ── Load maps ──────────────────────────────────────────
    try:
        room_img = read_pgm(MAP_ROOM_PGM).astype(float)
        kp_img = read_pgm(MAP_KEEPOUT_PGM).astype(float)
        res, ox, oy = read_yaml_origin(MAP_ROOM_YAML)
        h, w = room_img.shape
    except FileNotFoundError as e:
        print(f"WARNING: Map files not found ({e}), skipping map overlay")
        room_img = None

    dpi = 150 if not no_dpi else 72

    # ── Panel 1: Map overlay ───────────────────────────────
    fig_map, ax_map = plt.subplots(figsize=(12, 10))
    if room_img is not None:
        plot_map_overlay(ax_map, data, room_img, kp_img,
                         res, ox, oy, w, h, is_rich, n, csv_path)
    out_map = out_dir / f'{csv_path.stem}_map.png'
    fig_map.savefig(out_map, dpi=dpi, bbox_inches='tight')
    plt.close(fig_map)
    print(f"  Map:   {out_map}")

    if not is_rich:
        print("  (old CSV format — only map plot; no time-series panels)")
        return

    # ── Multi-panel analysis ───────────────────────────────
    fig = plt.figure(figsize=(16, 12))
    gs = GridSpec(3, 1, figure=fig, hspace=0.35,
                  height_ratios=[1, 1, 1])

    ax_vel = fig.add_subplot(gs[0])
    ax_plan = fig.add_subplot(gs[1])
    ax_res = fig.add_subplot(gs[2])

    plot_velocity(ax_vel, data, transitions)
    plot_plan(ax_plan, data, transitions)
    plot_resources(ax_res, data, transitions)

    # shared x-axis labels
    ax_res.set_xlabel('Elapsed time (s)')

    # titles
    ax_vel.set_title('Velocity Commands (cmd_vel_muxed)', fontsize=10,
                     fontweight='bold')
    ax_plan.set_title('Planner Output (Global Plan)', fontsize=10,
                      fontweight='bold')
    ax_res.set_title('System Resources', fontsize=10, fontweight='bold')

    # super title
    summary = load_summary(csv_path)
    super_title = f'Stage3 Analysis — {csv_path.name}'
    if summary:
        super_title = (f"Stage3 Analysis — exit={summary.get('exit_reason','?')} "
                       f"state={summary.get('final_state','?')} "
                       f"{summary.get('elapsed_total_s','?')}s")
    fig.suptitle(super_title, fontsize=12, fontweight='bold', y=0.995)

    out_analysis = out_dir / f'{csv_path.stem}_analysis.png'
    fig.savefig(out_analysis, dpi=dpi, bbox_inches='tight')
    plt.close(fig)
    print(f"  Analysis: {out_analysis}")


# ═══════════════════════════════════════════════════════════════
# main
# ═══════════════════════════════════════════════════════════════

def main():
    no_dpi = '--nodpi' in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith('--')]

    if '--list' in sys.argv or '-l' in sys.argv:
        list_csvs()
        return

    # find CSV
    if args:
        csv_path = Path(args[0])
    else:
        csv_path = find_latest_csv()
        if csv_path is None:
            sys.exit(1)

    if not csv_path.exists():
        print(f"ERROR: {csv_path} not found.")
        sys.exit(1)

    print(f"Loading: {csv_path}")
    is_rich, data = parse_csv(csv_path)
    n = len(data['elapsed'])
    fmt = "rich (14 cols)" if is_rich else "old (4 cols)"
    print(f"  Format: {fmt}, {n} points, "
          f"{data['elapsed'][-1]:.1f}s" if n > 0 else "  Format: {fmt}, 0 points")

    if is_rich and n > 0:
        states_seen = sorted(set(data['state']))
        print(f"  States: {', '.join(states_seen)}")
        if data['cpu'].max() >= 0:
            print(f"  CPU:    {data['cpu'][data['cpu']>=0].mean():.0f}% avg, "
                  f"max={data['cpu'].max()}%")
        if data['mem'].max() >= 0:
            print(f"  MEM:    {data['mem'][data['mem']>=0].mean():.0f}% avg, "
                  f"max={data['mem'].max()}%")
        if data['cpu_temp'].max() >= 0:
            print(f"  Temp:   {data['cpu_temp'][data['cpu_temp']>=0].mean():.0f}°C avg, "
                  f"max={data['cpu_temp'].max()}°C")

    summary = load_summary(csv_path)
    if summary:
        print(f"  Summary JSON found: {summary.get('exit_reason','?')} "
              f"→ {summary.get('final_state','?')}")

    # ★ 输出到 Z_PNG/outN/ (仿 YOLO 训练输出惯例)
    base_dir = Path("C:/Users/27826/Desktop/src/Z_PNG")
    base_dir.mkdir(parents=True, exist_ok=True)
    existing = sorted([int(d.name[3:]) for d in base_dir.iterdir()
                       if d.is_dir() and d.name.startswith('out') and d.name[3:].isdigit()])
    next_n = existing[-1] + 1 if existing else 1
    out_dir = base_dir / f"out{next_n}"
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"  Output: {out_dir}")
    plot_analysis(data, is_rich, csv_path, out_dir, no_dpi)


if __name__ == '__main__':
    main()
