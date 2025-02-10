#!/usr/bin/python3
"""create a function to return the JSON repr of an object"""
import json


def to_json_string(my_obj):
    """function to return repr of an object"""
    return json.dumps(my_obj)
