#!/usr/bin/python3
"""Define the class square."""


class Square:
    """Define the method square."""
    def __init__(self, size=0):
        """"Initialize the size of the square.

        Args:
            size (int): size of the square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """the gutter used to retrieve the size of the squares side

        Returns:
            int: Size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter method for setting the size of the square.

        Args:
            value (int): New size of the sqaure"""
        
    def area(self):
        """Calculoates the area of the square

        Returns:
            int: area of the square."""
        return (self.__size ** 2)
