#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class to test the function max_integer"""
    # Test with only integer
    def test_integer(self):
        self.assertEqual(max_integer([3, 6, 1, 9]), 9)

    # Test with the max value first
    def test_first(self):
        self.assertEqual(max_integer([10, 1, 2, 8]), 10)

    # Test with negative integer
    def test_negative(self):
        self.assertEqual(max_integer([-10, -1, -8, -49]), -1)

    # Test with one integer
    def test_with_oneint(self):
        self.assertEqual(max_integer([9]), 9)

    # Test with empty list
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    # Test with True in list
    def test_string_inlist(self):
        self.assertEqual(max_integer([1, True, 10, 5]), 10)

    # Test with float in list
    def test_float(self):
        self.assertEqual(max_integer([1.5, 1.7, 3.7, 3.9]), 3.9)

    # Test with negative, positive and float
    def test_boulgiboulga(self):
        self.assertEqual(max_integer([-1, 8, 8.4, -22]), 8.4)

    # make sure type errors are raised if necessary
    def test_types(self):
        self.assertRaises(TypeError, max_integer, True)

    def test_string(self):
        self.assertRaises(TypeError, max_integer, str)
