class Cell(object):

    def __init__(self, row, column):
        self.row = row
        self.column = column


class Board(object):
    def __init__(self, numbers):
        self.numbers = numbers

    def show(self):
        print("")

