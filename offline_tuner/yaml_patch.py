"""
Generate valid Nav2 YAML patches from tuned parameters.

Translates flat param dicts (e.g. 'controller.lookahead_dist': 0.68)
into nested Nav2 YAML structure via PARAM_TO_YAML_PATH mapping.

Output YAML can be loaded with `ros2 param load` or diff'd against
the base originbot_nav2_rpp.yaml.
"""
import logging
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

from . import config as _cfg
from .config import DEFAULTS, PARAM_TO_YAML_PATH, OUT_DIR

log = logging.getLogger('Nav2Tuner.YamlPatch')


class YamlPatchGenerator:
    """Generate valid Nav2 YAML patches from tuned parameters.

    Usage:
      gen = YamlPatchGenerator(base_yaml_path=...)
      gen.write_patch(params, score=0.12)
      # → tuning_results/nav2_patch_<timestamp>.yaml
    """

    def __init__(self, base_yaml_path: Optional[Path] = None):
        self.base_yaml_path = Path(base_yaml_path) if base_yaml_path else None
        self.base_config = self._load_base() if self.base_yaml_path else {}

    def _load_base(self) -> Dict:
        """Load base YAML config for comparison."""
        try:
            with open(self.base_yaml_path, 'r') as f:
                return yaml.safe_load(f) or {}
        except Exception as e:
            log.warning(f"Failed to load base YAML: {e}")
            return {}

    def generate_patch(
        self,
        params: Dict[str, float],
        changed_only: bool = True,
        threshold_pct: float = 3.0,
    ) -> Dict:
        """Generate nested dict for YAML dump.

        Args:
          params: Flat dict like {'controller.lookahead_dist': 0.68, ...}
          changed_only: If True, only include params that differ from DEFAULTS
          threshold_pct: Min % change to include (default 3%)

        Returns nested dict following Nav2 YAML structure.
        """
        nested: Dict[str, Any] = {}

        for key, value in sorted(params.items()):
            # Check if changed enough
            default = DEFAULTS.get(key)
            if changed_only and default is not None and default != 0:
                pct_change = abs(value - default) / max(abs(default), 0.001) * 100
                if pct_change < threshold_pct:
                    continue

            # Map to YAML path
            yaml_path = PARAM_TO_YAML_PATH.get(key)
            if yaml_path is None:
                log.debug(f"No YAML path mapping for: {key}")
                continue

            self._set_nested(nested, yaml_path, value)

        return nested

    def write_patch(
        self,
        params: Dict[str, float],
        output_path: Optional[Path] = None,
        score: Optional[float] = None,
        baseline_score: Optional[float] = None,
        changed_only: bool = True,
    ) -> Path:
        """Write YAML patch to disk.

        Returns path to written file.
        """
        nested = self.generate_patch(params, changed_only=changed_only)

        if output_path is None:
            ts = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_path = _cfg.RUN_OUT_DIR / f"nav2_patch_{ts}.yaml"

        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Count changed params
        def count_params(d: Dict, depth: int = 0) -> int:
            n = 0
            for v in d.values():
                if isinstance(v, dict):
                    n += count_params(v, depth + 1)
                else:
                    n += 1
            return n

        n_changed = count_params(nested)

        # Write with header comment
        with open(output_path, 'w') as f:
            f.write(f"# Nav2 Auto-Tuner — Recommended Parameter Patch\n")
            if score is not None:
                f.write(f"# Score: {score:.4f}")
                if baseline_score is not None:
                    delta = (score - baseline_score) / max(baseline_score, 0.001) * 100
                    f.write(f" (baseline: {baseline_score:.4f}, delta: {delta:+.1f}%)")
                f.write("\n")
            f.write(f"# Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"# Changed parameters: {n_changed}\n")
            f.write(f"# Load with: ros2 param load /path/to/node <this_file.yaml>\n")
            f.write(f"# Or diff against: originbot_nav2_rpp.yaml\n\n")

            yaml.dump(nested, f, default_flow_style=False, allow_unicode=True,
                      sort_keys=False)

        log.info(f"YAML patch ({n_changed} params) → {output_path}")
        return output_path

    @staticmethod
    def _set_nested(d: Dict, path: str, value: Any) -> None:
        """Set d['a']['b']['c'] = value from dotted path 'a.b.c'."""
        keys = path.split('.')
        for key in keys[:-1]:
            if key not in d:
                d[key] = {}
            d = d[key]
        d[keys[-1]] = value

    def generate_diff_text(self, params: Dict[str, float]) -> str:
        """Generate human-readable diff summary against defaults."""
        lines = ["# Parameter Changes vs Current Config", ""]
        changes = []
        for key, value in sorted(params.items()):
            default = DEFAULTS.get(key)
            if default is not None and default != 0:
                pct = (value - default) / abs(default) * 100
                if abs(pct) >= 3.0:
                    ypath = PARAM_TO_YAML_PATH.get(key, key)
                    changes.append((pct, ypath, default, value))

        if not changes:
            return "# No significant changes (>3%) found.\n"

        changes.sort(key=lambda x: -abs(x[0]))

        max_path_len = max(len(c[1]) for c in changes)
        for pct, ypath, old, new in changes:
            lines.append(
                f"# {ypath:<{max_path_len}}  {old:>7.3f} → {new:<7.3f}  ({pct:+.1f}%)"
            )

        return '\n'.join(lines)

    def validate_patch(self, params: Dict[str, float]) -> List[str]:
        """Validate that all YAML paths map to known Nav2 parameters.
        Returns list of warnings.
        """
        warnings = []
        for key in params:
            if key not in PARAM_TO_YAML_PATH:
                warnings.append(f"Unknown mapping for: {key}")
            ypath = PARAM_TO_YAML_PATH.get(key, '')
            if ypath and self.base_config:
                # Check if path exists in base yaml (best effort)
                try:
                    d = self.base_config
                    for part in ypath.split('.'):
                        d = d[part]
                except (KeyError, TypeError):
                    warnings.append(f"Path not found in base YAML: {ypath}")
        return warnings
