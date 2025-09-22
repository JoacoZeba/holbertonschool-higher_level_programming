#!/usr/bin/python3
"""
This module defines the Square class for representing a square shape.

The Square class includes a private size attribute with type
and value validation.
"""


class Square:
    """
    Represents a square with a private size attribute.

    Attributes:
        __size (int): The size of the square's side. Must be an integer >= 0.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int, optional): The size of the square's side.
            Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
