#!/usr/bin/python3
"""Creates an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Read a JSON file and return the corresponding Python object.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        object: The Python object represented by the JSON content.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
