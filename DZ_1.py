from random import randint, choice
from collections import OrderedDict


def play_matches_in_pairs(teams_list, table, part_of_league):
    teams_quantity = len(teams_list)
    for _ in range(teams_quantity//2):
        table[part_of_league][(teams_list.pop(randint(0, len(teams_list)-1)),
                               teams_list.pop(randint(0, len(teams_list)-1)))] = randint(0,10), randint(0,10)
    return table


def find_winners(table, part_of_league):
    winners = []
    for match, score in table[part_of_league].items():
        if score[0] > score[1]:
            winners.append(match[0])
        elif score[0] < score[1]:
            winners.append(match[1])
        else:
           winners.append(roll_winner_in_draw(match))
    return winners


def roll_winner_in_draw(match):
    return choice(match)


def print_table(table):
    for stage, results in table.items():
        print("{stage}: ".format(stage=stage))
        for match, score in results.items():
            print("{match} - {score}".format(match=match, score=score))
    print()


def show_team_plays(table, team):
    print("Showing matches for {team}".format(team=team))
    for stage, results in table.items():
        for match, score in results.items():
            if team in match:
                print(stage, end=' : ')
                print(match, score)


if __name__ == '__main__':
    teams = ['Russia', 'France', 'UK', 'Italy', 'Germany', 'Spain', 'Sweden', 'Portugal',
             'Ukraine', 'Poland', 'Czech', 'Serbia', 'Netherlands', 'Switzerland', 'Norway', 'Greece']
    table = {'1:8': {}, '1:4': {}, '1:2': {}, 'final': {}}
    table = OrderedDict(sorted(table.items(), key=lambda t: t[0], reverse=True))
    table.move_to_end('final')
    table = play_matches_in_pairs(teams, table, '1:8')
    eighths_finals_winners = find_winners(table, '1:8')
    table = play_matches_in_pairs(eighths_finals_winners, table, '1:4')
    quarters_winners = find_winners(table, '1:4')
    table = play_matches_in_pairs(quarters_winners, table, '1:2')
    semi_winners = find_winners(table, '1:2')
    table = play_matches_in_pairs(semi_winners, table, 'final')
    print_table(table)
    input_team = input('Enter team to see its games: ')
    show_team_plays(table, input_team)
