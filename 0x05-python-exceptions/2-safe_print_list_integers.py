#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    values = 0
    for i in range (0, x):
        try:
            print("{:d}".format(my_list[i]), end='')
            values += 1
        except:
            pass
    print()
    return (values)
