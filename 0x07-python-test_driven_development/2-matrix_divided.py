#!/usr/bin/python3
"""Module for matrix_divided"""


def matrix_divided(matrix, div):
    """
    Return matrix with all the items divided by div

    Parameters:
        matrix ([[]]): A list of lists of floats or ints
        div (int/float): The divisor

    Exceptions:
        If div is not an int or float a TypeError is raised
        If div is equal to 0 (zero) a ZeroDivisionError is raised
        If matrix is not a matrix of floats and/or ints a TypeError is raised

    Returns:
        A new matrix with all the items divided by div
    """

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list or type(matrix[0]) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    else:
        size = len(matrix[0])

    div_matrix = []
    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        elif len(matrix[i]) != size:
            raise TypeError("Each row of the matrix must have the same size")
        else:
            div_matrix.append([])

        for col in matrix[i]:
            if type(col) is not int and type(col) is not float:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
            else:
                div_matrix[i].append(float(f"{col / div:.2f}"))

    return div_matrix
