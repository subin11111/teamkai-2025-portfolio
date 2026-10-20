"""Offline portfolio excerpt: look-ahead selection and Pure Pursuit geometry.

Adapted from Team K.A.I. 2025 Planning pure_pursuit_static.cpp.
Competition paths, tuning, vehicle geometry and ROS output are omitted.
"""

from math import atan2, hypot, isfinite

Point = tuple[float, float]


def select_target(points: list[Point], distance: float) -> Point | None:
    """Pick the first forward point outside the requested look-ahead radius."""
    if not isfinite(distance) or distance <= 0:
        raise ValueError("distance must be finite and positive")
    forward = [p for p in points if all(isfinite(v) for v in p) and p[0] > 0]
    return next((p for p in forward if hypot(*p) >= distance),
                forward[-1] if forward else None)


def steering_radians(target: Point, wheelbase: float) -> float:
    """Return the standard geometric angle, without actuation or tuning."""
    x, y = target
    if not all(isfinite(v) for v in (x, y, wheelbase)) or x <= 0 or wheelbase <= 0:
        raise ValueError("a finite forward target and positive wheelbase are required")
    return atan2(2.0 * wheelbase * y, x * x + y * y)


if __name__ == "__main__":
    synthetic_path = [(1.0, 0.0), (3.0, 1.0), (6.0, 2.0)]
    target = select_target(synthetic_path, distance=3.0)
    if target is not None:
        print({"target": target, "angle_rad": steering_radians(target, wheelbase=1.0)})
