#!/usr/bin/python3
"""Module for add_attribute"""


def add_attribute(obj, attr_name, attr_val):
    """Add an attribute to an object if possible otherwise raise TypeError"""

    if hasattr(obj, "__dict__") and type(obj.__dict__) is dict:
        obj.__dict__[str(attr_name)] = attr_val
    else:
        raise TypeError("can't add new attribute")


if __name__ == "__main__":
    class MyClass():
        pass

    mc = MyClass()
    add_attribute(mc, "name", "John")
    print(mc.name)

    try:
        a = "My String"
        add_attribute(a, "name", "Bob")
        print(a.name)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
