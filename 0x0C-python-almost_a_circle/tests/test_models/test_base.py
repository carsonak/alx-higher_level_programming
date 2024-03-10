#!/usr/bin/python3
"""Module for test_base."""
from models.base import Base
import unittest


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b74 = Base(74)

    def tearDown(self):
        """Reset public class attribute."""

        setattr(Base, "_Base__nb_objects", 0)

    def test_base_init(self):
        """Test if Base.id initialises properly."""

        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 2)
        self.assertEqual(self.b74.id, 74)
