#!/usr/bin/python3
"""
    a class Student that defines a student
"""


class Student:
    """ the body of the class"""

    def __init__(self, first_name, last_name, age):
        """
            Initialize student props in contructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """make it to json"""
        return self.__dict__
