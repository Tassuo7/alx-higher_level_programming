#!/usr/bin/python3
"""creates a class Rectangle that defines a rectangle"""


class Rectangle:
    """Rectangle with private instance attributes width and height
    and public instance methods area and perimeter
    and print the rectangle with the character #
    and recreate a new instance with eval
    and print msg when deleted"""

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

    def area(self):
        """define area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """define perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return ((2 * self.width) + (2 * self.height))

    def __str__(self):
        """returns string rectangle"""
        rec_str = ""
        if self.width == 0 or self.height == 0:
            return (rec_str)
        for row in range(self.height):
            for column in range(self.width):
                rec_str += "#"
            rec_str += "\n"
        rec_str = rec_str[:-1]
        return (rec_str)

    def __repr__(self):
        """return a string representation of the rectangle
        to be able to recreate a new instance by using eval()"""
        rec_str = "Rectangle(%s, %s)" % (self.width, self.height)
        return (rec_str)

    def __del__(self):
        """Print the message Bye rectangle... when deleted"""
        print("Bye rectangle...")
