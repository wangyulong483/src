#!/usr/bin/env python3
"""
centerline_extractor.py — Extract Voronoi skeleton centerline from PGM occupancy grid.

Reads a PGM map + YAML metadata + optional keepout mask, computes the Voronoi
skeleton of the free space via Euclidean Distance Transform + morphological
skeletonization, then traces the longest connected path to produce an ordered
set of (x_m, y_m) waypoints suitable as a racing reference line.

Usage:
    python centerline_extractor.py room.pgm room.yaml [--keepout keepout_mask.pgm]
    python centerline_extractor.py room.pgm room.yaml --robot-radius 0.15

Output:
    centerline.csv   — x_m, y_m waypoints in world frame (one per line, header row)
    centerline.png   — visualization: grayscale map + extracted centerline overlay
"""

import argparse
import sys
from pathlib import Path

import numpy as np
import yaml
from scipy import ndimage
from skimage import morphology


# ---------------------------------------------------------------------------
# PGM I/O (hand-written for P5 binary; imageio/pillow are fine but this
# avoids an extra dependency and handles edge cases explicitly.)
# ---------------------------------------------------------------------------

def _read_pgm_p5(path: str) -> tuple[np.ndarray, int, int]:
    """Return (ndarray[H,W] uint8, width, height) for a P5 PGM file."""
    with open(path, "rb") as fh:
        header = fh.readline().strip()
        if header != b"P5":
            raise ValueError(f"Expected P5 PGM, got {header!r}")

        # Skip comment lines
        line = fh.readline()
        while line.startswith(b"#"):
            line = fh.readline()

        width, height = map(int, line.split())
        maxval_line = fh.readline().strip()
        maxval = int(maxval_line)
        if maxval > 255:
            raise ValueError(f"Only 8-bit PGM supported (maxval={maxval})")

        raw = fh.read()
        data = np.frombuffer(raw, dtype=np.uint8).reshape((height, width))
    return data, width, height


# ---------------------------------------------------------------------------
# Main class
# ---------------------------------------------------------------------------

class CenterlineExtractor:
    """Extract Voronoi-skeleton centerline from a PGM occupancy grid."""

    def __init__(
        self,
        pgm_path: str,
        yaml_path: str,
        keepout_path: str | None = None,
        robot_radius: float = 0.15,
        min_corridor_width_px: int = 3,
    ):
        self.pgm_path = Path(pgm_path)
        self.yaml_path = Path(yaml_path)
        self.keepout_path = Path(keepout_path) if keepout_path else None
        self.robot_radius = robot_radius
        self.min_corridor_width_px = min_corridor_width_px

        # Internal state populated by load_map()
        self.map_data: np.ndarray | None = None       # raw PGM uint8 [H,W]
        self.resolution: float = 0.05
        self.origin: list[float] = [-3.5, -3.7, 0.0]
        self.width: int = 0
        self.height: int = 0
        self.negate: bool = False

        self.free_mask: np.ndarray | None = None       # bool [H,W], True = free
        self.edt: np.ndarray | None = None              # float [H,W]
        self.skeleton: np.ndarray | None = None         # bool [H,W]
        self.ordered_path: np.ndarray | None = None     # float [N,2] (pixels)
        self.world_path: np.ndarray | None = None       # float [N,2] (meters)

    # ------------------------------------------------------------------
    # Step 1 — load map & metadata
    # ------------------------------------------------------------------

    def load_map(self) -> None:
        """Read PGM, YAML, and optionally keepout mask.  Populate free_mask."""
        # --- PGM ---
        data, w, h = _read_pgm_p5(str(self.pgm_path))
        self.map_data = data
        self.width = w
        self.height = h

        # --- YAML ---
        with open(self.yaml_path) as fh:
            meta = yaml.safe_load(fh)

        self.resolution = float(meta.get("resolution", 0.05))
        self.origin = list(meta.get("origin", [-3.5, -3.7, 0.0]))
        self.negate = bool(meta.get("negate", False))

        print(f"[INFO] Map  : {w}x{h}, resolution={self.resolution} m/pix")
        print(f"[INFO] Origin: {self.origin}")

        # --- Free-space mask ---
        self._build_free_mask()

        # --- Keepout overlay ---
        if self.keepout_path:
            self._apply_keepout()

        # --- Dilation for robot footprint ---
        self._dilate_obstacles()

    def _build_free_mask(self) -> None:
        """
        Binary free-space mask from raw PGM.

        Convention (ROS nav_msgs/OccupancyGrid, values 0-100 scale mapped to 0-255):
          0-50    → known free
          205     → unknown (treat as obstacle)
          254/255 → wall / occupied
        The keepout mask (separate file) uses 0 = lethal, 255 = free.

        If negate=True in YAML, invert the interpretation.
        """
        data = self.map_data.astype(np.int32)

        if self.negate:
            # negate=True: 0=occupied, 255=free (e.g. keepout-style maps)
            free = data >= 200
        else:
            # Standard ROS convention
            free = data <= 50          # known free
            # known obstacles & unknown are already False

        # Guard: make sure we have *some* free space
        if not np.any(free):
            raise RuntimeError("No free space detected in map — check PGM values / negate flag.")

        self.free_mask = free
        print(f"[INFO] Free pixels: {np.sum(free)} / {free.size} "
              f"({100 * np.sum(free) / free.size:.1f}%)")

    def _apply_keepout(self) -> None:
        """Overlay keepout mask: mark keepout pixels (value 0) as obstacles."""
        kp_data, kw, kh = _read_pgm_p5(str(self.keepout_path))
        if (kw, kh) != (self.width, self.height):
            print(f"[WARN] Keepout size {kw}x{kh} != map size {self.width}x{self.height} — skipping")
            return

        # keepout_mask convention: 0 = lethal (occupied), 255 = free
        lethal = kp_data <= 128         # anything dark is lethal
        before = np.sum(self.free_mask)
        self.free_mask[lethal] = False
        after = np.sum(self.free_mask)
        print(f"[INFO] Keepout removed {before - after} pixels "
              f"({100 * (before - after) / max(before, 1):.1f}%)")

    def _dilate_obstacles(self) -> None:
        """Dilate obstacles by robot_radius / resolution pixels."""
        radius_px = max(1, int(np.ceil(self.robot_radius / self.resolution)))
        struct = morphology.disk(radius_px)
        obstacles = ~self.free_mask
        dilated = morphology.binary_dilation(obstacles, struct)
        self.free_mask = ~dilated
        print(f"[INFO] Dilated obstacles by {radius_px} px "
              f"(robot_radius={self.robot_radius:.2f} m)")

    # ------------------------------------------------------------------
    # Step 2 — EDT + skeletonize
    # ------------------------------------------------------------------

    def compute_skeleton(self) -> None:
        """Compute Euclidean Distance Transform and Voronoi skeleton."""
        if self.free_mask is None:
            raise RuntimeError("Call load_map() first.")

        # EDT on free space (distance to nearest obstacle)
        self.edt = ndimage.distance_transform_edt(self.free_mask)

        # Threshold: only keep skeleton inside corridors wider than min width
        wide_enough = self.edt >= self.min_corridor_width_px
        print(f"[INFO] EDT thresholded at {self.min_corridor_width_px} px: "
              f"{np.sum(wide_enough)} pixels remain")

        # Skeletonize (1-pixel-wide medial axis)
        self.skeleton = morphology.skeletonize(wide_enough)
        skel_count = np.sum(self.skeleton)
        print(f"[INFO] Skeleton pixels: {skel_count}")

        if skel_count == 0:
            raise RuntimeError(
                "Skeleton is empty — try lowering min_corridor_width_px "
                "or checking that the map has traversable corridors."
            )

    # ------------------------------------------------------------------
    # Step 3 — trace longest connected path
    # ------------------------------------------------------------------

    def extract_ordered_path(self) -> None:
        """Trace the longest connected skeleton path, ordered end-to-end."""
        if self.skeleton is None:
            raise RuntimeError("Call compute_skeleton() first.")

        # Label connected components
        labeled, num_components = ndimage.label(self.skeleton, structure=np.ones((3, 3)))
        print(f"[INFO] Skeleton connected components: {num_components}")

        if num_components == 0:
            raise RuntimeError("No connected skeleton components after labeling.")

        # Work with the largest component (most likely the main corridor)
        sizes = ndimage.sum_labels(np.ones_like(self.skeleton, dtype=np.int32), labeled, range(1, num_components + 1))
        main_label = np.argmax(sizes) + 1
        main_component = labeled == main_label
        print(f"[INFO] Main component size: {sizes[main_label - 1]} pixels")

        # Find endpoints (8-connected pixels with exactly 1 neighbour in the component)
        endpoints = self._find_endpoints(main_component)
        print(f"[INFO] Endpoints found: {len(endpoints)}")

        if len(endpoints) < 2:
            # Degenerate case: single endpoint or loop → pick arbitrary endpoints
            ys, xs = np.where(main_component)
            if len(ys) < 2:
                raise RuntimeError("Skeleton component too small to trace a path.")
            p0 = (ys[0], xs[0])
            p1 = (ys[-1], xs[-1])
        else:
            # Pick the two farthest-away endpoints (longest path through T-junctions)
            max_dist = -1
            p0 = p1 = endpoints[0]
            for i in range(len(endpoints)):
                for j in range(i + 1, len(endpoints)):
                    dy = endpoints[i][0] - endpoints[j][0]
                    dx = endpoints[i][1] - endpoints[j][1]
                    d = dy * dy + dx * dx
                    if d > max_dist:
                        max_dist = d
                        p0 = endpoints[i]
                        p1 = endpoints[j]

        print(f"[INFO] Traversing from {p0} to {p1}")

        # Trace path via simple BFS-style walk on the 1-pixel skeleton.
        # Because the skeleton is 1-pixel-wide (8-connected), a greedy walk
        # that never revisits pixels works for non-branching segments.
        # For the main component we first thin any remaining branch points.
        path_pixels = self._walk_skeleton(main_component, p0, p1)

        if len(path_pixels) < 2:
            # Fallback: order by closest-pixel chain from p0
            path_pixels = self._walk_skeleton_fallback(main_component, p0)

        self.ordered_path = np.array(path_pixels, dtype=np.float64)
        print(f"[INFO] Traced path: {len(self.ordered_path)} points")

    def _find_endpoints(self, component: np.ndarray) -> list[tuple[int, int]]:
        """Return list of (row, col) skeleton endpoints (exactly 1 neighbor)."""
        # Count 8-connected neighbors for each skeleton pixel
        kernel = np.ones((3, 3), dtype=np.uint8)
        kernel[1, 1] = 0
        neighbor_count = ndimage.convolve(
            component.astype(np.uint8), kernel, mode="constant", cval=0
        )
        # Endpoints: skeleton pixel with exactly 1 neighbor
        endpoint_mask = component & (neighbor_count == 1)
        ys, xs = np.where(endpoint_mask)
        return list(zip(ys.tolist(), xs.tolist()))

    def _walk_skeleton(
        self,
        component: np.ndarray,
        start: tuple[int, int],
        goal: tuple[int, int],
    ) -> list[tuple[int, int]]:
        """Greedy walk from start toward goal, not revisiting.

        For a 1-pixel-wide skeleton this is equivalent to following the
        unique path.  If the skeleton has branches we prune at the first
        junction by preferring the neighbour closest to `goal`.
        """
        visited = np.zeros_like(component, dtype=bool)
        path: list[tuple[int, int]] = []
        current = start
        visited[current] = True
        path.append(current)

        # 8-connected offsets
        neighbours = [
            (-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1),
        ]

        while current != goal:
            cy, cx = current
            candidates = []
            for dy, dx in neighbours:
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < self.height and 0 <= nx < self.width:
                    if component[ny, nx] and not visited[ny, nx]:
                        # Prefer moving toward goal
                        dist = abs(ny - goal[0]) + abs(nx - goal[1])
                        candidates.append((dist, ny, nx))

            if not candidates:
                break

            # Greedy: pick the step closest to goal
            candidates.sort(key=lambda t: t[0])
            _, ny, nx = candidates[0]
            visited[ny, nx] = True
            current = (ny, nx)
            path.append(current)

        return path

    def _walk_skeleton_fallback(
        self, component: np.ndarray, start: tuple[int, int]
    ) -> list[tuple[int, int]]:
        """Fallback trace when goal-directed walk fails: DFS to longest leaf."""
        visited = np.zeros_like(component, dtype=bool)
        stack = [(start, [start])]
        longest_path: list[tuple[int, int]] = [start]

        neighbours = [
            (-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1),
        ]

        while stack:
            current, path = stack.pop()
            cy, cx = current
            visited[cy, cx] = True

            if len(path) > len(longest_path):
                longest_path = path

            extended = False
            for dy, dx in neighbours:
                ny, nx = cy + dy, cx + dx
                if 0 <= ny < self.height and 0 <= nx < self.width:
                    if component[ny, nx] and not visited[ny, nx]:
                        stack.append(((ny, nx), path + [(ny, nx)]))
                        extended = True

            if not extended and len(path) > len(longest_path):
                longest_path = path

        return longest_path

    # ------------------------------------------------------------------
    # Step 4 — smoothing
    # ------------------------------------------------------------------

    def smooth_path(self, window: int = 3) -> None:
        """Apply moving-average smoothing to pixel-path."""
        if self.ordered_path is None or len(self.ordered_path) < window:
            return

        kernel = np.ones(window, dtype=np.float64) / window
        smoothed_y = np.convolve(self.ordered_path[:, 0], kernel, mode="same")
        smoothed_x = np.convolve(self.ordered_path[:, 1], kernel, mode="same")

        # Keep ends fixed to preserve start/goal positions
        half = window // 2
        smoothed_y[:half] = self.ordered_path[:half, 0]
        smoothed_y[-half:] = self.ordered_path[-half:, 0]
        smoothed_x[:half] = self.ordered_path[:half, 1]
        smoothed_x[-half:] = self.ordered_path[-half:, 1]

        self.ordered_path = np.column_stack([smoothed_y, smoothed_x])
        print(f"[INFO] Smoothed path (moving average, window={window})")

    # ------------------------------------------------------------------
    # Step 5 — pixel → world coordinates
    # ------------------------------------------------------------------

    def to_world(self) -> np.ndarray:
        """Convert ordered pixel path to world-frame (x_m, y_m)."""
        if self.ordered_path is None:
            raise RuntimeError("Call extract_ordered_path() first.")

        # ROS map convention:
        #   x_world = origin_x + (pixel_col + 0.5) * resolution
        #   y_world = origin_y + (map_height - pixel_row - 0.5) * resolution
        ox = self.origin[0]
        oy = self.origin[1]

        points = []
        for row, col in self.ordered_path:
            wx = ox + (col + 0.5) * self.resolution
            wy = oy + (self.height - row - 0.5) * self.resolution
            points.append((wx, wy))

        self.world_path = np.array(points, dtype=np.float64)
        return self.world_path

    # ------------------------------------------------------------------
    # Step 6 — output
    # ------------------------------------------------------------------

    def save_csv(self, output_path: str | Path) -> None:
        """Write centerline waypoints as CSV (x_m,y_m header + rows)."""
        if self.world_path is None:
            raise RuntimeError("Call to_world() first.")

        output_path = Path(output_path)
        np.savetxt(
            str(output_path),
            self.world_path,
            delimiter=",",
            header="x_m,y_m",
            comments="",
            fmt="%.6f",
        )
        print(f"[INFO] Saved {len(self.world_path)} waypoints → {output_path}")

    def save_visualization(self, output_path: str | Path) -> None:
        """Render grayscale map + centerline overlay to PNG."""
        try:
            import matplotlib
            matplotlib.use("Agg")
            import matplotlib.pyplot as plt
        except ImportError:
            print("[WARN] matplotlib not available — skipping visualization")
            return

        output_path = Path(output_path)

        fig, ax = plt.subplots(figsize=(10, 10 * self.height / max(self.width, 1)))

        # Background: raw PGM as grayscale
        if self.map_data is not None:
            ax.imshow(self.map_data, cmap="gray", origin="upper")

        # Skeleton overlay
        if self.skeleton is not None:
            ys, xs = np.where(self.skeleton)
            ax.scatter(xs, ys, c="cyan", s=0.3, alpha=0.4, label="full skeleton")

        # Extracted centerline (pixel coords: col=x, row=y)
        if self.ordered_path is not None:
            ax.plot(
                self.ordered_path[:, 1],
                self.ordered_path[:, 0],
                "r-",
                linewidth=1.5,
                label="centerline",
            )

        ax.set_title("Voronoi Centerline Extraction")
        ax.legend(loc="upper right")
        ax.set_xlabel("pixel x")
        ax.set_ylabel("pixel y")

        fig.tight_layout()
        fig.savefig(str(output_path), dpi=150, bbox_inches="tight")
        plt.close(fig)
        print(f"[INFO] Visualization saved → {output_path}")

    # ------------------------------------------------------------------
    # Top-level pipeline
    # ------------------------------------------------------------------

    def run(self) -> None:
        """Execute the full extraction pipeline."""
        self.load_map()
        self.compute_skeleton()
        self.extract_ordered_path()
        self.smooth_path(window=3)
        self.to_world()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract Voronoi skeleton centerline from a PGM occupancy grid.",
    )
    parser.add_argument("pgm", help="Path to room.pgm")
    parser.add_argument("yaml", help="Path to room.yaml")
    parser.add_argument(
        "--keepout",
        default=None,
        help="Path to keepout_mask.pgm (optional)",
    )
    parser.add_argument(
        "--robot-radius",
        type=float,
        default=0.15,
        help="Robot radius in meters (default: 0.15)",
    )
    parser.add_argument(
        "--min-corridor-width-px",
        type=int,
        default=3,
        help="Minimum EDT value for skeleton inclusion (default: 3 px)",
    )
    parser.add_argument(
        "--csv-out",
        default="centerline.csv",
        help="Output CSV path (default: centerline.csv)",
    )
    parser.add_argument(
        "--png-out",
        default="centerline.png",
        help="Output visualization PNG path (default: centerline.png)",
    )
    parser.add_argument(
        "--no-viz",
        action="store_true",
        help="Skip visualization PNG",
    )
    args = parser.parse_args()

    # Resolve paths relative to cwd so the tool works from any directory
    pgm_path = str(Path(args.pgm).resolve())
    yaml_path = str(Path(args.yaml).resolve())
    keepout_path = str(Path(args.keepout).resolve()) if args.keepout else None

    extractor = CenterlineExtractor(
        pgm_path=pgm_path,
        yaml_path=yaml_path,
        keepout_path=keepout_path,
        robot_radius=args.robot_radius,
        min_corridor_width_px=args.min_corridor_width_px,
    )

    try:
        extractor.run()
    except Exception as exc:
        print(f"[ERROR] Extraction failed: {exc}", file=sys.stderr)
        sys.exit(1)

    extractor.save_csv(args.csv_out)

    if not args.no_viz:
        extractor.save_visualization(args.png_out)

    print("[INFO] Done.")


if __name__ == "__main__":
    main()
