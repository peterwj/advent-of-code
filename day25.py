#!/usr/bin/python
import math
import numpy as np
from sys import argv as argv
from unittest import main, TestCase

class TestDay25(TestCase):
    def test_nrow_calculation(self):
        assert(calculate_matrix_size(6) == 3)
        assert(calculate_matrix_size(21) == 6)

    def test_generate_triangular_matrix(self):
        tiny_table = np.zeros((2,2))
        tiny_table[0][0] = 1
        tiny_table[1][0] = 2
        tiny_table[0][1] = 3
        tiny_table[0][0] = 0
        assert(tiny_table[i][j] == generate_triangular_matrix(3)[i][j] for i in (0,1) for j in (0,1))

    def test_solve_problem(self):
        assert(solve_problem(1,1) == 20151125)
        assert(solve_problem(4,4) == 9380097)

def calculate_matrix_size(n_entries):
    # total entries = 1/2 * (n^2 + n)
    # 6 = 1/2 * (9 + 3) -- looks good!
    # n^2 / 2 + n / 2 - nentries = 0
    a = 0.5
    b = 0.5
    c = -n_entries 
    nrows = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    return int(nrows)

def generate_triangular_matrix(n_entries):
    ncols = nrows = calculate_matrix_size(n_entries)
    table = np.zeros((nrows, ncols))
    (row, col) = (0,0)
    for i in range(1, n_entries+1):
        table[row][col] = i
        if row == 0:
            row = col+1
            col = 0
        else:
            row -= 1
            col += 1
    return table

def generate_number_to_index_map(n_entries):
    triangular_matrix = generate_triangular_matrix(n_entries)
    result = {}
    for row in triangular_matrix:
        for col in triangular_matrix[row]:
            if triangular_matrix[row][col] != 0:
                n = triangular_matrix[row][col]
                result[n] = (row,col)
    return result

def generate_code_table(n_entries):
    ncols = nrows = calculate_matrix_size(n_entries)
    codes = np.zeros((n_entries+2,))
    codes[1] = 20151125
    for i in range(2, n_entries+2):
        codes[i] = codes[i-1] * 252533 % 33554393
    return codes

def solve_problem(row, col):
    nrows = row+col
    n_entries = int(1/2 * (nrows**2 + nrows))
    codes = generate_code_table(n_entries)
    triangular_table = generate_triangular_matrix(n_entries)
    code_number = triangular_table[row-1][col-1]
    return codes[code_number]

if __name__ == '__main__':
    if len(argv) == 1:
        main()
    elif len(argv) == 3:
        row = int(argv[1])
        col = int(argv[2])
        print(solve_problem(row, col))
    else:
        print('Usage: `{} [row col]`'.format(argv[0]))

    goal = (2947, 3029)
