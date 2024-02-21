import matplotlib.pyplot as plt

from helper import *
from helper import copyBoard
from helper import copyCars
from util import *

LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)

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

def getMove(car, cars, direction):
    neighbor = copyCars(cars)
    for i in range(len(neighbor[car])): # for each tuple
        neighbor[car][i] = (neighbor[car][i][0] + direction[0], neighbor[car][i][1] + direction[1])
    return makeBoard(neighbor)

def canMove(car, cars, board, direction):
    if direction == LEFT:
        row = cars[car][0][0]
        col = cars[car][0][1]
        return cars[car][0][1] > 0 and board[row][col-1] == -1
    if direction == RIGHT:
        row = cars[car][-1][0]
        col = cars[car][-1][1]
        return cars[car][-1][1] < 5 and board[row][col+1] == -1
    if direction == UP:
        row = cars[car][0][0]
        col = cars[car][0][1]
        return cars[car][0][0] > 0 and board[row-1][col] == -1
    if direction == DOWN:
        row = cars[car][-1][0]
        col = cars[car][-1][1]
        return cars[car][-1][0] < 5 and board[row+1][col] == -1
    
def isHorizontal(car, cars):
    return cars[car][0][0] == cars[car][1][0]

def getSuccessors(board):
    neighbors = []
    cars = makeCars(board)
    for car in cars:
        if isHorizontal(car, cars):
            if canMove(car, cars, board, LEFT):
                neighbors.append(getMove(car, cars, LEFT))
            if canMove(car, cars, board, RIGHT): 
                neighbors.append(getMove(car, cars, RIGHT))
        else: # vertical
            if canMove(car, cars, board, UP):
                neighbors.append(getMove(car, cars, UP))
            if canMove(car, cars, board, DOWN):
                neighbors.append(getMove(car, cars, DOWN))
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
            q.sort(key=lambda x: len(x[1]) + carsBlockingHeuristic(x[0]))

def carsBlockingHeuristic(board):
    """
    Blocking heuristic
    h(B) = 0 if the red car is at the goal when the board is in state S
    h(B) = 1 if the red car is not at the goal but there's nothing in the way when the board is in state S
    h(B) = 2 if the red car is not at the goal and there is at least one car in between it and the goal when the board is in state S
    """
    cars = makeCars(board)
    if goalTest(board):
        return 0
    row = 2
    col = cars[0][1][1] + 1
    while col < 6:
        if board[row][col] != -1:
            return 2
        col += 1

    return 1
    
def astarYourHeuristic(start):
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
            q.sort(key=lambda x: len(x[1]) + myHeuristic(x[0]))

def myHeuristic(board):
    cars_blocking = set()
    cars = makeCars(board)
    row = 2
    col = cars[0][1][1] + 1
    while col < 6:
        if board[row][col] != -1:
            cars_blocking.add(board[row][col])
        col += 1
    return distToExitHeuristic(board) + len(cars_blocking)


if __name__=="__main__":
    cars = loadPuzzle("jams/1.txt")
    board = makeBoard(cars)
    plot(board)
    plt.show()
