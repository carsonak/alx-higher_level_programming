#!/usr/bin/python3
"""Square"""


class Square:
    """Square"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """Set size, raise exceptions on invalid values"""

        if type(value) is not int and not float:
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def __eq__(self, other):
        return self.__size == other.__size

    def __le__(self, other):
        return self.__size <= other.__size

    def __lt__(self, other):
        return self.__size < other.__size

    def __gt__(self, other):
        return self.__size > other.__size

    def __ge__(self, other):
        return self.__size >= other.__size

    def __ne__(self, other):
        return self.__size != other.__size


if __name__ == "__main__":
    s_5 = Square(5.3)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
