"""Represents a series of games between 2 games. Used in generating a schedule."""

from dataclasses import dataclass
from team import Team


@dataclass
class Series:
    """A series has an away team and a home team. Used to generate a schedule."""

    home_team: Team
    away_team: Team

    def __init__(self, home_team: Team, away_team: Team) -> None:
        self.home_team = home_team
        self.away_team = away_team

    def __str__(self) -> str:
        return self.home_team.name + " @ " + self.away_team.name

    def teams_in_dict(self, target_dict: dict[str, bool]) -> bool:
        """Checks to see if a dict has a key for the series home team or away team."""
        return self.home_team.name_in_dict(target_dict) or self.away_team.name_in_dict(
            target_dict
        )

    def add_teams_to_dict(self, target_dict: dict[str, bool]) -> None:
        """Takes a dict, and add's the series home and away teams as keys with a true value for each."""
        self.home_team.add_name_to_dict(target_dict)
        self.away_team.add_name_to_dict(target_dict)


def generate_series_list(
    home_team: Team, all_teams: list[Team], series_per_matchup: int
) -> list[Series]:
    """Generates a list of series with self as the home team"""

    series_list: list[Series] = []
    for away_team in all_teams:
        if away_team != home_team:
            for _ in range(series_per_matchup):
                new_series = Series(home_team, away_team)
                series_list.append(new_series)

    return series_list
