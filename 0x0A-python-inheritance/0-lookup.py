#!/usr/bin/python3
"""lookup module"""


def lookup(obj):
    """Return a list of an object's attributes and methods"""

    return dir(obj)


if __name__ == "__main__":
    class MyClass1(object):
        pass

    class MyClass2(object):
        my_attr1 = 3

        def my_meth(self):
            pass

    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))
