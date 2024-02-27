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

def evaluationFunction(p1side, p2side, player):
	'''
	Write a better evaluation function here. You should 
	have a few! The one above is an example of a pretty bad 
	evaluation function - yours should definitely be better!
	'''
	pass

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

def minimaxPlayer(p1side, p2side, player):
	'''
	Make the best move possible using depth-limited
	'''
	maxDepth = 2 # adjust this as needed!
	
	# add code below here!
	pass

def myCustomPlayer(p1side, p2side, player):
	'''
	Fill in your custom player here! Start with your minimax player
	and try tweaking the maxDepth and evaluation function being
	used to see what gets you the best game play. If you'd like to 
	go completely off the rails here and do something that's not even
	minimax, go for it!

	Feel free to name your custom player something more fun too!
	'''
	pass
