#!/usr/bin/python3
def weight_average(my_list=[]):
    """Return weighted average of numbers in a list of tuples.

    my_list -- a list of tuples where the first item of a tuple should be
            the number and the second its frequency.
    """

    total, itm_num = 0, 0
    if my_list and type(my_list) is list:
        for block in my_list:
            if type(block) is tuple and len(block) > 1:
                total += block[0] * block[1]
                itm_num += block[1]

    return float(total/itm_num)
