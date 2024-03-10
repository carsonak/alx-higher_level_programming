#!/usr/bin/python3
"""Module for square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return details of a Square instance"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, sz: int):
        self.width = sz
        self.height = sz

    def update(self, *args, **kwargs):
        """Updates attributes of an instance with values from a tuple"""

        attributes = ("id", "size", "x", "y")
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
        """Return the dictionary representation of a Rectangle instance"""
        inst_dict = dict()
        for attribute in ("id", "size", "x", "y"):
            inst_dict[attribute] = getattr(self, attribute)

        return inst_dict
