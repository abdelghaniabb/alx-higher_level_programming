#!/usr/bon/python3
def print_sorted_dictionary(a_dictionary):
    new = dict()
    for key in a_dictionary:
        new[key] = a_dictionary[key]

    for key in dict(sorted(new.items())):
        print("{:s}: {}".format(key, new[key]))
