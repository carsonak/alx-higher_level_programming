#!/usr/bin/python3
"""Module for MyInt class"""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, value):
        """Reversed equal to"""
        return super().__ne__(value)

    def __ne__(self, value):
        """Reversed not equal to"""
        return super().__eq__(value)


if __name__ == "__main__":

    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)
