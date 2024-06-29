import random
import time
from itertools import cycle
from tabulate import tabulate
from colorama import Fore, Style
from tic_tac_toe import Game
from tic_tac_toe import SmallTTT


class OuterTTT:

    def __init__(self):
        self.large_game = Game.Game()
        self.large_TTT = [[SmallTTT.SmallTTT() for _ in range(3)] for _ in range(3)]
        self.NumOfTurns = 0
        self.LastMove = None
        self.complete = False
        self.large_player_turn = self.large_game.turn
        self.trackM = self.large_game.track
        self.list_moves = []
        self.X = f"{Fore.LIGHTGREEN_EX}X{Style.RESET_ALL}"
        self.O = f"{Fore.MAGENTA}O{Style.RESET_ALL}"

    def checkWin(self):
        if self.checkRow() or self.checkCol() or self.checkDiag():
            return True
        return False

    def checkDraw(self):
        if self.checkRow() or self.checkCol() or self.checkDiag() and self.NumOfTurns == 80:
            return True
        return False

    def checkRow(self):
        t_list = []
        m_list = []
        b_list = []
        for i in range(3):
            for j in range(3):
                if i == 0:
                    t_list.append(self.get_small_game(i, j).winner)
                elif i == 1:
                    m_list.append(self.get_small_game(i, j).winner)
                elif i == 2:
                    b_list.append(self.get_small_game(i, j).winner)
        if all(item == self.X for item in t_list) or all(item == self.O for item in t_list):
            print(f"T is winner")
            return True
        if all(item == self.X for item in m_list) or all(item == self.O for item in m_list):
            print("M is winner")
            return True
        if all(item == self.X for item in b_list) or all(item == self.O for item in b_list):
            print("B is winner")
            return True
        return False

    def checkCol(self):
        s = self.large_TTT
        l_list = []
        m_list = []
        r_list = []
        for i in range(len(s)):
            for j in (range(len(s))):
                if i == 0:
                    l_list.append(self.get_small_game(j, i).winner)
                elif i == 1:
                    m_list.append(self.get_small_game(j, i).winner)
                elif i == 2:
                    r_list.append(self.get_small_game(j, i).winner)
        if all(item == self.X for item in l_list) or all(item == self.O for item in l_list):
            print("L is winner")
            return True
        if all(item == self.X for item in m_list) or all(item == self.O for item in m_list):
            print("M is winner")
            return True
        if all(item == self.X for item in r_list) or all(item == self.O for item in r_list):
            print("R is winner")
            return True
        return False

    def checkDiag(self):
        d_list = []
        nd_list = []
        for i in range(len(self.large_TTT)):
            d_list.append(self.get_small_game(i, i).winner)
            nd_list.append(self.get_small_game(i, 2 - i).winner)
        if all(item == self.X for item in d_list) or all(item == self.O for item in d_list):
            print("Diag is winner")
            return True
        if all(item == self.X for item in nd_list) or all(item == self.O for item in nd_list):
            print("anti-Diag is winner")
            return True
        return False

    def large_checkTicked(self):
        large_x, large_y = self.get_coord()
        if self.large_TTT[large_x][large_x].winner is None:
            return False
        return True

    def LargeMove(self):
        def format_enumerated_list(lst, num_columns):
            enumerated_list = [(i + 1, item) for i, item in enumerate(lst)]
            rows = [enumerated_list[i:i + num_columns] for i in range(0, len(enumerated_list), num_columns)]
            formatted_rows = [[f"{num}. {item}" for num, item in row] for row in rows]
            return tabulate(formatted_rows, tablefmt="grid")

        def turn_increment(large_coord: tuple):
            self.track_moves(self.trackM, large_coord, self.LastMove)
            self.NumOfTurns += 1
            self.large_player_turn = next(self.large_game.players)
            self.trackM = next(self.large_game.playersT)
            table = format_enumerated_list(self.list_moves, 5)
            print(
                f"Turns played: {self.NumOfTurns}, next Player: {self.large_player_turn},list of moves: \n{table} \n\n\n")

        def playLargeTurn():
            OutCoord = self.large_game.coordinates.get(self.chooseLocation())  # get first outer play
            playedX, playedY = OutCoord[0], OutCoord[1]  # unpack the coordinates from player choice
            SmallBoard = self.large_TTT[playedX][playedY]  # using the coord get the small game to be played
            time.sleep(2)
            InCoord = SmallBoard.player_move_large_game(self.large_player_turn)  # play the move on the small board,
            # store played coord as a tuple of coord and boolean
            self.LastMove = InCoord[0]  # store the last played move coord in small
            # game that will become next in large game
            if InCoord[1]:
                turn_increment(OutCoord)  # logistics of

        def updateWinners():
            for row in range(len(self.large_TTT)):
                for col in range(len(self.large_TTT[row])):
                    element = self.large_TTT[row][col]
                    element.checkWinner()

        updateWinners()
        if self.checkWin():
            self.large_TTT.winner = self.large_player_turn
            self.complete = True
        if self.checkDraw():
            self.complete = True
        if not self.complete:
            if self.NumOfTurns == 0:
                playLargeTurn()
            else:
                if self.large_checkTicked():
                    playLargeTurn()

                else:
                    BeforePlay = self.LastMove
                    LX, LY = self.get_coord()
                    CoordToStr = self.get_key_from_value(self.large_game.coordinates, self.LastMove)
                    print(f"Player {self.large_player_turn}, you are playing in the {CoordToStr} of the large game.")
                    InCoord = self.get_small_game(LX, LY).player_move_large_game(self.large_player_turn)
                    self.LastMove = InCoord[0]
                    if InCoord[1]:
                        turn_increment(BeforePlay)  # logistics of

    def __str__(self):
        def center_align(data):
            max_lengths = [max(len(str(item)) for item in column) for column in zip(*data)]
            return [[str(item).center(max_lengths[idx]) for idx, item in enumerate(row)] for row in data]

        centered_data = center_align(self.large_TTT)
        table = tabulate(centered_data, tablefmt="grid")
        return table

    # helper functions
    def get_coord(self):
        large_x, large_y = self.LastMove
        return large_x, large_y

    def chooseLocation(self):
        direction = str(input("Enter large location: ")).upper()
        while direction not in self.large_game.validOptions:
            print("Please enter a valid response: ")
            direction = str(input("Enter large location: ")).upper()
        return direction

    def get_key_from_value(self, dict, search_value):
        for key, value in dict.items():
            if value == search_value:
                return key
        return None  # Optional: return None if no key found

    def get_small_game(self, x, y):
        return self.large_TTT[x][y]

    def track_moves(self, player, large, small):
        string = f"{player}-O{large}-I{small}"
        self.list_moves.append(string)

    def set_rows_winner(self, player: str):
        output = ""
        for row in range(len(self.large_TTT)):
            for col in range(len(self.large_TTT[row])):
                self.large_TTT[row][col].set_winner(player)
        return output

    def place_player_L(self, player: str, one: str, two: str, three: str):
        one = self.large_game.coordinates.get(one.upper())
        x = one[0]
        y = one[1]
        self.large_TTT[x][y].set_winner(player)
        two = self.large_game.coordinates.get(two.upper())
        x = two[0]
        y = two[1]
        self.large_TTT[x][y].set_winner(player)
        three = self.large_game.coordinates.get(three.upper())
        x = three[0]
        y = three[1]
        self.large_TTT[x][y].set_winner(player)

    def print_large_game_with_data(self):
        output = ""
        game_win = ""
        for row in range(len(self.large_TTT)):
            output += f"Row {row} printed"
            for col in range(len(self.large_TTT[row])):
                element = self.large_TTT[row][col]
                if element is None:
                    pass
                else:
                    output += f"\n game {col} printed \n" + str(element) + "\n"
                    game_win += f"\nRow {row}: Col {col} - {self.large_TTT[row][col].winner}"
            output += "\n"  # Add a new line after each row
        return output + f"Game won: {game_win}"

    def print_rowcol_data(self):
        output = ""
        game_win = ""
        for row in range(len(self.large_TTT)):
            for col in range(len(self.large_TTT[row])):
                element = self.large_TTT[row][col]
                if element is None:
                    pass
                else:
                    game_win += f"\nRow {row}: Col {col} - {self.large_TTT[row][col].winner}"
            print("\n")
        return f"Game won: {game_win}"

    def choose_input_Location(self, location):
        direction = str(location).upper()
        while direction not in self.large_game.validOptions:
            print("Please enter a valid response: ")
            direction = str(input("Enter large location: ")).upper()
        return direction

    def test_player_move(self, location: str):
        if self.NumOfTurns == 0:
            # Get tuple coordinate for large board
            large_coord = self.large_game.coordinates.get(self.choose_input_Location(location))
            # Unpack the coordinate
            large_x, large_y = large_coord
            # Reference the small board game that is being played on
            small_within_large = self.large_TTT[large_x][large_y]
            # Play the move on the small board and return the coordinates as a tuple
            self.LastMove, played = small_within_large.player_move_test_game(self.large_player_turn, location)
            # Track the move
            self.turn_increment(large_coord)
        else:
            if not self.large_checkTicked():
                if not self.checkWin() or self.checkDraw():
                    before_change = self.LastMove
                    # Retrieve coordinate from the last move on the small game
                    large_x, large_y = self.get_coord()
                    # Get the string value of the coordinate and notify the player whose turn it is
                    large_game_dict = self.get_key_from_value(self.large_game.coordinates, self.LastMove)
                    print(
                        f"Player {self.large_player_turn}, you are playing in the {large_game_dict} of the large game.")
                    # Plays the turn (replaces last coordinates)
                    self.LastMove, played = self.large_TTT[large_x][large_y].player_move_test_game(
                        self.large_player_turn, location)
                    if played:
                        print(f"Location played: {location}")
                        self.turn_increment(before_change)
                    else:
                        print(f"Player {self.large_player_turn} unsuccessfully played.")
                else:
                    return True
            else:
                large_x, large_y = self.get_coord()
                print(f"Invalid move, this box belongs to {self.get_small_game(large_x, large_y).winner}.")
                self.find_unchecked()
        return False

    def find_unchecked(self):
        for i in range(3):
            for j in range(3):
                if self.get_small_game(i, j).winner is None:
                    self.LastMove = (i, j)

    def return_random_coord(self):
        t = random.choice(list(self.large_game.coordinates))
        return t

    def PlaceOneAtATimeS(self):
        inputs = self.readinputs()
        loops = int(inputs[0])
        players = inputs[1::3]
        coords = inputs[2::3]
        placement = inputs[3::3]
        game = Game.Game()
        for i in range(loops):
            try:
                player = players[i]
                print(f"{Fore.LIGHTMAGENTA_EX} //Inputting Player {player} // {Style.RESET_ALL}")
                time.sleep(2.5)
                coord = game.coordinates.get(coords[i].upper())
                print(f"{Fore.LIGHTMAGENTA_EX} //Inputting Coordinates {coord} // {Style.RESET_ALL}")
                time.sleep(2.5)
                SmallBoard = self.get_small_game(coord[0], coord[1])
                print(
                    f"{Fore.LIGHTMAGENTA_EX} //Retrieving game board at Large ({coord[0]}, {coord[1]}) // {Style.RESET_ALL}")
                time.sleep(2.5)
                SmallBoard.place_player2(player.upper(), placement[i].upper())
                print(f"{Fore.LIGHTMAGENTA_EX} //Playing move at {placement[i]} with {player} // {Style.RESET_ALL}")
                time.sleep(2.5)
                print(f"{Fore.YELLOW} ---------------------{Style.RESET_ALL}")
                print(SmallBoard)
                print(f"{Fore.YELLOW} ---------------------{Style.RESET_ALL}")
                time.sleep(3)
            except IndexError:
                print("Index Error")
                break
        print(f"{Fore.GREEN}~~~~~ PlayOneAtATimeS has been executed ~~~~~{Style.RESET_ALL}")

    def readinputs(self):
        with open('.\\Tests\\test_Place1AtATime.txt', 'r') as file:
            inputs = []
            lines = file.readlines()
            for i, line in enumerate(lines):
                if i <= 4:
                    pass
                else:
                    inputs.append(line.strip().upper())
            print(inputs)
        return inputs

    from colorama import Fore, Style

    def TESTLargeMove(self):
        def format_enumerated_list(lst, num_columns):
            enumerated_list = [(i + 1, item) for i, item in enumerate(lst)]
            rows = [enumerated_list[i:i + num_columns] for i in range(0, len(enumerated_list), num_columns)]
            formatted_rows = [[f"{num}. {item}" for num, item in row] for row in rows]
            return tabulate(formatted_rows, tablefmt="grid")

        def turn_increment(large_coord: tuple):
            print(Fore.GREEN + "Step: turn_increment" + Style.RESET_ALL)
            self.track_moves(self.trackM, large_coord, self.LastMove)
            self.NumOfTurns += 1
            self.large_player_turn = next(self.large_game.players)
            self.trackM = next(self.large_game.playersT)
            table = format_enumerated_list(self.list_moves, 5)
            print(
                f"Turns played: {self.NumOfTurns}, next Player: {self.large_player_turn},list of moves: \n{table} \n")
            updateWinners()

        def playLargeTurn():
            print(Fore.GREEN + "Step1: first turn" + Style.RESET_ALL)
            OutCoord = self.large_game.coordinates.get(self.chooseLocation())  # get first outer play
            print(Fore.GREEN + f"Step2: get first Outer turn location {OutCoord}" + Style.RESET_ALL)
            time.sleep(2)
            playedX, playedY = OutCoord[0], OutCoord[1]  # unpack the coordinates from player choice
            print(Fore.GREEN + f"Step3: unpack coords {playedX}:{playedY}" + Style.RESET_ALL)
            SmallBoard = self.large_TTT[playedX][playedY]  # using the coord get the small game to be played
            time.sleep(2)
            InCoord = SmallBoard.player_move_large_game(self.large_player_turn)  # play the move on the small board,
            # store played coord as a tuple of coord and boolean
            print(Fore.GREEN + f"Step4: Play in small board {InCoord}" + Style.RESET_ALL)
            self.LastMove = InCoord[0]  # store the last played move coord in small
            # game that will become next in large game
            print(Fore.LIGHTRED_EX + f"Step5: Check if turn has been played: {InCoord[1]}" + Style.RESET_ALL)
            if InCoord[1]:
                print(Fore.GREEN + f"Step6: turn has been played" + Style.RESET_ALL)
                turn_increment(OutCoord)  # logistics of

        def updateWinners():
            for row in range(len(self.large_TTT)):
                for col in range(len(self.large_TTT[row])):
                    element = self.large_TTT[row][col]
                    element.checkWinner()

        if self.checkWin():
            print(Fore.GREEN + "Step: checkWin" + Style.RESET_ALL)
            self.large_TTT.winner = self.large_player_turn
            self.complete = True
            print(f"THE GAME IS OVER: The game has been won by: {self.large_player_turn}. func:LargeMove")
        if self.checkDraw():
            print(Fore.GREEN + "Step: checkDraw" + Style.RESET_ALL)
            self.complete = True
            print("The game has ended in a Draw. func:LargeMove")
        if not self.complete:
            if self.NumOfTurns == 0:
                playLargeTurn()
            else:
                print(Fore.GREEN + f"Step: Check if OuterTTT is ticked" + Style.RESET_ALL)
                if self.large_checkTicked():
                    print(Fore.LIGHTRED_EX + "Step: large_checkTicked" + Style.RESET_ALL)
                    print("This outer tictactoe has been played. func:LargeMove")
                    playLargeTurn()

                else:
                    BeforePlay = self.LastMove
                    LX, LY = self.get_coord()
                    CoordToStr = self.get_key_from_value(self.large_game.coordinates, self.LastMove)
                    print(Fore.GREEN + f"Step1: get Sting Coordinates:  {CoordToStr}" + Style.RESET_ALL)
                    print(f"Player {self.large_player_turn}, you are playing in the {CoordToStr} of the large game.")
                    InCoord = self.get_small_game(LX, LY).player_move_large_game(self.large_player_turn)
                    self.LastMove = InCoord[0]
                    print(Fore.LIGHTRED_EX + f"Step2: Check if turn has been played: {InCoord[1]}" + Style.RESET_ALL)
                    if InCoord[1]:
                        print(Fore.GREEN + f"Step3: turn has been played" + Style.RESET_ALL)
                        turn_increment(BeforePlay)  # logistics of
