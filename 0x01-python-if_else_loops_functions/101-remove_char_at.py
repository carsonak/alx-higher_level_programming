#!/usr/bin/python3
def remove_char_at(str, n):
    if str and n >= 0:
        str_cpy = str[:n] + str[n + 1:]
    else:
        str_cpy = str

    return str_cpy
