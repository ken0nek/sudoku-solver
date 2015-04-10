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

    def is_finished(self):
        for i in range(9):
            for j in range(9):


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
                        print("detect")
        print("finish check box")

    def check_row(self, cell):
        print("start check row")
        if not cell.is_fixed:
            for x in range(9):
                if x != cell.column:
                    print("detect")
                    # if let number = self.mat[cell.row][x].number {
                    #     println("detect : \(number)")
                    #     cell.candidates[number - 1] = 0
        print("finish check row")

    def check_column(self, cell):
        print("start check column")
        if not cell.is_fixed:
            for y in range(9):
                if y != cell.row:
                    print("detect")

        print("finish check column")