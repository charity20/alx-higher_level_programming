#!/usr/bin/python3
"""Module defining the class Student"""


class Student:
    """define the atributes of a student"""

    def __init__(self, first_name, last_name, age):
        """create new public instances of a student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return dict representation of class """

        return self.__dict__
