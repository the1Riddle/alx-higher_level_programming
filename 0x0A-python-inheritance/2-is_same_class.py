#!/usr/bin/python3
"""
     function that returns True if the object is exactly
     an instance of the specified class ; otherwise it returns False
"""


def is_same_class(obj, a_class):
    """the body"""
    if type(obj) == a_class:
        return (True)
    return (False)
