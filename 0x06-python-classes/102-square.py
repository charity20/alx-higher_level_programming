#!/usr/bin/python3
"""Define the class square."""


class Square:
    """Define the method square."""
    def __init__(self, size=0):
        """"Initialize the size of the square.

        Args:
            size (int): size of the square."""
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
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculoates the area of the square

        Returns:
            int: area of the square."""
        return (self.__size ** 2)

    def __eq__(self, other):
        """Compare area to other square"""
        return (self.area() == other.area())

    def __ne__(self, other):
        return (self.area() != other.area())

    def __gt__(self, other):
        return (self.area() > other.area())

    def __ge__(self, other):
        return (self.area() >= other.area())

    def __lt__(self, other):
        return (self.area() < other.area())

    def __le__(self, other):
        return (self.area() <= other.area())
