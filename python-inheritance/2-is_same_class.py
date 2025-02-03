#!/usr/bin/python3
"""Create a function who return True if
obj is an instance of specified class"""


def is_same_class(obj, a_class):
    """is_same_class : check if obj is an instance of a_class

    obj : instance of a_class
    a_class : specified class

    Return : True if obj is exactly an instance of a_class
    false instead"""
    return (type(obj) is a_class)
