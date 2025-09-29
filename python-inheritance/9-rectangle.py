#!/usr/bin/python3
"""Module for the Rectangle class that inherits from BaseGeometry."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    This module defines a class Rectangle that inherits from BaseGeometry.
    It represents a rectangle with width and height, and provides
    validation and area calculation.
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return f"[Rectangle] {self.__width:d}/{self.__height:d}"

    def area(self):
        return self.__width * self.__height
