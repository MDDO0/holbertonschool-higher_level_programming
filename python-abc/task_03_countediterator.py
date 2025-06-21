#!/usr/bin/env python3
"""Defines CountedIterator class that counts number of iterations."""


class CountedIterator:
    """Custom iterator that counts how many items have been iterated."""

    def __init__(self, iterable):
        """Initialize with iterable and a counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Return next item and increment the counter."""
        item = next(self.iterator)  # May raise StopIteration
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items iterated over so far."""
        return self.count

    def __iter__(self):
        """Return self to make it an iterable."""
        return self
