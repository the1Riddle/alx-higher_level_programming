#!/usr/bin/python3
""""
     a function that removes all characters c and C from a string
"""""
def no_c(my_string):
    new_str = ' '
    for char in my_string:
        if char != 'c' and char != 'C':
            new_str += char
    return (new_str)
