#!/usr/bin/python3
"""create a function that returns an object represented by a json str"""
import json


def from_json_string(my_str):
    """function that return an object repr by a json str"""
    return json.loads(my_str)
