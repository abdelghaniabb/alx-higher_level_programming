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
    result = [[1]]
    if n == 1:
        return result
    result = [[1], [1, 1]]
    for i in range(1, n):
        if i != 1:
            row = [1]
            for j in range(1, i):
                row.append(result[-1][j - 1] + result[-1][j])
            row.append(1)
            result.append(row)
    return result
