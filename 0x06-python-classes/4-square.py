#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:

    """define a square with Private instance attribute: size
    Instantiation with optional size"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """property def size(self): to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter def size(self, value)"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public instance method: def area self
        that returns the current square area"""
        return(self.__size * self.__size)
