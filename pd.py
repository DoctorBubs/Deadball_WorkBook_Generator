
from enum import Enum
from player import Player_Quality, Batter_Quality, Pitcher_Quality
from league import Era
from rpg_dice import roll
class PitchDie(Enum):
    d20 = 20
    d12 = 12
    d8 = 8
    d6 = 6
    d4 = 4
    NONE = 0
    md4 = -4
    md8 = -8

modern_d8_range = range(2,4)
modern_d4_range = range(4,8)

def new_modern_die(off_set: int) -> PitchDie:
    pitch_roll = roll("1d8") + off_set
    match pitch_roll:
        case 1:
            return PitchDie.d12
        case modern_d8_range if pitch_roll in modern_d8_range:
            return PitchDie.d8
        case modern_d4_range if pitch_roll in modern_d4_range:
            return PitchDie.d4
        case _:
            return PitchDie.d8
            



def get_pitch_die(era: Era, quality: Pitcher_Quality) -> PitchDie:
    off_set
    match quality:
        case Pitcher_Quality.PROSPECT:
            off_set = 0
        case Pitcher_Quality.FARMHAND:
            off_set = 2
    match era:
        case Era.MODERN():
            return new_modern_die(off_set)
        case era.ANCIENT():
            return new_ancient_die(off_set)
    
