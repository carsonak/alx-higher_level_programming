#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add all unique items in a list"""

    band = 0
    if my_list:
        for itm in set(my_list):
            band += itm

    return band
