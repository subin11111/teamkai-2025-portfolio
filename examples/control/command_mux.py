"""Offline portfolio excerpt: stop priority and manual/automatic selection.

Adapted from Team K.A.I. 2025 Control throttle_serial_py/rpm_mux.py.
Values are dimensionless demo inputs; no RPM conversion or hardware output.
"""

from enum import Enum
from math import isfinite


class Mode(Enum):
    MANUAL = "manual"
    AUTO = "auto"


def select_value(*, mode: Mode, manual: float, automatic: float,
                 stopped: bool, automatic_enabled: bool) -> float:
    """Show the selection concept; this is not a vehicle safety controller."""
    if not isinstance(mode, Mode):
        raise ValueError("mode must be a Mode")
    if stopped:
        return 0.0
    if mode is Mode.MANUAL:
        value = manual
    elif automatic_enabled:
        value = automatic
    else:
        return 0.0
    if not isfinite(value):
        raise ValueError("selected demo input must be finite")
    return value


if __name__ == "__main__":
    for stopped in (False, True):
        value = select_value(mode=Mode.AUTO, manual=0.2, automatic=0.4,
                             stopped=stopped, automatic_enabled=True)
        print({"stopped": stopped, "selected_demo_value": value})
