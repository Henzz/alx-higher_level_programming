#!/usr/bin/python3
"""
test_square.py

Test class for the Square class in `models/square.py`

Classes:
    TestSquare
"""
import unittest
from models.square import Square
from io import StringIO
from unittest.mock import patch


class TestSquare(unittest.TestCase):
    """
    Test case for the Square class.

    Methods:
        test_square_constructor(self)
    """

    def test_square_constructor(self):
        """Test the constructor of the Square class."""
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_str(self):
        """Test the __str__ method of the Square class."""
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")


if __name__ == '__main__':
    unittest.main()
