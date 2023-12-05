#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an item in a copy of a list"""

    if type(my_list) is list and idx >= 0 and idx < len(my_list):
        nw_list = my_list[:]
        nw_list[idx] = element

    return nw_list
