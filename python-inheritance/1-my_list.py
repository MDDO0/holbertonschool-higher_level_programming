#!/usr/bin/python3
class MyList(list):
    """Custom list class that inherits from built-in list."""

    def print_sorted(self):
        """Prints the list in ascending sorted order (without modifying the original list)."""
        print(sorted(self))
