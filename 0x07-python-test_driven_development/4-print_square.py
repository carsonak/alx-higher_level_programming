#!usr/bin/python3
"""Module for print_square"""


def print_square(size):
    """
    Print a square with # of size 'size'

    Parameters:
        size (int): an int greater than or equal to 0

    Return:
        Nothing
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)


if __name__ == "__main__":

    """
    print_square(4)
    print("")
    print_square(10)
    print("")
    print_square(0)
    print("")
    print_square(1)
    print("")
    try:
        print_square(-1)
    except Exception as e:
        print(e)
    print("")
    """

    print_square()
