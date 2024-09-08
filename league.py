"""Leagues currently contain the settings such as Era and gender to create teams. This module is currently a WIP."""

import random
from league_data import Era, LeagueGender
from team import Team
from series import Series, generate_series_list

type Schedule = list[Series]


class League:
    """The League class.Leagues currently contain the settings
    such as Era and gender to create teams."""

    def __init__(self, name: str, era: Era, gender: LeagueGender) -> None:
        self.name = name
        self.era = era
        self.gender = gender
        self.teams: list[Team] = []

    def new_team(self, city: str, name: str) -> Team:
        """Generates a new team based off the league's setting."""
        result = Team(city, name, self.era, self.gender)
        self.teams.append(result)
        return result

    def new_schedule(self, series_per_matchup: int) -> Schedule:
        """Generates a list of list of series to be used of a schedules"""
        # The result will be a list, so we create an empty one.
        result: list[Series] = []
        # all_series will be a list that contains series created by teams.
        all_series: list[Series] = []
        # Since all teams will be active in a round, but can only play one team per round, we need a number that is half the number of teams.
        half_teams = len(self.teams) / 2
        # we have every team generate a list of series with the team as the home team
        matchup_per_team = int(series_per_matchup / 2)
        for team in self.teams:
            # We divide series per matchup by 2, as each team will be generating only the home series for each matchup.
            team_series = generate_series_list(team, self.teams, matchup_per_team)
            all_series = all_series + team_series
        print("Teams have generated series")
        while len(all_series) > 0:
            # the new round is a list.
            new_round: list[Series] = []
            # We also use a dict to keep track  of what teams have already been scheduled this round.
            used_teams: dict[str, bool] = {}
            # We start by picking a random series. The series is removed from all series and added to the round.
            first_series = random.choice(all_series)
            all_series.remove(first_series)
            new_round.append(first_series)
            # We take the home team and away team from the series and add it to the used teams list
            first_series.add_teams_to_dict(used_teams)

            while True:
                potential_series: list[Series] = []
                for series in all_series:
                    if not series.teams_in_dict(used_teams):
                        potential_series.append(series)
                if len(potential_series) == 0:
                    break
                new_series = random.choice(potential_series)
                new_series.add_teams_to_dict(used_teams)
                all_series.remove(new_series)
                new_round.append(new_series)

            result.append(new_round)
            print("round added to result")
        return result
