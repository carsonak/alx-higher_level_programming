#!/usr/bin/python3
"""Module for Rectangle"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width: int, height: int):
        """Validates height and witdth and initialises their private attrs"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return area of Rectangle"""

        return self.__height * self.__width

    def __str__(self):
        """Return an informal representation of the instance"""

        return f"[Rectangle] {self.__width}/{self.__height}"


if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(r.area())
