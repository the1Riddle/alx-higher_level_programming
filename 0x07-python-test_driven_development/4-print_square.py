#!/usr/bin/bash
""" a function that prints a square with # character """


def print_square(size):
    """ the body of the function """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    """the square constraction"""
    for x in range(size):
        for y in range(size):
            print("#", end="")
        print()
