#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print elements of a 2D matrix in a row column format"""

    if matrix:
        for row in matrix:
            for itm in row:
                print("{:d}".format(itm), end="")
                if itm != row[-1]:
                    print("", end=" ")
            else:
                print("")
