#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represents a square shape, inherits from Rectangle."""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        return (
            f"[Square] {self._Rectangle__width:d}/{self._Rectangle__height:d}"
        )
