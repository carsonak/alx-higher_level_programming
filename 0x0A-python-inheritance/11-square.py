#!/usr/bin/python3
"""Module for Square"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initialises a square instance by calling parent class initialiser"""

        super().__init__(size, size)

    def __str__(self):
        """Return an informal representation of the instance"""

        return f"[Square] {self._Rectangle__height}/{self._Rectangle__width}"


if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())
