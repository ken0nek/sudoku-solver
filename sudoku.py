from sudoku_components import *

class Sudoku(object):
    def __init__(self):
        numbers = [
            [0, 3, 8, 0, 5, 0, 0, 0, 0],
            [9, 0, 4, 6, 0, 1, 0, 7, 2],
            [0, 0, 0, 7, 0, 8, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 5, 0, 0],
            [0, 4, 1, 9, 0, 0, 7, 0, 3],
            [8, 9, 5, 3, 7, 2, 0, 0, 6],
            [2, 8, 0, 1, 6, 0, 0, 5, 4],
            [0, 6, 7, 5, 0, 3, 9, 0, 1],
            [0, 0, 3, 8, 4, 9, 2, 6, 0]
        ]
        self.board = Board(numbers)

    def solve(self):
        print("START")

    def scan(self):
        print("SCAN")


def main():
    sudoku = Sudoku()
    sudoku.solve()

if __name__ == '__main__':
    main()