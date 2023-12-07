#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    if matrix and type(matrix) is list:
        return [list(map(lambda iL: list(map((lambda x: x**2), iL)), matrix))]
