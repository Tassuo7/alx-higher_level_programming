#!/usr/bin/python3
""" a class Square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """the class Square that inherits from Rectangle with area"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """implementation of the area"""
        return (self.__size * self.__size)
