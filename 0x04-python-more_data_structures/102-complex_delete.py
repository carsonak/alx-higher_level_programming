#!/usr/bin/python3
def complex_delete(a_dictionary, value):

    whch_kys = []
    if a_dictionary and type(a_dictionary) is dict:
        for a_key in a_dictionary.keys():
            if a_dictionary[a_key] == value:
                whch_kys.append(a_key)
        else:
            for a_key in whch_kys:
                a_dictionary.pop(a_key)

    return a_dictionary
