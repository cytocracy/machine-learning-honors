from computerHelper import *

class Battleship:
    def __init__(self):
        self.board = initializeGameBoard()
        self.firedAt = []
        self.ships = self.getShipDictionary()

    def getShipDictionary(self):
        '''
        Returns a dictionary mapping ship types to the
        coordinates they are placed in on self.board.
        Make sure "~" is not added to the dictionary since 
        it's not a ship!
        '''
        return {}

    def getNumShipsRemaining(self):
        '''
        Returns the number of ships that are still afloat 
        (i.e. ships that still have >0 coordinates remaining
        in self.ships)
        '''
        return 0

    def getLocationsFiredAt(self):
        '''
        Returns the list of locations that have already been
        fired at.
        '''
        return []

    def makeMove(self, row, col):
        '''
        Returns True if the shot hit a ship, and False otherwise.
        If a shot was fired at a place it has been fired at previously,
        should also return False

        Updates self.firedAt when a new location has been targeted.
        Updates self.ships to remove a coordinate of a ship 
        if one has been hit.
        '''
        return False

    def makeHiddenBoard(self):
        '''
        Returns the "visible" version of the board based on these
        rules:
        * A location that hasn't been fired on should be water ("~")
        * A location that has been fired on and is a miss (no ship)
          should be blank (" ")
        * A location that has been fired on but is not a complete
          wrecked ship should be an asterisk ("*")
        * And lastly, a location that has been fired on where the ship
          is completely sunk should be the letter corresponding to that 
          ship (either "C", "B", "D", "S", or "P")
        '''
        return self.board

    def printBoard(self, hidden): 
        '''
        Prints a version of the board to the terminal.
        Parameter hidden is a boolean, set to true if ships that 
        have not been hit on the board yet should remain hidden,
        false otherwise
        '''
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
    
    

