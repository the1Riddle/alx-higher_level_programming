#!/usr/bin/python3
"""
    a function that returns an object represented by a JSON string
"""
import json


def from_json_string(my_str):
    """the body"""
    return (json.loads(my_str))
