

from player import Player
from player_quality import Batter_Quality, Pitcher_Quality, Player_Quality
from league_data import Era,League_Gender

lineup_strings = ["C","1B","2B","3B","SS","LF","CF","RF"]

modern_bench_strings = ["C","INF","INF","OF","OF"]

ancient_bench_strings = ["C","INF","OF","UT"]

def sort_bt(player: Player):
    return player.bt

def sort_pd(player: Player):
    return player.pitch_die.value

class Team:
    def __init__(self,city: str, name: str, era: Era, gender: League_Gender) -> None:
        self.name = name
        self.city = city
        self.era = era
        batting_score = 0
        self.starting_lineup = []
        for starting_pos in lineup_strings:
            new_start_batter = Player(era,gender,Batter_Quality.PROSPECT,starting_pos)
            batting_score += new_start_batter.bt
            self.starting_lineup.append(new_start_batter)
        self.starting_lineup.sort(key = sort_bt, reverse = True)
        self.bench = []
        bench_strings = None
        match era:
            case Era.ANCIENT:
                bench_strings = ancient_bench_strings
            case _: 
                bench_strings = modern_bench_strings
        for bench_pos in bench_strings:
            new_bench_batter = Player(era,gender,Batter_Quality.PROSPECT,bench_pos)
            batting_score += new_bench_batter.bt
            self.bench.append(new_bench_batter)
        self.bench.sort(key = sort_bt, reverse = True)
        pitching_score = 0
        match era:
            case Era.ANCIENT:
                self.pitchers = []
                for _ in range(5):
                    new_pitcher = Player(era,gender,Pitcher_Quality.PROSPECT,"P")
                    pitching_score += new_pitcher.pitch_die.value
                    self.pitchers.append(new_pitcher)
                self.pitchers.sort(key = sort_pd, reverse = True)
            case _:
                self.starting_rotation = []
                for _ in range(5):
                    new_starting_pitcher = Player(era,gender,Pitcher_Quality.PROSPECT,"SP")
                    pitching_score += new_starting_pitcher.pitch_die.value
                    self.starting_rotation.append(new_starting_pitcher)
                self.starting_rotation.sort(key = sort_pd, reverse = True)
                self.bullpen = []
                for _ in range(7):
                    new_reliever = Player(era,gender,Pitcher_Quality.PROSPECT,"RP")
                    pitching_score += new_reliever.pitch_die.value
                    self.bullpen.append(new_reliever)
                self.bullpen.sort(key = sort_pd, reverse = True)

        pitching_score = pitching_score * 7
        self.pitching_score = pitching_score
        self.batting_score = batting_score
        self.team_score = (batting_score + pitching_score) / 10
        

        