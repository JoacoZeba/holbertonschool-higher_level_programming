#!/usr/bin/python3
"""
This module defines a class Square that represents a square shape.

The Square class allows setting and retrieving the size of the square,
with validation to ensure that the size is always a non-negative integer.
It also provides a method to calculate the area of the square.
"""


class Square:
    """
    Represents a square with a specific size.

    This class provides methods to set and get the size of the square,
    while ensuring that it is always a non-negative integer.
    It also includes a method to calculate the area.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter for the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size**2

    def my_print(self):
        """
        Prints the square to stdout using the character '#'.

        If the size is 0, it prints an empty line.

        This method visually represents the square by printing
        rows of '#' characters corresponding to its current size.
        """
        if self.__size == 0:
            print()
            return

        for i in range(self.__size):
            print("#" * self.__size)
