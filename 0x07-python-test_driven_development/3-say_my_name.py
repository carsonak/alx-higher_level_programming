#!/usr/bin/python3
"""Module for say_my_name"""


def say_my_name(first_name, last_name=""):
    """
    Print a string with first_name and last_name

    Parameters:
        first_name (str): A str
        last_name (str): an optional str, default ''

    Return:
        Nothing
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
