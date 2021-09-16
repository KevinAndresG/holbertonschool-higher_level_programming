#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = []
    for i in matrix:
        matrix2.append([j**2 for j in i])

    return matrix2
