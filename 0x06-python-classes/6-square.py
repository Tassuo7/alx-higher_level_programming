#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:

    """define a square with Private instance attribute: size
    Instantiation with optional size"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """property def position(self): to retrieve it"""
        return self.__position

    @position.setter
    def position(self, value):
        """property setter def position(self, value): to set it"""
        if ((not isinstance(value, tuple) or len(value) != 2) or
                (not isinstance(value[0], int) and not isinstance(value[1], int))
                or (if not value[0] >= 0 and not value[1] >= 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Public instance method: def area self
        that returns the current square area"""
        return(self.__size * self.__size)

    def my_print(self):
        """Public instance method: def my_print(self)
        that prints in stdout the square with the character #"""
        if self.__size != 0:
            for i in range(self.__size):
                print("#" * self.__size)
        else:
            print()
