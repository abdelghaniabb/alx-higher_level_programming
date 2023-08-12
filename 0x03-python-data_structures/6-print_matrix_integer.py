#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    else:
        for line in matrix:
            for i in range(0, len(line) - 1):
                print("{} ".format(line[i]), end="")
            print("{}".format(line[len(line) - 1]))
