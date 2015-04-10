from sudoku_components import *
import time


class Sudoku(object):
    def __init__(self, numbers):
        self.board = Board(numbers)

    def solve(self):
        print("START")
        count = 0
        while not self.board.is_finished():
            flag = 0
            try:
                count += 1
                for i in range(9):
                    for j in range(9):
                        if self.board.check(row=i, column=j):
                            flag = 1
                            time.sleep(0.2)
            except:
                self.board.show()
                break

            if flag == 0:
                print("After {} loops".format(count))
                print("higher")
                break
        print("FINISH")


def main():
    numbers = [
        [5, 0, 0, 2, 0, 0, 0, 0, 9],
        [0, 0, 0, 0, 0, 4, 0, 8, 0],
        [0, 9, 6, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 9, 0, 1, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 2, 0],
        [0, 3, 0, 6, 2, 0, 0, 0, 0],
        [6, 0, 0, 0, 8, 0, 0, 0, 5],
        [0, 0, 1, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 1, 0]
    ]

    # numbers = [
    #         [0, 3, 8, 0, 5, 0, 0, 0, 0],
    #         [9, 0, 4, 6, 0, 1, 0, 7, 2],
    #         [0, 0, 0, 7, 0, 8, 0, 0, 0],
    #         [0, 0, 0, 0, 1, 0, 5, 0, 0],
    #         [0, 4, 1, 9, 0, 0, 7, 0, 3],
    #         [8, 9, 5, 3, 7, 2, 0, 0, 6],
    #         [2, 8, 0, 1, 6, 0, 0, 5, 4],
    #         [0, 6, 7, 5, 0, 3, 9, 0, 1],
    #         [0, 0, 3, 8, 4, 9, 2, 6, 0]
    # ]
    sudoku = Sudoku(numbers)
    sudoku.solve()

if __name__ == '__main__':
    main()