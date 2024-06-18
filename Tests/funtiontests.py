from tic_tac_toe import OuterTTT
from tic_tac_toe import Game


def __init__(self):
    pass


def test_row_win_condition():
    test_game = OuterTTT.OuterTTT()
    print(test_game, "\n Testing row check with no winners")
    test_game.checkRow()
    print("\n Testing row check with winners")
    test_game.place_player("O", "tr", "bm", "bl")
    print(test_game)
    test_game.checkRow()
