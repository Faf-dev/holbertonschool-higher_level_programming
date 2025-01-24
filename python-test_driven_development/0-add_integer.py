#!/usr/bin/python3
"""
add_integer : add a with b
"""
def add_integer(a, b=98):
    """
    add to integer

    args:
    a : integer or float
    b : integer or float, 98 if only one argument

    return : the addition of two int    
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer") 
    return int(a) + int(b)
