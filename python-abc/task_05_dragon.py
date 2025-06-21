#!/usr/bin/env python3
"""Defines SwimMixin, FlyMixin, and Dragon class using mixins."""


class SwimMixin:
    """Provides swimming ability to a class."""

    def swim(self):
        """Print swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Provides flying ability to a class."""

    def fly(self):
        """Print flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class with swim and fly abilities via mixins."""

    def roar(self):
        """Print dragon's roar."""
        print("The dragon roars!")
