#!/usr/bin/python3
"""Module for is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Return True obj is instance of a_class or of its children, else False"""

    return isinstance(obj, a_class)


if __name__ == "__main__":
    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))
