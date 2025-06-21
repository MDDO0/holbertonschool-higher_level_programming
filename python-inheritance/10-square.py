#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle,
with size validation and area calculation.
"""


class BaseGeometry:
    """Base class for geometry operations with validation."""

    def area(self):
        """Raises an exception indicating the method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle with width and height validated by BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a Rectangle.

        Args:
            width (int): Rectangle width.
            height (int): Rectangle height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


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
