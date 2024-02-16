#!/usr/bin/
def magic_string():
    magic_string.call += 1
    return "BestSchool" + (", BestSchool" * magic_string.call)


magic_string.call = -1
