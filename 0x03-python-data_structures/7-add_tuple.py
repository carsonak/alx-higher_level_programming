#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """"Add coresponding members of tuples, return results in a tuple"""

    len_a, len_b = len(tuple_a), len(tuple_b)
    max_len = 2
    sum = []

    for i in range(max_len):
        if i < len_a and i < len_b:
            sum.append(tuple_a[i] + tuple_b[i])
        else:
            if i < len_a:
                sum.append(tuple_a[i])
            elif i < len_b:
                sum.append(tuple_b[i])
            else:
                sum.append(0)

    return (tuple(sum))
