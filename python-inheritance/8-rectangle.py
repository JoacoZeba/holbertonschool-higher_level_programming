#!/usr/bin/python3
"""Module for the Rectangle class that inherits from BaseGeometry."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.

    This class represents a rectangle with a validated width and height.
    It uses the `integer_validator` method from BaseGeometry to ensure
    that the dimensions are valid positive integers.
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
