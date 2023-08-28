#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for line in matrix:
        new_line = []
        for i in line:
            new_line.append(i * i)
        new_matrix.append(new_line)
    return new_matrix
    """new = matrix.copy()
    print("fgg ", new)
    for i in range(len(matrix)):
        new = list(map(lambda x: (list(map(lambda y: (y**2), x), matrix[i]))))
    return new"""
