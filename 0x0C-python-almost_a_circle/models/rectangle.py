#!/usr/bin/python3
"""define class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """the Class constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """Getter for the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        """Getter for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def y(self):
        """Getter for the y """
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def x(self):
        """Getter for the x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for sf in range(self.y):
            print()
        for m in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            elem = ["id", "width", "height", "x", "y"]
            for f, ar in enumerate(args):
                setattr(self, elem[f], ar)
        else:
            for k, va in kwargs.items():
                setattr(self, k, va)

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.width * self.height

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y,
                }

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height
                )
