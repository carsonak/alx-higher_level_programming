#!/usr/bin/python3
"""Module for add_integer"""


def add_integer(a, b=98):
    """
    Return sum of two numbers and catch some exceptions

    Arguments:
        a (int/float): a compusolary number
        b (int/float): an optional number, default is 98

    Exceptions:
        If a or b is not either a float or an int a TypeError will be raised

    Returns:
        int: The sum of a and b
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
