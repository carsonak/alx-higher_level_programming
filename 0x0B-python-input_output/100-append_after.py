#!/usr/bin/python3
"""
Module for append_after

Functions:
    insert_strings: inserts objects as strings into text
    append_after: inserts a string after particular string within a line
"""


def insert_strings(dest: str, src, pos: int | str = -1):
    """
    Insert an object string representation in a string at the specified pos

    Args:
        dest (str): string to affix object in
        src (any): an object which can be represented as a string
        pos (int | str): index to affix after or string to affix after

    Return:
        The resultant string
    """

    nw_str = ""
    if type(dest) is not str:
        raise TypeError("dest is not a str type")

    s_src = str(src)
    if type(pos) is int:
        if pos > len(dest):
            raise IndexError("Index is out of range")

        nw_str = dest[:pos] + s_src + dest[pos:]
    elif type(pos) is str:
        f_foot, b_foot, slen = 0, 0, len(s_src)
        nw_str = dest[:]
        while f_foot >= 0:
            f_foot = nw_str.find(pos, b_foot)
            if f_foot >= 0:
                f_foot = nw_str.find("\n", f_foot) + 1
                nw_str = nw_str[:f_foot] + s_src + nw_str[f_foot:]
                b_foot = f_foot + slen
    else:
        raise TypeError("pos is not an int or str type")

    return nw_str


def append_after(filename="", search_string: str = "", new_string: str = ""):
    """
    Search for a given string in a file and append a given string after it

    Args:
        filename (str): Path of the file
        search_string (str): string to search for
        new_string (str): string to insert in file
    """

    with open(filename, "r+", encoding="utf-8") as afile:
        text = afile.read()
        afile.seek(0, 0)  # Setting cursor to 0 so as to overwrite the file
        afile.write(insert_strings(text, new_string, search_string))


if __name__ == "__main__":
    append_after("./append_after_100.txt", "Python", "\"C is fun!\"\n")
