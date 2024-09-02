


class Series:
    ''' A series has an away team and a home team. Used to generate a schedule.'''
    from team import Team
    def __init__(self, home_team: Team, away_team: Team) -> None:
        self.home_team = home_team
        self.away_team = away_team