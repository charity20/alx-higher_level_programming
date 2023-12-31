#!/usr/bin/python3
"""Defines a class Rectangle based on 7-base_geometry.py"""

BaseGeometry = __import__('9-rectangle').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""

    def __init__(self, width, height):
        """define rectangle properties """

        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
