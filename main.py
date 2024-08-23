from player import Player
from league import Era,League_Gender
from team import Team
from player_quality import Batter_Quality,Pitcher_Quality,Player_Quality
import sqlite3
import xlsxwriter
con = sqlite3.connect("deadball.db")

def main():
    bob = Player(Era.ANCIENT,League_Gender.MALE,Pitcher_Quality.PROSPECT,"SS")
    print(bob.first_name)
    
    import xlsxwriter

    workbook = xlsxwriter.Workbook('hello.xlsx')
    worksheet = workbook.add_worksheet()

    test_team = Team("Hollywood","Stars",Era.MODERN, League_Gender.MALE)

    worksheet.write('A1', 'Team Name')
    worksheet.write('B1', 'Batting Score')
    worksheet.write('C1', 'Pitching Score')
    worksheet.write('D1','Team Score')
    base_team_info = [test_team.name,test_team.batting_score,test_team.pitching_score,test_team.team_score]
    column = 0
    for data in base_team_info:
        worksheet.write(1,column,data)
        column += 1
    
    workbook.close()

    '''
    cur = con.cursor()
    cur.execute("CREATE TABLE team( id INTEGER NOT NULL PRIMARY KEY,era,gender)")
    cur.execute("CREATE TABLE team( id INTEGER NOT NULL PRIMARY KEY,league_id INTEGER NOT NULL FOREIGN KEY, city, name)")
    cur.execute("CREATE TABLE player( id INTEGER NOT NULL PRIMARY KEY, first_name, last_name, hand, pd)")

    batter_data = (bob.first_name,bob.last_name,str(bob.hand),  bob.get_pd_string())
    cur.execute("INSERT INTO player (first_name,last_name,hand,pd)VALUES(?,?,?,?)", batter_data)
    con.commit()
    '''
if __name__=="__main__":
    main()
