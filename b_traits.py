
from rpg_dice import roll
from enum import Enum
class BTrait(Enum):
    PMM = "P--"
    PM = "P-"
    SM = "S-"
    CM = "C-"
    DM = "D-"
    NONE = ""
    DP = "D+"
    PP = "P+"
    CP = "C+"
    SP = "S+"
    PPP = "P++"
    TP = "T+"


def get_random_trait() -> BTrait:
    trait_roll = ("2d10")
    match trait_roll:
        case 2:
            return BTrait.PMM
        case 3:
            return BTrait.PM
        case 4:
            return BTrait.SM
        case 5:
            return BTrait.CM
        case 6:
            return BTrait.DM
        case 15:
            return BTrait.DP
        case 16:
            return BTrait.PP
        case 17:
            return BTrait.CP
        case 18:
            return BTrait.SP
        case 19:
            return BTrait.TP
        case 20:
            return BTrait.PPP
        case _: 
            return BTrait.NONE
        