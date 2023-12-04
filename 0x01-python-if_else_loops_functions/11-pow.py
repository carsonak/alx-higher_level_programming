#!/usr/bin/python3
def pow(a, b):
    """a to power b"""

    a_cpy = abs(a) if a < 0 else a
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        for i in range(abs(b) - 1):
            a_cpy *= abs(a)

    if b < 0:
        a_cpy = 1 / a_cpy

    if abs(b) % 2 and a < 0:
        a_cpy = -a_cpy

    return a_cpy
