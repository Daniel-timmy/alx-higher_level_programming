#!/usr/bin/python3
class Square:
    """Class Square defines a square by its size
    """
    def __init__(self, size=0):
        """ Initializing this square class
        Args:
            size: represents the size of the square defined
        Raises:
            TypeError: if size is not innteger
            ValueError: if size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area of a square
        Returns: the area of the square
        """
        return (self.__size ** 2)
