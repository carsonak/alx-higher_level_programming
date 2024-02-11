#!/usr/bin/python3
"""Module for append_after"""


def insert_strings(dest, src, pos):
    """"""

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


def append_after(filename="", search_string="", new_string=""):
    """"""

    with open(filename, "r+", encoding="utf-8") as afile:
        p = afile.read()
        afile.seek(0, 0)
        afile.write(insert_strings(p, new_string, search_string))


if __name__ == "__main__":
    append_after("/home/line/Github_Repositories/alx-higher_level_programming/0x0B-python-input_output/append_after_100.txt",
                 "Python", "\"C is fun!\"\n")
