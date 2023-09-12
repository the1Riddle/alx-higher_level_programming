#!/usr/bin/python3
"""a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """the body of the func"""
    with open(filename, mode='r', encoding='utf8') as text:
        print(text.read(), end='')
