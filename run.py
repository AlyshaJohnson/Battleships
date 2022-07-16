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
player_1 = name
player_2 = "computer"
player_guess_count = 0
player_ships_count = 5
computer_ships_count = 5

player_ship_board = [[" "] * 8 for x in range(8)]
player_guess_board = [[" "] * 8 for i in range(8)]
computer_ship_board = [[" "] * 8 for p in range(8)]
computer_guess_board = [[" "] * 8 for m in range(8)]

convert_nums_to_letters = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7
}

# Classes
class ship:
    def __init__(self, length, row, column, direction):
        #initialising ship
        self.length = length
        self.row = row
        self.column = column
    
        if direction == 0:
            self.direction = "Horizontal"
        elif direction == 1:
            self.direction = "Vertical"
        else:
            raise ValueError("Number needs to be with a '0' or '1' to get direction")

    def iter(self, length, direction):
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
                    self[i] = "||"
                    i+=1
        return self    

ships = {
    "ship_type_1": ship(2, randint(0,7), randint(0,7), randint(0,1)),
    "ship_type_2": ship(3, randint(0,7), randint(0,7), randint(0,1)),
    "ship_type_3": ship(4, randint(0,7), randint(0,7), randint(0,1))
}

# Functions
def create_ships(dict, player):
    # creates ships
    for k, v in dict.items():
        print(k + "_" + player, '=', [ship.iter(dict[k], dict[k].length, dict[k].direction)])

def place_ships(board):
    # allows player to place ships
    pass

def load_board(board):
    # creates blank player guess and ship placement boards
    print("  a b c d e f g h")
    print(" -----------------")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1
    print(" -----------------")

def reset_player_board():
    # allows player to reset their game board
    pass

def player_guess():
    # player makes guess (hit and miss)
    pass
    if computer_ships_count > 0:
        computer_guess()
    else:
        end_game()

def computer_guess():
    # computer makes guess (hit and miss)
    pass
    if player_ships_count > 0:
        player_guess()
    else:
        end_game()

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
    print("<> - ship of length 2 cells, each player gets 2 of these")
    print("<=> - ship of length 3 cells, each player gets 2 of these")
    print("<==> - ship of length 4 cells, each player gets 1 of these")
    create_ships(ships, player_1)
    create_ships(ships, player_2)
    place_ships()
    load_board(player_ship_board)
    load_board(player_guess_board)
    while player_ships_count > 0 or computer_ships_count > 0:
        player_guess()