#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """defines a square with Private instance attribute: size"""

    def __init__(self, size=0):
        """Instantiation with optional size
        must be an integer, otherwise raise a TypeError exception """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
