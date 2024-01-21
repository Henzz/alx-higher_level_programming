#!/usr/bin/python3
"""
test_base.py

Test class for the `Base` class in `models/base.py`

Classes:
    TestBase
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test case for the `Base` class.

    Methods:
        setUp(self)
        test_base_with_id(self)
        test_base_without_id(self)
        test_base_private_attributes(self)
    """

    def setUp(self):
        """
        Pre-test setup method that resets the `__nb_objects`
        attribute of the `Base` class to 0.
        This ensures a clean state for each test case.
        """
        Base._Base__nb_objects = 0

    def test_case_with_id(self):
        """
        Test the behavior when an `id` is provided.
        """

        b1 = Base(id=42)
        self.assertEqual(b1.id, 42)

    def test_base_without_id(self):
        """
        Test the behavior when no `id` is provided.
        """

        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_base_private_attributes(self):
        """
        Test that attempting to access the private attribute
        `__nb_objects` raises an `AttributeError`.
        """

        b1 = Base()
        with self.assertRaises(AttributeError):
            _ = b1.__nb_objects


if __name__ == '__main__':
    unittest.main()
