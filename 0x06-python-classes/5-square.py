#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = 0
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        i = 0
        j = 0
        if self.__size == 0:
            print()
        while i < self.__size:
            while j < self.__size:
                print("#", end='')
                j += 1
            print()
            i += 1
            j = 0
