# This is a sample Python script.
from Tests import funtiontests
from tic_tac_toe import OuterTTT, SmallTTT
from tic_tac_toe import Game

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


ttt = SmallTTT.SmallTTT()
large_game = OuterTTT.OuterTTT()


def runGame():
    which_game = input("Which game do you want to play, 1: small or 2: large: ")
    if which_game == "1":
        while not ttt.complete:
            ttt.playerMoveSMALLGAME()
            print(ttt)

    if which_game == "2":
        if input("test? press t"):
            large_game.set_rows_winner()
            print(large_game)
            large_game.checkRow()
        while large_game.turn < 81:
            large_game.large_game_move()
            print(large_game)


runGame()

#test = funtiontests
#test.test_row_win_condition()
# test.test_column_win_condition()
# test.test_diagonal_win_condition()
#test.play_random()
