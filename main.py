import csv
from team import Team

teams = {}

with open('team_list.csv') as team_list:
    team_list_reader = csv.reader(team_list, delimiter=',')
    for team in team_list_reader:
        teams[int(team[0])] = Team(int(team[0]), team[1])

with open('match_results.csv') as match_results:
    match_results_reader = csv.reader(match_results, delimiter=',')

    for match_result in match_results_reader:
        first_red_team = teams[int(match_result[0])]
        second_red_team = teams[int(match_result[1])]
        red_score = int(match_result[4])

        first_blue_team = teams[int(match_result[2])]
        second_blue_team = teams[int(match_result[3])]
        blue_score = int(match_result[5])

        first_red_team.update_ranking(red_score, second_red_team, first_blue_team, second_blue_team)
        second_red_team.update_ranking(red_score, first_red_team, first_blue_team, second_blue_team)

        first_blue_team.update_ranking(blue_score, second_blue_team, first_red_team, second_red_team)
        second_blue_team.update_ranking(blue_score, first_blue_team, first_red_team, second_red_team)

for team in teams:
    print(teams[team].team_number, teams[team].team_name, teams[team].ranking)