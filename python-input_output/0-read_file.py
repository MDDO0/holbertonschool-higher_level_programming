#!/usr/bin/python3
"""Reads a text file (UTF8) and prints its content to stdout."""


def read_file(filename=""):
    """Read and print the content of a UTF-8 text file.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
