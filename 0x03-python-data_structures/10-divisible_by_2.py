#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """"""

    multiples = [] if my_list else [False]
    for num in my_list:
        if num % 2:
            multiples.append(False)
        else:
            multiples.append(True)

    return multiples
