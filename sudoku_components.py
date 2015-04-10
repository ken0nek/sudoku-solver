
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
                cells.append(Cell(i, j, numbers[i][j]))
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

    def check(self, row, column):
        cell = self.cells[row][column]
        pre_candidates = cell.candidates
        print("start check {}, {}, {}", row, column, pre_candidates)

        self.check_box(cell)

        self.check_column(cell)

        self.check_row(cell)

        post_candidates = cell.candidates
        print("finish check {}, {}, {}", row, column, post_candidates)

        self.show()

    def check_box(self, cell):
        print("start check box")
        if not cell.is_fixed:
            r_base = (cell.row / 3) * 3
            c_base = (cell.column / 3) * 3
            for r in range(r_base, r_base + 3):
                for c in range(c_base, c_base + 3):
                    if cell.row != r and cell.column != c:
                        cell_around = self.cells[r][c]
                        if cell_around.is_fixed:
                            number = cell_around.get_numbers()
                            print("detect {}".format(number))
                            cell.candidates[number - 1] = 0
        print("finish check box")

    def check_row(self, cell):
        print("start check row")
        if not cell.is_fixed:
            for x in range(9):
                if x != cell.column:
                    cell_around = self.cells[cell.row][x]
                    if cell_around.is_fixed:
                        number = cell_around.get_numbers()
                        print("detect {}".format(number))
                        cell.candidates[number - 1] = 0
        print("finish check row")

    def check_column(self, cell):
        print("start check column")
        if not cell.is_fixed:
            for y in range(9):
                if y != cell.row:
                    cell_around = self.cells[y][cell.column]
                    if cell_around.is_fixed:
                        number = cell_around.get_numbers()
                        print("detect {}".format(number))
                        cell.candidates[number - 1] = 0
        print("finish check column")
