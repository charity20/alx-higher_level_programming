#!/usr/bin/python3
"""Base Geometry"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """calculate area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check if value is integer"""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
