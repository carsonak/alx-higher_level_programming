#!/usr/bin/python3
"""Square"""


class Square:
    """Square"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, val):
        """Set size, raise exceptions on invalid values"""

        if type(val) is not int:
            raise TypeError("size must be an integer")
        elif val < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = val

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, pos):
        """Set position, raise exception on invalid values"""

        if type(pos) is not tuple or len(pos) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(pos[0]) is not int or type(pos[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif pos[0] < 0 or pos[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = pos

    def area(self):
        return self.__size ** 2

    def my_print(self):
        """Print square with #'s and offset at position"""

        if self.__size:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
        else:
            print()


if __name__ == "__main__":
    my_square_1 = Square(3)
    my_square_1.my_print()

    print("\n<----->")
    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("\n<----->")
    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("\n<----->")
    try:
        my_square_4 = Square("Master", ("0", 3))
        my_square_4.my_print()
    except Exception as e:
        print(e)

    print("\n<----->")
    try:
        my_square_4 = Square(4, ("0", 3))
        my_square_4.my_print()
    except Exception as e:
        print(e)

    print("\n<----->")
    try:
        print(f"size = {my_square_1.size}")
        print(f"position = {my_square_1.position}")
        print(f"type = {type(my_square_1)}")
        print(f"__dict__ = {my_square_1.__dict__}")
    except Exception as e:
        print(e)

    print("\n<----->")
    try:
        print(f"__size = {my_square_1.__size}")
    except Exception as e:
        print(e)

    print("\n<----->")
    try:
        print(f"__position = {my_square_1.__position}")
    except Exception as e:
        print(e)

    print("\n<----->")
