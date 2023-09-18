#!/usr/bin/python3
"""
    the square class implementation of the rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """the body of the class"""

    def __init__(self, size, x=0, y=0, id=None):
        """ initialization"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ the width of the size"""
        return (self.width)

    @size.setter
    def size(self, value):
        """some comment """
        self.width = value
        self.height = value

    def __str__(self):
        """^2 class str"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    def update(self, *args, **kwargs):
        """ prop update """
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ ret the prop dict """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
