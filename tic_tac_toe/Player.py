from symtable import Symbol

from colorama import Fore, Style


class Player:

    def __init__(self, symbol, track):
        self.symbol = symbol
        self.track = track


    def __str__(self):
        return self.symbol