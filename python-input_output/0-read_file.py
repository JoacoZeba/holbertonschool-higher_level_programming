#!/usr/bin/python3

"""Read file"""


def read_file(filename=""):
    """Read a file utf-8"""

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
