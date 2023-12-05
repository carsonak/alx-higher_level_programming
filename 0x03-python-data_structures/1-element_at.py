#!/usr/bin/python3
def element_at(my_list, idx):
    """Get an item in a list"""

    if type(my_list) is not list or not my_list:
        return None
    elif idx >= 0 and idx < len(my_list):
        return my_list[idx]
    else:
        return None
