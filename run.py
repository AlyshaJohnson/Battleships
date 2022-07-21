"""
This is a game of battle ships.
<==>   Rules   <==>
1. You will be playing against the computer.
2. A board will be randomly generated for you and your oponent.
3. Input coordinates of where you wish to strike.
4. You will take it in turns to strike each others boards.
5. The winner is the one who hits all their oponents ships first.
Legend:
   " " - unhit
   "X" - hit
   "O" - miss
 Ship legend:
   <> - ship of length 2 cells, each player gets 2 of these
   <=> - ship of length 3 cells, each player gets 2 of these
   <==> - ship of length 4 cells, each player gets 1 of these
"""

from random import randint


class Ship:
    """ classify ships """
    def __init__(self, length, direction):
        """ initialising ship """
        self.length = length
        if direction == 0:
            self.direction = "Horizontal"
        elif direction == 1:
            self.direction = "Vertical"
        else:
            raise ValueError("Number needs to be with a '0' or '1' to get\
                 direction")

    def iter_ship(self, length, direction):
        """ transform ship into list for required length then replace with boat
        symbols to produce ships """
        self = []
        for i in range(length):
            self.append(i)
        if direction == "Horizontal":
            self[0] = "<"
            self[-1] = ">"
            if length > 2:
                i = 1
                while i >= 1 and i <= length-2:
                    self[i] = "="
                    i += 1
        if direction == "Vertical":
            self[0] = "^"
            self[-1] = "v"
            if length > 2:
                i = 1
                while i >= 1 and i <= length-2:
                    self[i] = "|"
                    i += 1
        return self


ships = {
    "ship_type_1": Ship(2, randint(0, 1)),
    "ship_type_2": Ship(3, randint(0, 1)),
    "ship_type_3": Ship(4, randint(0, 1))
}


player_1 = ships.copy()
player_2 = ships.copy()


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


RESULT = None
PLAYER_GUESS_COUNT = 0
PLAYER_SHIPS_COUNT = 9
COMPUTER_SHIP_COUNT = 9
GAME_OVER = False


player_ship_board = [[" "] * 8 for w in range(8)]
computer_ship_board = [[" "] * 8 for y in range(8)]
player_guess_board = [[" "] * 8 for x in range(8)]
computer_guess_board = [[" "] * 8 for z in range(8)]


def create_ships(player_ships_dict):
    """ checks for duplicates and creates ships at specified location """
    for key, value in player_ships_dict.items():
        player_ships_dict[key] = [Ship.iter_ship(player_ships_dict[key], player_ships_dict[key].length, player_ships_dict[key].direction)]  # noqa
    return player_ships_dict


def place_ships(board, player_ship_dict):
    """ place ships on board whilst checking the space is blank and the whole \
        ship will fit on the board"""
    create_ships(player_ship_dict)
    ship_row, ship_column = randint(0, 7), randint(0, 7)
    while True:
        for key, value in player_ship_dict.items():
            while board[ship_row][ship_column] != " ":
                ship_row, ship_column = randint(0, 7), randint(0, 7)
            if player_ship_dict[key][0][0] == "<":
                while ship_column + len(player_ship_dict[key][0]) > len(board[ship_row]):  # noqa
                    ship_column -= 1
                board[ship_row][ship_column:(ship_column + len(player_ship_dict[key][0]))] = player_ship_dict[key][0]  # noqa
            elif player_ship_dict[key][0][0] == "^":
                while ship_row + len(player_ship_dict[key][0]) > len(board[ship_row]):  # noqa
                    ship_row -= 1
                i = 0
                while i <= len(player_ship_dict[key][0])-1:
                    board[ship_row + i][ship_column] = player_ship_dict[key][0][i]  # noqa
                    i += 1
        sum = 0
        for r in board:
            sum += r.count("<") + r.count("=") + r.count(">") + r.count("^") + r.count("|") + r.count("v")  # noqa
        if sum == 9:
            return board
        else:
            i = 0
            while i < len(board):
                board[i] = [" ", " ", " ", " ", " ", " ", " ", " "]
                i += 1
    return board


def load_board(guess_board, ship_board):
    """ creates blank player guess and ship placement boards """
    print("<-> SHIP BOARD <->")
    print("  A B C D E F G H")
    print(" -----------------")
    row_number = 1
    for row in ship_board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1
    print(" -----------------")
    print("<-> GUESS BOARD <->")
    print("  A B C D E F G H")
    print(" -----------------")
    row_number = 1
    for row in guess_board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1
    print(" -----------------")
    print("Number of enemy ships left: " + str(COMPUTER_SHIP_COUNT))
    print("No. of ships left: " + str(PLAYER_SHIPS_COUNT))
    print("No. of missiles launched: " + str(PLAYER_GUESS_COUNT))


def reset_player_board(ship_board, player):
    """ allows player to reset their game board """
    while True:
        refresh = input("Are you happy with this board? (Y/N): \n")
        if len(refresh) == 1:
            if refresh in "yYnN":
                break
        print("Invalid input, try again.")
    if refresh == "n" or refresh == "N":
        player = ships.copy()
        ship_board = [[" "] * 8 for w in range(8)]
        place_ships(ship_board, player)
        load_board(player_guess_board, ship_board)
        reset_player_board(ship_board, player)
    elif refresh == "y" or refresh == "Y":
        return


def player_guess():
    """ player makes guess, generates coordinates for launch and determines
    hit or miss """
    global PLAYER_GUESS_COUNT, COMPUTER_SHIP_COUNT
    while True:
        while True:
            guess = input("Enter column (A-H) and row (1-8) such as A3: \n").upper()  # noqa
            if len(guess) == 2:
                if guess[0] in "ABCDEFGH" and guess[1] in "12345678":  # noqa
                    column = convert_nums_to_letters[guess[0]]
                    row = int(guess[1]) - 1
                    break
            print("Invalid input, try again.")
        if player_guess_board[row][column] == " ":
            break
        print("Coordinates already input, try again.")
    player_guess_coords = [row, column]
    hit_miss(computer_ship_board, player_guess_board, player_guess_coords)
    result = hit_miss(computer_ship_board, player_guess_board, player_guess_coords)[2]  # noqa
    if result == "It's a hit!":
        COMPUTER_SHIP_COUNT -= 1
    else:
        pass
    PLAYER_GUESS_COUNT += 1
    load_board(player_guess_board, player_ship_board)
    if COMPUTER_SHIP_COUNT > 0:
        computer_guess()
    else:
        end_game()
    return


def computer_guess():
    """ computer makes guess, generates coordinates for launch and determines
    hit or miss """
    global PLAYER_SHIPS_COUNT
    while True:
        row, column = randint(0, 7), randint(0, 7)
        computer_guess_coords = [row, column]
        if computer_guess_board[row][column] == " ":
            break
    print("The computer aimed a missile at " + str(computer_guess_coords) + " coordinates")  # noqa
    hit_miss(player_ship_board, computer_guess_board, computer_guess_coords)
    result = hit_miss(player_ship_board, computer_guess_board, computer_guess_coords)[2]  # noqa
    if result == "It's a hit!":
        PLAYER_SHIPS_COUNT -= 1
    else:
        pass
    load_board(player_guess_board, player_ship_board)
    if PLAYER_SHIPS_COUNT > 0:
        player_guess()
    else:
        end_game()
    return


def hit_miss(ship_board, guess_board, guess):
    """ determines if launch hits or misses ships """
    global RESULT
    row = guess[0]
    column = guess[1]
    if ship_board[row][column] == " ":
        ship_board[row][column] = "O"
        guess_board[row][column] = "O"
        RESULT = "It's a miss!"
    elif ship_board[row][column] in "<=>^|v":
        ship_board[row][column] = "X"
        guess_board[row][column] = "X"
        RESULT = "It's a hit!"
    else:
        print("Coordinates already submitted")
    return ship_board, guess_board, RESULT


def end_game():
    """ determines winner of battleships game and turns game_over to true """
    global GAME_OVER
    if PLAYER_SHIPS_COUNT > COMPUTER_SHIP_COUNT:
        print("Congratulations! You are the winner!")
        print("You hit all your enemies battleships in " + str(PLAYER_GUESS_COUNT) + " turns!")  # noqa
        GAME_OVER = True
    else:
        print("Oh no! All your battleships have been destroyed!")
        GAME_OVER = True
    return GAME_OVER


if __name__ == "__main__":
    global GAME_OVER
    while GAME_OVER is False:
        print("               <====>  Welcome to Battleships!  <====>")
        print("The aim of the game is to sink your opponents battleships before they")  # noqa
        print("sink yours!")
        print("-----------------------------------------------------------------------")  # noqa
        name = input("Who is taking on this challenge? (Enter name): \n")
        print("Good to have you on board, " + name + "!")
        print("Here are the rules:")
        print("-----------------------------------------------------------------------")  # noqa
        print("   <==>   Rules   <==>")
        print("1. You will be playing against the computer.")
        print("2. A board will be randomly generated for you and your oponent.")  # noqa
        print("3. Input coordinates of where you wish to strike.")
        print("4. You will take it in turns to strike each others boards.")
        print("5. The winner is the one who hits all their oponents ships first.")  # noqa
        print("Legend:")
        print('  " " - unhit')
        print('  "X" - hit')
        print('  "O" - miss')
        print("Ships:")
        print("  <> - ship of length 2 cells, each player gets 1 of these")
        print("  <=> - ship of length 3 cells, each player gets 1 of these")
        print("  <==> - ship of length 4 cells, each player gets 1 of these")
        print("-----------------------------------------------------------------------")  # noqa
        place_ships(player_ship_board, player_1)
        place_ships(computer_ship_board, player_2)
        load_board(player_guess_board, player_ship_board)
        reset_player_board(player_ship_board, player_1)
        player_guess()
    while True:
        new_game = input("Do you think you can do better? (Y/N): \n")
        if len(new_game) == 1:
            if new_game in "yYnN":
                break
        print("Invalid input, try again.")
    if new_game == "yY":
        print("Game restarting...")
        GAME_OVER = True
    elif new_game in "nN":
        print("Thank you for playing, see you next time!")
