#!/usr/bin/pyhton3
"""
    a function that writes a string to a text file (UTF8)
    and returns the number of characters written
"""


def write_file(filename="", text=""):
    with open(finename, mode='w', encoding='utf8') as thefile:
        return (thefile.write(text))
