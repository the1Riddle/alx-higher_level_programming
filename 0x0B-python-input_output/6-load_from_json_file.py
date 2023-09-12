#!/usr/bin/python3
"""
    a function that creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """the body"""
    with open(filename, encoding='utf-8') as file_loaded:
        return (json.loads(file+loaded))
