'''PTrait determine what traits a pitcher has.'''
from enum import Enum
from rpg_dice import roll



class PTrait(Enum):
    '''This enun represents a pitchers trait. NONE represents no trait.'''
    CNMINUS = "CN-"
    KPLUS = "K+"
    GBPLUS = "GB+"
    CNPLUS = "C+"
    STPLUS = "ST+"
    NONE = ""

    def __str__(self) -> str:
        return self.value


def get_random_ptrait() -> PTrait:
    '''Generates a random PTrait'''
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


def sort_ptrait(trait: PTrait) -> int:
    '''Sorts PTraits. CMINUS = -1, NONE = 0, all others = 1'''
    match trait:
        case PTrait.CNMINUS:
            return -1
        case PTrait.NONE:
            return 0
        case _:
            return 1


# Unlike batting traits, only 2 pitching trains contracdict eachother, CNMINUS and CNPLUS.
command_traits = [PTrait.CNMINUS, PTrait.CNPLUS]


def conflicting_ptrait(trait_a: PTrait, trait_b: PTrait) -> bool:
    ''' To determine if there is a conflict between two pitching traits,
     we check if both traits are related to command.
     If they are, their is a conflict'''
    return trait_a in command_traits and trait_b in command_traits
