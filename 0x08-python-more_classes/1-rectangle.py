#!/usr/bin/python3
"""creates a class Rectangle that defines a rectangle"""


class Rectangle:
    """Rectangle with private instance attributes width and height"""

    def __init__(self, width=0, height=0):
        """initialisation of instances width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get private instance attribute width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """get private instance attribute height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """set private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
