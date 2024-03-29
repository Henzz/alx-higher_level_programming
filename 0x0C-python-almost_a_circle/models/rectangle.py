#!/usr/bin/python3
"""This module defines the Rectangle class, which represents
a rectangle shape. The Rectangle class inherits from the
Base class.

Private instance attributes:
    __width - The width of the rectangle.
    __height - The height of the rectangle.
    __x - The x-coordinate of the rectangle's position.
    __y - The y-coordinate of the rectangle's position.

Public getter and setter methods are provided for each
private attribure.
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class representing a rectangle object.
    """
    __width = None
    __height = None
    __x = None
    __y = None

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class.

        Args:
            width (int)
            height (int)
            x (int, optional)
            y (int, optional)
            id (int, optional)
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Prints in stdout the rectangle with the character #"""
        display_str = ""
        for _ in range(self.y):
            display_str += "\n"
        for _ in range(self.height):
            display_str += " " * self.x + "#" * self.width + "\n"
        print(display_str, end="")

    def update(self, *args, **kwargs):
        """Updates values in the rectangle starting from id to y coordinate.
        Added kwargs to get key/value pair and update"""
        if args:
            num_args = len(args)
            if num_args > 0:
                self.id = args[0]
            if num_args > 1:
                self.width = args[1]
            if num_args > 2:
                self.height = args[2]
            if num_args > 3:
                self.x = args[3]
            if num_args > 4:
                self.y = args[4]
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Prints in stdout the rectangle values in string"""
        """Prints in stdout the rectangle values in string"""
        i = self.id
        x = self.x
        y = self.y
        w = self.width
        h = self.height
        return f"[Rectangle] ({i}) {x}/{y} - {w}/{h}"
