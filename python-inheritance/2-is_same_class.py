#!/usr/bin/python3
"""
This module provides a function to check if an object is exactly
an instance of a specific class, excluding inheritance.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the given class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
