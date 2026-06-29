#!/usr/bin/env python3
"""
Nav2 Offline Auto Tuner — Data-driven parameter optimization for Ackermann robots.

Strategy (auto-selected):
  0 CSV    → Heuristic expert scoring
  1-29 CSV → Correlation-based weights (corr(metric, total_time))
  30+ CSV  → ML model prediction (LightGBM/XGBoost/RandomForest)
  +rosbag  → Same tier, richer feature set

Usage:
  python _analyze_plans.py                          # Quick: analyze + tune (5000 trials)
  python _analyze_plans.py --csv Z_PNG/out12/       # CSV directory
  python _analyze_plans.py --tune 10000             # More search
  python _analyze_plans.py --tier tier1 --freeze "planner.*"  # Tier1, freeze planner
  python _analyze_plans.py --gpu-prescreen 100000   # GPU Sobol screening first
  python _analyze_plans.py --analyze-only           # Just analyze, rebuild DB
  python _analyze_plans.py --compare                # Compare all runs
  python _analyze_plans.py --sensitivity controller.lookahead_dist  # Sensitivity
  python _analyze_plans.py --rosbag-dir rosbags/    # Enhance with rosbag data
"""
import sys, os, logging, argparse, warnings
from pathlib import Path
from datetime import datetime

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from offline_tuner import config as _cfg
from offline_tuner.config import OUT_DIR, KNOWN_PHASES, DEFAULTS
from offline_tuner.feature_extractor import FeatureExtractor
from offline_tuner.phase_metrics import PhaseMetricsDB
from offline_tuner.score_model import ScoreModel
from offline_tuner.optuna_search import OptunaTieredSearch, resolve_tier, parse_freeze_arg
from offline_tuner.yaml_patch import YamlPatchGenerator
from offline_tuner.compare import RunComparer
from offline_tuner.visualizer import Visualizer

try:
    from offline_tuner.evolution_engine import EvolutionEngine
    _HAS_EVOLUTION = True
except ImportError:
    _HAS_EVOLUTION = False

OUT_DIR.mkdir(parents=True, exist_ok=True)
# Per-run output directory: tuning_results/out1/, out2/, ...
_run_dir = _cfg.next_out_dir()
_cfg.RUN_OUT_DIR = _run_dir

# ── Logging ───────────────────────────────────────────
log_file = _run_dir / f"tune_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-7s | %(message)s',
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler(sys.stdout),
    ])
log = logging.getLogger('Nav2Tuner')

warnings.filterwarnings('ignore')


# ═══════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════

def main():
    ap = argparse.ArgumentParser(
        description='Nav2 Offline Auto Tuner — Data-driven parameter optimization',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python _analyze_plans.py                          # Quick auto
  python _analyze_plans.py --csv Z_PNG/out12/       # With data
  python _analyze_plans.py --tier tier1 --freeze "planner.*"
  python _analyze_plans.py --gpu-prescreen 100000   # GPU pre-screening
  python _analyze_plans.py --compare                # Compare runs
        """)
    # Data input
    ap.add_argument('csv', nargs='?', help='CSV file or directory (auto-detect if omitted)')
    ap.add_argument('--rosbag-dir', type=str, default='data/rosbags/', metavar='DIR', help='Rosbag2 directory (default: data/rosbags/)')
    ap.add_argument('--db', type=str, metavar='PATH', help='Metrics database path')
    ap.add_argument('--map-dir', type=str, metavar='DIR', help='Map directory (default: originbot_navigation/maps/)')

    # Search
    ap.add_argument('--tune', type=int, default=5000, metavar='N', help='Optuna trials (default: 5000)')
    ap.add_argument('--tier', type=str, default='default', metavar='T',
                    help='Tier: tier1(7) / default(19) / full(27)')
    ap.add_argument('--freeze', type=str, metavar='PATTERNS', help='Freeze params (comma-sep globs)')
    ap.add_argument('--cpu', type=int, default=None, metavar='N', help='Parallel workers')
    ap.add_argument('--gpu', action='store_true', default=True, help='Enable GPU acceleration (default: on)')
    ap.add_argument('--no-gpu', action='store_true', help='Disable GPU')
    ap.add_argument('--gpu-prescreen', type=int, default=5000, metavar='N',
                    help='GPU batch screening with N Sobol samples before Optuna (default: 5000)')

    # Analysis only
    ap.add_argument('--analyze-only', action='store_true', help='Analyze data + rebuild DB, skip optimization')
    ap.add_argument('--evolve', action='store_true', help='Continue evolution: load prior study, re-score, search more')
    ap.add_argument('--re-score', action='store_true', help='Re-score all prior trials without new search')
    ap.add_argument('--compare', action='store_true', help='Compare all runs and print markdown table')
    ap.add_argument('--sensitivity', type=str, metavar='PARAM', help='Generate sensitivity curve for param')

    # Output
    ap.add_argument('--pareto', type=int, default=10, metavar='N', help='Top N Pareto results (default: 10)')
    ap.add_argument('--no-plots', action='store_true', help='Skip visualization')

    args = ap.parse_args()

    log.info(f"{'='*60}")
    log.info(f"Nav2 Offline Auto Tuner v3 — Data-driven Optimization")
    log.info(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log.info(f"Log:  {log_file}")
    log.info(f"{'='*60}")

    # ── Load data ──────────────────────────────────────

    db = PhaseMetricsDB(Path(args.db) if args.db else None)
    extractor = FeatureExtractor()

    # Scan CSVs
    csv_inputs = _find_csvs(args.csv)
    if csv_inputs:
        log.info(f"Scanning {len(csv_inputs)} CSVs...")
        all_runs = []
        for cp in csv_inputs:
            if os.path.isdir(cp):
                runs = extractor.analyze_directory(cp)
            else:
                run = extractor.analyze_run(cp)
                runs = [run] if run else []
            all_runs.extend(runs)
        db.add_runs(all_runs)
        log.info(db.summary())
    else:
        log.info("No CSVs found — using heuristic scoring")

    # Rosbag enhancement: extract controller metrics, attach to matching runs
    if args.rosbag_dir:
        try:
            from offline_tuner.rosbag_loader import RosbagLoader, find_rosbags
            loader = RosbagLoader()
            bags = find_rosbags(args.rosbag_dir)
            if bags:
                log.info(f"Loading {len(bags)} rosbag metrics...")
                for bag in bags:
                    metrics = loader.extract_metrics(bag)
                    if metrics:
                        db.attach_rosbag_metrics(bag, metrics)
            else:
                log.info(f"No rosbags found in: {args.rosbag_dir}")
        except Exception as e:
            log.warning(f"Rosbag loading failed: {e}")

    # ── Score Model ────────────────────────────────────

    map_dir = args.map_dir or str(HERE / 'originbot_navigation' / 'maps')
    model = ScoreModel(db, map_dir=map_dir)
    log.info(str(model))

    # ── Compare mode ───────────────────────────────────

    if args.compare:
        comparer = RunComparer(db)
        table = comparer.compare_runs_table()
        log.info(f"\n{table}")
        phase_table = comparer.phase_summary_table()
        log.info(f"\n{phase_table}")
        return

    # ── Sensitivity analysis ───────────────────────────

    if args.sensitivity:
        viz = Visualizer()
        viz.sensitivity_curve(model, args.sensitivity)
        return

    # ── Analyze only ───────────────────────────────────

    if args.analyze_only:
        log.info(f"\nDatabase: {db.run_count} runs")
        for phase_name in KNOWN_PHASES:
            stats = db.get_phase_stats(phase_name)
            if stats:
                log.info(f"\n{phase_name}: {stats['count']} runs, "
                         f"mean={stats['mean_time']:.1f}s, "
                         f"best={stats['best_time']:.1f}s, "
                         f"std=±{stats['std_time']:.1f}s")
        import json
        log.info(f"\nCorrelations: {json.dumps(db.data.get('feature_correlations', {}), indent=2)[:500]}")
        return

    # ── Evolution mode ──────────────────────────────────

    if args.evolve and _HAS_EVOLUTION:
        engine = EvolutionEngine(model, db)
        prior_study = engine.load_study()
        if prior_study is not None:
            log.info("Evolution: %d prior trials loaded",
                     len([t for t in prior_study.trials if t.state.name == 'COMPLETE']))
            summary = engine.on_data_changed()
            log.info("Re-training: %s", summary)
        else:
            log.info("Evolution: no prior study found, starting fresh")

    if args.re_score and _HAS_EVOLUTION:
        engine = EvolutionEngine(model, db)
        prior_study = engine.load_study()
        if prior_study is not None:
            summary = engine.on_data_changed()
            log.info("Re-score: %d trials, mean drift=%.4f",
                     summary.get('trials_re_scored', 0),
                     summary.get('score_drift_mean', 0))
        return

    # ── Optuna Search ──────────────────────────────────

    tier = resolve_tier(args.tier)
    freeze = parse_freeze_arg(args.freeze)
    n_jobs = args.cpu
    use_gpu = args.gpu and not args.no_gpu

    # ★ Warm start: enqueue known-good params from historical CSV runs
    warm_start = []
    for run in db._runs:
        rp = run.get('params', {})
        if rp:
            warm_start.append(rp)
    if warm_start:
        log.info(f"Warm start: {len(warm_start)} known configs from CSV data")

    # If evolving, pass the existing study to Optuna via warm start
    if args.evolve and _HAS_EVOLUTION and 'engine' in dir():
        if engine.study is not None:
            # Extract best params from prior study as seeds
            completed = [t for t in engine.study.trials if t.state.name == 'COMPLETE' and t.value is not None]
            best_prior = sorted(completed, key=lambda t: t.value)[:min(10, len(completed))]
            for t in best_prior:
                warm_start.append({k: v for k, v in t.params.items()})
            log.info("Evolution warm start: %d prior-best params", len(best_prior))

    # ── GPU prescreen: batch-score Sobol samples, seed best into Optuna ──
    gpu_seeds = []
    if use_gpu and args.gpu_prescreen > 0:
        try:
            from offline_tuner.gpu_search import GPUPreScreener
            screener = GPUPreScreener(model, use_gpu=True)
            log.info(f"GPU prescreen: {args.gpu_prescreen} Sobol samples...")
            top = screener.screen(n_samples=args.gpu_prescreen, top_k=min(1000, args.gpu_prescreen // 10))
            if top:
                gpu_seeds = [t['params'] for t in top[:50]]  # top 50 as seeds
                log.info(f"GPU prescreened {len(top)} candidates, seeding Optuna with top {len(gpu_seeds)}")
        except Exception as e:
            log.warning(f"GPU prescreen failed ({e}), skipping")

    all_seeds = (gpu_seeds + warm_start) if warm_start else gpu_seeds
    if all_seeds:
        # Deduplicate
        seen = set()
        unique = []
        for s in all_seeds:
            key = tuple(sorted(s.items()))
            if key not in seen:
                seen.add(key)
                unique.append(s)
        all_seeds = unique
        log.info(f"Total warm start seeds: {len(all_seeds)} (GPU: {len(gpu_seeds)}, CSV: {len(warm_start)})")

    search = OptunaTieredSearch(
        model,
        tier=tier,
        freeze=freeze,
        seed_params=all_seeds if all_seeds else None,
    )
    study = search.run(n_trials=args.tune, n_jobs=n_jobs)

    if study is None:
        log.error("Search failed. Install optuna: pip install optuna")
        sys.exit(1)

    # ── Results ────────────────────────────────────────

    search.print_results(top_n=15)
    search.print_best_vs_baseline()
    search.save_results()

    # ── Evolution: save study + suggest next params ──
    if _HAS_EVOLUTION:
        engine2 = EvolutionEngine(model, db)
        engine2.study = study
        engine2._save_study()

        suggestions = engine2.suggest_next_params(k=3)
        if suggestions:
            log.info(f"\n{'='*60}")
            log.info("SUGGESTED NEXT PARAMS (for real robot test):")
            log.info(f"{'='*60}")
            for i, s in enumerate(suggestions):
                log.info(f"  #{i+1}: predicted_score={s.get('predicted_score', '?'):.4f} "
                         f"diversity={s.get('diversity', 0):.3f}")
        # Data quality report
        report = engine2.data_quality_report()
        log.info(f"\n{report}")

    # ── YAML Patch ─────────────────────────────────────

    yaml_gen = YamlPatchGenerator()
    patch_path = yaml_gen.write_patch(
        study.best_params,
        score=study.best_value,
        baseline_score=model.baseline_score(),
    )

    # ── Visualizations ─────────────────────────────────

    if not args.no_plots:
        viz = Visualizer()
        importances = search.get_param_importance()
        if importances:
            viz.parameter_importance(importances, title="Parameter Importance (Optuna)")
        viz.convergence_plot(study)

        # Sensitivity matrix for top params
        top_keys = sorted(importances, key=lambda k: -importances.get(k, 0))[:6]
        if top_keys:
            viz.sensitivity_matrix(model, top_keys)

    # ── Best path visualization (from closest real CSV) ──
    try:
        from offline_tuner.costmap_generator import CostmapGenerator
        from offline_tuner.astar_planner import AstarPlanner

        import numpy as np
        from scipy.ndimage import distance_transform_edt

        # Generate costmap with obstacles to get obstacle positions
        gen = CostmapGenerator()
        gen.load_maps()
        base = gen.static_map.copy()
        base[gen.keepout_map == 254] = 254
        # Place obstacles same way as generate_with_obstacles
        from scipy.ndimage import distance_transform_edt
        lm = (base == 254); dist = distance_transform_edt(~lm)
        mask = (base == 0) & (dist >= 1)
        rows, cols = np.where(mask)
        obs_pixels = []
        if len(rows) >= 5:
            rng = np.random.RandomState(42)
            idx = rng.choice(len(rows), 5, replace=False)
            obs_pixels = [(int(cols[i]), int(rows[i])) for i in idx]

        # Generate segmented competition paths (CCW + CW) with best params
        # A* where reachable, straight-line fallback for blocked segments
        from offline_tuner.costmap_generator import (CCW_PATH, CW_PATH,
                                                      CostmapData, ORIGIN_X, ORIGIN_Y)
        best_costmap = gen.generate(study.best_params, with_keepout=False)
        best_planner = AstarPlanner()
        path_items = []
        for path_wps, color, label in [(CCW_PATH, '#00ff00', 'CCW'), (CW_PATH, '#ff8808', 'CW')]:
            # Build segmented path: A* for each segment, straight line fallback
            all_px = []
            total_len = 0.0
            reachable = True
            for i in range(len(path_wps) - 1):
                sw, gw = path_wps[i], path_wps[i + 1]
                r = best_planner.plan(best_costmap, start_world=sw, goal_world=gw)
                if r.reachable and r.path:
                    if all_px:
                        r.path = r.path[1:]  # dedup segment join
                    all_px.extend(r.path)
                    total_len += r.path_len
                else:
                    # Straight-line fallback: world -> pixel
                    import math as _math
                    n_interp = max(2, int(_math.hypot(gw[0]-sw[0], gw[1]-sw[1]) / 0.1))
                    for j in range(n_interp + (0 if i == 0 and not all_px else 1)):
                        t = j / n_interp
                        wx = sw[0] + t * (gw[0] - sw[0])
                        wy = sw[1] + t * (gw[1] - sw[1])
                        c = int((wx - ORIGIN_X) / 0.05)
                        r = int((ORIGIN_Y + 141 * 0.05 - wy) / 0.05)
                        all_px.append((r, c))
                    total_len += _math.hypot(gw[0]-sw[0], gw[1]-sw[1])
                    reachable = False

            if all_px:
                from offline_tuner.astar_planner import PathResult
                pr = PathResult(
                    reachable=reachable, path=all_px, path_len=total_len,
                    curvature_mean=0.0, clearance_min=0.5,
                    cusp_count=0, in_lethal_count=0, total_cost=0.0,
                )
                suffix = '' if reachable else ' (partial straight)'
                path_items.append((pr, f'{label} {total_len:.1f}m{suffix}', color))

        if path_items:
            _ts = datetime.now().strftime('%Y%m%d_%H%M%S')
            path_png = _run_dir / f"best_path_{_ts}.png"
            base_grid = best_costmap.grid.copy()
            for ox, oy in obs_pixels:
                if 0 <= oy < base_grid.shape[0] and 0 <= ox < base_grid.shape[1]:
                    base_grid[oy, ox] = 200
            vis_costmap = CostmapData(
                grid=base_grid, width=best_costmap.width, height=best_costmap.height,
                resolution=0.05, origin_x=ORIGIN_X, origin_y=ORIGIN_Y,
                inflation_radius=best_costmap.inflation_radius,
                cost_scaling_factor=best_costmap.cost_scaling_factor,
            )
            AstarPlanner.render_multi_path(
                vis_costmap, path_items, str(path_png),
                title=f"Best Params Competition Paths (score={study.best_value:.4f})"
            )
            log.info(f"Best path PNG: {path_png}")
        else:
            log.warning("Best path: no paths")
    except Exception as e:
        log.debug(f"Path render skip: {e}")

    # ── Multi-path comparison removed (was duplicate of best_path) ──
    # Path comparison at the A* level is not meaningful because:
    # (a) P→VLM straight line ignores keepout and competition waypoints.
    # (b) Full competition path has unreachable segments through walls.
    # (c) RPP simulation per-param is too expensive for batch rendering.
    # Best_path already shows the real competition trajectory on the costmap.

    # ── Summary ────────────────────────────────────────

    log.info(f"\n{'='*60}")
    log.info(f"DONE. Best score: {study.best_value:.4f} (baseline: {model.baseline_score():.4f})")
    log.info(f"YAML patch: {patch_path}")
    log.info(f"Full log:  {log_file}")
    log.info(f"{'='*60}")


def _find_csvs(user_path: str = None) -> list:
    """Find trajectory CSV files."""
    if user_path:
        p = Path(user_path)
        if p.is_dir():
            return [str(p)]
        elif p.is_file():
            return [str(p)]

    # Auto-detect
    candidates = []
    for pattern in ['trajectory_*.csv', 'data/trajectories/trajectory_*.csv',
                    'Z_PNG/out*/trajectory_*.csv']:
        for f in sorted(HERE.glob(pattern)):
            if '_plans' not in f.name and '_summary' not in f.name:
                candidates.append(str(f))

    # Deduplicate by filename
    seen = set()
    unique = []
    for c in candidates:
        name = Path(c).name
        if name not in seen:
            seen.add(name)
            unique.append(c)
    return unique


if __name__ == '__main__':
    main()
