#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """
         returns a list of lists of integers
         representing the Pascal’s triangle of n
    """
    result = []
    if n <= 0:
        return result

    
