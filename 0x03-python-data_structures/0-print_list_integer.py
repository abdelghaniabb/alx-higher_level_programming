#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if not my_list:
        exit()
    for i in reversed(my_list):
        print("{:d}".format(i))