from tic_tac_toe import Game
from tic_tac_toe import SmallTTT


class OuterTTT:

    def __init__(self):
        self.large_game = Game.Game()
        self.large_TTT = [[SmallTTT.SmallTTT() for _ in range(3)] for _ in range(3)]
        self.turn = 0
        self.large_last_move = None
        self.complete = False
        self.large_player_turn = self.large_game.turn
        self.list_moves = []

    def checkWin(self):
        pass

    def checkDraw(self):
        pass

    def checkRow(self):
        s = self.large_TTT
        t_list = []
        m_list = []
        b_list = []
        for i in range(len(s)):
            for j in (range(len(s))):
                if i == 0:
                    t_list.append(self.get_small_game(i, j).winner)
                elif i == 1:
                    m_list.append(self.get_small_game(i, j).winner)
                elif i == 2:
                    b_list.append(self.get_small_game(i, j).winner)
        if all(item == "X" for item in t_list) or all(item == "O" for item in t_list):
            print("T is winner")
            return True
        if all(item == "X" for item in m_list) or all(item == "O" for item in m_list):
            print("M is winner")
            return True
        if all(item == "X" for item in b_list) or all(item == "O" for item in b_list):
            print("B is winner")
            return True
        return False

    def checkCol(self):
        s = self.large_TTT
        t_list = []
        m_list = []
        b_list = []
        for i in range(len(s)):
            for j in (range(len(s))):
                if i == 0:
                    t_list.append(self.get_small_game(j, i).winner)
                elif i == 1:
                    m_list.append(self.get_small_game(j, i).winner)
                elif i == 2:
                    b_list.append(self.get_small_game(j, i).winner)
        if all(item == "X" for item in t_list) or all(item == "O" for item in t_list):
            print("T is winner")
            return True
        if all(item == "X" for item in m_list) or all(item == "O" for item in m_list):
            print("M is winner")
            return True
        if all(item == "X" for item in b_list) or all(item == "O" for item in b_list):
            print("B is winner")
            return True
        return False

    def checkDiag(self):
        pass

    def large_checkTicked(self):
        large_x, large_y = self.get_coord()
        if self.large_TTT[large_x][large_x].winner is None:
            return False
        return True

    def large_game_move(self):
        if self.turn == 0:
            # Get tuple coordinate for large board
            large_coord = self.large_game.coordinates.get(self.chooseLocation())
            # Unpack the coordinate
            large_x, large_y = large_coord
            # Reference the small board game that is being played on
            small_within_large = self.large_TTT[large_x][large_y]
            # Play the move on the small board and return the coordinates as a tuple
            self.large_last_move, played = small_within_large.player_move_large_game(self.large_player_turn)
            # Track the move
            self.turn_increment(large_coord)
        else:
            if not self.large_checkTicked():
                before_change = self.large_last_move
                # Retrieve coordinate from the last move on the small game
                large_x, large_y = self.get_coord()
                # Get the string value of the coordinate and notify the player whose turn it is
                large_game_dict = self.get_key_from_value(self.large_game.coordinates, self.large_last_move)
                print(f"Player {self.large_player_turn}, you are playing in the {large_game_dict} of the large game.")
                # Plays the turn (replaces last coordinates)
                self.large_last_move, played = self.large_TTT[large_x][large_y].player_move_large_game(
                    self.large_player_turn)
                if played:
                    self.turn_increment(before_change)
                else:
                    print(f"Player {self.large_player_turn} unsuccessfully played.")
            else:
                large_x, large_y = self.get_coord()
                print(f"Invalid move, this box belongs to {self.get_small_game(large_x, large_y).winner}.")

    def __str__(self):
        output = ""
        for row in range(len(self.large_TTT)):
            output += f"Row {row} printed"
            for col in range(len(self.large_TTT[row])):
                element = self.large_TTT[row][col]
                if element is None:
                    pass
                else:
                    output += f"\n game {col} printed \n" + str(element) + "\n"
            output += "\n"  # Add a new line after each row
        return output

    # helper functions
    def get_coord(self):
        large_x, large_y = self.large_last_move
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
        string = f"{player}-{large}-{small}"
        self.list_moves.append(string)

    def turn_increment(self, large_coord):
        self.track_moves(self.large_player_turn, large_coord, self.large_last_move)
        self.turn += 1
        self.large_player_turn = next(self.large_game.players)
        print(
            f"Turns played: {self.turn}, next Player: {self.large_player_turn},list of moves: {self.list_moves} \n\n\n")

    def set_rows_winner(self, player: str):
        output = ""
        for row in range(len(self.large_TTT)):
            for col in range(len(self.large_TTT[row])):
                self.large_TTT[row][col].set_winner(player)
        return output

    def place_player(self, player: str, one: str, two: str, three: str):
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

    def get_small_game(self, x, y):
        return self.large_TTT[x][y]

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