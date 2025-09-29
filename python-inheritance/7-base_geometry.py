#!/usr/bin/python3
"""
This module defines a base geometry class with an unimplemented area method.

The class is intended to be subclassed by more specific geometric
shape classes,
which should provide their own implementation of the area method.
"""


class BaseGeometry:
    """
    A base class for geometry-related operations.

    This class serves as a blueprint for geometric shapes.
    It includes a placeholder method for calculating area.
    """

    def integer_validator(self, name, value):
        """
        Verify if the size of the a geometric shape is valid.

        Raises:
            TypeError: "<Geometric shape name> must be an integer"
                        if the value is not an int.

            ValueError: "<Geometric shape name> must be greater than 0"
                        if the value is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name:s} must be an integer")

        if value <= 0:
            raise ValueError(f"{name:s} must be greater than 0")

    def area(self):
        """
        Calculate the area of a geometric shape.

        This method is intended to be overridden in subclasses.
        It raises an Exception to indicate that it has not been implemented.

        Raises:
            Exception: Always, with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")
