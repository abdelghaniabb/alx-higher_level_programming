#!/usr/bin/python3
def weight_average(my_list=[]):
    s = 0
    for item in my_list:
        s = s + item[1]
    return s / len(my_list)
