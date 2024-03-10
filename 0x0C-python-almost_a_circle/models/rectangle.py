#!/usr/bin/python3
"""Module for rectangle."""
from base import Base


class Rectangle(Base):
    """Rectangle class."""

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

        attributes = ("id", "width", "height", "x", "y")
        if args and len(args):
            for idx, val in enumerate(args):
                if idx < len(attributes):
                    setattr(self, attributes[idx], val)
                else:
                    break
        else:
            for attr in attributes:
                new_val = kwargs.get(attr, getattr(self, attr))
                setattr(self, attr, new_val)

    def to_dictionary(self) -> dict[str, int]:
        """Return the dictionary representation of a Rectangle instance"""
        inst_dict = dict()
        for attribute in ("x", "y", "id", "height", "width"):
            inst_dict[attribute] = getattr(self, attribute)

        return inst_dict


if __name__ == "__main__":
    r = Rectangle(5, 3, 3, 3)
    r.display()
    print(r)
    r.update(id=789, x=1, height=4, y=5, width=7)
    print(r)
    r.update(5, 3, 3, 3)
    print(r)
    r_dict = r.to_dictionary()
    print(r_dict)
    print(type(r_dict))
