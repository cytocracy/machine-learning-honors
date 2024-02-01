from util import *
def neighbors(state):
	r, c = state
	spots = [(x,y) for (x,y) in [(r-1, c+2), (r-1, c-2), (r+1, c+2), (r+1, c-2), (r+2, c-1), (r+2, c+1), (r-2, c+1), (r-2, c-1)] if not (x<0 or x>7 or y<0 or y>7)]
	return spots
def minKnightMoves(start, goal):
	visited = set()
	q = [(start, 0)]
	count = 0
	while q:
		state, count = q.pop(0)
		if state not in visited:
			visited.add(state)
			if state == goal: return count
			else:
				for neighbor in neighbors(state):
					q.append((neighbor, count+1))
if __name__=="__main__":
	pass