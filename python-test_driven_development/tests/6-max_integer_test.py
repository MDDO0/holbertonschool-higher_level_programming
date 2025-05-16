#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        """Test list with increasing order"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test list not in order"""
        self.assertEqual(max_integer([1, 3, 2, 4]), 4)

    def test_max_at_beginning(self):
        """Test max at the beginning"""
        self.assertEqual(max_integer([5, 3, 2, 1]), 5)

    def test_all_negative(self):
        """Test list of negative numbers"""
        self.assertEqual(max_integer([-1, -4, -2, -10]), -1)

    def test_one_element(self):
        """Test list with one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Test empty list"""
        self.assertIsNone(max_integer([]))

    def test_equal_elements(self):
        """Test list with all same values"""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_float_numbers(self):
        """Test list with float numbers"""
        self.assertEqual(max_integer([1.2, 3.5, 2.1]), 3.5)

    def test_mix_int_float(self):
        """Test list with mix of ints and floats"""
        self.assertEqual(max_integer([1, 2.2, 3]), 3)

    def test_string_list(self):
        """Test list of strings"""
        self.assertEqual(max_integer(["a", "z", "b"]), "z")

    def test_string_chars(self):
        """Test string instead of list"""
        self.assertEqual(max_integer("Holberton"), "t")

    def test_empty_string(self):
        """Test empty string"""
        self.assertIsNone(max_integer(""))
