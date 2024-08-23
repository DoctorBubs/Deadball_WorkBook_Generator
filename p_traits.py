from rpg_dice import roll
from enum import Enum


class PTrait(Enum):
    CNMINUS = "CN-"
    KPLUS = "K+"
    GBPLUS = "GB+"
    CNPLUS = "C+"
    STPLUS = "ST+"
    NONE = ""

    def __str__(self) -> str:
        return self.value


def get_random_PTrait() -> PTrait:
    trait_roll = roll("2d10")
    match trait_roll:
        case 5:
            return PTrait.CNMINUS
        case 15:
            return PTrait.KPLUS
        case 16:
            return PTrait.GBPLUS
        case 17:
            return PTrait.CNPLUS
        case 18:
            return PTrait.STPLUS
        case _:
            return PTrait.NONE


def sort_PTrait(trait: PTrait) -> int:
    match trait:
        case PTrait.CNMINUS:
            return -1
        case PTrait.NONE:
            return 0
        case _:
            return 1


# Unlike batting traits, only 2 pitching trains contracdict eachother, CNMINUS and CNPLUS.
command_traits = [PTrait.CNMINUS, PTrait.CNPLUS]


# To determine if there is a conflict between two pitching traits, we check if both traits are related to command
# If they are, their is a conflict
def conflicting_PTrait(trait_a: PTrait, trait_b: PTrait) -> bool:
    return trait_a in command_traits and trait_b in command_traits
