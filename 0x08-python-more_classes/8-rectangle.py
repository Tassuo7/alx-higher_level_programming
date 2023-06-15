#!/usr/bin/python3
"""creates a class Rectangle that defines a rectangle"""


class Rectangle:
    """Rectangle with private instance attributes width and height
    and public instance methods area and perimeter
    and print the rectangle with a given symbol
    and recreate a new instance with eval
    and print msg when deleted
    and calculate number of instances"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initialisation of instances width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                rec_str += str(self.print_symbol)
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
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not rect_1:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not rect_2:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return (rect_2)
        else:
            return (rect_1)
