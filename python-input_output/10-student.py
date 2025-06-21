#!/usr/bin/python3
"""Defines a Student class with optional attribute filtering for JSON."""


class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the student.

        If attrs is a list of strings, returns only those attributes.
        Otherwise, returns all attributes.
        """
        if (isinstance(attrs, list) and
                all(type(attr) is str for attr in attrs)):
            return {
                key: getattr(self, key)
                for key in attrs
                if hasattr(self, key)
            }
        return self.__dict__
