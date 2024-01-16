#!/usr/bin/python3
"""This module contains the definition of the `Base` class."""


class Base:
    """
    Base class representing a base object.

    Attributes:
        id (int): Public instance attribute representing the unique identifier
        of the object.

    Private Attributes:
        __nb_objects (int): Private class attribute representing the cound of
        created object.

    Methods:
        __init_(self, id=None)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int, optional): The unique identifier for the object.
            If provided, it will be assigned to the public instance
            attribute `id`. If not provided, the private class attribute
            `__nb_objects` will be incremented, and the new value will
            be assigned to the public instance attribute `id`.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
