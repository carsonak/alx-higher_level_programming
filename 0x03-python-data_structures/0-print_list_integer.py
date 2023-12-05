#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Prints each element of a list per line"""

    if my_list and type(my_list) is list:
        for i in my_list:
            print("{:d}".format(i))
