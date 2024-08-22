
from enum import Enum
#Determines if a pitcher will get better results on average, with Prospect considered a higher quality player.
class Pitcher_Quality(Enum):
   PROSPECT = 1
   FARMHAND = 2
# Similar to Pitcher Quality but for Batters
class Batter_Quality(Enum):
   PROSPECT = 1
   FARMHAND = 2

#We create a union for  both types of player quality
Player_Quality = Batter_Quality | Pitcher_Quality