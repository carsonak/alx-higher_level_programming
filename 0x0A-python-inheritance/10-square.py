#!/usr/bin/python3
"""Module for Square class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initialises a square instance by calling parent class initialiser"""

        self.integer_validator("size", size)
        super().__init__(size, size)


if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())
    try:
        s = Square("44")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
