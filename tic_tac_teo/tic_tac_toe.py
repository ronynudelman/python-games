#!/usr/bin/python3


import subprocess


EMPTY = " "
X = "X"
O = "O"


def show_table(table):
    subprocess.run(["clear"])
    print()
    print()
    print(table[0][0] + "|" + table[0][1] + "|" + table[0][2])
    print("-----")
    print(table[1][0] + "|" + table[1][1] + "|" + table[1][2])
    print("-----")
    print(table[2][0] + "|" + table[2][1] + "|" + table[2][2])
    print()
    print()


def table_is_full(table):
    counter = 0
    for i in range(3):
        for j in range(3):
            if table[i][j] != EMPTY:
                counter = counter + 1
    return counter == 9


def check_rows(table):
    for i in range(3):
        if EMPTY != table[i][0] and table[i][0] == table[i][1] and table[i][1] == table[i][2]:
            if table[i][0] == X:
                print("Ziv won!")
            else: # table[i][0] == O
                print("Rony won! (not really...)")
            return True
    return False


def check_columns(table):
    for i in range(3):
        if EMPTY != table[0][i] and table[0][i] == table[1][i] and table[1][i] == table[2][i]:
            if table[i][0] == X:
                print("Ziv won!")
            else: # table[i][0] == O
                print("Rony won! (not really...)")
            return True
    return False


def check_diagonals(table):
    if EMPTY != table[0][0] and table[0][0] == table[1][1] and table[1][1] == table[2][2]:
        if table[0][0] == X:
                print("Ziv won!")
        else: # table[i][0] == O
            print("Rony won! (not really...)")
        return True
    if EMPTY != table[0][2] and table[0][2] == table[1][1] and table[1][1] == table[2][0]:
        if table[0][2] == X:
                print("Ziv won!")
        else: # table[i][0] == O
            print("Rony won! (not really...)")
        return True
    return False


def check_tie(table):
    if table_is_full(table):
        print("It's a tie! (actually ziv won)")
        return True
    return False


def is_game_over(table):
    return check_rows(table) or check_columns(table) or check_diagonals(table) or check_tie(table)


def make_a_turn(current_player, table):
    print(current_player + ", it's your turn!")
    position = input("Choose coordinates (1,2,3 X 1,2,3): ")
    row = int(position[0]) - 1
    column = int(position[1]) - 1
    while not table[row][column] == EMPTY:
        print("Oops... Those coordinates are not empty")
        position = input("Please choose again: ")
        row = int(position[0]) - 1
        column = int(position[1]) - 1
    if current_player == "Ziv":
        table[row][column] = X
    else: # current_player == "Rony"
        table[row][column] = O

def choose_next_player(current_player):
    if current_player == "Rony":
        return "Ziv"
    else: # current_player == "Ziv"
        return "Rony"


def play_the_game():
    game_is_over = False
    current_player = "Rony"
    table = [
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ]
    subprocess.run(["clear"])
    show_table(table)
    while not game_is_over:
        make_a_turn(current_player, table)
        show_table(table)
        game_is_over = is_game_over(table)
        current_player = choose_next_player(current_player)


play_the_game()
