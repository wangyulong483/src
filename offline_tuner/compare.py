"""
Compare multiple trajectory runs and parameter optimization results.

Output: Markdown tables with per-run metrics and trend detection.
"""
import json
import logging
from pathlib import Path
from glob import glob
from typing import Dict, List, Optional
import numpy as np

from .feature_extractor import FeatureExtractor
from .phase_metrics import PhaseMetricsDB
from .config import KNOWN_PHASES

log = logging.getLogger('Nav2Tuner.Compare')


class RunComparer:
    """Compare multiple trajectory runs or parameter optimization results.

    Output markdown tables with trend detection.
    """

    def __init__(self, db: PhaseMetricsDB):
        self.db = db

    def compare_runs_table(self) -> str:
        """Generate markdown comparison table of all runs in the database.

        Columns: File | Total | Cruise | Return | Backing | DIR | Replan | Hz | Trend
        """
        runs = self.db._runs
        if not runs:
            return "# No trajectory data available.\n"

        # Sort by timestamp
        sorted_runs = sorted(runs, key=lambda r: r.get('timestamp', ''))

        # Columns
        headers = ['File', 'Status', 'Total', 'Cruise', 'Return',
                   'Backing', 'DIR_SW', 'Replan', 'Hz', 'Trend']

        rows = []
        prev_time = None
        for run in sorted_runs:
            fname = Path(run.get('source', '?')).name[:35]
            status = '✓' if run.get('goal_reached') else '✗'
            total = f"{run.get('total_time', 0):.1f}s"

            # Phase times
            phases = run.get('phases', {})
            cruise = f"{phases.get('CRUISE_CHANNEL', {}).get('elapsed', 0):.1f}s"
            ret = f"{phases.get('RETURN_P', {}).get('elapsed', 0):.1f}s"
            back = f"{phases.get('BACKING_UP', {}).get('elapsed', 0):.1f}s"

            dir_sw = str(run.get('total_dir_switches', '?'))
            replan = str(run.get('total_replans', '?'))
            hz = f"{run.get('planner_hz_overall', 0):.1f}"

            # Trend vs previous
            if prev_time is not None:
                cur = run.get('total_time', 0)
                delta = (cur - prev_time) / max(prev_time, 0.1) * 100
                if delta < -3:
                    trend = '↓'  # faster (better)
                elif delta > 3:
                    trend = '↑'  # slower (worse)
                else:
                    trend = '≈'
            else:
                trend = '--'
            prev_time = run.get('total_time', 0)

            rows.append([fname, status, total, cruise, ret, back,
                         dir_sw, replan, hz, trend])

        return self._format_markdown_table(headers, rows, align='lccccccccc')

    def compare_params_history(self, json_dir: Optional[str] = None) -> str:
        """Compare parameter optimization history from best_params_*.json files.

        Shows score progression over time.
        """
        search_dir = json_dir or str(self.db.db_path.parent)
        jsons = sorted(glob(f"{search_dir}/best_params_*.json"))

        if not jsons:
            return "# No parameter optimization history found.\n"

        headers = ['Time', 'Score', 'Δ from Best', 'Strategy', 'Trials']
        rows = []
        best_score = float('inf')

        for jp in jsons:
            try:
                with open(jp, 'r') as f:
                    d = json.load(f)
            except Exception:
                continue

            score = d.get('best_score', 1)
            if score < best_score:
                best_score = score

            delta = ((score - best_score) / max(best_score, 0.001) * 100) if best_score > 0 else 0
            ts = d.get('timestamp', '?')[:19]
            strategy = d.get('scoring_strategy', '?')
            n_trials = str(d.get('n_trials', '?'))

            rows.append([ts, f"{score:.4f}", f"{delta:+.1f}%", strategy, n_trials])

        result = [f"# Parameter Optimization History ({len(jsons)} runs)"]
        result.append(f"Best score: {best_score:.4f}\n")
        result.append(self._format_markdown_table(headers, rows))
        return '\n'.join(result)

    def phase_summary_table(self) -> str:
        """Per-phase aggregated statistics table."""
        phase_stats = self.db.data.get('phase_statistics', {})
        if not phase_stats:
            return "# No phase statistics available.\n"

        headers = ['Phase', 'Runs', 'Mean', 'Best', 'Std', 'DIR_SW', 'Replan', 'Smooth']
        rows = []
        for phase_name in KNOWN_PHASES:
            ps = phase_stats.get(phase_name, {})
            if not ps:
                continue
            rows.append([
                phase_name,
                str(ps.get('count', 0)),
                f"{ps.get('mean_time', 0):.1f}s",
                f"{ps.get('best_time', 0):.1f}s",
                f"±{ps.get('std_time', 0):.1f}s",
                f"{ps.get('mean_dir_switches', 0):.1f}",
                f"{ps.get('mean_replans', 0):.1f}",
                f"{ps.get('mean_smoothness', 0):.2f}",
            ])

        return self._format_markdown_table(headers, rows)

    @staticmethod
    def _format_markdown_table(
        headers: List[str],
        rows: List[List[str]],
        align: str = 'l',
    ) -> str:
        """Format a markdown table with aligned columns."""
        if not rows:
            return "*(empty)*\n"

        # If align is a single char, repeat for all columns
        if len(align) == 1:
            align = align * len(headers)

        # Calculate column widths
        all_rows = [headers] + rows
        widths = [max(len(str(r[i])) for r in all_rows) for i in range(len(headers))]

        lines = []
        # Header
        header_cells = [f" {headers[i]:<{widths[i]}} " for i in range(len(headers))]
        lines.append('|' + '|'.join(header_cells) + '|')

        # Separator
        sep_map = {'l': ':', 'c': ':', 'r': '-'}
        sep_cells = []
        for i in range(len(headers)):
            a = align[i] if i < len(align) else 'l'
            left = sep_map.get(a, '-')
            right = sep_map.get(a, '-') if a == 'c' else ('-' if a == 'l' else ':')
            dashes = '-' * (widths[i])
            sep_cells.append(f"{left}{dashes}{right}")
        lines.append('|' + '|'.join(sep_cells) + '|')

        # Rows
        for row in rows:
            cells = [f" {str(row[i]):<{widths[i]}} " for i in range(len(headers))]
            lines.append('|' + '|'.join(cells) + '|')

        return '\n'.join(lines) + '\n'


def compare_runs(dir_path: str) -> str:
    """Convenience function: load data, run comparison, return markdown string."""
    from .feature_extractor import FeatureExtractor
    from .phase_metrics import PhaseMetricsDB

    db = PhaseMetricsDB()
    extractor = FeatureExtractor()
    runs = extractor.analyze_directory(dir_path)
    db.add_runs(runs)

    comparer = RunComparer(db)
    return comparer.compare_runs_table()
