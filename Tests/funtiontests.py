from tic_tac_toe import OuterTTT


def test_row_check():
    test_game = OuterTTT.OuterTTT()
    print(test_game + "\n Testing row check with no winners")
    test_game.checkRow()
