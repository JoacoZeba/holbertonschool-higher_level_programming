#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    result = 0
    prev = 0
    for char in reversed(roman_string):
        current_value = roman_int(char)
        if current_value < prev:
            result -= current_value
        else:
            result += current_value
            prev = current_value

    return result


def roman_int(roman_char):
    chars = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    return chars.get(roman_char)
