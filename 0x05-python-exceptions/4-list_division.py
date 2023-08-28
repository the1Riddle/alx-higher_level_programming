#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    hold_result = 0
    for x in range(0, list_length):
        try:
            hold_result = my_list_1[x] / my_list_2[x]
        except (TypeError):
            hold_result = 0
            print('wrong type')
        except (ZeroDivisionError):
            hold_result = 0
            print('division by 0')
        except (IndexError):
            hold_result = 0
            print('out of range')
        finally:
            pass
        new_list.append(hold_result)
    return (new_list)
