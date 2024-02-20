#!/usr/bin/python3
"""Module for inherits_from"""


def inherits_from(obj, a_class):
    """Retrun true if obj inherited from a_class, else false"""

    return isinstance(obj, a_class) and type(obj) is not a_class


if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
