#!/usr/bin/python3
"""
test_rectangle.py

Test class for the Rectangle class in `models/rectangle.py`

Classes:
    TestRectangle
"""
import unittest
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    """
    Test case for the Rectangle class.

    Methods:
        test_rectangle_creation(self)
        test_rectangle_setters(self)
        test_rectangle_valid_values(self)
        test_rectangle_invalid_width(self)
        test_rectangle_invalid_height(self)
        test_rectangle_invalid_x(self)
        test_rectangle_invalid_y(self)
        test_rectangle_area_value(self)
        test_rectangle_display(self)
        test_rectangle_str_default(self)
        test_rectangle_str_large_values(self)
        test_display_default(self)
        test_display_with_coordinates(self)
    """

    def test_rectangle_creation(self):
        """
        Test the creation of a Rectangle instance.
        """

        rectangle = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)
        self.assertEqual(rectangle.id, 1)

    def test_rectangle_setters(self):
        """
        Test the setter methods.
        """

        rectangle = Rectangle(5, 10)
        rectangle.width = 7
        rectangle.height = 12
        rectangle.x = 3
        rectangle.y = 4

        self.assertEqual(rectangle.width, 7)
        self.assertEqual(rectangle.height, 12)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)

    def test_rectangle_valid_values(self):
        """Test creating a rectangle with valid parameters"""
        r = Rectangle(5, 10, 2, 3)

        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_rectangle_invalid_width(self):
        """Test creating a rectangle with invalid width"""
        with self.assertRaises(TypeError):
            r = Rectangle("invalid", 10, 2, 2)

        with self.assertRaises(ValueError):
            rectangle = Rectangle(-5, 10, 2, 2)

    def test_rectangle_invalid_height(self):
        """Test creating a rectangle with invalid height"""
        with self.assertRaises(TypeError):
            r = Rectangle(4, "invalid", 2, 2)

        with self.assertRaises(ValueError):
            rectangle = Rectangle(5, -10, 2, 2)

    def test_rectangle_invalid_x(self):
        """Test creating a rectangle with invalid x"""
        with self.assertRaises(TypeError):
            r = Rectangle(5, 10, "invalid", 2)

        with self.assertRaises(ValueError):
            rectangle = Rectangle(5, 10, -2, 2)

    def test_rectangle_invalid_y(self):
        """Test creating a rectangle with invalid y"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, 2, "invalid")

        with self.assertRaises(ValueError):
            rectangle = Rectangle(5, 10, 2, -2)

    def test_rectangle_area_value(self):
        """Test a rectangle area value is correct"""
        r = Rectangle(10, 5, 2, 2)

        self.assertEqual(r.area(), 50)

        r2 = Rectangle(8, 4, 1, 6)

        self.assertEqual(r2.area(), 32)

    def test_rectangle_display(self):
        """Test a rectangle display on stdout is correct"""
        r = Rectangle(5, 3)

        expected_output = "#####\n" \
            "#####\n" \
            "#####\n"

        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_rectangle_str_default(self):
        """Test a rectangle that has specified coordinates and dimensions"""
        r = Rectangle(5, 3, 2, 1, 10)
        expected = "[Rectangle] (10) 2/1 - 5/3"
        self.assertEqual(str(r), expected)

    def test_rectangle_str_large_values(self):
        """Test a rectangle that has large values for coordinates and
        dimensions"""
        r = Rectangle(1000000, 1000000, 999999, 999999, 9999)
        expected = "[Rectangle] (9999) 999999/999999 - 1000000/1000000"
        self.assertEqual(str(r), expected)

    def test_display_default(self):
        r = Rectangle(5, 3)
        expected_output = "#####\n#####\n#####\n"

        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display_with_coordinates(self):
        r = Rectangle(4, 2, 2, 1)
        expected_output = "  ####\n  ####\n"

        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()