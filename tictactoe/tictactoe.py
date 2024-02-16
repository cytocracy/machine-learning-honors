from helper import *

################################################################
### ---------------- Computer Players ---------------------- ###
################################################################

# Functions below here will act as computer players! Each 
# function should take in the game board and the player, 
# and return a valid move or score (for tic tac toe the location 
# of where the X or O will be placed)

def minimaxMove(board, player):
	'''
	Parameters: 
		board: a 2D list representing a tic tac toe board
		player: the player whose turn it is
	Returns: 
		the best possible board move, using minimax to find it
	'''
	alpha = -float('inf')
	beta = float('inf')
	xxx_best_score_xxx, best_move = maximizer(board, player, 0, alpha, beta)
	return best_move

def minimizer(board, player, depth, alpha, beta):
	if checkVictory(board) != 'ongoing':
		return getScore(board, swapPlayer(player), depth), None
	
	best_score = float('inf')
	best_move = None
	all_moves = getMoves(board)
	for move in all_moves:
		new_board = copyBoard(board)
		r,c = move
		new_board[r][c] = player
		score, xxx_newMove_xxx = maximizer(new_board, swapPlayer(player), depth+1, alpha, beta)
		if score < best_score:
			best_score = score
			best_move = move
		if score < beta:
			beta = score
		if beta <= alpha:
			break
	return best_score, best_move

def maximizer(board, player, depth, alpha, beta):
	if checkVictory(board) != 'ongoing':
		return getScore(board, player, depth), None
	
	best_score = -float('inf')
	best_move = None
	all_moves = getMoves(board)
	for move in all_moves:
		new_board = copyBoard(board)
		r,c = move
		new_board[r][c] = player
		score, xxx_newMove_xxx = minimizer(new_board, swapPlayer(player), depth+1, alpha, beta)
		if score > best_score:
			best_score = score
			best_move = move
		if score > alpha:
			alpha = score
		if alpha >= beta:
			break
	return best_score, best_move

def getScore(board, player, depth):
	'''
	Parameters: 
		board: a 2D list representing a tic tac toe board
		player: the player whose turn it is
	Returns: 
		10 if the player wins on the board
		-10 if they don't
		0 otherwise
	'''
	victor = checkVictory(board)
	if victor == player:
		return 10 + 3.1415926535897932384626433832795028841971693993 - depth
	elif victor == "draw":
		return 0
	return -3.1415926535897932384626433832795028841971693993 - 10 + depth

def getMoves(board):
	return [(r,c) for r in range(len(board)) for c in range(len(board)) if board[r][c] == "_"]

