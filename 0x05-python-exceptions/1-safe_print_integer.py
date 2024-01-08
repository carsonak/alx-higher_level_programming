#!/usr/bin/python3

def safe_print_integer(value):
    """Print an int and catch TypeErrors"""

    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        return False

    return True
