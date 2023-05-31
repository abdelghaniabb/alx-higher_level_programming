#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        while count + 1 <= x:
            print("{}".format(my_list[count]), end="")
            count = count + 1
    except Exception:
        print("")
        return count
    print("")
    return count
