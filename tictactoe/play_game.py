import time
from tictactoe import *
from helper import *
import time

player1 = minimaxMove

# change this to minimax to use the minimax function!
player2 = 'human'

'''
This will be a the central file we'll use to play a game of tic-tac-toe. 
Set the two variables above to change if 
'''
game_board = [['_', '_', '_'],
       		  ['_', '_', '_'],
       		  ['_', '_', '_']]

victory = 'ongoing'
player = 'X'

# main game loop
while victory =='ongoing':
	printBoard(game_board)

	# if we're dealing with a human player, we have to get a move
	if (player == 'X' and player1 == 'human') or (player == 'O' and player2 == 'human'):
		unparsed_coordinates = input("Where do you want to place? ") 
		try: 
			parsed = unparsed_coordinates.replace('(', "").replace(')', "") # make sure input format is right
			if ', ' in parsed:
				coords = tuple(parsed.split(", "))
			else:
				coords = tuple(parsed.split(","))
			coordinates = (int(coords[0]), int(coords[1]))

		except: # if people put in anything that doesn't fit the format, it will be caught here
			print("Please enter a coordinate in the correct format.")
			continue
	else:
		# we're dealing with a computer player, we use the function passed in to decide the move
		print("Computer", player, "is deciding on a move!")
		start = time.time() 

		if player == 'X':
			coordinates = player1(game_board, player)
			if type(coordinates[1])!=int:
				coordinates = coordinates[1]
		else:
			coordinates = player2(game_board, player)
			if type(coordinates[1])!=int:
	  			coordinates = coordinates[1]
	
		end = time.time() # will tell you how long running the algorithm took
		print("It took", end-start, "seconds for computer", player, "to choose!")

	if not isMoveOk(coordinates, game_board):
		print("Please enter a coordinate in bounds that is open.")
		continue
	else:
		game_board[coordinates[0]][coordinates[1]] = player
		if player == 'X':
			player = 'O'
		else:	
			player = 'X'
		victory = checkVictory(game_board)

# game is over!
printBoard(game_board)
if victory == 'draw':
	print("The game ended in a draw!")
else:
	if (victory == 'X' and player1 != 'human') or (victory == 'O' and player2 != 'human'):
		print("Computer", victory, "won the game!")
	else:
		print("Player", victory, "won the game!")


