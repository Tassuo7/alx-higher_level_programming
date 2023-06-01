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
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """property def position(self): to retrieve it"""
        return self.__position

    @position.setter
    def position(self, value):
        """property setter def position(self, value): to set it"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Public instance method: def area self
        that returns the current square area"""
        return(self.__size * self.__size)

    def my_print(self):
        """Public instance method: def my_print(self)
        that prints in stdout the square with the character #
        position should be use by using space"""
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """define a Square instance should have the same behavior"""
        if self.__size != 0:
            for i in range(self.__position[1]):
                print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for i in range(self.__size):
                print("#", end="")
            if i != self.__size - 1:
                print("")
        return ("")
