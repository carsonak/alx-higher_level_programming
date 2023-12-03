#!/usr/bin/python3
def uppercase(str):
    for ltr in str:
        if ord(ltr) > 96 and ord(ltr) < 173:
            print(chr(ord("{}".format(ltr)) - 32), end="")
        else:
            print("{}".format(ltr), end="")
    else:
        print("")
