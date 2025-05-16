#!/usr/bin/python3
"""This module provides a function to divide all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number.

    Args:
        matrix (list of lists): A matrix of integers/floats.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with the divided values.

    Raises:
        TypeError: If the matrix is not a list of lists of int/float.
        TypeError: If rows of the matrix are not of the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = None
    for row in matrix:
        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
