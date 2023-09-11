#!/usr/bin/python3
"""
    a function that adds a new attribute to an object if it’s possible
"""


def add_attribute(obj, att, value):
    """
        dds the atribute if posible
        typeerror is raised if the attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
