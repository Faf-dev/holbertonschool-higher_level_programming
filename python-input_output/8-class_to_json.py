#!/usr/bin/python3
"""create a function that return the dict description with simple
data structure for JSON serialization of an obj"""


def class_to_json(obj):
    """function that return the dict
        obj : class with attribute to return"""
    return obj.__dict__
