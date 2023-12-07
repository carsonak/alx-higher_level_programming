#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    sqr_matrix = []
    if matrix and type(matrix) is list:
        sqr_matrix = [[map(lambda x: x**2, row)] for row in matrix]

    return sqr_matrix
