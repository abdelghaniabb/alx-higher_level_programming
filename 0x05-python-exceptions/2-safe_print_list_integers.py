#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """didn´t work"""
    count = 0
    i = 0
    while i < x:
        try:
            value = int(my_list[i])
        except Exception:
            i = i + 1
            continue
        count = count + 1
        print("{:d}".format(my_list[i]), end="")
        i = i + 1
    print("")
    return count
