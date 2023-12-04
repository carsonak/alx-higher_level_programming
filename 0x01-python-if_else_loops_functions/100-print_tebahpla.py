#!/usr/bin/python3
for ltr in "zyxwvutsrqponmlkjihgfedcba":
    if ord(ltr) % 2:
        print(f"{chr(ord(ltr) -32)}", end="")
    else:
        print(ltr, end="")
