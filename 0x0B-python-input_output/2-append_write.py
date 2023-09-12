#!/usr/bin/python3
"""
    a function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
"""


def append_write(filename="", text=""):
    """the body"""
    with open(filename, mode='a', encoding='utf-8') as thefile:
        return (thefile.write(text))
