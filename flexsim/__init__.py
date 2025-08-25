"""FlexSim core package."""

from .mechanics import (
    calculate_damage,
    encounter_occurs,
    save_game,
    load_game,
)

__all__ = [
    "calculate_damage",
    "encounter_occurs",
    "save_game",
    "load_game",
]
