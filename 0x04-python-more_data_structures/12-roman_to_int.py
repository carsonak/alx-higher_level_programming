#!/usr/bin/python3
def roman_to_int(roman_string):
    """"""

    rmn_s = roman_string
    s_ln = len(roman_string)
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    if roman_string:
        if s_ln > 1 and roman[rmn_s[1]] > roman[rmn_s[0]]:
            decimal = -roman[rmn_s[0]]
        else:
            decimal = 0

        for ltr in rmn_s[1:] if decimal < 0 else rmn_s:
            decimal += roman[ltr]

    else:
        return 0

    return decimal
