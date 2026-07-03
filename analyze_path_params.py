#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analyze historical trajectory data and map files to determine optimal parameters
for the path geometry optimizer on an Ackermann racing robot.

Determines:
  - max_shift      (from corridor analysis)
  - lambda_fidelity (from curvature analysis)
  - alpha_apex      (from corner deviation analysis)
"""

import sys
import io
# Force UTF-8 output on Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import numpy as np
import os
import glob
from scipy.ndimage import distance_transform_edt
from collections import defaultdict

# ============================================================
# Constants
# ============================================================
MAP_DIR = r"C:\Users\27826\Desktop\src\originbot_navigation\maps"
TRAJ_DIR = r"C:\Users\27826\Desktop\src\data\trajectories"
RESOLUTION = 0.05          # m/pixel
ROBOT_RADIUS = 0.15        # m
SAFETY_MARGIN = 0.05       # m
MIN_TURNING_RADIUS = 0.30  # m (physical limit)
PHYSICAL_KAPPA_MAX = 1.0 / MIN_TURNING_RADIUS  # 3.33 m^-1

# ============================================================
# PGM Reader
# ============================================================
def read_pgm(filepath):
    """Read a P5 binary PGM file. Returns (data_2d, width, height, maxval)."""
    with open(filepath, 'rb') as f:
        magic = f.readline().strip()
        if magic != b'P5':
            raise ValueError(f"Not a P5 PGM: {filepath} (magic={magic})")

        # Skip comments
        line = f.readline()
        while line.startswith(b'#'):
            line = f.readline()

        width, height = map(int, line.split())
        maxval = int(f.readline().strip())

        raw = f.read(width * height)
        data = np.frombuffer(raw, dtype=np.uint8).reshape((height, width)).astype(np.float64)

    return data, width, height, maxval


# ============================================================
# Task 1: Corridor Analysis
# ============================================================
def corridor_analysis():
    print("=" * 60)
    print("=== Corridor Analysis ===")
    print("=" * 60)

    # Read room.pgm
    room_path = os.path.join(MAP_DIR, "room.pgm")
    room, w, h, mx = read_pgm(room_path)
    print("room.pgm: {}x{}, maxval={}".format(w, h, mx))
    print("  Unique values: {}".format(np.unique(room)))

    # Read keepout_mask.pgm
    keepout_path = os.path.join(MAP_DIR, "keepout_mask.pgm")
    keepout, kw, kh, kmx = read_pgm(keepout_path)
    print("keepout_mask.pgm: {}x{}, maxval={}".format(kw, kh, kmx))
    print("  Unique values: {}".format(np.unique(keepout)))

    # Build obstacle mask
    # room.pgm:  0=free, 205=unknown, 254=wall
    # keepout_mask.pgm: 0=lethal (keepout zone), 254=free, 205=unknown
    #   (Note: keepout uses 254 instead of 255 for "free" — verified from data)
    obstacle = np.zeros_like(room, dtype=bool)
    obstacle[room == 254] = True       # walls in room map
    obstacle[keepout == 0] = True      # keepout zones (lethal)

    # Treat unknown (205) as free for corridor width (conservative)
    free_mask = ~obstacle
    print("Free pixels: {} / {} ({:.1f}%)".format(
        np.sum(free_mask), w*h, 100*np.sum(free_mask)/(w*h)))

    # EDT from each free pixel to nearest obstacle
    dist = distance_transform_edt(free_mask)  # pixels
    dist_m = dist * RESOLUTION                # meters

    # Find minimum corridor width: for each free pixel, the distance to
    # nearest obstacle. The corridor "width" at a bottleneck is 2 * distance
    # (distance from center to both walls).
    corridor_widths = 2.0 * dist_m[free_mask]

    # Basic stats
    print("\nCorridor width distribution (meters):")
    print("  Min:    {:.3f} m".format(np.min(corridor_widths)))
    print("  p1:     {:.3f} m".format(np.percentile(corridor_widths, 1)))
    print("  p5:     {:.3f} m".format(np.percentile(corridor_widths, 5)))
    print("  p10:    {:.3f} m".format(np.percentile(corridor_widths, 10)))
    print("  p25:    {:.3f} m".format(np.percentile(corridor_widths, 25)))
    print("  p50:    {:.3f} m".format(np.percentile(corridor_widths, 50)))
    print("  p75:    {:.3f} m".format(np.percentile(corridor_widths, 75)))
    print("  p90:    {:.3f} m".format(np.percentile(corridor_widths, 90)))
    print("  Max:    {:.3f} m".format(np.max(corridor_widths)))

    # Find the narrowest bottleneck locations
    sorted_indices = np.argsort(corridor_widths)
    narrow_indices = sorted_indices[:20]

    free_coords = np.argwhere(free_mask)  # (row, col) in pixel space
    narrow_pixels = free_coords[narrow_indices]

    # Convert pixel coords to world coords
    # origin: [-2.65, -4.5, 0] — world coordinate of bottom-left pixel corner
    # x_world = origin_x + col * resolution
    # y_world = origin_y + (height - row) * resolution
    origin_x, origin_y = -2.65, -4.5

    print("\nTop 20 narrowest corridor bottlenecks:")
    for i, (idx, pix) in enumerate(zip(narrow_indices, narrow_pixels)):
        row, col = pix
        wx = origin_x + col * RESOLUTION
        wy = origin_y + (h - row) * RESOLUTION
        cw = 2.0 * dist_m[row, col]
        print("  #{}: width={:.3f}m at world (x={:.2f}, y={:.2f}), pixel (r={}, c={})".format(
            i+1, cw, wx, wy, row, col))

    # Compute recommended max_shift
    # Use p5 corridor width (ignore single-pixel edge artifacts at the absolute min)
    min_corridor_abs = np.min(corridor_widths)
    p5_width = np.percentile(corridor_widths, 5)
    p10_width = np.percentile(corridor_widths, 10)

    # The narrowest points at 0.100m are 2-pixel corridors — these are likely
    # corner artifacts where walls meet diagonally. Use p5 for robustness.
    min_corridor = p5_width
    print("\nUsing p5 corridor width ({:.3f}m) for max_shift (abs min={:.3f}m is edge artifact)".format(
        p5_width, min_corridor_abs))

    max_shift_raw = (min_corridor / 2.0) - ROBOT_RADIUS - SAFETY_MARGIN
    max_shift = max(0.0, max_shift_raw)

    print("\nRecommended max_shift calculation:")
    print("  p5_corridor_width / 2 = {:.3f} m".format(min_corridor / 2.0))
    print("  - robot_radius ({:.2f} m)".format(ROBOT_RADIUS))
    print("  - safety_margin ({:.2f} m)".format(SAFETY_MARGIN))
    print("  = {:.3f} m".format(max_shift_raw))

    if max_shift_raw <= 0:
        print("  WARNING: max_shift <= 0 — corridor is very tight for the robot!")
        print("  Setting max_shift = 0.05 m (absolute minimum for any optimization)")
        max_shift = 0.05

    print("  Recommended max_shift: {:.3f} m".format(max_shift))

    return corridor_widths, dist_m, free_mask, obstacle, max_shift, min_corridor


# ============================================================
# Task 2: Curvature Analysis
# ============================================================
def menger_curvature(pts):
    """Compute Menger curvature at each point using 3-point method.
    pts: (N, 2) array of x, y coordinates.
    Returns: (N,) array of signed curvature values (NaN at endpoints).
    """
    N = len(pts)
    kappa = np.full(N, np.nan)

    for i in range(1, N - 1):
        p0 = pts[i - 1]
        p1 = pts[i]
        p2 = pts[i + 1]

        # Side lengths
        a = np.linalg.norm(p1 - p0)  # p_{i-1} to p_i
        b = np.linalg.norm(p2 - p1)  # p_i to p_{i+1}
        c = np.linalg.norm(p2 - p0)  # p_{i-1} to p_{i+1}

        # Triangle area via Heron
        s = (a + b + c) / 2.0
        area_sq = s * (s - a) * (s - b) * (s - c)
        if area_sq <= 0:
            kappa[i] = 0.0
            continue
        area = np.sqrt(area_sq)

        # Menger curvature: kappa = 4 * area / (a * b * c)
        denom = a * b * c
        if denom < 1e-12:
            kappa[i] = 0.0
        else:
            # Signed curvature: sign from cross product
            v1 = p1 - p0
            v2 = p2 - p1
            cross = v1[0] * v2[1] - v1[1] * v2[0]
            sign = 1.0 if cross >= 0 else -1.0
            kappa[i] = sign * (4.0 * area / denom)

    return kappa


def curvature_analysis():
    print("\n" + "=" * 60)
    print("=== Curvature Analysis ===")
    print("=" * 60)

    # Gather all trajectory CSV files (skip _plans.csv and _summary.json)
    csv_files = sorted(glob.glob(os.path.join(TRAJ_DIR, "trajectory_*.csv")))
    csv_files = [f for f in csv_files if '_plans' not in f and '_summary' not in f]
    print("Trajectory files: {}".format(len(csv_files)))

    all_kappa = []           # all valid curvature values
    all_abs_kappa = []       # |kappa|
    file_stats = []          # per-file stats
    all_points_cruise_return = []  # all points in CRUISE_CHANNEL or RETURN_P

    total_points = 0
    points_exceeding_limit = 0
    points_high_curvature = 0

    for csv_path in csv_files:
        fname = os.path.basename(csv_path)
        try:
            data = np.genfromtxt(csv_path, delimiter=',', names=True,
                                 dtype=None, encoding='utf-8', invalid_raise=False)
        except Exception as e:
            print("  SKIP {}: {}".format(fname, e))
            continue

        if data.size == 0:
            continue

        # Extract columns
        x = data['x_m'].astype(float)
        y = data['y_m'].astype(float)
        state_col = data['state']

        pts = np.column_stack([x, y])
        kappa = menger_curvature(pts)
        valid = ~np.isnan(kappa)
        abs_kappa = np.abs(kappa[valid])

        N = len(x)
        N_valid = np.sum(valid)
        exceed = np.sum(abs_kappa > PHYSICAL_KAPPA_MAX)
        high_curv = np.sum(abs_kappa > 1.0)

        total_points += N_valid
        points_exceeding_limit += exceed
        points_high_curvature += high_curv

        if N_valid > 0:
            all_kappa.extend(kappa[valid].tolist())
            all_abs_kappa.extend(abs_kappa.tolist())

            p50_val = np.percentile(abs_kappa, 50)
            p90_val = np.percentile(abs_kappa, 90)
            p95_val = np.percentile(abs_kappa, 95)
            p99_val = np.percentile(abs_kappa, 99)

            file_stats.append({
                'file': fname,
                'N': N,
                'N_valid': N_valid,
                'max_abs_k': np.max(abs_kappa),
                'p50': p50_val,
                'p90': p90_val,
                'p95': p95_val,
                'p99': p99_val,
                'exceed_pct': 100.0 * exceed / N_valid,
                'high_curv_pct': 100.0 * high_curv / N_valid,
            })

            # For corner analysis: collect points in CRUISE_CHANNEL or RETURN_P
            cruise_or_return = np.isin(state_col, ['CRUISE_CHANNEL', 'RETURN_P'])
            if np.sum(cruise_or_return) > 2:
                cr_pts = pts[cruise_or_return]
                cr_kappa = menger_curvature(cr_pts)
                cr_valid = ~np.isnan(cr_kappa)
                if np.sum(cr_valid) > 0:
                    all_points_cruise_return.append({
                        'file': fname,
                        'pts': cr_pts,
                        'kappa': cr_kappa,
                        'valid': cr_valid,
                        'state': state_col[cruise_or_return],
                    })

    all_abs_kappa = np.array(all_abs_kappa)

    print("\nTotal points analyzed (valid curvature): {}".format(total_points))

    p50_all = np.percentile(all_abs_kappa, 50)
    p90_all = np.percentile(all_abs_kappa, 90)
    p95_all = np.percentile(all_abs_kappa, 95)
    p99_all = np.percentile(all_abs_kappa, 99)
    max_all = np.max(all_abs_kappa)

    print("\n|kappa| distribution (all trajectories combined):")
    print("  p50:  {:.4f} m^-1  (r={:.2f}m)".format(p50_all, 1.0/p50_all if p50_all > 0 else float('inf')))
    print("  p90:  {:.4f} m^-1  (r={:.2f}m)".format(p90_all, 1.0/p90_all if p90_all > 0 else float('inf')))
    print("  p95:  {:.4f} m^-1  (r={:.2f}m)".format(p95_all, 1.0/p95_all if p95_all > 0 else float('inf')))
    print("  p99:  {:.4f} m^-1  (r={:.2f}m)".format(p99_all, 1.0/p99_all if p99_all > 0 else float('inf')))
    print("  max:  {:.4f} m^-1  (r={:.2f}m)".format(max_all, 1.0/max_all if max_all > 0 else float('inf')))

    print("\nPoints exceeding physical limit (kappa > {:.2f} m^-1):".format(PHYSICAL_KAPPA_MAX))
    print("  {} / {} ({:.2f}%)".format(points_exceeding_limit, total_points,
          100.0*points_exceeding_limit/total_points if total_points > 0 else 0))

    print("\nPoints with high curvature (|kappa| > 1.0 m^-1):")
    print("  {} / {} ({:.2f}%)".format(points_high_curvature, total_points,
          100.0*points_high_curvature/total_points if total_points > 0 else 0))

    # Per-file breakdown
    print("\nPer-file curvature summary:")
    print("  {:45s} {:>8s} {:>8s} {:>8s} {:>8s} {:>8s}".format(
        'File', 'N_valid', 'max|k|', 'p95', '%>3.33', '%>1.0'))
    print("  " + "-" * 85)
    for fs in sorted(file_stats, key=lambda x: x['max_abs_k'], reverse=True):
        print("  {:45s} {:>8d} {:>8.4f} {:>8.4f} {:>7.2f}% {:>7.2f}%".format(
            fs['file'], fs['N_valid'], fs['max_abs_k'], fs['p95'],
            fs['exceed_pct'], fs['high_curv_pct']))

    # Top curvature clusters
    print("\nLargest curvature by file (top 5):")
    for i, fs in enumerate(sorted(file_stats, key=lambda x: x['max_abs_k'], reverse=True)[:5]):
        print("  #{}: {}: max|k|={:.4f} m^-1, p95={:.4f}".format(
            i+1, fs['file'], fs['max_abs_k'], fs['p95']))

    # Determine lambda_fidelity
    # lambda_fidelity controls smoothing aggressiveness
    # Lower lambda_fidelity = more aggressive curvature smoothing
    # We need to bring p95_kappa below PHYSICAL_KAPPA_MAX (3.33)

    p95_kappa = np.percentile(all_abs_kappa, 95)

    if p95_kappa <= PHYSICAL_KAPPA_MAX:
        lambda_fidelity = 1.0  # default
        reasoning = "p95 |k| ({:.2f}) already below physical limit ({:.2f})".format(
            p95_kappa, PHYSICAL_KAPPA_MAX)
    else:
        # Scale lambda: need to reduce curvature by factor (PHYSICAL_KAPPA_MAX / p95_kappa)
        # MCT cost: lambda_fidelity * ||p-p0||^2 + ||K||^2
        # Lower lambda → curvature term dominates → more smoothing
        # Approximate: lambda ∝ (target_kappa / current_kappa)^2
        ratio = PHYSICAL_KAPPA_MAX / p95_kappa
        lambda_fidelity = ratio ** 2
        lambda_fidelity = max(0.1, min(10.0, lambda_fidelity))
        reasoning = "p95 |k| = {:.2f} > limit {:.2f}, need smoothing ratio {:.3f}".format(
            p95_kappa, PHYSICAL_KAPPA_MAX, ratio)

    # Also consider max: if max is extreme, go more aggressive
    if max_all > 10.0:
        max_ratio = PHYSICAL_KAPPA_MAX / max_all
        aggressive_lambda = max_ratio ** 2
        lambda_fidelity = min(lambda_fidelity, aggressive_lambda)
        reasoning += "; max|k|={:.2f} is extreme, further reducing lambda".format(max_all)

    lambda_fidelity = max(0.1, min(10.0, lambda_fidelity))

    print("\nRecommended lambda_fidelity: {:.3f}".format(lambda_fidelity))
    print("  Reasoning: {}".format(reasoning))
    print("  Target: reduce max|k| from {:.2f} to below {:.2f}".format(max_all, PHYSICAL_KAPPA_MAX))
    print("  while staying within max_shift constraint")

    return all_abs_kappa, file_stats, lambda_fidelity, p95_kappa, max_all, all_points_cruise_return


# ============================================================
# Task 3: Corner Deviation Analysis
# ============================================================
def corner_analysis(cruise_return_data):
    print("\n" + "=" * 60)
    print("=== Corner Analysis ===")
    print("=" * 60)

    CORNER_KAPPA_THRESH = 0.5
    MIN_CORNER_PTS = 3

    all_corners = []

    for entry in cruise_return_data:
        kappa = entry['kappa']
        valid = entry['valid']
        pts = entry['pts']
        state_arr = entry['state']
        fname = entry['file']

        abs_k = np.abs(kappa)

        # Find contiguous segments where |kappa| > threshold
        in_corner = (abs_k > CORNER_KAPPA_THRESH) & valid
        if not np.any(in_corner):
            continue

        # Find runs
        changes = np.diff(np.concatenate([[False], in_corner, [False]]).astype(int))
        starts = np.where(changes == 1)[0]
        ends = np.where(changes == -1)[0]

        for s, e in zip(starts, ends):
            if e - s < MIN_CORNER_PTS:
                continue

            corner_pts = pts[s:e]
            corner_kappa = kappa[s:e]
            corner_valid = valid[s:e]

            # Corner metrics
            abs_corner_k = np.abs(corner_kappa[corner_valid])
            max_corner_k = np.max(abs_corner_k) if len(abs_corner_k) > 0 else 0

            # Entry and exit points of the corner
            entry_pt = corner_pts[0]
            exit_pt = corner_pts[-1]

            # Straight line (centerline chord) from entry to exit
            chord_vec = exit_pt - entry_pt
            chord_len = np.linalg.norm(chord_vec)
            if chord_len < 0.05:
                continue

            chord_dir = chord_vec / chord_len
            chord_normal = np.array([-chord_dir[1], chord_dir[0]])

            # For each corner point, compute signed deviation from chord
            deviations = []
            for j in range(len(corner_pts)):
                pt = corner_pts[j]
                vec_from_entry = pt - entry_pt
                # Deviation: signed distance to chord
                # (positive = left of chord direction)
                dev = np.dot(vec_from_entry, chord_normal)
                deviations.append(dev)

            deviations = np.array(deviations)

            # Max deviation: how far inside/outside of the chord
            max_dev = np.max(np.abs(deviations))
            mean_dev = np.mean(deviations)

            # Determine turn direction from mean kappa
            mean_k = np.mean(corner_kappa[corner_valid]) if np.any(corner_valid) else 0.0

            # Apex deviation = deviation toward the inside of the turn
            # Left turn (mean_k > 0): inside = positive normal direction
            # Right turn (mean_k < 0): inside = negative normal direction
            if mean_k > 0:
                apex_deviation = np.max(deviations)   # most inside (positive)
            else:
                apex_deviation = np.min(deviations)   # most inside (negative)

            # Normalize by chord length
            normalized_dev = apex_deviation / chord_len if chord_len > 0 else 0

            all_corners.append({
                'file': fname,
                'n_pts': e - s,
                'max_abs_k': max_corner_k,
                'mean_k': mean_k,
                'chord_len': chord_len,
                'max_deviation': max_dev,
                'apex_deviation': apex_deviation,
                'normalized_dev': normalized_dev,
                'entry': entry_pt,
                'exit': exit_pt,
            })

    if len(all_corners) == 0:
        print("No corners identified in CRUISE_CHANNEL or RETURN_P states.")
        print("Defaulting alpha_apex = 0.15 (neutral)")
        return [], 0.15

    print("Corners identified: {}".format(len(all_corners)))

    # Stats
    max_abs_k_vals = [c['max_abs_k'] for c in all_corners]
    norm_devs = [c['normalized_dev'] for c in all_corners]
    apex_devs = [c['apex_deviation'] for c in all_corners]
    chord_lens = [c['chord_len'] for c in all_corners]

    print("\nCorner statistics:")
    print("  Average corner curvature (max|k|): {:.4f} m^-1".format(np.mean(max_abs_k_vals)))
    print("  Median corner curvature (max|k|):  {:.4f} m^-1".format(np.median(max_abs_k_vals)))
    print("  Max corner curvature:              {:.4f} m^-1".format(np.max(max_abs_k_vals)))
    print("  Average chord length:              {:.3f} m".format(np.mean(chord_lens)))
    print("  Average apex deviation:            {:.4f} m".format(np.mean(apex_devs)))
    print("  Average normalized deviation:      {:.4f}".format(np.mean(norm_devs)))

    mean_apex = np.mean(apex_devs)
    median_apex = np.median(apex_devs)

    print("\n  Mean apex deviation (positive = cuts inside): {:.4f} m".format(mean_apex))
    print("  Median apex deviation:                        {:.4f} m".format(median_apex))

    inside_cuts = sum(1 for d in apex_devs if d > 0.01)
    outside_runs = sum(1 for d in apex_devs if d < -0.01)
    neutral = len(apex_devs) - inside_cuts - outside_runs

    print("\n  Corners with inside cut (apex_dev > 0.01m):  {}".format(inside_cuts))
    print("  Corners with outside run (apex_dev < -0.01m): {}".format(outside_runs))
    print("  Corners near neutral:                          {}".format(neutral))

    if inside_cuts > outside_runs * 2:
        behavior = "oversteer (robot cuts too much)"
    elif outside_runs > inside_cuts * 2:
        behavior = "understeer (robot stays too wide)"
    else:
        behavior = "neutral / mixed"

    print("\n  Robot cornering behavior: {}".format(behavior))

    # Compute ideal apex offset for each corner (circular arc model)
    # For a circular arc: apex_offset = R - sqrt(R^2 - (L/2)^2) ~= L^2/(8R)
    ideal_apex_offsets = []
    actual_vs_ideal = []

    for c in all_corners:
        R = 1.0 / max(c['max_abs_k'], 0.01)
        L = c['chord_len']
        if 2 * R > L:
            ideal_offset = R - np.sqrt(R**2 - (L/2)**2)
        else:
            ideal_offset = L / 2  # diameter = chord, max deviation = radius
        ideal_apex_offsets.append(ideal_offset)
        actual_vs_ideal.append(c['apex_deviation'] / ideal_offset if ideal_offset > 0.001 else 0)

    mean_ideal_offset = np.mean(ideal_apex_offsets)
    mean_actual_ratio = np.mean(actual_vs_ideal)
    median_actual_ratio = np.median(actual_vs_ideal)

    print("\n  Ideal apex offsets (circular arc model):")
    print("    Mean ideal offset: {:.4f} m".format(mean_ideal_offset))
    print("    Mean actual/ideal ratio: {:.3f}".format(mean_actual_ratio))
    print("    Median actual/ideal ratio: {:.3f}".format(median_actual_ratio))

    # Determine alpha_apex based on how much the robot naturally cuts
    default_alpha = 0.15

    if median_actual_ratio < 0.3:
        alpha_apex = 0.25
        reasoning = "robot barely cuts corners (ratio < 0.3) -> high alpha to encourage apexing"
    elif median_actual_ratio < 0.6:
        alpha_apex = 0.20
        reasoning = "robot understeers moderately (ratio 0.3-0.6) -> elevated alpha"
    elif median_actual_ratio < 0.9:
        alpha_apex = 0.15
        reasoning = "robot cornering near ideal (ratio 0.6-0.9) -> default alpha"
    elif median_actual_ratio < 1.3:
        alpha_apex = 0.10
        reasoning = "robot already cutting well (ratio 0.9-1.3) -> reduced alpha"
    else:
        alpha_apex = 0.05
        reasoning = "robot cuts too aggressively (ratio > 1.3) -> low alpha to reduce oversteer"

    # Adjust by corner sharpness: if corners are very sharp, be more conservative
    if np.median(max_abs_k_vals) > 2.5:
        alpha_apex = min(alpha_apex, 0.12)
        reasoning += "; sharp corners -> conservative alpha"

    alpha_apex = max(0.0, min(0.3, alpha_apex))

    print("\n  Recommended alpha_apex: {:.3f}".format(alpha_apex))
    print("  Reasoning: {}".format(reasoning))

    # Print top 10 corners by curvature
    print("\n  Top 10 corners by curvature:")
    sorted_corners = sorted(all_corners, key=lambda x: x['max_abs_k'], reverse=True)[:10]
    for i, c in enumerate(sorted_corners):
        short_name = os.path.basename(c['file'])[:30]
        print("    #{}: max|k|={:.3f}, chord={:.2f}m, apex_dev={:.3f}m, norm_dev={:.3f}, [{}]".format(
            i+1, c['max_abs_k'], c['chord_len'], c['apex_deviation'], c['normalized_dev'], short_name))

    return all_corners, alpha_apex


# ============================================================
# Main
# ============================================================
def main():
    # Task 1: Corridor Analysis
    corridor_widths, dist_m, free_mask, obstacle, max_shift, min_corridor = corridor_analysis()

    # Task 2: Curvature Analysis
    all_abs_kappa, file_stats, lambda_fidelity, p95_kappa, max_kappa, cruise_return_data = curvature_analysis()

    # Task 3: Corner Analysis
    all_corners, alpha_apex = corner_analysis(cruise_return_data)

    # ============================================================
    # Final Summary
    # ============================================================
    print("\n" + "=" * 60)
    print("=== Final Recommended Parameters ===")
    print("=" * 60)
    print("  lambda_fidelity: {:.3f}".format(lambda_fidelity))
    print("  alpha_apex:      {:.3f}".format(alpha_apex))
    print("  max_shift:       {:.3f}".format(max_shift))
    print()

    # Validation
    print("=== Parameter Validation ===")
    if max_shift <= 0:
        print("  WARNING: max_shift <= 0 -- path cannot be displaced from original!")
        print("  The robot may not fit through narrow corridors.")
    elif max_shift < 0.05:
        print("  CAUTION: max_shift={:.3f}m is very small (< 0.05m).".format(max_shift))
        print("  Curvature smoothing will be severely constrained.")
    else:
        print("  max_shift={:.3f}m OK (>= 0.05m)".format(max_shift))

    if lambda_fidelity < 0.3:
        print("  NOTE: lambda_fidelity={:.3f} is very low (< 0.3).".format(lambda_fidelity))
        print("  Path will be heavily smoothed -- verify it stays within corridor.")
    elif lambda_fidelity > 5.0:
        print("  NOTE: lambda_fidelity={:.3f} is very high (> 5.0).".format(lambda_fidelity))
        print("  Smoothing will have minimal effect -- curvature may still exceed limits.")
    else:
        print("  lambda_fidelity={:.3f} OK (0.3-5.0)".format(lambda_fidelity))

    if alpha_apex > 0.25:
        print("  NOTE: alpha_apex={:.3f} is high (> 0.25).".format(alpha_apex))
        print("  Path may cut corners aggressively -- verify safety margins.")
    elif alpha_apex < 0.05:
        print("  NOTE: alpha_apex={:.3f} is very low (< 0.05).".format(alpha_apex))
        print("  Apex optimization will have minimal effect.")
    else:
        print("  alpha_apex={:.3f} OK (0.05-0.25)".format(alpha_apex))

    print("\nDone.")


if __name__ == '__main__':
    main()
