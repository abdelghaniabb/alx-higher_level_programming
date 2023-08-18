#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new = []
    for k in a_dictionary:
        if a_dictionary[k] is value:
            new.append(k)
    for k in new:
        a_dictionary.pop(k)
    return a_dictionary
