#!/usr/bin/python3
import sys


def infinite_add():
    av = sys.argv[1:]
    addition = 0

    for num in av:
        addition += int(num)

    print(addition)


if __name__ == "__main__":
    infinite_add()
