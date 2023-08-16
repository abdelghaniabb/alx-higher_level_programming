#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    for item in my_list:
        if item in new:
            continue
        else:
            new.append(item)
    return sum(new)
