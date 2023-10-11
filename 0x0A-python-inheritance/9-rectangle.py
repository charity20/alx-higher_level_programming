#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Base class geometry"""


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initialized rectangle attrubutes"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """calculate area"""

        return self.__width * self.__height

    def __str__(self):
        """string representation"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
