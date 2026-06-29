#!/usr/bin/env python3
"""
Generate Sobol sequence experimental design for 27-parameter Nav2 tuning.

Usage:
  python offline_tuner/generate_design.py [--n-runs 20] [--output-dir designs/]

Outputs:
  - designs/sobol_NNN.csv        — all N parameter sets
  - designs/run_XX_nav2.yaml     — one YAML per run (ros2 param load compatible)
  - designs/run_XX_params.json   — one JSON per run (for tuner DB)
"""
import sys, os, json, argparse
from pathlib import Path
import numpy as np

HERE = Path(__file__).parent.parent
sys.path.insert(0, str(HERE))

from offline_tuner.config import PARAM_SPACE, DEFAULTS, PARAM_TO_YAML_PATH
from offline_tuner.yaml_patch import YamlPatchGenerator


def generate_sobol_design(n_runs: int = 20, seed: int = 42) -> list:
    """Generate N Sobol quasi-random parameter sets covering all 27 dimensions.

    Sobol sequences have the best low-discrepancy properties in high dimensions,
    outperforming LHS for d > 10 (LHS optimization becomes NP-hard).
    """
    from scipy.stats.qmc import Sobol

    keys = sorted(PARAM_SPACE.keys())
    d = len(keys)

    sampler = Sobol(d=d, scramble=True, seed=seed)
    samples = sampler.random(n=n_runs)

    designs = []
    for i in range(n_runs):
        p = {}
        for j, key in enumerate(keys):
            lo, hi, kind = PARAM_SPACE[key]
            raw = float(samples[i, j])
            if kind == 'float':
                p[key] = round(float(lo + raw * (hi - lo)), 4)
            elif kind == 'int':
                p[key] = int(lo + raw * (hi - lo + 1))
        designs.append(p)

    return designs


def print_design_summary(designs):
    """Print coverage statistics for the design."""
    keys = sorted(PARAM_SPACE.keys())
    d = len(keys)

    print(f"\n{'='*70}")
    print(f"Sobol {len(designs)}-point design for {d}-dim parameter space")
    print(f"{'='*70}")
    print(f"{'Run':<5} {'Changed/27':<12} {'Sample params (first 4)'}")
    print(f"{'-'*70}")

    for i, p in enumerate(designs):
        changed = sum(1 for k in keys
                     if abs(p[k] - DEFAULTS[k]) / max(abs(DEFAULTS[k]), 0.001) > 0.03)
        preview = ', '.join(
            f"{keys[j].split('.')[-1]}={p[keys[j]]}"
            for j in range(min(4, d))
        )
        print(f"  {i+1:<3} {changed:>3}/27       {preview}")

    # Coverage stats
    coverages = []
    for k in keys:
        vals = [p[k] for p in designs]
        lo, hi, _ = PARAM_SPACE[k]
        span = (max(vals) - min(vals)) / (hi - lo) if hi > lo else 0
        coverages.append(span)

    print(f"\n  Avg range coverage: {np.mean(coverages)*100:.0f}%")
    print(f"  Min coverage:       {np.min(coverages)*100:.0f}%")
    print(f"  Max coverage:       {np.max(coverages)*100:.0f}%")
    print(f"  Low-coverage params (<30%): {sum(1 for c in coverages if c < 0.3)}/{d}")


def export_design(designs, output_dir: Path):
    """Export designs to CSV, per-run YAML, and per-run JSON."""
    output_dir.mkdir(parents=True, exist_ok=True)
    keys = sorted(PARAM_SPACE.keys())
    yaml_gen = YamlPatchGenerator()

    # 1. Master CSV
    csv_path = output_dir / f"sobol_{len(designs)}.csv"
    with open(csv_path, 'w') as f:
        f.write('run,' + ','.join(keys) + '\n')
        for i, p in enumerate(designs):
            vals = [str(p[k]) for k in keys]
            f.write(f"{i+1}," + ','.join(vals) + '\n')
    print(f"  CSV: {csv_path}")

    # 2. Per-run YAML + JSON
    for i, p in enumerate(designs):
        run_dir = output_dir / f"run_{i+1:02d}"
        run_dir.mkdir(parents=True, exist_ok=True)

        # YAML patch (changed params only)
        yaml_path = run_dir / "nav2_patch.yaml"
        yaml_gen.write_patch(p, output_path=yaml_path, changed_only=False)

        # JSON (full params for tuner DB)
        json_path = run_dir / "params.json"
        with open(json_path, 'w') as f:
            json.dump({'run': i+1, 'params': p}, f, indent=2)

    print(f"  Per-run YAML+JSON: {output_dir}/run_01/ ... run_{len(designs):02d}/")


def main():
    ap = argparse.ArgumentParser(description='Generate Sobol experimental design for Nav2 tuning')
    ap.add_argument('--n-runs', type=int, default=20, help='Number of runs (default: 20)')
    ap.add_argument('--seed', type=int, default=42, help='Sobol seed (default: 42)')
    ap.add_argument('--output-dir', type=str, default='designs', help='Output directory')
    args = ap.parse_args()

    print(f"Generating Sobol design: {args.n_runs} runs, {len(PARAM_SPACE)} params, seed={args.seed}")

    designs = generate_sobol_design(n_runs=args.n_runs, seed=args.seed)

    output_dir = HERE / args.output_dir
    print_design_summary(designs)
    export_design(designs, output_dir)

    print(f"\nDone. Deploy with:")
    print(f"  ros2 param load /controller_server {output_dir}/run_01/nav2_patch.yaml")
    print(f"  ros2 param load /planner_server {output_dir}/run_01/nav2_patch.yaml")


if __name__ == '__main__':
    main()
