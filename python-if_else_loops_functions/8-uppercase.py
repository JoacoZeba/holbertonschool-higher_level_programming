#!/usr/bin/python3
def uppercase(str):
    str_upper = ""
    for char in str:
        str_upper += chr(ord(char) - 32) if 96 < ord(char) < 123 else char

    print("{:s}".format(str_upper))
