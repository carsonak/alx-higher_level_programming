#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_list_of_ints(self):
        self.assertEqual(max_integer([0, 1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([0, 1]), 1)
        self.assertEqual(max_integer([57, 2, 3, 20, 58]), 58)
        self.assertEqual(max_integer([0, 0, 0, 77, 77, 77]), 77)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([-3, -2, -1, 0]), 0)
        self.assertEqual(max_integer([400, 400, 400, 400]), 400)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_list_of_non_integers(self):
        self.assertEqual(max_integer(["are", " not", " ints"]), "are")
        self.assertEqual(max_integer([37.055, 12.1, 54.77, 3.333]), 54.77)
        self.assertEqual(max_integer([True, False, True, False]), True)

    def test_not_a_list(self):
        self.assertEqual(max_integer((45, 77, 12, 12)), 77)
        self.assertEqual(max_integer("234519"), "9")

    def test_exceptions(self):
        with self.assertRaises(TypeError):
            max_integer()
            max_integer([0, float("infinity")], float("nan"))
            max_integer(None)
            max_integer(float("infinity"))
            max_integer(45)
            max_integer([54, 69, "234", "999.99"])
