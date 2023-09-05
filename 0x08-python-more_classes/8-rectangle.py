#!/usr/bin/python3
""" shoer desc """


class Rectangle:
    """a class Rectangle that defines a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ the instanciation """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ returns the string rep"""
        if self.__height == 0 or self.__width == 0:
            return ''
        _str = ''
        for x in range(self.__height):
            for y in range(self.__width):
                _str += str(self.print_symbol)
            _str += '\n'
        return (_str[:-1])

    def __repr__(self):
        """ret str rep"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """print on delete"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """gets the width"""
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
        """ gets the hight"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the hight """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ area calculation """
        return self.__width * self.__height

    def perimeter(self):
        """ perimeter calculation """
        if self.__height == 0 or self.__width == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compare to find the big area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return (rect_1)
        if rect_1.area() < rect_2.area():
            return (rect_2)
