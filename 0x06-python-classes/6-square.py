#!/usr/bin/python3

"""Define a class square."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square object.
        Assigns size to private attribute size if size type is an integer.

        Args:
            size (int): The length of the square's length.
            position (int, int): The position of the square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2 or type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1])  is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        A Function that calculates the area of the square.

        Returns:
            int: the area of a square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        A Function that prints space with the size of postion[0]
        and prints # * size on stdout.
        If size is 0 prints empty line.
        """

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()

            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
