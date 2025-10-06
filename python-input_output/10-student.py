#!/usr/bin/python3
"""Student class with simplified JSON representation."""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Set up the student with name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return a dictionary of attributes."""
        if isinstance(attrs, list):
            result = {}
            for name in attrs:
                if isinstance(name, str) and hasattr(self, name):
                    result[name] = getattr(self, name)
            return result
        else:
            return self.__dict__
