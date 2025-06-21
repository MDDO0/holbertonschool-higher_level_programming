#!/usr/bin/python3
"""Defines CustomObject class with pickle serialization/deserialization."""
import pickle


class CustomObject:
    """Custom class that can be serialized with pickle."""

    def __init__(self, name="", age=0, is_student=False):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print object attributes in the required format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance to a file.

        Args:
            filename (str): Destination filename for the pickle.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            # Ignore all errors; requirement: no exception propagation.
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an instance from a pickle file.

        Args:
            filename (str): Source filename of the pickle.

        Returns:
            CustomObject | None: Deserialized object or None on failure.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            return obj if isinstance(obj, cls) else None
        except Exception:
            return None
