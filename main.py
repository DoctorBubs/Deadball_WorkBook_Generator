from player import Player
from league import Era,League_Gender
from team import Team
from player_quality import Batter_Quality,Pitcher_Quality,Player_Quality
import os
import xlsxwriter
from beaupy import confirm, prompt, select, select_multiple
team_headers = ["City","Team Name","Batting Score","Pitching Score","Team Score"]
batting_headers = ["Position","Name","Hand","BT","OBT", "Traits","Age"]
pitching_headers = ["Position","Name","Hand","PD","BT","OBT","Age"]

# Adds a new team to the workbook under a new worksheet
def new_team(city: str, name: str, era: Era, gender: League_Gender,workbook):
    # We name the worksheet  after a comnibation of the team's city and nickname
    worksheet = workbook.add_worksheet(city + " " + name)
    # We then generatate a team object based off the paramaters
    team = Team(city,name,era,gender)
    # We write to the worksheet headers for the most important info regarding the team.
    # current_row is a number that marks which row to write data to. The number increases over time as we add more data.
    current_row = 0
    for column,data in enumerate(team_headers):
        worksheet.write(current_row,column,data)
    current_row = 1
    # Some of the team data is already known to us, so we put that data in a list.
    base_team_info = [team.city, team.name]
    
    # We write 
    for column,data in enumerate(base_team_info):
        worksheet.write(current_row,column,data)
    # In cell C2, we write a formulate to calcualte the batting score, which is based off all batters bt.   
    worksheet.write('C2','=SUM(D7:D14,D19:D23)')
    # We also write in cell E2 a function that calculates team score, which is calculated by adding a teams hitting and pitching scores, and divide by 10
    worksheet.write('E2','=SUM(C2:D2) / 10')

    current_row = 4
    worksheet.write(current_row,0,"Starting Lineup")
    # We write thhe batting headers for the starting lineup
    for column,info in enumerate(batting_headers):
        worksheet.write(5,column,info)
    # We go down a row
    current_row = 6
    
    for batter in team.starting_lineup:
        # get_bating_info is a method for Players that returns a list of data that corresponds to each of the batting headers.
        batter_info = batter.get_batting_info()
        # We then fill the row with the data in batter info.
        for column,data in enumerate(batter_info):
            worksheet.write(current_row,column,data)
        # We next increase the current row
        current_row += 1
    worksheet.write(current_row + 2,0,"Bench")
    current_row = current_row + 3
    # We repeat the process for the bench players
    for column,info in enumerate(batting_headers):
        worksheet.write(current_row,column,info)
    current_row = current_row + 1
    for bench_batter in team.bench:
        bench_batter_info = bench_batter.get_batting_info()
        for column,data in enumerate(bench_batter_info):
            worksheet.write(current_row,column,data)
        current_row += 1

    current_row += 2
    
    # Teams in the ancient era and the modern era have different amounts of pitchers on their roster, so each era is handled differently.
    match team.era:
        case Era.ANCIENT:
            # Ancient teams do not have a bullpen, so we only create one group of pitchers on the worksheet.
            worksheet.write(current_row,0,"Pitchers")
            # We wire the pitching headers to the sheet
            for column,info in enumerate(pitching_headers):
                worksheet.write(current_row,column,info)
            current_row += 1
            for pitcher in team.pitchers:
                # get pitching info is a player method that returns a list of it's fields related to pitching
                pitcher_info = pitcher.get_pitching_info()
                # We wirte the data from pitcher_info to the row
                for column, data in enumerate(pitcher_info):
                    worksheet.write(current_row,column,data)
                # Next we go down a row.
                current_row += 1
            # To cell D2, we assign a formulat that will calculatate the pitching scoore based off the pitchers die
            worksheet.write('D2','= SUM(D26:D31) * 7')
        case Era.MODERN:
            # If the team is in the modern era, we do a similar process to ancient teams, however we have 2 groups of pitchers to account for: the starting rotation and the bullpen.
            worksheet.write(current_row,0,"Starting Rotation")
            current_row += 1
            for column,info in enumerate(pitching_headers):
                worksheet.write(current_row,column,info)
            current_row += 1
            for starting_pitcher in team.starting_rotation:
                starting_pitcher_info = starting_pitcher.get_pitching_info()
                for column,info in enumerate(starting_pitcher_info):
                    worksheet.write(current_row,column,info)
                current_row += 1
            current_row += 2
            worksheet.write(current_row,0,"Bullpen")
            current_row += 1
            for column,info in enumerate(pitching_headers):
                worksheet.write(current_row,column,info)
            current_row += 1
            for reliever in team.bullpen:
                reliever_info = reliever.get_pitching_info()
                for column,info in enumerate(reliever_info):
                    worksheet.write(current_row,column,info)
                current_row += 1
            # We adjust the formula for pitching score to reflect there are pitchers in the rotation and bullpen to account for.
            worksheet.write('D2','=SUM(D28:D32,D37:D43) * 7')

def valid_workbook_name(input: str) -> bool:
    test_path = input + ".xlsx"
    if os.path.exists(test_path):
        return False
    else:
        return True
def get_workbook_name() -> str:
    input = prompt("Please enter the file name you would like to save the new league under.")
    result = None
    while True:
        valid_name = valid_workbook_name(input)
        if valid_name:
            result = input
            break
        else:
            input = prompt("There is already a worksheet with that name in this folder, please try a different file name.")
    return result + ".xlsx"
def main():
 
    

    print("Welcome to the Deadball League Generator")
    workbook_name = get_workbook_name()

    workbook = xlsxwriter.Workbook(workbook_name)
    all_eras = [Era.ANCIENT, Era.MODERN]
    print("Please select the era for the league.")
    era = select(all_eras,lambda val: val.value )
    all_genders = [League_Gender.COED,League_Gender.FEMALE, League_Gender.MALE]
    print("Please select the gender for the league")
    gender = select(all_genders, lambda val: val.value)
    new_team("Hollywood","Stars",era,gender,workbook)



    workbook.close()

  

if __name__=="__main__":
    main()
