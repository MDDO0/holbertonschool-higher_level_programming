#!/usr/bin/python3
"""Converts a JSON string to a Python object."""
import json


def from_json_string(my_str):
    """Return the Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert.

    Returns:
        object: The corresponding Python object.
    """
    return json.loads(my_str)
