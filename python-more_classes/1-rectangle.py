#!/usr/bin/python3
"""
Module creates a class rectangle
"""


class Rectangle:
    """
    Class will be a rectangle
    """

    def validate_size(self, value, axis):
        if type(value) is not int:
            raise (TypeError(f"{axis} must be an integer"))
        if value < 0:
            raise (ValueError(f"{axis} must be >= 0"))
        return True

    def __init__(self, width=0, height=0):
        if self.validate_size(width, "width"):
            self.__width = width
        if self.validate_size(height, "height"):
            self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (self.validate_size(value, "width")):
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if self.validate_size(value, "height"):
            self.__height = value
