
from rpg_dice import roll
from enum import Enum



class BTraitValue:
    def __init__(self,str: str, category: str, number: int) -> None:
        self.str = str
        self.category = category
        self.number = number

  

class BTrait(Enum):
    PMinusMinus = BTraitValue("P--","Power",-2)
    PMinus = BTraitValue("P-","Power",-1)
    SMinus = BTraitValue("S-","Speed",-1)
    CMinus = BTraitValue("C-","Contact",-1)
    DMinus = BTraitValue("D-","Defense",-1)
    NONE = BTraitValue("","None",0)
    DPlus = BTraitValue("D+","Defense",1)
    PPlus = BTraitValue("P+","Power",1)
    CPlus = BTraitValue("C+","Contact",1)
    SPlus = BTraitValue("S+","Speed",1)
    PPlusPlus = BTraitValue("P++","Power",2)
    TPlus = BTraitValue("T+","Durability",1)


def get_random_trait() -> BTrait:
    trait_roll = roll("2d10")
    match trait_roll:
        case 2:
            return BTrait.PMinusMinus
        case 3:
            return BTrait.PMinus
        case 4:
            return BTrait.SMinus
        case 5:
            return BTrait.CMinus
        case 6:
            return BTrait.DMinus
        case 15:
            return BTrait.DPlus
        case 16:
            return BTrait.PPlus
        case 17:
            return BTrait.CPlus
        case 18:
            return BTrait.SPlus
        case 19:
            return BTrait.TPlus
        case 20:
            return BTrait.PPlusPlus
        case _: 
            return BTrait.NONE

def sort_BTrait(trait: BTrait) -> int:
    return trait.value.number             