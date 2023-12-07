#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    sqr_matrix = []
    if matrix and type(matrix) is list:
        sqr_matrix = [list(
            map(lambda iter_L: list(
                map((lambda x: x**2), iter_L)), matrix))]

    return sqr_matrix
