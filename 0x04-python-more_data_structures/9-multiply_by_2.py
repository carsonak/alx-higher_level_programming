#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Multiply all values of a dictionary by 2"""

    mul_apt = {}
    if a_dictionary:
        for a_key in a_dictionary.keys():
            mul_apt[a_key] = a_dictionary[a_key] * 2

    return mul_apt
