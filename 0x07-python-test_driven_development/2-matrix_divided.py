#!/usr/bin/python3
"""
divide a matrix
the matrix must be divided by div
div must be an integer number
"""


def matrix_divided(matrix, div):
    """
    each element in the matrix
    must be divided by div
    """
    new_matrix = []
    count = len(matrix[0])

    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for x in range(len(matrix)):
        new_matrix.append([])
        for z in range(len(matrix[x])):
            if len(matrix[x]) != count:
                raise TypeError("Each row of the matrix "
                                "must have the same size")
            wr = isinstance(matrix[x][z], (int, float))
            if wr is False:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
            new_matrix[x].append(round(matrix[x][z] / div, 2))
    return new_matrix
