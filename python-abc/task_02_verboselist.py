#!/usr/bin/env python3
"""Defines a VerboseList class that extends the built-in list with notifications."""


class VerboseList(list):
    """Custom list that prints messages when modified."""

    def append(self, item):
        """Append item and print notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend list and print notification."""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Print notification before removing item."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Print notification before popping item."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
