#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Print a dictionary sorted by its keys"""

    for d_key in sorted(a_dictionary.keys()):
        print(f"{d_key:s}: {a_dictionary[d_key]}")
