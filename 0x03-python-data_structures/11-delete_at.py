#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new = my_list
    j = 0
    if idx >= 0 and idx < len(my_list):
        for i in range(0, len(my_list)):
            if i != idx:
                new[j] = my_list[i]
                j = j + 1
        my_list = new
    return my_list
