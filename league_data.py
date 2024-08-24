""" League data contains 2 enums, Era and LeagueGender, 
which are used in the process of generating players and teams."""

from enum import Enum


class Era(Enum):
    """Deadball has 2 rulesets, a ruleset for modern baseball,
    and a ruleset for baseball in the 1900. The ruleset effect
    player generation, and the number of pitchers a team has.
    ANCIENT represents 1900's baseball, while MODERN is for the modern era.
    Pitchers generated with the ANCIENT variant will tend to have higher pitch
    die, however their teams will have less pitchers."""

    ANCIENT = "Ancient"
    MODERN = "Modern"


class LeagueGender(Enum):
    """This enum is used when creating a player's name,
    it does not affect a players performance."""

    MALE = "Male"
    FEMALE = "Female"
    COED = "Coed"
