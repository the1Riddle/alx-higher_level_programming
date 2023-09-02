#!/usr/bin/python3
""" a function that divides all elements of a matrix. """


def matrix_divided(matrix, div):
    """
        the body of the function
        returns the new matrix
    """

    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        for col in row:
            if type(col) is not int and type(col) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    rows_L = []
    for row in matrix:
        rows_L.append(len(row))
    if not all(col == rows_L[0] for col in rows_L):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(col / div, 2) for col in row] for row in matrix]

    return (new_matrix)
