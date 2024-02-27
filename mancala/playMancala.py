from mancala import *
from mancalaPlayers import *

# you can change either player to be humanMove or 
# any one of the players you write. To play a game
# against another person, set player1 and player2 to 
# both be humanMove. To play computers against each 
# other, set each to be the name of the function, maybe
# player1 = instantMovePlayer and player2 = minimaxPlayer.

player1 = humanMove
player2 = instantMovePlayer

p1side = [4, 4, 4, 4, 4, 4, 0]
p2side = [4, 4, 4, 4, 4, 4, 0]
player = 1

while isVictory(p1side, p2side)=="ongoing":
	displayBoard(p1side, p2side)
	if player == 1:
		if player1 != humanMove:
			print("Computer is making a move.")
		anyMove(player1, p1side, p2side, player)
	else:
		if player2 != humanMove:
			print("Computer is making a move.")
		anyMove(player2, p1side, p2side, player)

	player = swapPlayer(player)

victor = isVictory(p1side, p2side)
print("Player",victor,"has won, with a score of",p1side[-1],"to",p2side[-1])

