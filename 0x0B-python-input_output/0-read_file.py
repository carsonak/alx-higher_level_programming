#!/usr/bin/python3
"""Module for read_file"""


def read_file(filename=""):
    """
    Print contents of a file to stdout

    Args:
        filename (str): Name of the file to read
    """

    with open(filename, encoding="utf-8") as afile:
        print(afile.read())


if __name__ == "__main__":
    read_file("0-read_file.py")
