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

    def to_json(self):
        """Return a dict of instance attributes"""

        return self.__dict__


if __name__ == "__main__":
    students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

    for student in students:
        j_student = student.to_json()
        print(type(j_student))
        print(j_student['first_name'])
        print(type(j_student['first_name']))
        print(j_student['age'])
        print(type(j_student['age']))
