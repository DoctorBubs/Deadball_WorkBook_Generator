"""Leagues currently contain the settings such as Era and gender to create teams. This module is currenty a WIP."""

from league_data import Era, LeagueGender
from team import Team
from series import Series
from SeasonSeries import SeasonSeries
type Schedule = list[Series]

class League:
    """The League class.Leagues currently contain the settigns
    such as Era and gender to create teams."""

    def __init__(self, name: str, era: Era, gender: LeagueGender) -> None:
        self.name = name
        self.era = era
        self.gender = gender
        self.teams = []
    def new_team(self, city: str, name: str) -> Team:
        """Generates a new team based off the league's setting."""
        result = Team(city, name, self.era, self.gender)
        self.teams.append(result)
        return result
    
    

    def new_schedule(self, series_per_matchup: int, games_per_series: int) -> Schedule:
        result = []
        all_series = []
        for team in self.teams:
           new_series = SeasonSeries(team,self.teams,series_per_matchup)
           all_series.append(new_series)
        matchup_per_round = len(all_series) / 2
        while True:
            active_series = [season_series for season_series in all_series if season_series.is_active()]
            if len (active_series) == 0:
                break
            new_round = []
