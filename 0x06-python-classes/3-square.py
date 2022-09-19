#!/usr/bin/python3
"""Square Class."""
class Square:
    '''Represent a square.'''

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: if size < 0.
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''Public method for area of a square
        return value: area of a square
        '''
        return self.__size ** 2
