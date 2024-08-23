from enum import Enum
from rpg_dice import roll


class BTraitValue:
    """Value used for the BTrait enum, used to compare traits."""

    def __init__(self, string: str, category: str, number: int) -> None:
        self.string = string
        self.category = category
        self.number = number


class BTrait(Enum):
    """BTraits are the traits that only batters have, such as increased speed or lowered defense."""

    PMINUSMINUS = BTraitValue("P--", "Power", -2)
    PMINUS = BTraitValue("P-", "Power", -1)
    SMINUS = BTraitValue("S-", "Speed", -1)
    CMINUS = BTraitValue("C-", "Contact", -1)
    DMINUS = BTraitValue("D-", "Defense", -1)
    NONE = BTraitValue("", "None", 0)
    DPLUS = BTraitValue("D+", "Defense", 1)
    PPLUS = BTraitValue("P+", "Power", 1)
    CPLUS = BTraitValue("C+", "Contact", 1)
    SPLUS = BTraitValue("S+", "Speed", 1)
    PPLUSPLUS = BTraitValue("P++", "Power", 2)
    TPLUS = BTraitValue("T+", "Durability", 1)


def get_random_btrait() -> BTrait:
    """Generates a random BTrait based of one d20 roll"""
    trait_roll = roll("2d10")
    match trait_roll:
        case 2:
            return BTrait.PMINUSMINUS
        case 3:
            return BTrait.PMINUS
        case 4:
            return BTrait.SMINUS
        case 5:
            return BTrait.CMINUS
        case 6:
            return BTrait.DMINUS
        case 15:
            return BTrait.DPLUS
        case 16:
            return BTrait.PPLUS
        case 17:
            return BTrait.CPLUS
        case 18:
            return BTrait.SPLUS
        case 19:
            return BTrait.TPLUS
        case 20:
            return BTrait.PPLUSPLUS
        case _:
            return BTrait.NONE


def sort_btrait(trait: BTrait) -> int:
    """Used to sort BTraits via their values number."""
    return trait.value.number
