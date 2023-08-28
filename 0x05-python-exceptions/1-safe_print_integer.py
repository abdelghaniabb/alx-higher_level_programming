#!/usr/bin/python3
def safe_print_integer(value):
    """prints an integer with "{:d}".format()"""
    try:
        value = int(value)
    except Exception:
        return False
    print("{:d}".format(value))
    return True
