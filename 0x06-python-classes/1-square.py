#!/usr/bin/python3
"""Defines a class square."""


class square:
    """
    Defines the square size as a private attribute.

    Attribute:
        size: size of thge square.
    """
    def __init__(self, size):
        """
        Initialize the size of the square.
        
        Args:
            size (int): size of the square.
        """
        self.__size = size
