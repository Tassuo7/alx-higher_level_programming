#!/usr/bin/python3

"""does exactly the same as the following Python bytecode"""

import math


class MagicClass:
    """define a circle with some calculations"""

    def __init__(self, radius=0):
        """ initialize the Magic class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """define the area of the magic class"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """define the circumference of the magic class."""
        return 2 * math.pi * self.__radius
