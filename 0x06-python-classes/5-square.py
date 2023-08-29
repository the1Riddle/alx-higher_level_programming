#!/usr/bin/python3
""" a class Square that defines a square """


class Square:
    """ the class body """
    def __init__(self, size):
        """
            Square contructor
        """
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
            Returns the area of tha square.
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
            Print the square and character in stdout
        """
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
