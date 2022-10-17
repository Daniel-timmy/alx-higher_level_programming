#!/usr/bin/python3

"""A class that defines a rectangle"""

class Rectangle:
    """An empty class representing rectangle"""
    def __init__(self, width=0, height=0):
        """ Method that initializes a rectangle instance

        Args:
            width: width of the rectangle
            height: height of the rectangle

        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height
    @property.setter
    def width(self, value):
        """ sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def width(self):
        """ Returns thewidth """
        return self.__width

    @property.setter
    def height(self, value):
        """ sets the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    @property
    def height(self):
        """returns the height attribute"""
        return self.__height