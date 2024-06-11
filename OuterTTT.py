import SmallTTT


class OuterTTT:

    def __init__(self):
        self.tictac = SmallTTT.SmallTTT()
        self.board = [[self.tictac.tictactoe for _ in range(3)] for _ in range(3)]

    def __str__(self):
        for i, content in enumerate(self.board):
            print(str(self.board[i]) + "\n")
