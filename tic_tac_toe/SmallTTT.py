from tic_tac_toe import Game


class SmallTTT:

    def __init__(self):
        self.small_game = Game.Game()
        self.complete = False
        self.tictactoe = [[' ' for _ in range(3)] for _ in range(3)]
        self.winner = None
        self.amount_of_turns = 0

    def checkWinner(self):
        # Check rows
        row_done, player = self.checkRow()
        if row_done:
            self.winner = player
            print("Won by row", f"{self.winner}")
            return True

        # Check columns
        col_done, player = self.checkCol()
        if col_done:
            self.winner = player
            print("Won by column", f"{self.winner}")
            return True

        # Check diagonals
        diag_done, player = self.checkDiag()
        if diag_done:
            self.winner = player
            print("Won by diagonal", f"{self.winner}")
            return True

        # If no winner, continue game or check for draw
        return False

    def checkRow(self):
        for i, row in enumerate(self.tictactoe):
            if all(x == 'X' for x in self.tictactoe[i]):
                return True, self.small_game.PlayerX.symbol
            if all(x == 'O' for x in self.tictactoe[i]):
                return True, self.small_game.PlayerO.symbol
        return False, None

    def checkCol(self):
        for col in range(len(self.tictactoe[0])):
            if all(self.tictactoe[row][col] == 'X' for row in range(3)):
                return True, self.small_game.PlayerX.symbol
            if all(self.tictactoe[row][col] == 'O' for row in range(3)):
                return True, self.small_game.PlayerO.symbol
        return False, None

    def checkDiag(self):
        # diagonal
        if all(self.tictactoe[i][i] == 'X' for i in range(3)):
            return True, self.small_game.PlayerX.symbol
        if all(self.tictactoe[i][i] == 'O' for i in range(3)):
            return True, self.small_game.PlayerO.symbol

        # anti-diagonal
        if all(self.tictactoe[i][2 - i] == 'X' for i in range(3)):
            return True, self.small_game.PlayerX.symbol
        if all(self.tictactoe[i][2 - i] == 'O' for i in range(3)):
            return True, self.small_game.PlayerO.symbol
        return False, None

    def checkTicked(self, row, col):
        if self.tictactoe[row][col] == ' ':
            return False
        return True

    def chooseLocation(self, direction):
        while direction not in self.small_game.validOptions:
            print("Please enter a valid response: ")
            direction = str(input("Enter small location: ")).upper()
        return direction

    def playerMoveSMALLGAME(self):
        if self.checkWinner():
            turn = next(self.small_game.players)
            print(f"Player {self.winner} is winner ")
            self.winner = turn
            self.complete = True
        else:
            direction = self.chooseLocation(str(input("Enter small location: ")).upper())
            coord = self.small_game.coordinates.get(direction)
            x = coord[0]
            y = coord[1]
            if not self.checkTicked(x, y):
                self.tictactoe[x][y] = self.small_game.turn
                self.amount_of_turns += 1
                self.small_game.turn = next(self.small_game.players)
                return coord
            else:
                print("You already placed a tictactoe")

    def player_move_large_game(self, player_turn):
        if self.checkWinner():
            turn = next(self.small_game.players)
            print(f"Player {self.winner} is winner ")
            self.winner = turn
            self.complete = True
        direction = self.chooseLocation(str(input("Enter small location: ")).upper())
        coord = self.small_game.coordinates.get(direction)
        x = coord[0]
        y = coord[1]
        if not self.checkTicked(x, y):
            self.tictactoe[x][y] = player_turn
            self.amount_of_turns += 1
            return coord, True
        else:
            print("You already placed a tictactoe")
            return coord, False

    def printMap(self):
        return str(self.small_game.coordinates)

    def __str__(self):
        row1 = "0 ", self.tictactoe[0]
        row2 = "1 ", self.tictactoe[1]
        row3 = "2 ", self.tictactoe[2]
        winner = self.winner
        tic = str(row1) + "\n" + str(row2) + "\n" + str(row3) + "\n Winner: " + str(winner)
        return tic
    def set_winner(self, player: str):
        self.winner = player

    def player_move_test_game(self, player_turn, input):
        if self.checkWinner():
            self.winner = next(self.small_game.players)
            print(f"Player {self.winner} is winner ")
            self.complete = True
        direction = self.chooseLocation(str(input).upper())
        coord = self.small_game.coordinates.get(direction)
        x = coord[0]
        y = coord[1]
        if not self.checkTicked(x, y):
            self.tictactoe[x][y] = player_turn
            self.amount_of_turns += 1
            return coord, True
        else:
            print("You already placed a tictactoe")
            return coord, False



















