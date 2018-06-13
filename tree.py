import random
import os


def random_city():
    cities_list = ['dublin', 'london', 'paris', 'madrid', 'berlin', 'budapest', 'rome']
    city = random.randint(1, len(cities_list))
    return (cities_list[city-1])


def create_the_play_city(city):
    goal_city = (list(city))
    play_city = list('*' * len(goal_city))
    return play_city


def play_game(goal_city, play_city, table):
    print(goal_city)
    charachter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                       'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    fault = []
    good_letters = 0
    while len(fault) <= 5:
        good_letters, table = print_screen(fault, play_city, good_letters, table)
        if good_letters < len(goal_city):
            characther = input('Give a letter: ')
            if characther in charachter_list:
                if characther not in fault and characther not in play_city:
                    if characther in goal_city:
                        for i in range(len(goal_city)):
                            if goal_city[i] == characther:
                                play_city[i] = characther
                        good_letters += 1
                    else:
                        fault.append(characther)
                else:
                    pass
            else:
                pass
        else:
            return (play_city)


def print_screen(fault, play_city, good_letters, table):
    os.system('clear')
    fault_dict = {}
    if len(fault) > 0:
        if len(fault) == 1:
            fault_dict = {'73': '-', '74': '-', '75': '-', '76': '-', '77': '-', '78': '-', '79': '-'}
        elif len(fault) == 2:
            fault_dict = {'12': '|', '21': '|', '30': '|', '39': '|', '48': '|', '57': '|', '66': '|'}
        elif len(fault) == 3:
            fault_dict = {'3': '-', '4': '-', '5': '-', '6': '-'}
        elif len(fault) == 4:
            fault_dict = {'15': '|'}
        elif len(fault) == 5:
            fault_dict = {'24': 'O', '32': '/', '33': '|', '34': '\\', '41': ' | ', '50': '/', '52': '\\'}
    table = create_table(table, fault_dict)
    print(table)
    print('The wrong letters: ' + ' '.join(fault))
    print('The city: ' + ' '.join(play_city))
    if '*' not in play_city or len(fault) == 5:
        good_letters += 5
    return good_letters, table


def create_table(table, fault_dict):
    table_list = list(table)
    for k in fault_dict:
        table_list[int(k)] = fault_dict.get(k)
    return ''.join(table_list)


def greeting(goal_city, play_city):
    if '*' in play_city:
        print('Game Over')
        print('The city was: ' + goal_city)
    else:
        print('Congratulation')
    index = 0
    while index < 1:
        new_play = input('Do you want to play again (Y or N): ')
        if new_play == 'Y':
            main()
        elif new_play == 'N':
            index += 1
        else:
            print('Wrong letter')
    print('Goodbye')
    exit()


def main():
    table = "        \n        \n        \n        \n        \n        \n        \n        \n        \n"
    goal_city = random_city()
    play_city = create_the_play_city(goal_city)
    result = play_game(goal_city, play_city, table)
    greeting(goal_city, result)


if __name__ == "__main__":
    main()
