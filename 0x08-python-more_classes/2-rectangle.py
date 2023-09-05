#!/usr/bin/python3
""" short desc """


class Rectangle:
    """a class Rectangle that defines a rectangle """

    def __init__(self, width=0, height=0):
        """ the initialization """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ gets the with of the rec from ^^ def"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ now it gets the hight"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """
            Sets the instance of the hight
            value of the height, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            now i will be calculating the area
            the fomulae is given by height * width
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
            now am geting the perimeter
            the fomulae is given by 2 * (height + width) for all sides
            if length && width = 0 : 0
        """
        if self.__height == 0 or self.__width == 0:
            return (0)
        return (2 * (self.__width + self.__height))
