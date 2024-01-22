from battleship import Battleship
import sys

play_game = True

print("\n\nHELLO AND WELCOME TO BATTLESHIP WOOO\n\n")

while play_game:
    game = Battleship()

    print("You have " + str(game.getNumShipsRemaining()) + " ships remaining")
    print("---------------------------------------\n")

    game.printBoard(True)

    while game.getNumShipsRemaining() > 0:
        print("Where would you like to guess?")
        try:
            row = int(input("Row: "))
            col = int(input("Col: "))
        except ValueError:
            print("U did a silly and fat fingered the enter button ig")
            continue
        coord = (row, col)
        if game.makeMove(coord):
            print("Hit!")
        else: print("Miss.")
        print("You have " + str(game.getNumShipsRemaining()) + " ships remaining.")
        print("---------------------------------------\n")
        game.printBoard(True)

    print("You won!")
    print("Would you like to play again?")
    response = input("Y/N: ")
    if response.lower() == "n":
        play_game = False


print('yippee bye bye')