#!/usr/bin/python3
"""Module for base."""
from typing import Optional


class Base:
    """"""
    __nb_objects = 0

    def __init__(self, id: Optional[int] = None):
        if id:
            if type(id) is not int:
                raise TypeError("x must be an integer")

            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
