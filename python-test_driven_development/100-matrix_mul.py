#!/usr/bin/python3
"""Module for matrix multiplication."""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices m_a and m_b.

    Args:
        m_a: list of lists of ints/floats
        m_b: list of lists of ints/floats

    Returns:
        A new matrix that is the product of m_a and m_b.

    Raises:
        TypeError, ValueError: if inputs are invalid
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(
        isinstance(el, (int, float)) for row in m_a for el in row
    ):
        raise TypeError("m_a should contain only integers or floats")
    if not all(
        isinstance(el, (int, float)) for row in m_b for el in row
    ):
        raise TypeError("m_b should contain only integers or floats")

    row_length = len(m_a[0])
    if not all(len(row) == row_length for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    row_length = len(m_b[0])
    if not all(len(row) == row_length for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            total = 0
            for k in range(len(m_b)):
                total += m_a[i][k] * m_b[k][j]
            new_row.append(total)
        result.append(new_row)

    return result
