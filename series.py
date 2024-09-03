class Series:
    """A series has an away team and a home team. Used to generate a schedule."""

    def __init__(self, home_team, away_team) -> None:
        self.home_team = home_team
        self.away_team = away_team

    def __str__(self) -> str:
        return self.home_team.name + " @ " + self.away_team.name
