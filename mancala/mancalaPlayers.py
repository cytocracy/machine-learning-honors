from mancala import *

def badEvaluationFunction(p1side, p2side, player):
	'''
	This is not a great evaluation function. This function
	returns the differences in the number of stones in each
	Mancala between the player and the opponent.
	'''
	if player == 1:
		return p1side[-1]-p2side[-1]
	else:
		return p2side[-1] - p1side[-1]

def evaluationFunction1(p1side, p2side, player):
	'''
	Write a better evaluation function here. You should 
	have a few! The one above is an example of a pretty bad 
	evaluation function - yours should definitely be better!
	'''
	if player == 1:
		return sum(p1side) - sum(p2side)
	else:
		return sum(p2side) - sum(p1side)


def evaluationFunction2(p1side, p2side, player):
	player_side = p1side if player == 1 else p2side
	other_side = p2side if player == 1 else p1side

	total = 0
	total += player_side[-1] - other_side[-1]
	for i in range(6):
		if other_side[5-i] == 0:
			total -= player_side[i]
		if (i + player_side[i]) == 6:
			total += 2
	return total

def evaluationFunction3(p1side, p2side, player):
	player_side = p1side if player == 1 else p2side
	other_side = p2side if player == 1 else p1side

	total = 0
	total += (player_side[-1] - other_side[-1]) * 10
	for i in range(6):	
		if other_side[5-i] == 0:
			total -= (player_side[i])
		endindex = i + player_side[i]
		if endindex == 6:
			total += 2
		elif endindex < 6 and player_side[endindex] == 0 and other_side[5-endindex] != 0:
			total += (other_side[5-endindex] + 1) * 2
		total += player_side[i]
	return total
   
   
    
 


def instantMovePlayer(p1side, p2side, player):
	'''
	The instantMovePlayer does not look ahead at all, just
	evaluates the possible moves it can make and chooses the 
	one that the evaluation function says will be the best.
	'''
	bestMove = 0
	bestMoveScore = -float('inf')
	for move in getAllPossibleMoves(p1side, p2side, player):
		p1sideNext = copySide(p1side)
		p2sideNext = copySide(p2side)
		makeMove(p1sideNext, p2sideNext, player, move)

		score = badEvaluationFunction(p1sideNext, p2sideNext, player)
		if score > bestMoveScore:
			bestMoveScore = score
			bestMove = move
	return bestMove

def testingPlayer(p1side, p2side, player):
	'''
	The instantMovePlayer does not look ahead at all, just
	evaluates the possible moves it can make and chooses the 
	one that the evaluation function says will be the best.
	'''
	bestMove = 0
	bestMoveScore = -float('inf')
	for move in getAllPossibleMoves(p1side, p2side, player):
		p1sideNext = copySide(p1side)
		p2sideNext = copySide(p2side)
		makeMove(p1sideNext, p2sideNext, player, move)

		score = evaluationFunction3(p1sideNext, p2sideNext, player)
		if score > bestMoveScore:
			bestMoveScore = score
			bestMove = move
	return bestMove

def minimaxPlayer(p1side, p2side, player):
	'''
	Make the best move possible using depth-limited
	'''
	maxDepth = 10 # adjust this as needed!
	
	alpha = -float('inf')
	beta = float('inf')
  	
	_, best_move = maximizer(p1side, p2side, player, maxDepth, alpha, beta)
 
	return best_move


def maximizer(p1side, p2side, player, depth, alpha, beta):
	if isVictory(p1side, p2side) != "ongoing" or depth == 0:
		return evaluationFunction3(p1side, p2side, player), None
    
	actions = getAllPossibleMoves(p1side, p2side, player)
 
	max_score = -float('inf')
	max_move = None
 
	for move in actions:
		p1sideNext = copySide(p1side)
		p2sideNext = copySide(p2side)
		makeMove(p1sideNext, p2sideNext, player, move)
		score, _ = minimizer(p1sideNext, p2sideNext, swapPlayer(player), depth-1, alpha, beta)
		if score > max_score:
			max_score = score
			max_move = move
		alpha = max(alpha, max_score)
		if alpha >= beta:
			break

	return max_score, max_move

def minimizer(p1side, p2side, player, depth, alpha, beta):
	if isVictory(p1side, p2side) != "ongoing" or depth == 0:
		return evaluationFunction3(p1side, p2side, player), None
	
	actions = getAllPossibleMoves(p1side, p2side, player)
 
	min_score = float('inf')
	min_move = None
 
	for move in actions:
		p1sideNext = copySide(p1side)
		p2sideNext = copySide(p2side)
		makeMove(p1sideNext, p2sideNext, player, move)
		score, _ = maximizer(p1sideNext, p2sideNext, swapPlayer(player), depth-1, alpha, beta)
		if score < min_score:
			min_score = score
			min_move = move
		beta = min(beta, min_score)
		if alpha >= beta:
			break

	return min_score, min_move

def roshan_tanejas_player(p1side, p2side, player):
	maxDepth = 10 
 
	alpha = -float('inf')
	beta = float('inf')
  	
	_, best_move = maximizer(p1side, p2side, player, maxDepth, alpha, beta)
 
	return best_move
