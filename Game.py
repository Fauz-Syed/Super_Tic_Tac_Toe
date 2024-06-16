from itertools import cycle
import SmallTTT
import OuterTTT
import Player
class Game:

    def __init__(self):
        self.coordinates = {
            "TL": (0, 0),
            "TM": (0, 1),
            "TR": (0, 2),
            "ML": (1, 0),
            "MM": (1, 1),
            "MR": (1, 2),
            "BL": (2, 0),
            "BM": (2, 1),
            "BR": (2, 2)
        }
        self.validOptions = ["TL", "TM", "TR", "ML", "MM", "MR", "BL", "BM", "BR"]
        self.PlayerX = Player.Player("X")
        self.PlayerO = Player.Player("O")
        self.players = cycle([self.PlayerX.symbol, self.PlayerO.symbol])
        self.turn = next(self.players)
