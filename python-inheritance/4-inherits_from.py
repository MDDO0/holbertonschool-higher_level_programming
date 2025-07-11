#!/usr/bin/python3
"""Defines a function to check if an object inherits from a class
(but is not an instance of it directly).
"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a subclass of a_class,
    otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
