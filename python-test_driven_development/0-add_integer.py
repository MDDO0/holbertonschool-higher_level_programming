#!/usr/bin/python3
"""
This module provides a function to add two integers.

The function ensures that both arguments are either integers or floats,
and raises appropriate errors otherwise.
"""

def add_integer(a, b=98):
    """
    Returns the sum of a and b as integers.

    Args:
        a: An integer or float.
        b: An integer or float (default is 98).

    Returns:
        The sum of a and b, casted to integers.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
