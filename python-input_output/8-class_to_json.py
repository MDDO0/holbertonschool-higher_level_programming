#!/usr/bin/python3
"""Returns the dictionary description of an object for JSON serialization."""


def class_to_json(obj):
    """Return the dictionary description of a simple object's attributes.

    Args:
        obj: The instance of a class.

    Returns:
        dict: Dictionary of attributes suitable for JSON serialization.
    """
    return obj.__dict__
