""" Teams generate new players and organize them in lists such as bullpen and starting lineup."""

from player import Player
from player_quality import BatterQuality, PitcherQuality
from league_data import Era, LeagueGender
from series import Series
    
lineup_strings = ["C", "1B", "2B", "3B", "SS", "LF", "CF", "RF"]

modern_bench_strings = ["C", "INF", "INF", "OF", "OF"]

ancient_bench_strings = ["C", "INF", "OF", "UT"]


def sort_bt(player: Player):
    """Sorts players by their bt"""
    return player.bt


def sort_pd(player: Player):
    """Sorts batter by their bt."""
    return player.pitch_die.value



class Team:
    """The Team object. When generated, it also generates many players based off the era and gender."""
    
    def __init__(self, city: str, name: str, era: Era, gender: LeagueGender) -> None:
        self.name = name
        self.city = city
        self.era = era
        batting_score = 0
        self.starting_lineup = []
        for starting_pos in lineup_strings:
            new_start_batter = Player(era, gender, BatterQuality.PROSPECT, starting_pos)
            batting_score += new_start_batter.bt
            self.starting_lineup.append(new_start_batter)
        self.starting_lineup.sort(key=sort_bt, reverse=True)
        self.bench = []
        bench_strings = None
        match era:
            case Era.ANCIENT:
                bench_strings = ancient_bench_strings
            case _:
                bench_strings = modern_bench_strings
        for bench_pos in bench_strings:
            new_bench_batter = Player(era, gender, BatterQuality.PROSPECT, bench_pos)
            batting_score += new_bench_batter.bt
            self.bench.append(new_bench_batter)
        self.bench.sort(key=sort_bt, reverse=True)
        pitching_score = 0
        match era:
            case Era.ANCIENT:
                self.pitchers = []
                for _ in range(5):
                    new_pitcher = Player(era, gender, PitcherQuality.PROSPECT, "P")
                    pitching_score += new_pitcher.pitch_die.value
                    self.pitchers.append(new_pitcher)
                self.pitchers.sort(key=sort_pd, reverse=True)
            case _:
                self.starting_rotation = []
                for _ in range(5):
                    new_starting_pitcher = Player(
                        era, gender, PitcherQuality.PROSPECT, "SP"
                    )
                    pitching_score += new_starting_pitcher.pitch_die.value
                    self.starting_rotation.append(new_starting_pitcher)
                self.starting_rotation.sort(key=sort_pd, reverse=True)
                self.bullpen = []
                for _ in range(7):
                    new_reliever = Player(era, gender, PitcherQuality.PROSPECT, "RP")
                    pitching_score += new_reliever.pitch_die.value
                    self.bullpen.append(new_reliever)
                self.bullpen.sort(key=sort_pd, reverse=True)

        pitching_score = pitching_score * 7
        self.pitching_score = pitching_score
        self.batting_score = batting_score
        self.team_score = (batting_score + pitching_score) / 10

    
    
    def generate_series_list(self, all_teams: list, series_per_matchup: int) -> dict:
        '''Generates a list of series with self as the home team'''
        series_list = []
        for away_team in all_teams:
            if away_team != self:
                for _ in range(series_per_matchup):
                    new_series = Series(self,away_team)
                    series_list.append(new_series)
        result = {
            'team' : self,
            'series_list' : series_list
        }
        return result
