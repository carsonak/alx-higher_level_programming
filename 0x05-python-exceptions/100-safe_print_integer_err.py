#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    """Print only integers"""

    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        print(f"Exception: {err}", file=stderr)
        return False

    return True
