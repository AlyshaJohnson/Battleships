# Legend:
# " " - unhit
# "X" - hit
# "O" - miss
# 
# Ship legend:
# <> - ship of length 2 cells, each player gets 2 of these
# <=> - ship of length 3 cells, each player gets 2 of these
# <==> - ship of length 4 cells, each player gets 1 of these

# Imports
from random import randint

# Global variables
player_guess_count = 0
player_ships_count = 5
computer_ships_count = 5

player_ship_board = [[" "] * 8 for w in range(8)]
computer_ship_board = [[" "] * 8 for y in range(8)]
player_guess_board = [[" "] * 8 for x in range(8)]
computer_guess_board = [[" "] * 8 for z in range(8)]

convert_nums_to_letters = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7
}

# Classes

class ship:
    def __init__(self, length, direction):
        #initialising ship
        self.length = length
    
        if direction == 0:
            self.direction = "Horizontal"
        elif direction == 1:
            self.direction = "Vertical"
        else:
            raise ValueError("Number needs to be with a '0' or '1' to get direction")

    def iter_ship(self, length, direction):
    #transform ship into list for required length then replace with boat symbols
        self = []
        for i in range(length):
            self.append(i)
        if direction == "Horizontal":
            self[0] = "<"
            self[-1] = ">"
            if length > 2:
                i=1
                while i >= 1 and i <= length-2:
                    self[i] = "="
                    i+=1
        if direction == "Vertical":
            self[0] = "^"
            self[-1] = "v"
            if length > 2:
                i=1
                while i >= 1 and i <= length-2:
                    self[i] = "|"
                    i+=1
        return self

ships = {
    "ship_type_1": ship(2, randint(0,1)),
    "ship_type_2": ship(3, randint(0,1)),
    "ship_type_3": ship(4, randint(0,1))
}

player_1 = ships.copy()
player_2 = ships.copy()

# Functions
def create_ships(player_ships_dict):
    # checks for duplicates and creates ships at specified location
    for k, v in player_ships_dict.items():
        player_ships_dict[k]  = [ship.iter_ship(player_ships_dict[k], player_ships_dict[k].length, player_ships_dict[k].direction)]
    return player_ships_dict

def place_ships(board, player_ship_dict):
    # place ships on board
    create_ships(player_ship_dict)
    ship_row, ship_column = randint(0,7), randint(0,7)
    for k, v in player_ship_dict.items():
        while board[ship_row][ship_column] != " ":
            ship_row, ship_column = randint(0,7), randint(0,7)
        if player_ship_dict[k][0][0] == "<":
            while ship_column + len(player_ship_dict[k][0]) > len(board[ship_row]):
                ship_column -= 1
            board[ship_row][ship_column:(ship_column + len(player_ship_dict[k][0]))] = player_ship_dict[k][0]
        elif player_ship_dict[k][0][0] == "^":
            while ship_row + len(player_ship_dict[k][0]) > len(board[ship_row]):
                ship_row -= 1
            i = 0
            while i <= len(player_ship_dict[k][0])-1:
                board[ship_row + i][ship_column] = player_ship_dict[k][0][i]
                i += 1
    return board

def load_board(board):
    # creates blank player guess and ship placement boards
    print("  A B C D E F G H")
    print(" -----------------")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1
    print(" -----------------")

def reset_player_board():
    # allows player to reset their game board
    refresh = input("Are you happy with this board? (Y/N): ")
    if len(refresh) > 1:
        print("ValueError: input can only be Y or N.")
        reset_player_board()
    elif refresh == "n" or refresh == "N":
        place_ships(player_ship_board, player_1)
    elif refresh == "y" or refresh == "Y":
        return

def player_guess():
    # player makes guess (hit and miss)
    guess = input("Enter column (A-H) and row (1-8) such as A3: ").upper()
    if len(guess) == 2:
        column = guess[0]
        row = guess[1]
    else:
        print("Not an appropriate choice, please try again")
        player_guess()
    while row not in "12345678":
        print("Not an appropriate choice, please select a valid row")
        player_guess()
    while column not in "ABCDEFGH":
        print("Not an appropriate choice, please select a valid column")
        player_guess()
    column = convert_nums_to_letters[column]
    row = int(row) - 1
    player_guess = [row, column]
    hit_miss(computer_ship_board, player_guess_board, player_guess)
    if computer_ships_count > 0:
        computer_guess()
    else:
        end_game()

def computer_guess():
    # computer makes guess, generates coordinates for launch and determines hit or miss
    row, column = randint(0, 7), randint(0, 7)
    computer_guess = [row, column]
    print("The computer aimed a missile to" + computer_guess + "coordinates")
    hit_miss(player_ship_board, computer_guess_board, computer_guess)
    if player_ships_count > 0:
        player_guess()
    else:
        end_game()

def hit_miss(ship_board, guess_board, guess):
    # determines if launch hits or misses ships
    pass
    print()

def end_game():
    # ends game (win or lose)
    if player_ships_count > computer_ships_count:
        print("Congratulations! You are the winner!")
        print("You hit all your enemies battleships in " + player_guess_count + "turns!")
        new_game = input("Do you think you can do better? (Y/N):")
    else: 
        print("Oh no! All your battleships have been destroyed!")
        print(new_game)

if __name__ == "__main__":
    print("             <====>  Welcome to Battleships!  <====>")
    print("The aim of the game is to sink your opponents battleships before they sink yours!")
    name = input("Who is taking on this challenge?: ")
    print("   <==>   Rules   <==>")
    print("1. You will be playing against the computer.")
    print("2. A board will be randomly generated for you and your oponent.")
    print("3. Input coordinates of where you wish to strike.")
    print("4. You will take it in turns to strike each others boards.")
    print("5. The winner is the one who hits all their oponents ships first.")
    print("Legend:")
    print("'"' '"' - unhit")
    print("'"'X'"' - hit")
    print("'"'O'"' - miss")
    print("Ships:")
    print("<> - ship of length 2 cells, each player gets 1 of these")
    print("<=> - ship of length 3 cells, each player gets 1 of these")
    print("<==> - ship of length 4 cells, each player gets 1 of these")
    place_ships(player_ship_board, player_1)
    place_ships(computer_ship_board, player_2)
    load_board(player_guess_board)
    load_board(player_ship_board)
    reset_player_board()
    player_guess()