#!/usr/bin/python3
"""Module for Rectangle"""


class Rectangle:
    """
    Rectangle class

    Attributes:
        width (int): a positive integer
        height (int): a positive integer
        number_of_instances (int) : instances of this class
        print_symbol (any) : symbol used to rep the rectangle

    Methods:
        __init__ : calls setters for width and height
        __str__ : return a string of hashes that represent the rectangle
        __repr__ : return a string that can recreate a Rectangle instance
        __del__ : Bye rectangle...
        area : return area of the rectangle
        perimeter : return perimeter of the rectangle
        bigger_or_equal : static method, compare areas of two instances of
            Rectangle
        square : alternative constructor, return a new instance of Rectangle
            as a square
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialise instance by calling setters

        Parameters:
            width (int): an optional integer
            height (int): an optional integer
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """Return a string of $print_symbol that represent the rectangle"""
        if self.area() > 0:
            symbols = (str(self.print_symbol) * self.__width) + "\n"
            leRectangle = symbols * self.__height
            return leRectangle.rstrip()
        else:
            return ""

    def __repr__(self):
        """Return code that can recreate a Rectangle instance as a string"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Bye rectangle..."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare areas of two instances of Rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Return a new instance of Rectangle as a square"""
        return cls(size, size)


if __name__ == "__main__":
    my_sqr = Rectangle.square(5)
    print("A: {} - P: {}".format(my_sqr.area(), my_sqr.perimeter()))
    print(my_sqr)
