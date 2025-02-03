#!/usr/bin/python3
"""Return the available attributes and method of an object"""


def lookup(obj):
    """lookup : Return the available attributes and method of an object
    obj : the object
    Return : available attributes and method of an object"""
    return (list(dir(obj)))
