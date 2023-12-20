#!/usr/bin/python3

"""Define a class square."""


class Square:
    """
    A class that defines a square.

    Attributes:
        size (int): The length of the square's length.
    """

    def __init__(self, size=0):
        """
        Initializes a Square object. Assigns size to private attribute size if
        size type is an integer.

        Args:
            size (int): The length of the square's length.
        """

        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        A Function that calculates the area of the square.

        Returns:
            int: the area of a square.
        """

        return self.__size ** 2
