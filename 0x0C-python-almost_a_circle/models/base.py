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

    @staticmethod
    def to_json_string(list_dictionaries):
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
        if type(list_objs) is list and len(list_objs):
            if all(type(obj) is Rectangle for obj in list_objs):
                filename = "./Rectangle.json"
            elif all(type(obj) is Square for obj in list_objs):
                filename = "./Square.json"

        if list_objs is None or (type(list_objs) is list and
                                 not len(list_objs)):
            filename = "both"
            list_objs = []

        if filename is None:
            raise TypeError(
                "list_objs must be a list of Rectangle or Square objects")

        if filename == "both" or filename == "./Rectangle.json":
            with open("./Rectangle.json", "w", encoding="UTF-8") as file:
                list_of_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_of_dicts))

        if filename == "both" or filename == "./Square.json":
            with open("./Square.json", "w", encoding="UTF-8") as file:
                list_of_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_of_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string."""
        if type(json_string) is str and json_string:
            return json.loads(json_string)

        return []

    @classmethod
    def create(cls, **dictionary):
        """Create a new instance of subclass with attributes already set."""
        from models.rectangle import Rectangle
        from models.square import Square

        if "size" in dictionary or type(cls) is Square:
            dummy = Square(2)
        else:
            dummy = Rectangle(2, 2)

        dummy.update(**{k: v for k, v in dictionary.items()})
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from a json file."""
        from models.square import Square

        filename = "./Rectangle.json"
        if cls is Square:
            filename = "./Square.json"

        try:
            with open(filename, encoding="UTF-8") as file:
                list_dictionaries = Base.from_json_string(file.readline())
        except FileNotFoundError:
            list_dictionaries = []

        return [Base.create(**d) for d in list_dictionaries]
