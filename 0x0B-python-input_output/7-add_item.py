#!/usr/bin/python3
"""
    a script that adds all arguments to a Python list,
    and then save them to a file
"""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
            __import__('6-load_from_json_file').load_from_json_file

    try:
        thelist = load_from_json_file("add_item.json")

    except FileNotFoundError:
        thelist = []
    thelist.extend(sys.argv[1:])
    save_to_json_file(thelist, "add_item.json")
