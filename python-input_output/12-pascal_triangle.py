#!/usr/bin/python3
"""
create a function that return a list of lists of int
representing the pascal's triangle of 'n'
"""


def pascal_triangle(n):
    """
    return a list of lists of int
    representing the pascal's triangle of 'n'
    """
    triangle = []

    if n <= 0:
        return []
    else:
        triangle.append([1])

        for i in range(1, n):
            prev_ligne = triangle[i - 1]
            new_ligne = [1]

            for j in range(len(prev_ligne) - 1):
                new_ligne.append(prev_ligne[j] + prev_ligne[j + 1])
            new_ligne.append(1)
            triangle.append(new_ligne)

        return triangle
