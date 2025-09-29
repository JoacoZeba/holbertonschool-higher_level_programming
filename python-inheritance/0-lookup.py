#!/usr/bin/python3
"""
This module provides a function to retrieve a list of available
attributes and methods of an object. It's useful for inspecting
objects and understanding what operations can be performed on them.
"""


def lookup(obj):
    """
    Returns a list of attributes and methods available for a given object.

    Args:
        obj (any): The object to inspect.

    Returns:
        list: A list of strings containing the names of the available
              attributes and methods of the object.
    """
    return dir(obj)
