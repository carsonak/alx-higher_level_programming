#!/usr/bin/python3
def roman_to_int(roman_string):
    """Convert a Roman numeral in a string to a decimal"""

    decimal = 0
    rom_nums = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    for ltr in roman_string.upper():
        if not rom_nums.get(ltr):
            return 0

    if roman_string and type(roman_string) is str:
        prev_val = rom_nums[roman_string[0].upper()]

        for ltr in roman_string.upper():
            if rom_nums[ltr] > prev_val:
                decimal += rom_nums[ltr] - (prev_val * 2)
            else:
                decimal += rom_nums[ltr]

            prev_val = rom_nums[ltr]

    return int(decimal)
