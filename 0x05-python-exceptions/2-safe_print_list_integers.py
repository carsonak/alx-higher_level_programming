#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print integers in a list and catch exceptions"""

    count = 0
    for i in range(x):
        if count >= x:
            break

        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            continue

        count += 1

    print()
    return int(count)
