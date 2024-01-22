from computerHelper import *
from copy import deepcopy

class Battleship:
    def __init__(self):
        self.board = initializeGameBoard()
        self.firedAt = []
        self.ships = self.getShipDictionary()

    def getShipDictionary(self):
        locDic = {}

        board = self.board

        for r in range(len(board)):
            for c in range(len(board[0])):
                letter = board[r][c]
                # print(letter)
                if letter != "~":
                    if letter in locDic:
                        locDic[letter].append((r,c))
                    else:
                        locDic[letter] = [(r,c)]
        # print(locDic)
        return locDic

    def getNumShipsRemaining(self):
        locDic = self.ships
        # print(locDic)
        count = 0
        for ship in locDic: 
            if len(locDic[ship]) != 0:
                count +=1
        # print(count)
        return count

    def getLocationsFiredAt(self):
        return self.firedAt

    def makeMove(self, coord):

        self.firedAt.append(coord)
        if self.board[coord[0]][coord[1]] != "~":
            self.ships[self.board[coord[0]][coord[1]]].remove(coord)
            return True
        return False

    def makeHiddenBoard(self):
        returnBoard = deepcopy(self.board)
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if (r,c) not in self.firedAt:
                    returnBoard[r][c] = "~"
                else:
                    if self.board[r][c] == "~":
                        returnBoard[r][c] = " "
                    elif len(self.ships[self.board[r][c]]) != 0:
                        returnBoard[r][c] = "*"
                    else: returnBoard[r][c] = self.board[r][c]
        return returnBoard

    def printBoard(self, hidden): 
        if hidden:
            boardToUse = self.makeHiddenBoard()
        else:
            boardToUse = self.board

        print(" 0123456789")
        for r in range(len(boardToUse)):
            print(r, end="")
            for c in range(len(boardToUse[0])):
                print(boardToUse[r][c], end="")
            print()