import json
import random
from typing import Any, Callable


def calculate_damage(attack: int, defense: int) -> int:
    """Calculate damage dealt.

    Damage is the attack minus defense with a minimum of 1.
    """
    return max(attack - defense, 1)


def encounter_occurs(rate: float, rng: Callable[[], float] = random.random) -> bool:
    """Determine if an encounter occurs given a rate and RNG."""
    return rng() < rate


def save_game(state: Any, filename: str) -> None:
    """Save state to a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(state, f)


def load_game(filename: str) -> Any:
    """Load game state from a JSON file."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
