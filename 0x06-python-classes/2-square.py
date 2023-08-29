#!/usr/bin/python3
""" a class Square that defines a square """


class Square:
    """
        the class's body
    """

    def __init__(self, size=0):
        """
            Square class contructor
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
