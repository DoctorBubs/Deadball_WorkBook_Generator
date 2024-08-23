

from player import Player, Batter_Quality,Pitcher_Quality, Player_Quality
from league import Era,League_Gender

lineup_strings = ["C","1B","2B","3B","SS","LF","CF","RF"]

modern_bench_strings = ["C","INF","OF","UT"]

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
        for bench_pos in modern_bench_strings:
            new_bench_batter = Player(era,gender,Batter_Quality.PROSPECT,bench_pos)
            batting_score += new_bench_batter.bt
            self.bench.append(new_bench_batter)
        self.bench.sort(key = sort_bt, reverse = True)
        match era:
            case Era.ANCIENT:
                self.pitchers = []
                for _ in range(6):
                    new_pitcher = Player(era,gender,Pitcher_Quality.PROSPECT,"P")
                    self.pitchers.append(new_pitcher)
            case _:
                self.starting_rotation = []
                for _ in range(6):
                    new_starting_pitcher = Player(era,gender,Pitcher_Quality.PROSPECT,"SP")
                    self.starting_lineup.append(new_starting_pitcher)
                self.bullpen = []
                for _ in range(8):
                    new_reliever = Player(era,gender,Pitcher_Quality.PROSPECT,"RP")
                    self.bullpen.append(new_reliever)
        

        