import numpy as np
from pyasn1.type.univ import Null


def generate_sudoku():
    sudoku = np.zeros((9, 9), dtype=int)

    for i in range(9):
        for j in range(9):
            sudoku[i, j] = (i * 3 + i // 3 + j) % 9 + 1

    np.random.shuffle(sudoku)
    sudoku = sudoku.T
    np.random.shuffle(sudoku)

    return sudoku


def empty_cell(sudoku, empty_cells):
    new_sudoku = sudoku.copy()
    for _ in range(empty_cells):
        row, col = np.random.randint(0, 9, size=2)
        new_sudoku[row, col] = 0
    return new_sudoku
