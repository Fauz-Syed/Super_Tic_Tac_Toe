from colorama import Fore, Style
from tabulate import tabulate

from tic_tac_toe import Game


class SmallTTT:

    def __init__(self):
        self.small_game = Game.Game()
        self.complete = False
        self.tictactoe = [[' ' for _ in range(3)] for _ in range(3)]
        self.winner = None
        self.amount_of_turns = 0
        self.X = f"{Fore.LIGHTGREEN_EX}X{Style.RESET_ALL}"
        self.O = f"{Fore.MAGENTA}O{Style.RESET_ALL}"

    def checkWinner(self):
        # Check rows
        row_done, player1 = self.checkRow()
        if row_done:
            self.winner = player1
            return True, player1

        # Check columns
        col_done, player2 = self.checkCol()
        if col_done:
            self.winner = player2
            return True, player2

        # Check diagonals
        diag_done, player3 = self.checkDiag()
        if diag_done:
            self.winner = player3
            return True, player3

        # If no winner, continue game or check for draw
        return False, None

    def checkRow(self):
        for i, row in enumerate(self.tictactoe):
            if all(x == self.X for x in self.tictactoe[i]):
                return True, self.small_game.PlayerX.symbol
            if all(x == self.O for x in self.tictactoe[i]):
                return True, self.small_game.PlayerO.symbol
        return False, None

    def checkCol(self):
        for col in range(len(self.tictactoe[0])):
            if all(self.tictactoe[row][col] == self.X for row in range(3)):
                return True, self.small_game.PlayerX.symbol
            if all(self.tictactoe[row][col] == self.O for row in range(3)):
                return True, self.small_game.PlayerO.symbol
        return False, None

    def checkDiag(self):
        # diagonal
        if all(self.tictactoe[i][i] == self.X for i in range(3)):
            return True, self.small_game.PlayerX.symbol
        if all(self.tictactoe[i][i] == self.O for i in range(3)):
            return True, self.small_game.PlayerO.symbol

        # anti-diagonal
        if all(self.tictactoe[i][2 - i] == self.X for i in range(3)):
            return True, self.small_game.PlayerX.symbol
        if all(self.tictactoe[i][2 - i] == self.O for i in range(3)):
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
        checkwin, player = self.checkWinner()
        if checkwin:
            print(f"Player {self.winner} is winner ")
            self.winner = player
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

    def board_as_string(self):
        lines = []
        for row in self.tictactoe:
            lines.append(" | ".join(row))
            lines.append("-" * 9)
        # Remove the last line of dashes
        g = "\n".join(lines[:-1])
        g += "\n" + f"Game Won by {self.winner}"
        return g

    def __str__(self):
        def center_align(data):
            max_lengths = [max(len(str(item)) for item in column) for column in zip(*data)]
            return [[str(item).center(max_lengths[idx]) for idx, item in enumerate(row)] for row in data]

        centered_data = center_align(self.tictactoe)
        table = tabulate(centered_data, tablefmt="fancy_grid")
        gameWinner = f"Game won: {self.winner}"
        return table + "\n" + gameWinner

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

    def place_player(self, player: str, one: str, two: str, three: str):
        one = self.small_game.coordinates.get(one.upper())
        x = one[0]
        y = one[1]
        self.tictactoe[x][y] = player
        two = self.small_game.coordinates.get(two.upper())
        x = two[0]
        y = two[1]
        self.tictactoe[x][y] = player
        three = self.small_game.coordinates.get(three.upper())
        x = three[0]
        y = three[1]
        self.tictactoe[x][y] = player
        if self.checkWinner():
            turn = next(self.small_game.players)
            print(f"Player {self.winner} is winner ")
            self.winner = turn
            self.complete = True

    def place_player2(self, player: str, one: str):
        one = self.small_game.coordinates.get(one.upper())
        x = one[0]
        y = one[1]
        self.tictactoe[x][y] = player
        if self.checkWinner():
            self.winner = player
            self.complete = True
            print(f"Player {self.winner} is winner ")
