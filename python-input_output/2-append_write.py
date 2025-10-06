#!/usr/bin/python3

"""Append write in file"""


def append_write(filename="", text=""):
    """Write a text at the end of a file"""

    with open(filename, 'a', encoding="utf-8") as file:
        return (file.write(text))
