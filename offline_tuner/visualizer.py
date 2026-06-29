"""
Visualization: sensitivity curves, Pareto fronts, parameter importance.
All plots saved to tuning_results/ directory. Uses matplotlib.
"""
import logging
from pathlib import Path
from typing import Dict, List, Optional
import numpy as np

from . import config as _cfg
from .config import DEFAULTS, OUT_DIR

log = logging.getLogger('Nav2Tuner.Visualizer')


class Visualizer:
    """Generate visualization outputs for the tuning pipeline.

    Usage:
      viz = Visualizer()
      viz.sensitivity_curve(model, 'controller.desired_linear_vel', 0.50)
      viz.parameter_importance(importances)
      viz.convergence_plot(study)
    """

    def __init__(self, output_dir: Path = None):
        self.output_dir = Path(output_dir) if output_dir else _cfg.RUN_OUT_DIR
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self._mpl_ok = self._check_mpl()

    @staticmethod
    def _check_mpl() -> bool:
        try:
            import matplotlib
            matplotlib.use('Agg')  # non-interactive backend
            return True
        except ImportError:
            log.warning("matplotlib not available — plots disabled")
            return False

    def sensitivity_curve(
        self,
        score_model,
        param_name: str,
        center_value: Optional[float] = None,
        range_pct: float = 0.30,
        n_points: int = 50,
        save: bool = True,
    ) -> Optional[Path]:
        """Generate sensitivity curve for one parameter.

        Varies param_name ±range_pct around center_value (default from DEFAULTS)
        while keeping all others at DEFAULTS.
        """
        if not self._mpl_ok:
            return None

        import matplotlib.pyplot as plt

        if center_value is None:
            center_value = DEFAULTS.get(param_name)
        if center_value is None:
            log.warning(f"No default value for {param_name}")
            return None

        lo = center_value * (1 - range_pct)
        hi = center_value * (1 + range_pct)

        x_vals = np.linspace(lo, hi, n_points)
        y_vals = np.zeros(n_points)

        for i, x in enumerate(x_vals):
            p = dict(DEFAULTS)
            p[param_name] = float(x)
            y_vals[i] = score_model.compute_score(p)

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(x_vals, y_vals, 'b-', linewidth=2)
        ax.axvline(center_value, color='gray', linestyle='--', alpha=0.7,
                   label=f'Current: {center_value:.3f}')

        # Mark best value
        best_idx = np.argmin(y_vals)
        best_x = x_vals[best_idx]
        ax.axvline(best_x, color='red', linestyle='--', alpha=0.7,
                   label=f'Best: {best_x:.3f} (score={y_vals[best_idx]:.4f})')

        short_name = param_name.split('.')[-1]
        ax.set_xlabel(short_name)
        ax.set_ylabel('Score (lower is better)')
        ax.set_title(f'Sensitivity: {param_name}')
        ax.legend()
        ax.grid(True, alpha=0.3)

        fig.tight_layout()

        if save:
            ts = _timestamp()
            out_path = self.output_dir / f"sensitivity_{short_name}_{ts}.png"
            fig.savefig(out_path, dpi=100)
            plt.close(fig)
            log.info(f"Sensitivity curve: {out_path}")
            return out_path
        else:
            plt.show()
            return None

    def sensitivity_matrix(
        self,
        score_model,
        top_params: List[str],
        save: bool = True,
    ) -> Optional[Path]:
        """Grid of sensitivity curves for multiple parameters."""
        if not self._mpl_ok:
            return None

        import matplotlib.pyplot as plt

        n = len(top_params)
        cols = min(3, n)
        rows = (n + cols - 1) // cols

        fig, axes = plt.subplots(rows, cols, figsize=(5*cols, 3*rows))
        if rows == 1 and cols == 1:
            axes = np.array([[axes]])
        elif rows == 1:
            axes = axes.reshape(1, -1)
        elif cols == 1:
            axes = axes.reshape(-1, 1)

        for idx, param_name in enumerate(top_params):
            r, c = idx // cols, idx % cols
            ax = axes[r, c]

            center = DEFAULTS.get(param_name, 0.5)
            x_vals = np.linspace(center * 0.7, center * 1.3, 30)
            y_vals = np.zeros(30)
            for i, x in enumerate(x_vals):
                p = dict(DEFAULTS)
                p[param_name] = float(x)
                y_vals[i] = score_model.compute_score(p)

            ax.plot(x_vals, y_vals, linewidth=1.5)
            best_idx = np.argmin(y_vals)
            ax.axvline(x_vals[best_idx], color='red', linestyle='--', alpha=0.5, linewidth=1)
            ax.axvline(center, color='gray', linestyle=':', alpha=0.5, linewidth=1)
            ax.set_title(param_name.split('.')[-1], fontsize=9)
            ax.tick_params(labelsize=7)
            ax.grid(True, alpha=0.2)

        # Hide unused subplots
        for idx in range(n, rows * cols):
            r, c = idx // cols, idx % cols
            axes[r, c].set_visible(False)

        fig.suptitle('Parameter Sensitivity Matrix', fontsize=12)
        fig.tight_layout()

        if save:
            ts = _timestamp()
            out_path = self.output_dir / f"sensitivity_matrix_{ts}.png"
            fig.savefig(out_path, dpi=120)
            plt.close(fig)
            log.info(f"Sensitivity matrix: {out_path}")
            return out_path
        return None

    def parameter_importance(
        self,
        importances: Dict[str, float],
        top_n: int = 15,
        title: str = "Parameter Importance",
        save: bool = True,
    ) -> Optional[Path]:
        """Horizontal bar chart of top N parameter importances."""
        if not self._mpl_ok:
            return None

        import matplotlib.pyplot as plt

        sorted_items = sorted(importances.items(), key=lambda x: x[1])
        if len(sorted_items) > top_n:
            sorted_items = sorted_items[-top_n:]

        names = [item[0].split('.')[-1] for item in sorted_items]
        values = [item[1] for item in sorted_items]

        fig, ax = plt.subplots(figsize=(9, 5))
        colors = plt.cm.viridis(np.linspace(0.3, 0.9, len(values)))
        bars = ax.barh(range(len(names)), values, color=colors)
        ax.set_yticks(range(len(names)))
        ax.set_yticklabels(names)
        ax.set_xlabel('Importance')
        ax.set_title(title)
        ax.grid(True, axis='x', alpha=0.3)

        # Add value labels
        for i, (bar, val) in enumerate(zip(bars, values)):
            ax.text(bar.get_width() + 0.002, bar.get_y() + bar.get_height()/2,
                    f'{val:.3f}', va='center', fontsize=8)

        fig.tight_layout()

        if save:
            ts = _timestamp()
            out_path = self.output_dir / f"importance_{ts}.png"
            fig.savefig(out_path, dpi=120)
            plt.close(fig)
            log.info(f"Importance chart: {out_path}")
            return out_path
        return None

    def convergence_plot(
        self,
        study,
        save: bool = True,
    ) -> Optional[Path]:
        """Optuna optimization history: best value vs trial number."""
        if not self._mpl_ok:
            return None

        import matplotlib.pyplot as plt

        if study is None:
            log.warning("No study to plot")
            return None

        trials = [t for t in study.trials if t.value is not None]
        if not trials:
            return None

        values = np.array([t.value for t in trials])
        best_so_far = np.minimum.accumulate(values)

        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot(range(len(values)), values, 'o', markersize=1, alpha=0.3,
                color='blue', label='Trial score')
        ax.plot(range(len(best_so_far)), best_so_far, '-', linewidth=2,
                color='red', label='Best so far')
        ax.set_xlabel('Trial')
        ax.set_ylabel('Score')
        ax.set_title(f'Optuna Convergence ({len(trials)} trials)')
        ax.legend()
        ax.grid(True, alpha=0.3)
        fig.tight_layout()

        if save:
            ts = _timestamp()
            out_path = self.output_dir / f"convergence_{ts}.png"
            fig.savefig(out_path, dpi=120)
            plt.close(fig)
            log.info(f"Convergence plot: {out_path}")
            return out_path
        return None

    def pareto_plot(
        self,
        params_list: List[Dict],
        scores: np.ndarray,
        x_obj: str = "score",
        y_obj: Optional[str] = None,
        save: bool = True,
    ) -> Optional[Path]:
        """Pareto front scatter plot."""
        if not self._mpl_ok or len(scores) == 0:
            return None

        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(figsize=(7, 5))

        if scores.ndim == 1:
            ax.scatter(range(len(scores)), scores, c=scores, cmap='viridis',
                       alpha=0.6, s=5)
            ax.set_xlabel('Rank')
            ax.set_ylabel('Score')
            ax.set_title('Parameter Score Distribution')
        else:
            ax.scatter(scores[:, 0], scores[:, 1], c='blue', alpha=0.6, s=10)
            ax.set_xlabel(x_obj)
            ax.set_ylabel(y_obj or 'Objective 2')
            ax.set_title('Pareto Front')

        ax.grid(True, alpha=0.3)
        fig.tight_layout()

        if save:
            ts = _timestamp()
            out_path = self.output_dir / f"pareto_{ts}.png"
            fig.savefig(out_path, dpi=120)
            plt.close(fig)
            log.info(f"Pareto plot: {out_path}")
            return out_path
        return None


def _timestamp() -> str:
    from datetime import datetime
    return datetime.now().strftime('%Y%m%d_%H%M%S')


def _setup_matplotlib_style():
    """Apply consistent matplotlib style."""
    try:
        import matplotlib.pyplot as plt
        plt.style.use('seaborn-v0_8-darkgrid')
    except Exception:
        pass
