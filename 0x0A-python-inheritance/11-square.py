#!/usr/bin/python3
"""a class Square that inherits frm Rectangle"""


Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    """the class Square that inherits frm Rectangle
    with area and description"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """returns the area of the square"""
        return (self.__size * self.__size)

    def __str__(self):
        """description of the square"""
        str_rep = "[Square] " + str(self.__size) + "/" + str(self.__size)
        return str_rep
