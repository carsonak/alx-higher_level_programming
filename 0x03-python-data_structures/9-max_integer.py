#!/usr/bin/python3
def max_integer(my_list=[]):
    """Return the largest number in a list"""

    max = my_list[0] if my_list else None
    for num in my_list:
        if num > max:
            max = num

    return max
