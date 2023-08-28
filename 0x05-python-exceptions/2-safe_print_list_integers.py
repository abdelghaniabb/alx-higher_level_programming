#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """didn´t work"""
    count = 0
    index = 0
    while index < x:
        try:
            value = int(my_list[index])
        except Exception:
            index = index + 1
            continue
        count = count + 1
        print("{:d}".format(my_list[index]), end="")
        index = index + 1
    print("")
    return count
            