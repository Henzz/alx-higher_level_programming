#!/usr/bin/python3
"""This
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Prints in stdout the square values in string"""
        i = self.id
        x = self.x
        y = self.y
        size = self.width

        return f"[Square] ({i}) {x}/{y} - {size}"
