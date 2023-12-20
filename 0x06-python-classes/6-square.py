#!/usr/bin/python3

"""Define a class square."""


class Square:
    """
    A class that defines a square.

    Attributes:
        size (int): The length of the square's length.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object. Assigns size to private attribute size if
        size type is an integer.

        Args:
            size (int): The length of the square's length.
            position (tuple): The position of the square.
        """

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """
        Retruns the position of the square.

        Returns:
            Retruns the position of the square.
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the new position for the square.

        Args:
            value: New position of the square.
        """

        j = 0
        for i in value:
            j += 1
        if j != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for i in value:
            if not type(i) is int:
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
        A Function that prints space with the size of postion[0 and prints # * size on stdout.
        If size is 0 prints empty line.
        """

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()

            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
