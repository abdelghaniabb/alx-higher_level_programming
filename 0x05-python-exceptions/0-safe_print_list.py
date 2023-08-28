#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """print x elements of a list"""
    count = 0
    while count < x:
        try:
            print("{}".format(my_list[count]), end="")
            count = count + 1
        except:
            break
    print("")
    return count
