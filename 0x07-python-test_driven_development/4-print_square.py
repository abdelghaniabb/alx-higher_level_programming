#!/usr/bin/python3
""" prints a square"""


def print_square(size):
    """
        prints a square with the character #
        Args:
            size: the size of the square
        Returns:
            None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(size):
        print("#" * size)
