#!/usr/bin/python3
"""Module for Square class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initialises a square instance by calling parent class initialiser"""

        super().__init__(size, size)


if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())
