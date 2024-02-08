#!/usr/bin/python3
"""Module for write_file"""


def write_file(filename="", text=""):
    """
    Write contents of a string to a file

    Args:
        filename (str): Name of the file to read
        text (str): String to be written to the file

    Return:
        Number of characters written
    """

    with open(filename, mode="w", encoding="utf-8") as afile:
        chars = afile.write(text)

    return int(chars)


if __name__ == "__main__":
    nb_characters = write_file("my_file.txt", "This School is so cool!\n")
    print(nb_characters)
