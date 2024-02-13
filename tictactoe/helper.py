import time

##############################################################################################
### ----------------------------- Given Helper Functions --------------------------------- ###
##############################################################################################

# Functions below here you will write to play tic tac toe and help you build your code later!

def copyBoard(board):
	'''
	Returns a non-aliasing copy of the board.
	'''
	return [[b for b in row] for row in board]

def printBoard(board):
	'''
	Prints out a human readable tic-tac-toe board.
	'''
	print('| ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2] + ' |')
	print('| ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2] + ' |')
	print('| ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2] + ' |')

def swapPlayer(player):
	'''
	Returns the opposite player.
	'''
	if player == "X":
		return "O"
	return "X"

def isMoveOk(loc, board):
	'''
	Parameters: 
		loc: a tuple representing a location on the board
		board: a 2D list representing a tic tac toe board
	Returns: 
		True if the location is a valid one to be placing, False otherwise
	'''
	return 0<=loc[0]<3 and 0<=loc[1]<3 and board[loc[0]][loc[1]]=='_'

def checkVictory(board):
	'''
	Parameters: 
		board: a 2D list representing a tic tac toe board
	Returns: 
		'ongoing' if the game is still going
		'X' if the X player wins
		'O' if the O player wins
		'draw' if the game ends in a draw
	'''
	if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1]!='_':
		return board[0][0]
	if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[1][1]!='_':
		return board[1][1]
	for i in range(3):
		if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0]!='_':
			return board[i][1]
		if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i]!='_':
			return board[1][i]
	mv = [(i,j) for i in range(3) for j in range(3) if board[i][j]=='_']
	if mv==[]:
		return 'draw'
	return 'ongoing'

def swapPlayer(player):
	'''
	Parameters: 
		player: the player whose turn it is
	Returns: 
		'X' if the player is 'O'
		'O' if the player is 'X'
	'''
	if player == 'X':
		return 'O'
	return 'X'



