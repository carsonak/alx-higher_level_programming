#!/usr/bin/python3
"""Module for Rectangle"""


class Rectangle:
    """
    Rectangle class

    Attributes:
    width (int): a positive integer
    height (int): a positive integer

    Methods:
    __init__ : calls setters for width and height
    __str__ : return a string of hashes that represent the rectangle
    __repr__ : return code that can recreate a Rectangle instance as a string
    area : return area of the rectangle
    perimeter : return perimeter of the rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initialise instance by calling setters

        Parameters:
            width (int): an optional integer
            height (int): an optional integer
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        """Initialise private value of width with a +ve int"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """Initialise private value of height with a +ve int"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Return perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """Return a string of hashes that represent the rectangle"""
        if self.area() > 0:
            hashes = ("#" * self.__width) + "\n"
            leRectangle = hashes * self.__height
            return leRectangle.rstrip()
        else:
            return ""

    def __repr__(self):
        """Return code that can recreate a Rectangle instance as a string"""
        return f"Rectangle({self.__width}, {self.__height})"


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print(str(my_rectangle))
    print("--")
    print(my_rectangle)
    print("--")
    print(repr(my_rectangle))
    print("--")
    print(hex(id(my_rectangle)))
    print("--")

    # create new instance based on representation
    new_rectangle = eval(repr(my_rectangle))
    print(str(new_rectangle))
    print("--")
    print(new_rectangle)
    print("--")
    print(repr(new_rectangle))
    print("--")
    print(hex(id(new_rectangle)))
    print("--")

    print(new_rectangle is my_rectangle)
    print(type(new_rectangle) is type(my_rectangle))
