#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    count = 0
    try:
        while i + 1 <= x:
            print("{:d}".format(my_list[i]), end="")
            i = i + 1
            count = count + 1
    except Exception:
        i = i + 1
    print("")
    return count
