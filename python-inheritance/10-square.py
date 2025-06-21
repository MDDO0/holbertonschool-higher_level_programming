#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""
import sys
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square that inherits from Rectangle with size validation."""

    def __init__(self, size):
        """Initialize a square.

        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
