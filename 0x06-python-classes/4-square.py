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

        self.__size = size

    @property
    def size(self):
        """
        Returns the size of the square.

        Returns:
            int: The size of the square.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the new size for the square.

        Args:
            value: New size of the square.
        """

        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        A Function that calculates the area of the square.

        Returns:
            int: the area of a square.
        """

        return self.__size ** 2
