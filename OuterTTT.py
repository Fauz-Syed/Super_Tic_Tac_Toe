import SmallTTT


class OuterTTT:

    def __init__(self):
        self.OTTT = [SmallTTT.SmallTTT() for _ in range(9)]
        self.turn = 1

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
    def checkTicked(self):
       pass
    def largeTTTmove(self):
        self.OTTT[0].playerMoveSMALLGAME2("tl")
    def completedSmTTT(self):
        pass

    def __str__(self):
        string = ""
        for i, content in enumerate(self.OTTT):
            string +="\n" + str(self.OTTT[i])  + f"{i}" + "\n"

        return string