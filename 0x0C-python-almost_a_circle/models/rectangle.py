#!/usr/bin/python3
"""Module for rectangle."""
from base import Base


class Rectangle(Base):
    """"""

    def __init__(self, width: int, height: int, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")

        if width < 1:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")

        if height < 1:
            raise ValueError("height must be > 0")

        self.__height = height

    @property
    def x(self) -> int:
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @property
    def y(self) -> int:
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y

    def area(self) -> int:
        """Return area of rectangle"""
        return self.width * self.height

    def display(self):
        """Print a visual representation of a rectangle"""
        rows = " " * self.x + ("#" * self.width) + "\n"
        rect = "\n" * self.y + rows * self.height
        print(rect.rstrip())

    def __str__(self) -> str:
        """Return details of rectangle instance"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Updates attributes of an instance with values from a tuple"""

        if args and len(args):
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]

            if len(args) > 2:
                self.height = args[2]

            if len(args) > 3:
                self.x = args[3]

            if len(args) > 4:
                self.y = args[4]
        else:
            for key, val in kwargs.items():
                if key == "id":
                    self.id = val
                elif key == "width":
                    self.width = val
                elif key == "height":
                    self.height = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val


if __name__ == "__main__":
    r = Rectangle(5, 3, 3, 3)
    r.display()
    print(r)
    r.update(789, x=1, height=4, y=5, width=7)
    print(r)
