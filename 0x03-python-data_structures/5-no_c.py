#!/usr/bin/python3
def no_c(my_string):
    arr = []
    for c in my_string:
        if c != 'c' and c != 'C':
            arr.append(c)
    return ''.join(arr)
