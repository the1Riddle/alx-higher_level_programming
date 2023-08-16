#!/usr/bin/python3
def uniq_add(my_list=[]):
    return (lambda x: sum(set(x)))(my_list)
