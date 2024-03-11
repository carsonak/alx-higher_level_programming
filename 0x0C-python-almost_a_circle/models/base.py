#!/usr/bin/python3
"""Module for base."""
from typing import Optional
import json

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

    def to_json_string(list_dictionaries: list[dict]):
        """Return the JSON string representation of list_dictionaries."""
        if type(list_dictionaries) is list and len(list_dictionaries):
            if not all(type(item) is dict for item in list_dictionaries):
                raise TypeError(
                    "list_dictionaries must be a list of dictionaries")
            else:
                return json.dumps(list_dictionaries)

        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""

        from models.rectangle import Rectangle
        from models.square import Square
        filename = None
        if type(list_objs) is list:
            if all(type(obj) is Rectangle for obj in list_objs):
                filename = "Rectangle.py"
            elif all(type(obj) is Square for obj in list_objs):
                filename = "Square.py"

        if list_objs is None:
            filename = "Rectangle.py"
            list_objs = []

        if filename is None:
            raise TypeError(
                "list_objs must be a list of Rectangle or Square objects")

        list_of_dicts = []
        with open(filename, "w", encoding="UTF-8") as file:
            list_of_dicts = [obj.to_dictionary() for obj in list_objs]
            file.write(cls.to_json_string(list_of_dicts))
