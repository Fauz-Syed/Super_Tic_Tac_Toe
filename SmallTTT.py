import random
import Player
from itertools import cycle
import Game


class SmallTTT:

    def __init__(self):
        self.game = Game.Game()
        self.complete = False
        self.tictactoe = [[' ' for _ in range(3)] for _ in range(3)]
        self.winner = None


    def checkWinner(self):
        if self.checkRow():
            print("Won by row")
            return True
        if self.checkCol():
            print("Won by col")
            return True
        if self.checkDiag():
            print("Won by diag")
            return True

    def checkRow(self):
        for i, row in enumerate(self.tictactoe):
            if all(x == 'X' for x in self.tictactoe[i]):
                return True
            if all(x == 'O' for x in self.tictactoe[i]):
                return True

    def checkCol(self):
        for col in range(len(self.tictactoe[0])):
            if all(self.tictactoe[row][col] == 'X' for row in range(3)):
                return True
            if all(self.tictactoe[row][col] == 'O' for row in range(3)):
                return True
        return False

    def checkDiag(self):
        #diagonal
        if all(self.tictactoe[i][i] == 'X' for i in range(3)):
            return True
        if all(self.tictactoe[i][i] == 'O' for i in range(3)):
            return True


        #anti-diagonal
        if all(self.tictactoe[i][2-i] == 'X' for i in range(3)):
            return True
        if all(self.tictactoe[i][2-i] == 'O' for i in range(3)):
            return True

    def checkTicked(self, row, col):
        if self.tictactoe[row][col] == ' ':
            return False
        return True

    def chooseLocation(self, direction):
        while direction not in self.game.validOptions:
            print("Please enter a valid response: ")
            direction = str(input("Enter location: ")).upper()
        return direction

    def playerMoveSMALLGAME(self):
        if self.checkWinner():
            self.turn = next(self.game.players)
            print(f"Player {self.turn} is winner ")
            self.winner = self.turn
        else:
            direction = self.chooseLocation(str(input("Enter location: ")).upper())
            coord = self.game.coordinates.get(direction)
            x = coord[0]
            y = coord[1]
            if not self.checkTicked(x, y):
                self.tictactoe[x][y] = self.game.turn
                self.game.turn = next(self.game.players)
                print(self)
                return True
            else:
                print("You already placed a tictactoe")
                return True




    def printMap(self):
        return str(self.game.coordinates)

    def __str__(self):
        row1 = self.tictactoe[0]
        row2 = self.tictactoe[1]
        row3 = self.tictactoe[2]
        tic = str(row1) + "\n" + str(row2) + "\n" + str(row3)
        return tic
