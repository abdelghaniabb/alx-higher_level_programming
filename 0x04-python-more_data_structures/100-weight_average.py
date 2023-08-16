#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    s = 0
    for item in my_list:
        s = s + item[1]
    return s / len(my_list)
