#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divide items in two lists and catch exceptions"""

    idx = 0
    res_list = []
    while idx < list_length:
        try:
            res_list.append(my_list_1[idx] / my_list_2[idx])
        except ZeroDivisionError:
            res_list.append(0)
            print("division by 0")
        except TypeError:
            res_list.append(0)
            print("wrong type")
        except IndexError:
            res_list.append(0)
            print("out of range")
        finally:
            pass
        idx += 1

    return res_list
