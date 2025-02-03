#!/usr/bin/python3
"""Create a function who return True if
obj is an instance of specified class
or if the object is an instance of a class that inherited from"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class : check if obj is an instance of a_class

    obj : instance of a_class
    a_class : specified class

    Return : True if obj is an instance of a_class
    or if the object is an instance of a class that inherited from
    false instead"""
    return (isinstance(obj, a_class))
