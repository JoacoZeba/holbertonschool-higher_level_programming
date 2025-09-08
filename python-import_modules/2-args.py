#!/usr/bin/python3
import sys


def args_print():
    av = sys.argv[1:]
    ac = len(av)

    message = (
        "0 arguments." if ac == 0 else "1 argument:" if ac == 1
        else f"{ac} arguments:")
    lines = ""
    lines = [f"{i}: {arg}"for i, arg in enumerate(av, start=1)]

    print(message + ("\n" + "\n".join(lines) if ac > 0 else ""))


if __name__ == "__main__":
    args_print()
