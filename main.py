from player import Player
from league import Era,League_Gender
from player_quality import Batter_Quality,Pitcher_Quality,Player_Quality
import sqlite3
con = sqlite3.connect("deadball.db")

def main():
    bob = Player(Era.ANCIENT,League_Gender.MALE,Pitcher_Quality.PROSPECT,"SS")
    print(bob.first_name)
    cur = con.cursor()
    cur.execute("CREATE TABLE player( id INTEGER NOT NULL PRIMARY KEY, first_name, last_name, hand, pd)")

    batter_data = (bob.first_name,bob.last_name,str(bob.hand),  bob.get_pd_string())
    cur.execute("INSERT INTO player (first_name,last_name,hand,pd)VALUES(?,?,?,?)", batter_data)
    con.commit()
if __name__=="__main__":
    main()
