#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """Print atleast x number of items in a ist"""

    count = 0
    try:
        for itm in my_list:
            if count >= x:
                break
            else:
                print("{}".format(itm), end="")
                count += 1
    except (IndexError, TypeError):
        pass

    print()
    return int(count)
