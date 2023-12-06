#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Square all elements in a 2D matrix"""

    squared_m = [[x**2 for x in row] for row in matrix] if matrix else []
    return squared_m


# def square_matrix_simple2(matrix=[]):
#     """"""

#     squared_m = matrix[:] if matrix else []
#     i = 0
#     for row in matrix:
#         squared_m[i] = list(map((lambda x: x ** 2), row))
#         i += 1

#     return squared_m
