"""Leagues currently contain the settings such as Era and gender to create teams. This module is currenty a WIP."""

from league_data import Era, LeagueGender
from team import Team
from series import Series

type Schedule = list[Series]
import random


class League:
    """The League class.Leagues currently contain the settings
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

    def new_schedule(self, series_per_matchup: int) -> Schedule:
        """Generates a list of list of series to be used of a schedules"""
        # The result will be a list, so we create an empty one.
        result = []
        # all_series will be a list that contains series created by teams.
        all_series = []
        # Since all teams will be active in a round, but can only play one team per round, we need a number that is half othe number of teams.
        half_teams = len(self.teams) / 2
        # we have every team generate a list of series with the team as the home team
        matchup_per_team = int(series_per_matchup / 2)
        for team in self.teams:
            # We divide series per matchup by 2, as each team will be generating only the home series for each matchup.
            team_series = team.generate_series_list(self.teams, matchup_per_team)
            all_series = all_series + team_series
        print("Teams have generated series")
        while len(all_series) > 0:
            # the new
            new_round = []
            used_teams = []
            first_series = random.choice(all_series)
            all_series.remove(first_series)
            new_round.append(first_series)
            used_teams.append(first_series.home_team)
            used_teams.append(first_series.away_team)
            while len(new_round) < half_teams:
                potential_series = []
                for series in all_series:
                    if (
                        not series.home_team in used_teams
                        and not series.away_team in used_teams
                    ):
                        potential_series.append(series)
                new_series = random.choice(potential_series)
                used_teams.append(new_series.home_team)
                used_teams.append(new_series.away_team)
                all_series.remove(new_series)
                new_round.append(new_series)

            result.append(new_round)
        return result
