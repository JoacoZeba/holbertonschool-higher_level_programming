#!/usr/bin/python3
"""
Module that defines a Square class with size and position.

This module provides a Square class capable of calculating its area
and printing a visual representation of itself considering its position.
"""


class Square:
    """Represents a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new square.

        Args:
            size (int): The size of the square sides. Must be >= 0.
            position (tuple): A tuple of 2 positive integers representing
                              the horizontal and vertical offset.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter for the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @property
    def position(self):
        """
        Getter for the position of the square.

        Returns:
            tuple: The current position of the square.
        """
        return self.__position

    @size.setter
    def size(self, value):
        """
        Setter for the size of the square.

        Args:
            value (int): The new size of the square. Must be an integer >= 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """
        Setter for the position of the square.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If the value is not a valid tuple
            of 2 positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size**2

    def my_print(self):
        """
        Print the square using the '#' character with
        the given position offset.

        If size is 0, an empty line is printed.
        The position is used to offset the square
        both vertically and horizontally.
        """
        if self.__size == 0:
            print()
            return

        if self.__position[1] > 0:
            print("\n" * self.__position[1], end="")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
