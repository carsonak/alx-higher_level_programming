#!/usr/bin/python3
"""Module for append_write"""


def append_write(filename="", text=""):
    """
    Append contents of a string to a file

    Args:
        filename (str): Name of the file to read
        text (str): String to be written to the file

    Return:
        Number of characters written
    """

    with open(filename, mode="a", encoding="utf-8") as afile:
        chars = afile.write(text)

    return int(chars)


if __name__ == "__main__":
    nb_characters = append_write("my_file.txt", "This School is so cool!\n")
    print(nb_characters)
