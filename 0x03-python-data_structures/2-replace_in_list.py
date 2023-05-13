#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if my_list:
        if idx >= 0 and idx < len(my_list):
            my_list.insert(idx, element)
        return my_list