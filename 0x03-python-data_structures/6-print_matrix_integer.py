#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for itm in row:
                print("{:d}".format(itm), end="")
                if itm != row[len(row) - 1]:
                    print("", end=" ")
            else:
                print("")
