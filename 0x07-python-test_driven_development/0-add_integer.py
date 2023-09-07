#!/usr/bin/python3
""" add integers"""


def add_integer(a, b=98):
    """
        this function adds tow integers
        Args:
            a: first number
            b: second number
        Raises:
            TypeError: the numbers must be integers
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an intger")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
