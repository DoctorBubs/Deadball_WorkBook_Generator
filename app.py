import os
import xlsxwriter
from beaupy import confirm, prompt, select
from league_data import Era, LeagueGender
from team import Team
from league import League


# These headers are used when writing on the worksheet.
team_headers = ["City", "Team Name", "Batting Score", "Pitching Score", "Team Score"]
batting_headers = ["Position", "Name", "Hand", "BT", "OBT", "Traits", "Age"]
pitching_headers = ["Position", "Name", "Hand", "PD", "Traits", "BT", "OBT", "Age"]


def new_team(team: Team, workbook) -> None:
    """Creates a worksheet in the workbook and fills it with data from the team and it's players."""

    # We create a worksheet based of the team's name and city.
    worksheet = workbook.add_worksheet(team.city + " " + team.name)

    # current_row is a number that marks which row to write data to. The number increases over time as we add more data.
    current_row = 0
    # We write the team headers on the top of the file.
    for column, data in enumerate(team_headers):
        worksheet.write(current_row, column, data)
    current_row = 1
    # Some of the team data is already known to us, so we put that data in a list.
    base_team_info = [team.city, team.name]

    # We write
    for column, data in enumerate(base_team_info):
        worksheet.write(current_row, column, data)
    # In cell C2, we write a formulate to calculate the batting score, which is based off all batters bt.
    worksheet.write("C2", "=SUM(D7:D14,D19:D23)")
    # We also write in cell E2 a function that calculates team score, which is calculated by adding a teams hitting and pitching scores, and divide by 10
    worksheet.write("E2", "=SUM(C2:D2) / 10")

    current_row = 4
    worksheet.write(current_row, 0, "Starting Lineup")
    # We write the batting headers for the starting lineup
    for column, info in enumerate(batting_headers):
        worksheet.write(5, column, info)
    # We go down a row
    current_row = 6

    for batter in team.starting_lineup:
        # get_bating_info is a method for Players that returns a list of data that corresponds to each of the batting headers.
        batter_info = batter.get_batting_info()
        # We then fill the row with the data in batter info.
        for column, data in enumerate(batter_info):
            worksheet.write(current_row, column, data)
        # We next increase the current row.
        current_row += 1
    worksheet.write(current_row + 2, 0, "Bench")
    current_row = current_row + 3
    # We repeat the process for the bench players.
    for column, info in enumerate(batting_headers):
        worksheet.write(current_row, column, info)
    current_row = current_row + 1
    for bench_batter in team.bench:
        bench_batter_info = bench_batter.get_batting_info()
        for column, data in enumerate(bench_batter_info):
            worksheet.write(current_row, column, data)
        current_row += 1

    current_row += 2

    # Teams in the ancient era and the modern era have different amounts of pitchers on their roster, so each era is handled differently.
    match team.era:
        case Era.ANCIENT:
            # Ancient teams do not have a bullpen, so we only create one group of pitchers on the worksheet.
            worksheet.write(current_row, 0, "Pitchers")
            # We wire the pitching headers to the sheet
            for column, info in enumerate(pitching_headers):
                worksheet.write(current_row, column, info)
            current_row += 1
            for pitcher in team.pitchers:
                # get pitching info is a player method that returns a list of it's fields related to pitching
                pitcher_info = pitcher.get_pitching_info()
                # We write the data from pitcher_info to the row
                for column, data in enumerate(pitcher_info):
                    worksheet.write(current_row, column, data)
                # Next we go down a row.
                current_row += 1
            # To cell D2, we assign a formula that will calculate the pitching score based off the pitcher's pitch die.
            worksheet.write("D2", "= SUM(D26:D31) * 7")
        case Era.MODERN:
            # If the team is in the modern era, we do a similar process to ancient teams, however we have 2 groups of pitchers to account for: the starting rotation and the bullpen.
            worksheet.write(current_row, 0, "Starting Rotation")
            current_row += 1
            for column, info in enumerate(pitching_headers):
                worksheet.write(current_row, column, info)
            current_row += 1
            for starting_pitcher in team.starting_rotation:
                starting_pitcher_info = starting_pitcher.get_pitching_info()
                for column, info in enumerate(starting_pitcher_info):
                    worksheet.write(current_row, column, info)
                current_row += 1
            current_row += 2
            worksheet.write(current_row, 0, "Bullpen")
            current_row += 1
            for column, info in enumerate(pitching_headers):
                worksheet.write(current_row, column, info)
            current_row += 1
            for reliever in team.bullpen:
                reliever_info = reliever.get_pitching_info()
                for column, info in enumerate(reliever_info):
                    worksheet.write(current_row, column, info)
                current_row += 1
            # We adjust the formula for pitching score to reflect there are pitchers in the rotation and bullpen to account for.
            worksheet.write("D2", "=SUM(D28:D32,D37:D43) * 7")


def valid_workbook_name(user_input: str) -> bool:
    """Determines if a user generated workbook is not in use by a workbook in the folder."""
    test_path = user_input + ".xlsx"
    if os.path.exists(test_path):
        return False
    else:
        return True


def get_workbook_name() -> str:
    """Prompts the user for a unique workbook name that is not already in use in the folder."""
    user_input = prompt(
        "Please enter the file name you would like to save the new league under."
    )
    result = None
    os.system("cls")
    while True:
        valid_name = valid_workbook_name(user_input)
        # If the user_input is a valid workbook name, we break the loop and return the input.
        if valid_name:
            result = user_input
            break
        else:
            # Otherwise, we prompt the user to try something else.
            user_input = prompt(
                "There is already a worksheet with that name in this folder, please try a different file name."
            )
    return result + ".xlsx"


def write_schedule(workbook, schedule) -> None:
    '''Writes a schedule to a new worksheet in the workbook.'''
    worksheet = workbook.add_worksheet("SCHEDULE")
    current_row = 0
    worksheet.write(0, 1, "Home Team")
    worksheet.write(0, 3, "Away Team")
    print("schedule length = " + str(len(schedule)))
    for round_number, round_list in enumerate(schedule):
        current_row += 1
        worksheet.write(current_row, 0, "Round " + str(round_number + 1))
        for series in round_list:
            current_row += 1
            worksheet.write(current_row, 1, series.home_team.name)
            worksheet.write(current_row, 2, "@")
            worksheet.write(current_row, 3, series.away_team.name)


def get_team_name(workbook,names_taken: list[str]) -> dict:
    """Returns a dict containing a city and team name, while also ensuring their is not already a worksheet with the same combo."""
    
    while True:
        city_input: str= prompt("Please enter the name of the city for the new team.")
        name_input: str = prompt("Please enter the name of the new team.")
        worksheet_name: str = city_input + " " + name_input
        existing_worksheet: bool = workbook.get_worksheet_by_name(worksheet_name)
        # If there is an existing worksheet with the same city and team name, we tell the user to try something else.
        if existing_worksheet:
            print(
                "There is already a worksheet with the same city and team name, please enter a different input."
            )
        else:
            
            # Otherwise, we break and return the dict.
            result = {"city": city_input, "name": name_input}
            names_taken.append(worksheet_name)
            return result


def main() -> None:
    """The main function. It is called when the script runs."""
    # We welcome the user
    print("Welcome to the Deadball Workbook Generator!")
    print("This tool is based off the Deadball tabletop game by W.M. Akers.")
    while True:
        workbook_name = get_workbook_name()
        workbook = xlsxwriter.Workbook(workbook_name)
        all_eras: list[Era] = [Era.ANCIENT, Era.MODERN]
        print("Please select the era for the league.")
        era: Era = select(all_eras, lambda val: val.value)
        os.system("cls")
        # The user then selects the league gender.
        all_genders: list[LeagueGender] = [LeagueGender.COED, LeagueGender.FEMALE, LeagueGender.MALE]
        print("Please select the gender for the league")
        gender: LeagueGender = select(all_genders, lambda val: val.value)
        # we create a new league.
        league = League(workbook_name, era, gender)
       
        os.system("cls")
        # We create a list of string that keeps track of what names have already been used in the current workbook.
        names_taken: list[str] = []
        # We then loop through the process of creating a new team and creating a worksheet until the user quits.
        while True:
            if len(names_taken) != 0:
                print("Names Taken: " + str(names_taken))
            team_name_dict = get_team_name(workbook,names_taken)
            team: Team = league.new_team(
                team_name_dict.get("city"), team_name_dict.get("name")
            )
            new_team(team,workbook)
            os.system("cls")
            # We asks the user if they would like to add another team to the league.
            if not confirm("Would you like to add another team to the league?"):
                
                break
        print("League Saved")

        team_number = len(league.teams)
        print("Team number = " + str(team_number))
        if team_number % 2 != 0:
            print("An even number of teams is need to generate a schedule")
        else:
            while True:
                sched_number = prompt(
                    "Please enter how many series will be schedule between every team.",int
                )
                if isinstance(sched_number,int):
                        if sched_number <= 0 or sched_number % 2 != 0 :
                            os.system("cls")
                            print("Input must be a whole even number greater than 0, please try again.")
                        else:    
                            sched = league.new_schedule(sched_number)
                            write_schedule(workbook, sched)
                            break
                else:
                    os.system("cls")
                    print("Input must be a whole number greater than 0, please try again.")
        workbook.close()
        if not confirm("Would you like to add create another workbook?"):
            os.system("cls")
            break
        else:
            os.system("cls")


if __name__ == "__main__":
    main()
