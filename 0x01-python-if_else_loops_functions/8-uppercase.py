#!/usr/bin/python3
def uppercase(str):
    for ltr in str:
        if ord(ltr) > 96 and ord(ltr) < 173:
            ltr = chr(ord(ltr) - 32)

        print("{}".format(ltr), end="")
    else:
        print("")
