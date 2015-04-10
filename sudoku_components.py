
class Cell(object):

    def __init__(self, row, column, number):
        self.row = row
        self.column = column
        if number == 0:
            self.candidates = [1] * 9
        else:
            self.candidates = [0] * 9
            self.candidates[number-1] = 1

    def number_of_candidates(self):
        return sum(self.candidates)

    def is_fixed(self):
        return self.number_of_candidates() == 1

    def get_numbers(self):
        possible_number = []
        for index, n in enumerate(self.candidates):
            if n:
                possible_number.append(index+1)
        return possible_number


class Board(object):
    def __init__(self, numbers):
        self.cells = [[]]
        for row in numbers:
            for column in row:





    def show(self):
        print("")

    def check_row(self):

    def check(self):