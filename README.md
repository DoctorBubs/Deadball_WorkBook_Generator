
# Summary
Based off the [Deadball tabletop baseball game by W.M. Akers](http://wmakers.net/deadball), this Python script automatically generates fictional leagues, teams, and players via an interactive prompt. When a league is created, all the teams and players are saved in an Excel workbook. The script can generate players based off both the ancient and modern Deadball rulesets, and the player may also choose the gender identity of the league upon creation.
Please note the script can only create new workbooks at this time, and the script will not let you create a workbook if there is another workbook with the same name in the current folder. This project is also currently a WIP, as I plan to add some sort of team leader board to each worksheet in the future, but if you are looking to generate a fictional Deadball league quickly this should speed up your workflow substantially.


# Schedule and issue
If a league has an even amount of teams, a schedule is also generated for the league. The user is given a prompt for how many series should be played between each teams, and a schedule tab is added to the worksheet. However, this is a work in process, as calculating a balanced schedule for teams is somewhat tricky, so currently the generated schedule does not have an even number of series played per round generated. It is also possible for the program to crash if the user selects a workbook name that is not a valid file name.

If you are interested in creating a Deadball League but have the result saved in a SQL database instead, please consider [my other repo](https://github.com/DoctorBubs/Deadball-Database-Generator). 


