#!/usr/bin/python3
for ltr in "zyxwvutsrqponmlkjihgfedcba":
    print("{}".format(chr(ord(ltr) - 32) if ord(ltr) % 2 else ltr), end="")
