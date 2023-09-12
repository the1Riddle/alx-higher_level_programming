#!/usr/bin/python3
"""
    a function that writes a string to a text file (UTF8)
    and returns the number of characters written
"""


def write_file(filename="", text=""):
    """the body"""
    with open(filename, mode='w', encoding='utf-8') as thefile:
        return (thefile.write(text))
