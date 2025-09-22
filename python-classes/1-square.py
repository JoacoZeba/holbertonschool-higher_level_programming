#!/usr/bin/python3
"""
This module defines a class Square with a private size attribute.
"""


class Square:
    """Defines a square by its size (private attribute)."""

    def __init__(self, size=None):
        """
        Initialize a new Square instance.

        Args:
            size: The size of the square (no type/value checking yet).
        """
        self.__size = size
