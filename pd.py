"""Pitchers in deadball have pitch dice, which correspnd to which dice is thrown when a pitcher is used during a plate appearance."""

from enum import Enum
from rpg_dice import roll
from league_data import Era
from player_quality import PitcherQuality


class PitchDie(Enum):
    """A pitcher's pitchdie. The value of each enum corresponds to max value
    away from zero that the die is capable of. Higher is better!"""

    d20 = 20
    d12 = 12
    d8 = 8
    d6 = 6
    d4 = 4
    NONE = 0
    md4 = -4
    md8 = -8

    def __str__(self) -> str:
        return str(self.value)


# These ranges are used when generating a pitch die based off modern setting.
modern_d8_range = range(2, 4)
modern_d4_range = range(4, 8)


def new_modern_die(off_set: int) -> PitchDie:
    """Generates a modern pitch die based off modern rules, with off_set limiting the best result possible."""
    pitch_roll = roll("1d8") + off_set
    match pitch_roll:
        case 1:
            return PitchDie.d12
        # Otherwise, we search the modern die ranges to see if we can find the roll.
        case pitch_roll if pitch_roll in modern_d8_range:
            return PitchDie.d8
        case pitch_roll if pitch_roll in modern_d4_range:
            return PitchDie.d4
        case _:
            # If we haven't, then we return the d8.
            return PitchDie.d8


# These r
ancient_ranges = [
    {
        "die": PitchDie.d12,
        "range": range(2, 4),
    },
    {
        "die": PitchDie.d8,
        "range": range(4, 6),
    },
    {
        "die": PitchDie.d6,
        "range": range(6, 9),
    },
    {
        "die": PitchDie.d4,
        "range": range(9, 11),
    },
    {"die": PitchDie.md4, "range": range(12, 14)},
]


def new_ancient_die(off_set: int) -> PitchDie:
    """Generates an pitch die based off ancient rules, with off_set limiting the best result possible."""
    pitch_roll = roll("1d12") + off_set
    match pitch_roll:
        # If the roll = 1, the pitchdie will be D20.
        case 1:
            return PitchDie.d20
        case _:
            # Otherwise, we loop ancient range. If the pitch_roll is found in the range, then the corresponsding die is returned.
            result = None
            for range_dict in ancient_ranges:
                if pitch_roll in range_dict.get("range"):
                    result = range_dict.get("die")
                    break
            # If we have not found a pitch die at this point, the d8 is returned.
            return result or PitchDie.md8


def get_pitch_die(era: Era, quality: PitcherQuality) -> PitchDie:
    """Generates a pitch die based off era and quality."""
    off_set = None
    match quality:
        case PitcherQuality.PROSPECT:
            off_set = 0
        case PitcherQuality.FARMHAND:
            off_set = 2
    match era:
        case Era.MODERN:
            return new_modern_die(off_set)
        case Era.ANCIENT:
            return new_ancient_die(off_set)
