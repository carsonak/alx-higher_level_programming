#!/usr/bin/python3
from add_0 import add

a, b = 1, 2
if __name__ == "__main__":
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))