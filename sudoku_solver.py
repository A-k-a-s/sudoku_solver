import numpy as np


sudoku =[[5,3,0,0,7,0,0,0,0],
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],
         [0,0,0,4,1,9,0,0,5],
         [0,0,0,0,8,0,0,7,9]]




def possible(row, column, number):
    global sudoku
    # Is the number appearing in the given row?
    for i in range(0, 9):
        if sudoku[row][i] == number:
            return False

    # Is the number appearing in the given column?
    for i in range(0, 9):
        if sudoku[i][column] == number:
            return False

    # Is the number appearing in the given [3X3]square?
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku[y0 + i][x0 + j] == number:
                return False

    return True


def solve():
    global sudoku
    for row in range(0, 9):
        for column in range(0, 9):
            if sudoku[row][column] == 0:
                for number in range(1, 10):
                    if possible(row, column, number):
                        sudoku[row][column] = number
                        solve()
                        sudoku[row][column] = 0

                return

    print(f"your solved sudoku is:\n {np.matrix(sudoku)}")
solve()
