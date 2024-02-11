#!/usr/bin/python3
"""Module for class Student"""


class Student():
    """
    Student class

    Attributes:
        first_name (str): first name
        last_name (str): last name
        age (str): age

    Methods:
        __init__: initialises some attributes
        to_json: returns a dict of instance attributes
        reload_from_json: updates an instance with dict
    """

    def __init__(self, first_name, last_name, age):
        """
        initialise some attributes

        Args:
            first_name (str): value for first_name
            last_name (str): value for last_name
            age (str): value for age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dict of instance attributes"""

        obj_d = self.__dict__
        filt = dict()
        if type(attrs) is list:
            for k in obj_d:
                if k in attrs:
                    filt.update([(k, obj_d.get(k))])
        else:
            filt = obj_d

        return filt

    def reload_from_json(self, json):
        """Update an instance with dict"""

        self.__dict__.update(json)


if __name__ == "__main__":
    pass
