#!/usr/bin/python3
"""Module for BaseGeometry"""


class BaseGeometry():
    """BaseGeometry class"""

    def area(self):
        """Work in progress"""

        raise Exception("area() is not implemented")


if __name__ == "__main__":

    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
