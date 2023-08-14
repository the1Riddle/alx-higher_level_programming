#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multpls = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multpls.append(True)
        else:
            multpls.append(False)
    return (multpls)
