class Cell(object):

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.candidates = [1] * 9


class Board(object):
    def __init__(self, numbers):
        self.cells = [[]]

    def show(self):
        print("  ―――――――― ――――――――― ――――――――")
        for i in range(9):
            print(end="| ")
            for j in range(9):
                number = self.numbers[i][j]
                if number == 0:
                    number = "-"
                if j == 2 or j == 5:
                    print(number, end=" | ")
                else:
                    if j == 8:
                        print(number, end="")
                    else:
                        print(number, end="  ")
            if i == 2 or i == 5:
                print(end=" |\n")
                print("| ―――――――― ――――――――― ―――――――― |")
            else:
                print(end=" |\n")
        print("  ―――――――― ――――――――― ――――――――  ")