#!/usr/bin/python3
"""Module for base."""

from typing import Optional


class Base:
    """Base class for the project."""

    __nb_objects = 0

    def __init__(self, id: Optional[int] = None):
        """Initialise id."""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @property
    def id(self):
        """Return id."""
        return self.__id

    @id.setter
    def id(self, val):
        """Check and set id."""
        if type(val) is not int:
            raise TypeError("id must be an integer")

        self.__id = val

    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
