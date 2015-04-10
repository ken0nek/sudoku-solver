from termcolor import colored

def number_to_array(number):
    if number == 0:
        array = [1] * 9
    else:
        array = [0] * 9
        array[number-1] = 1
    return array

class Cell(object):

    def __init__(self, row, column, number):
        self.row = row
        self.column = column
        self.candidates = number_to_array(number)

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

    def show(self, coordinate=(-1, -1)):
        print("  ―――――――― ――――――――― ――――――――")
        for i in range(9):
            print(end="| ")
            for j in range(9):
                cell = self.cells[i][j]
                if cell.is_fixed():
                    number = str(cell.get_numbers())
                    if coordinate == (i, j):
                        number = colored(number, "red")
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

    def scan(self):
        for number in range(1,10):
            self.scan_box(number)
            self.scan_row_and_column(number)

    def scan_row_and_column(self,number):
        for r in range(9):
            possible_place_of_the_number = []
            for c in range(9):
                cell = self.cells[r][c]
                if not cell.is_fixed() and number in cell.get_numbers():
                    possible_place_of_the_number.append((r,c))
            if len(possible_place_of_the_number) == 1:
                x,y = possible_place_of_the_number[0]
                self.cells[x][y] = number_to_array(number)

        for c in range(9):
            possible_place_of_the_number = []
            for r in range(9):
                cell = self.cells[r][c]
                if not cell.is_fixed() and number in cell.get_numbers():
                    possible_place_of_the_number.append((r,c))
            if len(possible_place_of_the_number) == 1:
                x,y = possible_place_of_the_number[0]
                self.cells[x][y] = number_to_array(number)

    def scan_box(self,number):
        for r_base in [0,3,6]:
            for c_base in [0,3,6]:
                possible_place_of_the_number = []
                for r in range(r_base, r_base + 3):
                    for c in range(c_base, c_base + 3):
                        cell = self.cells[r][c]
                        if (not cell.is_fixed()) and (number in cell.get_numbers()):
                            possible_place_of_the_number.append((r,c))
                if len(possible_place_of_the_number) == 1:
                    x, y = possible_place_of_the_number[0]
                    self.cells[x][y] = number_to_array(number)

    def check(self):
        flag = 1
        count = 0
        while flag:
            flag = 0
            try:
                count += 1
                for row in range(9):
                    for column in range(9):
                        # print(row,column)
                        cell = self.cells[row][column]
                        if not cell.is_fixed():
                            pre_number = cell.get_numbers()
                            print("start check ({}, {}) -> {}".format(row+1, column+1, pre_number))
                            self.check_box(cell)

                            self.check_column(cell)

                            self.check_row(cell)

                            print("finish check ({}, {}) -> {}".format(row+1, column+1, cell.get_numbers()))
                            is_changed = pre_number != cell.get_numbers()
                            if is_changed:
                                self.show((row, column))
                                flag = 1

            except:
                self.show()
                break




    def check_box(self, cell):
        # print("start check box")

        r_base = (cell.row // 3) * 3
        c_base = (cell.column // 3) * 3
        for r in range(r_base, r_base + 3):
            for c in range(c_base, c_base + 3):
                if not (cell.row == r and cell.column == c):
                    cell_around = self.cells[r][c]
                    if cell_around.is_fixed():
                        number = cell_around.get_numbers()
                        # print("detect {}".format(number))
                        cell.candidates[number - 1] = 0
        # print("finish check box")

    def check_row(self, cell):
        # print("start check row")
        for x in range(9):
            if x != cell.column:
                cell_around = self.cells[cell.row][x]
                if cell_around.is_fixed():
                    number = cell_around.get_numbers()
                    # print("detect {}".format(number))
                    cell.candidates[number - 1] = 0
        # print("finish check row")

    def check_column(self, cell):
        # print("start check column")
        for y in range(9):
            if y != cell.row:
                cell_around = self.cells[y][cell.column]
                if cell_around.is_fixed():
                    number = cell_around.get_numbers()
                    # print("detect {}".format(number))
                    cell.candidates[number - 1] = 0
        # print("finish check column")

    def is_finished(self):
        for cell_row in self.cells:
            for cell in cell_row:
                if not cell.is_fixed():
                    return False
        return True