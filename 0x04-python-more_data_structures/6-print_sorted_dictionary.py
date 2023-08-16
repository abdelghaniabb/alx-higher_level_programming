#!/usr/bon/python3
def print_sorted_dictionary(a_dictionary):
    for c in dict(sorted(a_dictionary.items())):
        print("{:s}: {}".format(c, a_dictionary[c]))
