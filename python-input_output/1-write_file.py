#!/usr/bin/python3
"""Writes a string to a text file and returns the number of characters
written.
"""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8) and return number of characters
    written.

    Args:
        filename (str): The name of the file to write.
        text (str): The string to write.

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
