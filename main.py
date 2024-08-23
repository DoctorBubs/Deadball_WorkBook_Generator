from player import Player
from league import Era,League_Gender
from team import Team
from player_quality import Batter_Quality,Pitcher_Quality,Player_Quality
import sqlite3
import xlsxwriter


def main():
    bob = Player(Era.ANCIENT,League_Gender.MALE,Pitcher_Quality.PROSPECT,"SS")
    print(bob.first_name)
    
    import xlsxwriter

    workbook = xlsxwriter.Workbook('hello.xlsx')
    worksheet = workbook.add_worksheet()

    test_team = Team("Hollywood","Stars",Era.MODERN, League_Gender.MALE)
    worksheet.write('A1', 'City')
    worksheet.write('B1', 'Team Name')
    worksheet.write('C1', 'Batting Score')
    worksheet.write('D1', 'Pitching Score')
    worksheet.write('E1','Team Score')
    base_team_info = [test_team.city, test_team.name]
    column = 0
    for data in base_team_info:
        worksheet.write(1,column,data)
        column += 1
    worksheet.write('C2','=SUM(D7:D14,D19:D23)')
    

    worksheet.write('B1', 'Starting Lineup')
    batting_headers = ["Pos","Name","Hand","BT","OBT", "Age"]
    for row,info in enumerate(batting_headers):
        worksheet.write(5,row,info)
    column = 6
    for batter in test_team.starting_lineup:
        batter_info = [batter.pos,batter.first_name +" " + batter.last_name,str(batter.hand),batter.bt,batter.obt,batter.age]
        for row,data in enumerate(batter_info):
            worksheet.write(column,row,data)
        column += 1
    worksheet.write(column + 2,0,"Bench")
    column = column + 3
    for row,info in enumerate(batting_headers):
        worksheet.write(column,row,info)
    column = column + 1
    for bench_batter in test_team.bench:
        bench_batter_info = [bench_batter.pos,bench_batter.first_name +" " + bench_batter.last_name,str(bench_batter.hand),bench_batter.bt,bench_batter.obt,bench_batter.age]
        for row,data in enumerate(bench_batter_info):
            worksheet.write(column,row,data)
        column += 1
    workbook.close()

  

if __name__=="__main__":
    main()
