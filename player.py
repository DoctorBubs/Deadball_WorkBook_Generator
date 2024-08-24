""" Players are  the people who make up teams. They may be pitchers or batters, and are customized in a variety of different ways."""

from enum import Enum
from rpg_dice import roll
import names
from league_data import Era, League_Gender
from b_traits import BTrait, get_random_btrait, sort_btrait
from p_traits import PTrait, get_random_ptrait, sort_ptrait, conflicting_ptrait

from pd import get_pitch_die, PitchDie
from player_quality import BatterQuality, PitcherQuality, PlayerQuality


class AgeCat(Enum):
    """AgeCat is an enum which is used for calculating a players age,
    with each value representing a different level of experience."""

    PROSPECT = 1
    ROOKIE = 2
    VETERAN = 3
    OLDTIMER = 4


def generate_age(age_cat: AgeCat) -> int:
    """Generates a players age based off AgeCat"""
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
            return 32 + age_roll


def random_age() -> int:
    """Assisgns a player to a random age"""
    age_roll = roll("1d6")
    # This will latter become an AgeCat value
    age_cat = None
    # We look through various ranges to find a match to determine age_cat.
    if age_roll in range(1, 3):
        age_cat = AgeCat.PROSPECT
    elif age_roll in range(3, 5):
        age_cat = AgeCat.ROOKIE
    elif age_roll == 5:
        age_cat = AgeCat.VETERAN
    elif age_roll == 6:
        age_cat = AgeCat.OLDTIMER
    return generate_age(age_cat)


def get_batter_bt(quality: BatterQuality) -> int:
    """Generates a batting target for a batter based off it's BatterQuality."""
    match quality:
        case BatterQuality.PROSPECT:
            return roll("2d10") + 15
        case BatterQuality.FARMHAND:
            return roll("2d10") + 12


def get_walk_rate(quality: PlayerQuality) -> int:
    """Generates a walk rate for a player based of whether or not it is a pitcher."""
    match quality:
        case BatterQuality():
            return roll("2d4")
        case PitcherQuality():
            return roll("1d8")


def generate_bt(quality: PlayerQuality) -> int:
    """Generates a players bt based off whether or not it is a pitcher"""
    match quality:
        case BatterQuality():
            return get_batter_bt(quality)
        case PitcherQuality():
            return roll("2d6") + 12


class Hand(Enum):
    """#As in real baseball, whether a player is left handed,
    right handed, or a switch hitter is important,
    which here is represented by an enum."""

    L = "L"
    R = "R"
    S = "S"

    def __str__(self) -> str:
        return str(self.value)


## Since players hands are generated at random, we create a list to aid in the generation.
hand_list = []

# we fill the hand_list with 7 instances of Hand.R
for _ in range(7):
    hand_list.append(Hand.R)

# And 4 instances of Hand.L
for _ in range(4):
    hand_list.append(Hand.L)


def get_batter_hand(quality: PlayerQuality) -> Hand:
    """Determines what hand a player uses."""
    # We roll a d10
    hand_roll = roll("1d10")
    match hand_roll:
        # Rolling a 10 is a special action. If the player is a batter,
        # then the batter will be a switch hitter,otherwise the batter will be a lefty '''
        case 10:
            match quality:
                case BatterQuality():
                    return Hand.S
                case PitcherQuality():
                    return Hand.L
        case _:
            # If the roll does not equal 10, we subtract 1 from the hand roll
            # and return the corresponding value from the hand array, and we return righty if the value doesn't exist
            return hand_list[hand_roll - 1] or Hand.R


class Player:
    """The player class"""

    def new_name(self, gender: League_Gender):
        """Generates a name for a player based off League_Gender"""
        self.last_name = names.get_last_name()
        match gender:
            case League_Gender.MALE:
                self.first_name = names.get_first_name(gender="male")
            case League_Gender.FEMALE:
                self.first_name = names.get_first_name(gender="female")
            case _:
                self.first_name = names.get_first_name()

    def __init__(
        self, era: Era, gender: League_Gender, quality: PlayerQuality, pos: str
    ) -> None:
        # First we generate a players bt,walk rate, obt, and hand.
        # bt is short for batting target. In real life baseball, it corresponds to a players batting average.
        self.bt = generate_bt(quality)
        # walk rate is how often a player's walks, as in real life baseball
        self.walk_rate = get_walk_rate(quality)
        """obt is short ofr on base target. It corresponds to a real life player OBP, and is calulated by adding a
        players bt and walkrate."""
        self.obt = self.bt + self.walk_rate
        """ We determine if a player bats and/or pitches right handed or left handed. 
        Batters can also be switch hitters, but not pitchers"""
        self.hand = get_batter_hand(quality)
        # Then we generate the player's gender and age.
        self.new_name(gender)
        self.age = random_age()
        """ We also define a players pos, which is short for position in the field.
        """
        self.pos = pos
        # We generate traits for the player, which varies depending if the player is a pitcher or batter

        self.traits = []
        match quality:
            case PitcherQuality():
                # If a player is a pitcher, we generate it's pitch die and a potential pitching trait.
                self.pitch_die = get_pitch_die(era, quality)
                first_trait = get_random_ptrait()
                self.traits.append(first_trait)
                match quality:
                    # If the pitcher is a farmhand, they roll for a trail only once.
                    case PitcherQuality.FARMHAND:
                        pass
                    # Otherwise, if the pitcher received a trait on the first roll, it rolls for another trait.
                    case PitcherQuality.PROSPECT:
                        match first_trait:
                            case PTrait.NONE:
                                pass
                            case _:
                                second_trait = get_random_ptrait()
                                # We check to make sure the second trait doesn't conflict with the first trait.
                                trait_conflict = conflicting_ptrait(
                                    first_trait, second_trait
                                )
                                if trait_conflict:
                                    pass
                                else:
                                    # If there is no conflict, the second trait is added to the trait list, which is sorted.
                                    self.traits.append(second_trait)
                                    self.traits.sort(reverse=True, key=sort_ptrait)
            case BatterQuality():
                first_trait = get_random_btrait()
                self.traits.append(first_trait)
                # If the batter is a prospect, the batter gets a second chance to gain a trait if the batter gained one on the first roll
                match quality:
                    case BatterQuality.FARMHAND:
                        pass
                    case BatterQuality.PROSPECT:
                        # If the batter did not gain a trait, then pass.
                        match first_trait:
                            case BTrait.NONE:
                                pass
                            case _:
                                # Otherwise, a second trait is found, and if it is not in the same category as the first, it is added to the trait list.
                                second_trait = get_random_btrait()
                                if (
                                    second_trait.value.category
                                    != first_trait.value.category
                                ):
                                    self.traits.append(second_trait)
                                    # The trait list is sorted so positive traits show first
                                    self.traits.sort(reverse=True, key=sort_btrait)

    def get_pitching_trait_string(self) -> str:
        """Converts a pitcher's trait list to a string."""
        result = None
        for trait in self.traits:
            if result:
                result = result + str(trait)
            else:
                result = str(trait)
        return result

    def get_pitching_info(self) -> list:
        """Returns a list of a pitcher's data to be used on a worksheet."""
        return [
            self.pos,
            self.first_name + " " + self.last_name,
            str(self.hand),
            self.pitch_die.value,
            self.get_pitching_trait_string(),
            self.bt,
            self.obt,
            self.age,
        ]

    def get_batting_trait_string(self) -> str:
        """Converts a batter's trait list to a string."""
        result = None
        for trait in self.traits:
            if result:
                result += trait.value.string
            else:
                result = trait.value.string
        return result

    def get_batting_info(self) -> list:
        """Returns a list of a hitter's data to be used on a worksheet."""
        return [
            self.pos,
            self.first_name + " " + self.last_name,
            str(self.hand),
            self.bt,
            self.obt,
            self.get_batting_trait_string(),
            self.age,
        ]
