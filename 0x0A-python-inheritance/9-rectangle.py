#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """the class rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """initializes Rectangle instances width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

def __str__(self):
    """description of the Rectangle"""
    str_desc = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
    return str_desc

def area(self):
    """returns area of rectangle"""
    return (self.__width * self.__height)
