from league_data import Era, League_Gender
from team import Team


class League:
    def __init__(self, name: str, era: Era, gender: League_Gender) -> None:
        self.name = name
        self.era = era
        self.gender = gender

    def new_team(self, city: str, name: str) -> Team:
        return Team(city, name, self.era, self.gender)
