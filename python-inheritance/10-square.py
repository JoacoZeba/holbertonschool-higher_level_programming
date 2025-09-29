#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represents a square shape, inherits from Rectangle."""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
