#!/usr/bin/python3

"""divides all elements of a matrix by a given divisor"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given divisor"""
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(isinstance(element, (int, float))
               for row in matrix for element in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if (len(matrix) > 0 and
            not all(len(row) == len(matrix[0]) for row in matrix)):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        result_matrix.append(new_row)

    return result_matrix
