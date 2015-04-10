
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
        possible_numbers = []
        for index, n in enumerate(self.candidates):
            if n:
                possible_numbers.append(index+1)
        if self.is_fixed():
            return possible_numbers[0]
        else:
            return possible_numbers


class Board(object):
    def __init__(self, numbers):
        self.cells = []
        for i in range(9):
            cells = []
            for j in range(9):
                cells.append(Cell(i,j,numbers[i][j]))
            self.cells.append(cells)

    def show(self):
        print("  ―――――――― ――――――――― ――――――――")
        for i in range(9):
            print(end="| ")
            for j in range(9):
                cell = self.cells[i][j]
                if cell.is_fixed():
                    number = cell.get_numbers()

                else:
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

