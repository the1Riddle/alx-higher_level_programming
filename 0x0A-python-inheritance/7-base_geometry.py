#!/usr/bin/python3
"""a class BaseGeometry"""


class BaseGeometry:
    """the body"""

    def area(self):
        """if not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a parameter format"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
