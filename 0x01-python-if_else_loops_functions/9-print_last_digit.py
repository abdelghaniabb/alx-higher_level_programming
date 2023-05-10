#!/usr/bin/python3
def print_last_digit(number):
    n_str = repr(abs(number))
    n = int(n_str[-1])
    print("{}".format(n), end="")
    return n
