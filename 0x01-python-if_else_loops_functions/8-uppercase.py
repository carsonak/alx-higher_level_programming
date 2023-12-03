#!/usr/bin/python3
def uppercase(str):
    for ltr in str:
        if ord(ltr) > 96 and ord(ltr) < 173:
            print(chr(ord(ltr) - 32), end="")
        else:
            print(ltr, end="")
    else:
        print("")
