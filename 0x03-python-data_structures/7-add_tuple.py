#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a[0] and tuple_b[0]:
        sum = (tuple_a[0] + tuple_b[0])
    else:
        sum = (tuple_a[0] or tuple_b[0])

    if tuple_a[1] and tuple_b[1]:
        sum += (tuple_a[1] + tuple_b[1])
    else:
        sum += (tuple_a[1] or tuple_b[1])

    return sum
