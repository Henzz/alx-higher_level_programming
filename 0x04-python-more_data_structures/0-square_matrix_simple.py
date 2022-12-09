#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if len(matrix) != 0:
        new_matrix = []
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix[i])):
                row.append(matrix[i][j] * matrix[i][j])
            new_matrix.append(row)
        return new_matrix
