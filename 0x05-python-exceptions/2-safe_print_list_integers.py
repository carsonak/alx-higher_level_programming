#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print integers in a list and catch exceptions"""

    count = 0
    try:
        for num in my_list:
            if count >= x:
                break
            try:
                print("{:d}".format(num), end="")
            except ValueError:
                continue
            count += 1
    except (TypeError, IndexError):
        pass

    print()
    return int(count)
