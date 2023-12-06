#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Substitute every occurence of an item with another in a list.

    my_list -- the list.
    search -- item to search for
    replace -- item to replace with
    """

    revised = []
    if my_list:
        for itm in my_list:
            revised.append(replace if itm == search else itm)

    return revised


# def search_replace2(my_list, search, replace):
#     """"""

#     revised = [replace if itm == search else itm for itm in my_list]\
#         if my_list else []

#     return revised
