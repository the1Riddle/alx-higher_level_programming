#!/usr/bin/python3
""" all about json"""


def class_to_json(obj):
    """Return the dictionary represntation of json."""
    return obj.__dict__
