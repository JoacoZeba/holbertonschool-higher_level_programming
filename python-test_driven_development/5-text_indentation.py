#!/usr/bin/python3

"""print text"""

def text_indentation(text):
    """print text with 2 new lines after each of these characters"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    temp = ""
    for char in text:
        temp += char
        if char in ".:?":
            print(temp.strip(), end="\n\n")
            temp = ""
    if temp.strip():
        print(temp.strip(), end="")
