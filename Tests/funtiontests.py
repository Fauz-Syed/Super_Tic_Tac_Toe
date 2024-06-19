import time

import keyboard

from tic_tac_toe import OuterTTT
from tic_tac_toe import Game


def __init__(self):
    pass


def test_row_win_condition():
    test_game = OuterTTT.OuterTTT()

    print(test_game, "\n Testing row check with no winners \n -------------------------------------------")
    test_game.checkRow()
    print("\n Testing row check with winners\n -----------------------------------------------------------")
    test_game.place_player("O", "br", "bm", "bl")
    print(test_game.print_large_game_with_data())
    test_game.checkRow()


def test_column_win_condition():
    test_game = OuterTTT.OuterTTT()
    print(test_game.print_rowcol_data(), "\n Testing column check with no winners "
                                         "\n -------------------------------------------")
    test_game.checkCol()
    test_game.place_player("O", "tl", "mr", "br")
    test_game.checkCol()
    print(test_game.print_rowcol_data(), "\n Testing column check with winners  "
                                         "\n -------------------------------------------")


def test_diagonal_win_condition():
    test_game = OuterTTT.OuterTTT()
    print(test_game.print_rowcol_data(), "\n Testing diag check with no winners "
                                         "\n -------------------------------------------")
    test_game.checkDiag()
    test_game.place_player("O", "tr", "mm", "bl")
    test_game.checkDiag()
    print(test_game.print_rowcol_data(), "\n Testing diag check with winners  "
                                         "\n -------------------------------------------")


def play_random():
    test_game = OuterTTT.OuterTTT()
    counter = 0
    f = 3
    s = 10
    m = 5
    while True:
        if keyboard.is_pressed("f"):
            f = .2
        if keyboard.is_pressed("m"):
            f = 3
        if keyboard.is_pressed("s"):
            f = 15
        if keyboard.is_pressed("p"):
            print(test_game)
        if keyboard.is_pressed("i"):
            print(test_game.print_large_game_with_data())

        location = test_game.return_random_coord()
        test_game.test_player_move(location)
        print(counter, "\n")
        counter += 1
        time.sleep(f)
