#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        my_list = []
    new = sorted(my_list)
    s = 0
    for i in range(0, len(new) - 1):
        if new[i] == new[i + 1]:
            continue
        else:
            s = s + new[i]
    s = s + new[i + 1]
    return s
