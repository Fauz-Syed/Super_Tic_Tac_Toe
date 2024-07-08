import tkinter as tk
from tic_tac_toe import SmallTTT as ST


# Assuming Game and SmallTTT are correctly imported from tic_tac_toe module
# from tic_tac_toe import Game, SmallTTT

class TicTacToeFinalEdit:
	def __init__(self):
		self.__root = tk.Tk()


	def RunApp(self):
		self.__root.mainloop()


class TicTacToeGame:
	TTT = TicTacToeFinalEdit()
	TTT.RunApp()
