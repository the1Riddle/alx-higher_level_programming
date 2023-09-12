#!/usr/bin/python3
"""
    a function that writes an Object to a text file,
    using a JSON representation:
"""
import json


def save_to_json_file(my_obj, filename):
    """the body"""
    with open(filename, mode='w' encoding='utf-8') as thefile:
        json.dump(my_obj, thefile, ensure_ascii=False)
