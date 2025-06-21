#!/usr/bin/python3
"""This module defines the MyList class that inherits from list."""


class MyList(list):
    """A subclass of list with a method to print sorted list."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
