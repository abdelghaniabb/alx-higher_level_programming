#!/usr/bin/python3
"""divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
        divides all elements of matrix
        Args:
            matrix: list of lists
            div: number
        Raises:
            TypeError: matrix and div must be numbers
    """
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if not (isinstance(item, int) or isinstance(item, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            new_row.append(round(item / div, 2))
        new_matrix.append(new_row)
    return new_matrix
