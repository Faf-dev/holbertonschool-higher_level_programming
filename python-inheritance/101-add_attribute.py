#!/usr/bin/python3
"""Add a new attribute to an object"""


def add_attribute(obj, name, value):
    """init the new attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
