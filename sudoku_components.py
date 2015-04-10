from termcolor import colored
import time

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

    def put(self,number):
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

        self.not_fixed = {}
        self.start = time.time()

    def show_possible(self):
        for row in range(9):
            for column in range(9):
                if not self.cells[row][column].is_fixed():
                    print("({}, {}) -> {}".format(row+1, column+1, self.cells[row][column].get_numbers()))

    def set_not_fixed(self):
        for row in range(9):
            for column in range(9):
               if not self.cells[row][column].is_fixed():
                   self.not_fixed[(row,column)] = self.cells[row][column].candidates

    def next_coordinate(self):
        for row in range(9):
            for column in range(9):
                cell = self.cells[row][column]
                if not cell.is_fixed():
                    return row,column
        return None,None

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

    def count_fixed(self):
        count = 0
        for row in range(9):
            for column in range(9):
                if self.cells[row][column].is_fixed():
                    count += 1
        return count

    def scan(self):
        flag = False
        for number in range(1,10):
            for r in range(9):
                possible_place_of_the_number = []
                for c in range(9):
                    cell = self.cells[r][c]
                    if not cell.is_fixed() and number in cell.get_numbers():
                        possible_place_of_the_number.append((r,c))
                if len(possible_place_of_the_number) == 1:
                    x,y = possible_place_of_the_number[0]
                    print(number,'row','(',x+1,y+1,')')
                    self.cells[x][y].candidates = number_to_array(number)
                    self.show((x, y))
                    flag = True
                    return True

            for c in range(9):
                possible_place_of_the_number = []
                for r in range(9):
                    cell = self.cells[r][c]
                    if not cell.is_fixed() and number in cell.get_numbers():
                        possible_place_of_the_number.append((r,c))
                if len(possible_place_of_the_number) == 1:
                    x,y = possible_place_of_the_number[0]
                    print(number,'column','(',x+1,y+1,')')
                    self.cells[x][y].candidates = number_to_array(number)
                    self.show((x, y))
                    flag = True
                    return True

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
                        print(number,'box','(',x+1,y+1,')')
                        self.cells[x][y].candidates = number_to_array(number)
                        self.show((x, y))
                        flag = True
                        return True
        return False

    def check(self):
        flag = True
        count = 0
        while flag:
            flag = False
            count += 1
            for row in range(9):
                for column in range(9):
                    # print(row,column)
                    cell = self.cells[row][column]
                    if not cell.is_fixed():
                        pre_number = cell.get_numbers()
                        pre_count = self.count_fixed()
                        self.check_box(cell)

                        self.check_column(cell)

                        self.check_row(cell)

                        is_changed = pre_number != cell.get_numbers()
                        post_count = self.count_fixed()
                        if is_changed:
                            print("start check ({}, {}) -> {}".format(row+1, column+1, pre_number))
                            print("finish check ({}, {}) -> {}".format(row+1, column+1, cell.get_numbers()))
                            flag = True
                            if post_count != pre_count:
                                self.show((row, column))

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

    def is_valid(self,row,column,number):

        r_base = (row // 3) * 3
        c_base = (column // 3) * 3
        for r in range(r_base, r_base + 3):
            for c in range(c_base, c_base + 3):
                if self.cells[r][c].is_fixed:
                    if number == self.cells[r][c].get_numbers():
                        return False
        r = row
        for c in range(9):
             if self.cells[r][c].is_fixed:
                    if number == self.cells[r][c].get_numbers():
                        return False
        c = column
        for r in range(9):
             if self.cells[r][c].is_fixed:
                    if number == self.cells[r][c].get_numbers():
                        return False
        return True

    def depth_first_search(self):
        x,y = self.next_coordinate()
        if (x,y) == (None,None):
            print(time.time() - self.start)
            exit()
            # return

        # time.sleep(1)
        for n in self.cells[x][y].get_numbers():
            if self.is_valid(x,y,n):
                self.cells[x][y].put(n)
                self.show((x,y))
                self.depth_first_search()
                self.cells[x][y].candidates = self.not_fixed[(x,y)]

        return

    def is_finished(self):
        for cell_row in self.cells:
            for cell in cell_row:
                if not cell.is_fixed():
                    return False
        return True
