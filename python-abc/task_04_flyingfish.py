#!/usr/bin/env python3
"""Defines Fish, Bird, and FlyingFish classes to demonstrate multiple inheritance."""


class Fish:
    """Fish class with swim and habitat behavior."""

    def swim(self):
        """Print swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Print habitat of fish."""
        print("The fish lives in water")


class Bird:
    """Bird class with fly and habitat behavior."""

    def fly(self):
        """Print flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Print habitat of bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class that inherits from both Fish and Bird."""

    def fly(self):
        """Override fly method with custom behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override swim method with custom behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override habitat method with custom behavior."""
        print("The flying fish lives both in water and the sky!")
