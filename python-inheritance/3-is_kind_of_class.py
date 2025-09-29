#!/usr/bin/python3
"""
This module provides a function to check whether an object is an instance of
a specified class or inherits from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a class or a subclass thereof.

    This function returns True if the object is an instance of the given class
    or an instance of a subclass that inherits from the given class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or a subclass, False otherwise.
    """
    return isinstance(obj, a_class)
