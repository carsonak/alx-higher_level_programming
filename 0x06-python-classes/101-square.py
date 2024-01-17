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

    def __str__(self):
        shiftdown = "\n" * self.__position[1]
        shiftright = " " * self.__position[0]
        hashes = ("#" * self.__size) + "\n"
        leSquare = shiftdown + ((shiftright + hashes) * self.__size)
        return leSquare[:-1]


if __name__ == "__main__":

    my_square = Square(5, (0, 0))
    print(my_square)

    print("--")

    my_square = Square(5, (4, 1))
    print(my_square)
