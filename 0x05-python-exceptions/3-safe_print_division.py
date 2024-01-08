#!/usr/bin/python3

def safe_print_division(a, b):
    """Divide numbers and catch exceptions"""

    res = None
    try:
        res = a / b
    except (TypeError, ValueError, ZeroDivisionError):
        pass
    finally:
        print("Inside result: {}".format(res))

    return res
