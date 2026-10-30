"""Numerical operations shared by the CLI and notebook."""

import numpy as np
import numpy.typing as npt

from .processing import summarize

ROOM_NAMES = ("north_room", "south_room", "storage_room")
type FloatArray = npt.NDArray[np.float64]


def select_warm_rounds(
    readings: FloatArray, umbral: int
) -> dict[str, dict[str, float]]:
    """Select warm measurement rounds by umbral."""
    select_readings = readings.copy()
    cell_mask = select_readings[:, 0] >= umbral
    return select_readings[cell_mask]
    
