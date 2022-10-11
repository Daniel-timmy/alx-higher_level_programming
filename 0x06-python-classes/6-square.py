#!/usr/bin/python3
class Square:
    """Class Square defines a square by its size
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Initializing this square class
        Args:
            position: position
            size: represents the size of the square defined
        """
        self.size = size
        self.position = position

    @property
    def position(self):
        """
        Method that returns the position value
        """
        return self.__postion

    @position.setter
    def position(self, value):
        """
        Method that sets the position value of a square object
    Args: value as atuple of two positive integers
    Raises:
        TypeError: if value is not a tuple or any int in tuple < 0
        """
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
        Calculate the area of a square
        Returns: the area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """
            prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()
    @property
    def size(self):
        """
        Returns: the value of size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Sets the value of size

        Args:
            value: value to be set
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        if not isintance(value, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
