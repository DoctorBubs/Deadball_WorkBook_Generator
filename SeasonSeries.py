


class SeasonSeries:
    from team import Team
    def __init__(self, home_team: Team, all_teams: list, series_per_matchup: int):
        
        from series import Series
        series_list = []
        self.home_team = home_team
        for away_team in all_teams:
            if away_team != home_team:
                for _ in range(series_per_matchup):
                    new_series = Series(home_team,away_team)
                    series_list.append(new_series)
        self.series_list = series_list

    def is_active(self):
        return len(self.series_list) > 0
    
    def get_valid_series(self, forbidden_teams: list) -> list | None:
        if self.home_team in forbidden_teams:
            return None
        else:
            result = [x for x in self.series_list if x.away_team not in forbidden_teams ]
            if len(result) > 0:
                return result
            else
                return None 
            