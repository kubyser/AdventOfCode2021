from copy import deepcopy

class Bingo:

    MARKED = "MARKED"
    WON = "WON"

    def __init__(self, data):
        self.__numbers = data[0].split(",")
        self.__boards = []
        self.__boardsMarked = []
        line = 0
        for s in data[1:]:
            if s == "":
                self.__boards.append({})
                line = 0
            else:
                pos = 0
                for n in s.split():
                    self.__boards[len(self.__boards) - 1][n] = {"pos": [pos, line], self.MARKED: False}
                    pos += 1
                line += 1
        self.__dimensions = [len(data[2].split()), line]
        zeroes = []
        for d in self.__dimensions:
            zeroes.append([0] * d)
        for b in self.__boards:
            b[self.MARKED] = deepcopy(zeroes)
            b[self.WON] = False

    def printBoard(self):
        print("Numbers: ", self.__numbers)
        print("Boards: ", len(self.__boards))
        for b in self.__boards:
            print(b)
            print("------")
#        print("Marks:")
#        print(self.__boardsMarked)

    def calculateResult(self, board, number):
        s = 0
        for x in board:
            if x != self.MARKED and x != self.WON:
                if not board[x][self.MARKED]:
                    s += int(x)
        return s * int(number)


    def markNumber(self, number, loserWins):
        for b in self.__boards:
            if number in b:
                if not b[number][self.MARKED]:
                    b[number][self.MARKED] = True
                    for p in range(len(b[number]["pos"])):
                        b[self.MARKED][p][b[number]["pos"][p]] += 1
                        if b[self.MARKED][p][b[number]["pos"][p]] == self.__dimensions[p]:
                            b[self.WON] = True
                            s = sum(map(lambda x: x[self.WON], self.__boards))
                            if not loserWins or s == len(self.__boards):
                                return b
        return None

    def playBingo(self, loserWins):
        for n in self.__numbers:
            res = self.markNumber(n, loserWins)
            if res != None:
                return self.calculateResult(res, n)
        return None








