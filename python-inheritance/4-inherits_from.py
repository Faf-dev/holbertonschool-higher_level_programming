#!/usr/bin/python3
"""Create a function who return True if
the object is an instance of a class that inherited
(directly or indirectly) from the specified class"""


def inherits_from(obj, a_class):
    """inherits_from : check if obj is an instance of a_class

    obj : instance of a_class
    a_class : specified class

    Return : True if
    the object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    false instead"""
    return (isinstance(obj, a_class) and type(obj) is not a_class)
