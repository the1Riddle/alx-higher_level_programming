#!/usr/bin/bash
"""
    a function that prints a text with 2 new lines after the characters
    . , ? and :
"""


def text_indentation(text):
    """ the body of the function """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    space = True
    for char in text:
        if char in ('.', '?', ':'):
            result += char + '\n\n'
            space = True
        elif char == ' ' and space:
            continue
        else:
            result += char
            space = False

    print(result)
