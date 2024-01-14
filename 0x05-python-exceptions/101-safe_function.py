#!/usr/bin/python3
""""""

from sys import stderr

def safe_function(fct, *args):
    """Catch exceptions from functions"""
    try:
        output = fct(*args)
    except Exception as err:
        print(f"Exception: {err}", file=stderr)
        return None

    return output
