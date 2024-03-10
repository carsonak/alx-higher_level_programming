#!/usr/bin/python3
"""Module for rectangle."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")

        if width < 1:
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")

        if height < 1:
            raise ValueError("height must be > 0")

        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")

        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y

    def area(self):
        """Return area of rectangle."""
        return self.width * self.height

    def display(self):
        """Print a visual representation of a rectangle."""
        y_offset = "\n" * self.y
        x_offset = " " * self.x
        row = x_offset + ("#" * self.width) + "\n"
        full_rec = y_offset + (row * self.height)
        print(full_rec.rstrip())

    def __str__(self):
        """Return details of rectangle instance."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Updates attributes of an instance with values from a tuple."""

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

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle instance."""
        inst_dict = dict()
        for attribute in ("x", "y", "id", "height", "width"):
            inst_dict[attribute] = getattr(self, attribute)

        return inst_dict
