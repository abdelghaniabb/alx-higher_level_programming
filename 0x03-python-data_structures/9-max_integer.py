#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        my_list = []
    if len(my_list) == 0:
        max_i = None
    else:
        max_i = my_list[0]
        for i in my_list:
            if max_i < i:
                max_i = i
    return max_i
