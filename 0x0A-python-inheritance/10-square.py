#!/usr/bin/python3
"""
    a class Square that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ the body of the class """

    def __init__(self, size):
        """the p method"""
        super().integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """the output"""
        return (self.__size * self.__size)
