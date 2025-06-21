#!/usr/bin/python3
"""Returns the JSON representation of an object (string)."""
import json


def to_json_string(my_obj):
    """Convert a Python object to its JSON string representation.

    Args:
        my_obj: The Python object to convert.

    Returns:
        str: JSON string representation of the object.
    """
    return json.dumps(my_obj)
