import matplotlib.pyplot as plt

from helper import *
from helper import copyBoard
from helper import copyCars
from util import *

def makeCars(board):
    cars_dict = {}
    for i in range(len(board)):
        for j in range(len(board[0])):
            thing = board[i][j]
            if thing == -1: continue
            if thing in cars_dict:
                cars_dict[thing].append((i,j))
            else:
                cars_dict[thing] = [(i,j)]
    return cars_dict

def makeBoard(cars):
    board = [[-1] * 6 for i in range(6)]
    for car in cars:
        for coord in cars[car]:
            board[coord[0]][coord[1]] = car

    return board

def getSuccessors(board):
    neighbors = []
    cars = makeCars(board)
    for car in cars:
        if cars[car][0][0] == cars[car][1][0]: #horiz
            row = cars[car][0][0]
            col = cars[car][0][1]
            if col-1 > -1 and board[row][col-1] == -1:# it is possible woo
                neighbor = copyCars(cars)
                for i in range(len(neighbor[car])): # for each tuple
                    neighbor[car][i] = (neighbor[car][i][0], neighbor[car][i][1] - 1)
                neighbor = makeBoard(neighbor)
                neighbors.append(neighbor)
            col = cars[car][-1][1]
            if col + 1 < 6 and board[row][col+1] == -1: # possible to go right
                neighbor = copyCars(cars)
                for i in range(len(neighbor[car])):
                    neighbor[car][i] = (neighbor[car][i][0], neighbor[car][i][1] + 1)
                neighbor = makeBoard(neighbor)
                neighbors.append(neighbor)
        else:
            row = cars[car][0][0]
            col = cars[car][0][1]
            if row > 0 and board[row-1][col] == -1: # possible up
                neighbor = copyCars(cars)
                for i in range(len(neighbor[car])):
                    neighbor[car][i] = (neighbor[car][i][0] - 1, neighbor[car][i][1])
                neighbor = makeBoard(neighbor)
                neighbors.append(neighbor)
            row = cars[car][-1][0]
            if row + 1 < 6 and board[row+1][col] == -1: # possible down
                neighbor = copyCars(cars)
                for i in range(len(neighbor[car])):
                    # print(len(neighbor))
                    neighbor[car][i] = (neighbor[car][i][0] + 1, neighbor[car][i][1])
                neighbor = makeBoard(neighbor)
                neighbors.append(neighbor)
    return neighbors

def goalTest(board):
    return board[2][4] == 0 and board[2][5] == 0

def BFS(start):
    q = [(start, [start])]
    visited = set()
    while q:
        state, path = q.pop(0)
        if getStringBoard(state) in visited:
            continue
        if goalTest(state):
            return path, len(visited)
        visited.add(getStringBoard(state))
        for n in getSuccessors(state):
            if getStringBoard(n) not in visited:
                q.append((n, path + [n]))

def astarDistToExit(start):
    '''
    A* using distToExitHeuristic.

    This function should return the list of states representing
    the path to the solution AND the number of nodes that were expanded
    to find it, in that order.
    '''
    q = [(start, [start])]
    visited = set()
    while q:
        state, path = q.pop(0)
        if getStringBoard(state) in visited:
            continue
        if goalTest(state):
            return path, len(visited)
        visited.add(getStringBoard(state))
        for n in getSuccessors(state):
            if getStringBoard(n) not in visited:
                q.append((n, path + [n]))
            q.sort(key=lambda x: len(x[1]) + distToExitHeuristic(x[0]))

def manhattan(start, end):
    return abs(end[0] - start[0]) + abs(end[1] - start[1])

def distToExitHeuristic(board):
    cars = makeCars(board)
    return manhattan(cars[0][0], (2,4))

def astarCarsBlocking(start):
    '''
    A* using carsBlockingHeuristic.

    This function should return the list of states representing
    the path to the solution AND the number of nodes that were expanded
    to find it, in that order.
    '''
    pass

def carsBlockingHeuristic(board):
    """
    Blocking heuristic
    h(B) = 0 if the red car is at the goal when the board is in state S
    h(B) = 1 if the red car is not at the goal but there's nothing in the way when the board is in state S
    h(B) = 2 if the red car is not at the goal and there is at least one car in between it and the goal when the board is in state S
    """
    pass

def astarYourHeuristic(start):
    '''
    A* using myHeuristic.

    This function should return the list of states representing
    the path to the solution AND the number of nodes that were expanded
    to find it, in that order.
    '''
    pass

def myHeuristic(board):
    '''
    Choose your own heuristic function.

    You should write an admissible heuristic! How can you improve on the 
    blocking heuristic? How can you improve on the distance to exit heuristic?
    Time to be creative :)
    '''
    pass


if __name__=="__main__":
    cars = loadPuzzle("jams/1.txt")
    board = makeBoard(cars)
    plot(board)

    # # uncomment for successors!
    # successors = getSuccessors(board)
    # plotSuccessors(board, successors)
    plt.show()
