#!/usr/bin/python3
""" a function that adds two ints """


def add_integer(a, b=98):
    """ the body """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return (int(a + b))
