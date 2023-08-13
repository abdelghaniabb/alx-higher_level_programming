#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    else:
        for line in matrix:
            for i in range(0, len(line) - 1):
                print("{:d} ".format(line[i]), end="")
            print("{:d}".format(line[len(line) - 1]))
