import time

def makeMove(p1side, p2side, player, move):
	'''	
	Remember, when a player makes a move in Mancala, they
	take all the stones from the chosen pit, then one by one 
	place them in the next pit going counter clock wise. Stones
	are placed in their personal Mancala, but not the other players.

	This method should MODIFY p1side and p2side to reflect the new
	configuration, and should return True if the player ended their turn
	in their Mancala, and False otherwise.

	Remember, if the player ends their turn in an EMPTY location on their
	own side (not including the Mancala) and the opposite side placement has
	stones in it, those stones and the one in the previously empty location
	get captured and put in the player's Mancala.
	'''

	if player == 1:
		player_side = p1side
		other_side = p2side
	else:
		player_side = p2side
		other_side = p1side

	own_side = True

	# player is 1 or 2
	# p1side and p2side are lists of integers representing the board

	hand = player_side[move]
	player_side[move] = 0
	index = move

	while hand > 0:
		index += 1
		if index == len(player_side) - 1:
			if own_side:
				hand -= 1
				player_side[index] += 1
				if hand == 0:
					return True
				own_side = not own_side
				index = 0
			else:
				own_side = not own_side
				index = 0
			
		hand -= 1
		if own_side:
			player_side[index] += 1
		else:
			other_side[index] += 1

		if hand == 0:
			if check_capture(own_side, player_side, other_side, index):
				capture(own_side, player_side, other_side, index)
			return False
		

def check_capture(own_side, player_side, other_side, index):
	return own_side and player_side[index] == 1 and other_side[get_opposite_idx(index)]>0

def capture(own_side, player_side, other_side, index):
	player_side[-1] += other_side[get_opposite_idx(index)] + player_side[index]
	player_side[index] = 0
	other_side[get_opposite_idx(index)] = 0



def get_opposite_idx(idx):
	return 5-idx






def get_other_side(side, p1side, p2side):
	return p1side if side == p2side else p2side




def getAllPossibleMoves(p1side, p2side, player):
	'''
	Returns all the valid moves a player can make.
	A player can not make a move at an empty pit.
	'''
	moves = []
	for i in range(0,6):
		if player == 1:
			if p1side[i]!=0:
				moves.append(i)
		else:
			if p2side[i]!=0:
				moves.append(i)
	return moves

def isVictory(p1side, p2side):
	'''
	Returns the player (1 or 2) who has won, or
	"ongoing" if the game is still in progress.
	'''
	if p1side[:-1].count(0) == len(p1side[:-1]):
		p2side[-1]+=sum(p2side[:-1])
		for i in range(len(p2side)-1):
			p2side[i]=0
	if p2side[:-1].count(0) == len(p2side[:-1]):
		p1side[-1]+=sum(p1side[:-1])
		for i in range(len(p1side)-1):
			p1side[i]=0
		
	if p1side[:-1].count(0)!=len(p1side[:-1]) and p2side[:-1].count(0)!=len(p2side[:-1]):
		return "ongoing"
	if p1side[-1]>p2side[-1]:
		return 1
	return 2

def copySide(side):
	'''
	Returns a non-aliasing copy of this side of the board.
	This will be useful when coding your minimax player.
	'''
	return [s for s in side]

def swapPlayer(player):
	'''
	Returns the opposite of the current player, useful in 
	implementing minimax.
	'''
	if player == 1:
		return 2
	return 1

def displayBoard(p1side, p2side):
    '''
    Displays the game board as ASCII-art based on the 
    two board lists.
    '''
    seedAmounts = []
    for pit in p2side[:-1][::-1]+p2side[-1:]+p1side[-1:]+p1side[:-1]:
        numSeedsInThisPit = str(pit).rjust(2)
        seedAmounts.append(numSeedsInThisPit)
    print(seedAmounts)
    print("""
        +------+------+--<<<<<-Player 2----+------+------+------+
        P      |5     |4     |3     |2     |1     |0     |      P
        2      |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |      1
        S      |      |      |      |      |      |      |      S
        T  {}  +------+------+------+------+------+------+  {}  T
        O      |0     |1     |2     |3     |4     |5     |      O
        R      |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |      R
        E      |      |      |      |      |      |      |      E
        +------+------+------+-Player 1->>>>>-----+------+------+
    
        """.format(*seedAmounts))

def humanMove(p1side, p2side, player):
    '''
    Code to get input for player move. Should ensure that move
    is valid.
    '''
    move = input("Player "+str(player)+", choose move 0-5: ")

    while (not move.isdigit() or int(move)<0 or int(move)>5 or 
        (player==1 and p1side[int(move)]==0) or
        (player==2 and p2side[int(move)]==0)):
        print("Not a valid move.")
        move = input("Player "+str(player)+", choose move 0-5: ")
    return int(move)

def anyMove(func, p1side, p2side, player):
    '''
    Makes a generic using the specific given function.
    Prints out the amount of time it takes to make the move.
    Handles moving multiple times in one turn.
    '''
    tic = time.time()
    move = func(p1side, p2side, player)
    toc = time.time()
    print("You took",toc-tic,"seconds to move!")
    while makeMove(p1side, p2side, player, move):
        if isVictory(p1side, p2side) != "ongoing":
            displayBoard(p1side, p2side)
            return
        displayBoard(p1side, p2side)
        print("You get to move again!")
        tic = time.time()
        move = func(p1side, p2side, player)
        toc = time.time()
        print("You took",toc-tic,"seconds to move!")