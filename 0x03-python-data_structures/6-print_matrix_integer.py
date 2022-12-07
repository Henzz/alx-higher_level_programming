#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) != 0:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j != 2:
                    print("{:d}".format(matrix[i][j]), end=" ")
                else:
                    print("{:d}".format(matrix[i][j]), end="")
            print("", end="\n")
