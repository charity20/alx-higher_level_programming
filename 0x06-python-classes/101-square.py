#!/usr/bin/python3
"""Define the class square."""


class Square:
    """Define the method square."""
    def __init__(self, size=0, position=(0, 0)):
        """"Initialize the size of the square.

        Args:
            size (int): size of the square."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """the gutter used to retrieve the size of the squares side"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter method for setting the size of the square.

        Args:
            value (int): New size of the sqaure"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter method for the position of a square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setter method for the positiion of the square.

        Args:
            value (int): The new posution pof the square. """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculoates the area of the square."""
        return (self.__size ** 2)

    def my_print(self):
        """Return the area of the square with the character # """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Custom string representation of the Square instance.

        Returns:
            str: A string representation of the square.
        """
        sr = ""
        if self.__size == 0:
            sr += '\n'
        else:
            for _ in range(self.__position[1]):
                sr += '\n'
            for _ in range(self.__size):
                sr += " " * self.__position[0] + "#" * self.__size + '\n'
        return sr.rstrip()
