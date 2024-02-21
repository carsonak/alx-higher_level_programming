#!/usr/bin/python3
"""Module for add_attribute"""


def add_attribute(obj, attr_name, attr_val):
    """Add an attribute to an object if possible otherwise raise TypeError"""

    if hasattr(obj, "__dict__") and type(obj.__dict__) is dict:
        obj.__dict__[str(attr_name)] = attr_val
    else:
        raise TypeError("can't add new attribute")


"""
New attributes can also be added to objects if they instead have the __slots__
attribute defined.
"""
