from enum import Enum
from rpg_dice import roll
from league import Era, League_Gender
from b_traits import BTrait, get_random_trait
import names

class AgeCat(Enum):
   Prospect = 1
   Rookie = 2
   Veteran = 3
   OldTimer = 4



class Pitcher_Quality(Enum):
   PROSPECT = 1
   FARMHAND = 2

class Batter_Quality(Enum):
   PROSPECT = 1
   FARMHAND = 2

Player_Quality = Batter_Quality | Pitcher_Quality



         
       
         

def generate_age(age_cat: AgeCat) -> int:
   age_roll = roll("1d6")
   match age_cat:
      case AgeCat.Prospect:
         return 18 + age_roll
      case AgeCat.Rookie:
         return 21 + age_roll
      case AgeCat.Veteran:
         return 26 + age_roll
      case AgeCat.Veteran:
         32 + roll


      
def get_batter_bt(quality: Batter_Quality, era: Era) -> int:
   match quality:
      case Batter_Quality.PROSPECT:
         return roll("2d10") + 15
      case Batter_Quality.FARMHAND:
         return roll ("2d10") + 12

def get_walk_rate(quality: Player_Quality) -> int:
   match quality:
      case Batter_Quality():
         return roll("2d4")
      case Pitcher_Quality():
         return roll("1d8")
      


def generate_bt(quality: Player_Quality) -> int:
 match quality:
    case Batter_Quality():
        return get_batter_bt()
    case Pitcher_Quality():
       return roll ("2d6") + 12





def time_2(num):
    return 3

class Hand(Enum):
   L = "L"
   R = "R"
   S = "S"

hand_array = []

for _ in range(6):
   hand_array.append(Hand.R)

for _ in range(3):
   hand_array.append(Hand.L)

def get_batter_hand(quality: Player_Quality) -> Hand:
   hand_roll = roll("1d10")
   match hand_roll:
      # Rolling a 10 is a special action. If the player is a batter. then the batter will be a switch hitter,otherwise the batter will be a lefty
      case 10:
         match quality:
            case Batter_Quality():
               return Hand.S
            case Pitcher_Quality():
               return Hand.L
      case _:
         # If the roll does not equal 10, we subtract 1 from the hand roll amd return the corresponding value from the hand array, and we return righty if the valeu doesn't exist
         return hand_array[hand_roll - 1] or Hand.R


class Player:
    def new_name(self, gender: League_Gender):
       self.last_name = names.get_last_name()
       match gender:
          case League_Gender.MALE: 
             self.first_name = names.get_first_name(gender='male') 
          case League_Gender.FEMALE:
             self.first_name = names.get_first_name(gender='female')
          case _:
             self.first_name = names.get_first_name()
    def __init__(self,era: Era, gender: League_Gender, quality: Player_Quality, pos: str) -> None:
       self.bt = generate_bt(quality)
       self.walk_rate = get_walk_rate(quality)
       self.obt = self.bt + self.walk_rate
       self.hand = get_batter_hand(quality)
       self.new_name(gender)
       
