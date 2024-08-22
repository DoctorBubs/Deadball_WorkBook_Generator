from player import Player
from league import Era,League_Gender
from player_quality import Batter_Quality,Pitcher_Quality,Player_Quality
import sqlite3
con = sqlite3.connect("tutorial.db")

def main():
    bob = Player(Era.ANCIENT,League_Gender.MALE,Batter_Quality.PROSPECT,"SS")
    print(bob.first_name)
    cur = con.cursor()
    cur.execute("CREATE TABLE player(first_name, last_name, hand)")

    batter_data = (bob.first_name, bob.last_name, bob.hand)
    cur.execute("INSERT INTO player VALUES(?,?,?)", batter_data)
    con.commit()
if __name__=="__main__":
    main()
