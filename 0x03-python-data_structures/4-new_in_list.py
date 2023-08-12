#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = []
    for item in my_list:
        new.append(item)
    if idx >= 0 and idx <= len(my_list) - 1:
        new[idx] = element
    return new
