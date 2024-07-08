import tkinter as tk


class SuperTicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Super Tic Tac Toe")
        self.create_main_board()

    def create_main_board(self):
        self.main_board = []
        for i in range(3):
            row = []
            for j in range(3):
                frame = tk.Frame(self.root, width=200, height=200, highlightbackground="#4B0082", highlightthickness=2)  # Dark purple color
                frame.grid(row=i, column=j)
                small_board = SmallTicTacToe(frame)
                row.append(small_board)
            self.main_board.append(row)


class SmallTicTacToe:
    def __init__(self, frame):
        self.frame = frame
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.frame, width=6, height=3, highlightbackground="black", highlightthickness=1, bg="")
                button.grid(row=i, column=j, padx=1, pady=1)


if __name__ == "__main__":
    root = tk.Tk()
    app = SuperTicTacToe(root)
    root.mainloop()