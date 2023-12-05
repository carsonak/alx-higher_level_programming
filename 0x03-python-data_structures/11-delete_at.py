#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Remove a character at specified index"""

    if my_list and idx >= 0:
        my_list = my_list[:idx] + my_list[idx + 1:]

    return my_list
