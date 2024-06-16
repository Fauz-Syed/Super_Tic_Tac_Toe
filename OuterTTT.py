import Game
import SmallTTT


class OuterTTT:

    def __init__(self):
        self.large_game = Game.Game()
        self.OTTT = [[SmallTTT.SmallTTT() for _ in range(3)] for _ in range(3)]
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
        pass

    def checkCol(self):
        pass

    def checkDiag(self):
        pass

    def large_checkTicked(self):
        large_x, large_y = self.get_coord()
        if self.OTTT[large_x][large_x].winner is None:
            return False
        return True

    def large_game_move(self):
        if self.turn == 0:
            # tuple coord for large board
            large_coord = self.large_game.coordinates.get(self.chooseLocation())
            # unpacks single coord
            large_x, large_y = large_coord[0], large_coord[1]
            # small board game that is being played on
            small_within_large = self.OTTT[large_x][large_y]
            # plays the move on the small board and returns the coordinates as tuple
            self.large_last_move, played = small_within_large.player_move_large_game(self.large_player_turn)
            # tracks moves
            self.turn_increment(large_coord)
        # after first move
        else:
            if not self.large_checkTicked():
                before_change = self.large_last_move
                # gets coord from last move small game
                large_x, large_y = self.get_coord()
                # gets the string value of the coordinate and notifies player whose turn it is
                large_game_dict = self.get_key_from_value(self.large_game.coordinates, self.large_last_move)
                print(f"Player {self.large_player_turn}, you are playing in the {large_game_dict} of the large game")
                # plays the turn (replaces last coordinates)
                self.large_last_move, played = self.OTTT[large_x][large_y].player_move_large_game(
                    self.large_player_turn)
                if played:
                    self.turn_increment(before_change)
                else:
                    print(f"Player {self.large_player_turn} unsuccessfully played")
                # after checked ticked
            else:
                large_x, large_y = self.get_coord()
                print(f"invalid move, this box belongs to {self.get_small_game(large_x, large_y).winner}")

    def __str__(self):
        output = ""
        for row in range(len(self.OTTT)):
            output += f"Row {row} printed"
            for col in range(len(self.OTTT[row])):
                element = self.OTTT[row][col]
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
        return self.OTTT[x][y]

    def track_moves(self, player, large, small):
        string = f"{player}-{large}-{small}"
        self.list_moves.append(string)

    def turn_increment(self, large_coord):
        self.track_moves(self.large_player_turn, large_coord, self.large_last_move)
        self.turn += 1
        self.large_player_turn = next(self.large_game.players)
        print(
            f"Turns played: {self.turn}, next Player: {self.large_player_turn}, "
            f"list of moves: {self.list_moves} \n\n\n")
