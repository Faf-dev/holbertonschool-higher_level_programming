#!/usr/bin/python3
"""
matrix_divided : divide all the matrix
"""


def matrix_divided(matrix, div):
    """
    matrix_divided:

    parameter:
    matrix: the matrix to divide
    div: All elements of the matrix should be divided by div

    Return: result of the division
    """
    result = [[round(x / div, 2) for x in row] for row in matrix]
    return result
