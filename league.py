'''Leagues currently contain the settings such as Era and gender to create teams. This module is currenty a WIP.'''
from league_data import Era, League_Gender
from team import Team


class League:
    '''  The League class.Leagues currently contain the settigns
      such as Era and gender to create teams.'''
    def __init__(self, name: str, era: Era, gender: League_Gender) -> None:
        self.name = name
        self.era = era
        self.gender = gender

    def new_team(self, city: str, name: str) -> Team:
        '''Generates a new team based off the league's setting.'''
        return Team(city, name, self.era, self.gender)
