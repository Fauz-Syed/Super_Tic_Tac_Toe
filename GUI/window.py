import tkinter as tk
from tkinter import messagebox
import random
import time
from itertools import cycle
from tabulate import tabulate
from colorama import Fore, Style


# Assuming Game and SmallTTT are correctly imported from tic_tac_toe module
# from tic_tac_toe import Game, SmallTTT

class UltimateTicTacToeApp:
	def __init__(self, root):
		self.root = root
		self.root.title("Ultimate Tic-Tac-Toe")


if __name__ == "__main__":
	root = tk.Tk()
	app = UltimateTicTacToeApp(root)
	root.mainloop()
