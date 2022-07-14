# Legend:
# "X" - hit
# "O" - miss
# 
# Ship legend:
# <> - ship of length 2 cells, each player gets 2 of these
# <=> - ship of length 3 cells, each player gets 2 of these
# <==> - ship of length 4 cells, each player gets 1 of these

# Imports
from random import randint

# Named variables
#player_name = input("Name: ")
player_hit_count = 0
player_ships_count = 5
computer_hit_count = 0
computer_ships_count = 0

ship_board = [[" "] * 8 for x in range(8)]
guess_board = [[" "] * 8 for i in range(8)]

convert_nums_to_letters = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}

# Functions
def create_computer_boards():
    # creates computer guess and ship placement boards
    pass

def load_empty_player_board(board):
    # creates blank player guess and ship placement boards
    print("  a b c d e f g h")
    print(" -----------------")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1
    print(" -----------------")

def place_ships():
    # allows player to place ships
    pass

def reset_player_board():
    # allows player to reset their game board
    pass

def print_boards():
    # prints player boards to terminal
    pass

def player_guess():
    # player makes guess (hit and miss)
    pass

def computer_guess():
    # computer makes guess (hit and miss)
    pass

def end_game():
    # ends game (win or lose)
    pass

load_empty_player_board(ship_board)
load_empty_player_board(guess_board)