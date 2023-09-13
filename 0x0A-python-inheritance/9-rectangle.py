#!/usr/bin/python3
"""
    a class Rectangle that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ the class body """

    def __init__(self, width, height):
        """the first of first"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """the area"""
        return (self.__width * self.__height)

    def __str__(self):
        """now the output"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
