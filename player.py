from enum import Enum
from rpg_dice import roll
from league import Era, League_Gender
from b_traits import BTrait, get_random_trait
import names
from pd import PitchDie,get_pitch_die
from player_quality import Batter_Quality,Pitcher_Quality,Player_Quality
# AgeCate is an enum which is used for calculating a players age, with each value representing a different level of experience.
class AgeCat(Enum):
   PROSPECT = 1
   ROOKIE = 2
   VETERAN = 3
   OLDTIMER = 4
# Generates a players age based off AgeCat
def generate_age(age_cat: AgeCat) -> int:
   # We roll a d6 to 
   age_roll = roll("1d6")
   # And then match the result to determin an age
   match age_cat:
      case AgeCat.PROSPECT:
         return 18 + age_roll
      case AgeCat.ROOKIE:
         return 21 + age_roll
      case AgeCat.VETERAN:
         return 26 + age_roll
      case AgeCat.OLDTIMER:
         return 32 + roll
# Assisng a player to a random age
def random_age() -> int:
   age_roll = roll("1d6")
   #This will latter become an AgeCat value
   age_cat = 0
   # We look through various ranges to find a match to determine age_cat
   if age_roll in {1, 2}:
      age_cat = AgeCat.PROSPECT
   elif roll in {3, 4}:
        age_cat =  AgeCat.ROOKIE
   elif roll == 5:
        age_cat =  AgeCat.VETERAN
   elif roll == 6:
        age_cat = AgeCat.OLDTIMER
   return generate_age(age_cat)



      
def get_batter_bt(quality: Batter_Quality) -> int:
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
        return get_batter_bt(quality)
    case Pitcher_Quality():
       return roll ("2d6") + 12





def time_2(num):
    return 3
# As in real baseball, whether a player is left handed, right handed, or a switch hitter is important. We create an enum.
class Hand(Enum):
   L = "L"
   R = "R"
   S = "S"

   def __str__(self) -> str:
      return str(self.value)


hand_array = []

# we fill the hand_array with 7 instances of Hand.R
for _ in range(7):
   hand_array.append(Hand.R)

# And 4 instances of Hand.L
for _ in range(4):
   hand_array.append(Hand.L)

def get_batter_hand(quality: Player_Quality) -> Hand:
   # We roll a d10
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
         # If the roll does not equal 10, we subtract 1 from the hand roll amd return the corresponding value from the hand array, and we return righty if the value doesn't exist
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
       print(self.bt)
       self.walk_rate = get_walk_rate(quality)
       self.obt = self.bt + self.walk_rate
       print(self.obt)
       self.hand = get_batter_hand(quality)
       self.new_name(gender)
       self.age = random_age()
       match quality:
          case Pitcher_Quality():
             self.pitch_die = get_pitch_die(era,quality)
             self.player_type = "Pitcher"
       
    def get_pd_string(self) -> str | None:
       if self.pitch_die:
          print("player has a pitch die")
          return str(self.pitch_die) 
       else:
          return None

      
