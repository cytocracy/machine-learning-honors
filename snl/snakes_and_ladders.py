def neighbors(loc, snakes, ladders):
	neighbors = []
	for i in range(1, 7):
		next_loc = loc + i
		if next_loc in snakes:
			neighbors.append(snakes[next_loc])
		elif next_loc in ladders:
			neighbors.append(next_loc)
			neighbors.append(ladders[next_loc])
		else:
			neighbors.append(next_loc)
	return neighbors

def snakesAndLadders(finalLocation, snakes, ladders):
	visited = set()
	q = [(0,0)]
	while q:
		loc, count = q.pop(0)
		if loc not in visited:
			visited.add(loc)
			if loc == finalLocation: 
				return count
			else:
				for neighbor in neighbors(loc, snakes, ladders):
					q.append((neighbor, count+1))

if __name__=="__main__":
	# if you'd like to make your own test cases, you
	# can do so here! Otherwise, you can run test.py
	pass
