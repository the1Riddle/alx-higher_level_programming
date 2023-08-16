#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return
    new_list = list(map(lambda c: replace if c == search else c, my_list))
    return (new_list)
