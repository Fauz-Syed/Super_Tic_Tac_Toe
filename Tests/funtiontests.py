import unittest
from unittest.mock import patch

from tic_tac_toe.OuterTTT import OuterTTT


def random_cycle(choices):
    while True:
        yield random.choice(choices)


def readinputs():
    with open("C:\\Users\\fauzs\\OneDrive\\Desktop\\Codes\\PyCharm Projects\\SuperTTT\\Tests\\test_Place1AtATime.txt", 'r') as file:
        inputs = []
        lines = file.readlines()
        for i, line in enumerate(lines):
            if i <= 4:
                pass
            else:
                inputs.append(line.strip().upper())
        print(inputs)
    return inputs


class TestLargeMove(unittest.TestCase):
    testcase1 = readinputs()
    print(testcase1)
    random_cycle(["TL", "TM", "TR", "ML", "MM", "MR", "BL", "BM", "BR"])

    def setUp(self):
        # Set up your test environment here, e.g., initialize the class containing LargeMove
        self.game_instance = OuterTTT()

    @patch('builtins.input', side_effect=testcase1)
    def test_LargeMove(self, mock_input):
        # Here you can simulate different states of the game and call LargeMove
        i = 0

        while not self.game_instance.complete:
            self.game_instance.TESTLargeMove()
            # Add assertions to verify the expected behavior
            print(self.game_instance, "\n", self.game_instance.print_rowcol_data())

            i += 1
        return self.game_instance, "\n", self.game_instance.print_rowcol_data()


if __name__ == '__main__':
    print(unittest.main())
