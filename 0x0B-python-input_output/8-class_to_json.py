#!/usr/bin/python3
"""Module for class_to_json"""


def class_to_json(obj):
    """Return a dictionary of an object's attributes"""
    return obj.__dict__


if __name__ == "__main__":
    class MyClass:
        """ My class
        """

        score = 0

        def __init__(self, name, number=4):
            self.__name = name
            self.number = number
            self.is_team_red = (self.number % 2) == 0

        def win(self):
            self.score += 1

        def lose(self):
            self.score -= 1

        def __str__(self):
            return "[MyClass] {} - {:d} => {:d}".format(self.__name, self.number, self.score)

    m = MyClass("John")
    m.win()

    mj = class_to_json(m)
    print(type(mj))
    print(mj)
