#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Defines a new square. """

    def __init__(self, size=0):
        """Initializes size and araes of a new square

        Args:
            size (int): size of the square. """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Define the area of the square"""
        return (self.__size ** 2)
