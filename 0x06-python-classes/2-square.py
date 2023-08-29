#!/usr/bin/python3
"""Defines the class Square."""


class Square:
    """Defines a respresentation of a Square."""
    def __init__(self, size=0):
        """Initializes the size of a new square.

        Args:
            size (int): Size of the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
