from player import Player
from league import Era,League_Gender
from team import Team
from player_quality import Batter_Quality,Pitcher_Quality,Player_Quality
import sqlite3
import xlsxwriter

batting_headers = ["Pos","Name","Hand","BT","OBT", "Age"]
pitching_headers = ["Pos","Name","Hand","PD","BT","OBT","Age"]

# Adds a new team to the workbook under a new worksheet
def new_team(city: str, name: str, era: Era, gender: League_Gender,workbook):
    # We name the worksheet  after a comnibation of the team's city and nickname
    worksheet = workbook.add_worksheet(city + " " + name)
    # We then generatate a team object based off the paramaters
    team = Team(city,name,era,gender)
    # We write to the worksheet headers for the most important info regarding the team.
    worksheet.write('A1', 'City')
    worksheet.write('B1', 'Team Name')
    worksheet.write('C1', 'Batting Score')
    worksheet.write('D1', 'Pitching Score')
    worksheet.write('E1','Team Score')
    # Some of the team data is already known to us, so we put that data in a list.
    base_team_info = [team.city, team.name]
    # Column is a number that marks which column to write data to. The number increases over time as we add more data.
    column = 0
    # We write 
    for data in base_team_info:
        worksheet.write(1,column,data)
        column += 1
    worksheet.write('C2','=SUM(D7:D14,D19:D23)')
    worksheet.write('E2','=SUM(C2:D2) / 10')

    worksheet.write('B1', 'Starting Lineup')
    
    for row,info in enumerate(batting_headers):
        worksheet.write(5,row,info)
    column = 6
    for batter in team.starting_lineup:
        batter_info = [batter.pos,batter.first_name +" " + batter.last_name,str(batter.hand),batter.bt,batter.obt,batter.age]
        for row,data in enumerate(batter_info):
            worksheet.write(column,row,data)
        column += 1
    worksheet.write(column + 2,0,"Bench")
    column = column + 3
    for row,info in enumerate(batting_headers):
        worksheet.write(column,row,info)
    column = column + 1
    for bench_batter in team.bench:
        bench_batter_info = [bench_batter.pos,bench_batter.first_name +" " + bench_batter.last_name,str(bench_batter.hand),bench_batter.bt,bench_batter.obt,bench_batter.age]
        for row,data in enumerate(bench_batter_info):
            worksheet.write(column,row,data)
        column += 1

    column += 2
    
    match team.era:
        case Era.ANCIENT:
            worksheet.write(column,0,"Pitchers")
            for row,info in enumerate(pitching_headers):
                worksheet.write(column,row,info)
            column += 1
            for pitcher in team.pitchers:
                pitcher_info = pitcher.get_pitching_info()
                for row, data in enumerate(pitcher_info):
                    worksheet.write(column,row,data)
                column += 1
            worksheet.write('D2','= SUM(D26:D31) * 7')
        case Era.MODERN:
            worksheet.write(column,0,"Starting Rotation")
            column += 1
            for row,info in enumerate(pitching_headers):
                worksheet.write(column,row,info)
            column += 1
            for starting_pitcher in team.starting_rotation:
                starting_pitcher_info = starting_pitcher.get_pitching_info()
                for row,info in enumerate(starting_pitcher_info):
                    worksheet.write(column,row,info)
                column += 1
            column += 2
            worksheet.write(column,0,"Bullpen")
            column += 1
            for reliever in team.bullpen:
                reliever_info = reliever.get_pitching_info()
                for row,info in enumerate(reliever_info):
                    worksheet.write(column,row,info)
                column += 1
            worksheet.write('D2','=SUM(D28:D32,D36:D42) * 7')

def main():
 
    


    workbook = xlsxwriter.Workbook('test.xlsx')
    

    new_team("Hollywood","Stars",Era.MODERN,League_Gender.MALE,workbook)



    workbook.close()

  

if __name__=="__main__":
    main()
