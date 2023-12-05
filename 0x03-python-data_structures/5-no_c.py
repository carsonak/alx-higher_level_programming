#!/usr/bin/python3
def no_c(my_string):
    """Strip 'C' and 'c' from a copied string, return the stripped string"""

    nw_str = ""
    if my_string and type(my_string) is str:
        split_strings = my_string.rsplit("c")
        nw_str = "".join(split_strings)
        split_strings = nw_str.rsplit("C")
        nw_str = "".join(split_strings)

    return nw_str
