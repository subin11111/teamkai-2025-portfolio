"""Offline portfolio excerpt: valid detection centers, ordered along x.

Adapted from Team K.A.I. 2025 Perception_25 cone_detection_node.cpp.
ROS messages, clustering, models, calibration and real sensor data are omitted.
"""

from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True)
class Detection:
    center: tuple[float, float, float]
    valid: bool


def ordered_centers(detections: list[Detection]) -> list[tuple[float, float, float]]:
    """Select valid finite centers and sort by the forward-axis coordinate."""
    centers = [item.center for item in detections
               if item.valid and all(isfinite(value) for value in item.center)]
    return sorted(centers, key=lambda point: point[0])


if __name__ == "__main__":
    synthetic = [Detection((6.0, 2.0, 0.0), True),
                 Detection((2.0, -1.0, 0.0), True),
                 Detection((1.0, 0.0, 0.0), False)]
    print(ordered_centers(synthetic))
