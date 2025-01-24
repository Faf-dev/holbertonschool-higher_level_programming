#!/usr/bin/python3
"""
print_square - print a square with #
"""


def print_square(size):
    """
    print_square :

    parameters :
    size : The size of the square

    Return : Nothing
    """
    if not isinstance(size, int) or isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    
    for i in range(size):
        print("#" * size)
