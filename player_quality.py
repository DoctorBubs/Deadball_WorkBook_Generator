""" Player Quality is used during player generation, to determine if a player is a batter or pitcher, and how good the player will be"""

from enum import Enum


class PitcherQuality(Enum):
    """Used to generate pitchers. Players generated with PROSPECT will tend to have higher pitch dice and more traits"""

    PROSPECT = 1
    FARMHAND = 2


# Similar to Pitcher Quality but for Batters
class BatterQuality(Enum):
    """Used to generate batters. Players generated with PROSPECT have higher bt and more traits."""

    PROSPECT = 1
    FARMHAND = 2


# We create a union for  both types of player quality
PlayerQuality = BatterQuality | PitcherQuality
