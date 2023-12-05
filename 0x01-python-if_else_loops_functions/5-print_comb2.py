#!/usr/bin/python3
for num in range(99):
    print("{:0>2}".format(num), end=", ")
else:
    print("{:0>2}".format(num + 1))
