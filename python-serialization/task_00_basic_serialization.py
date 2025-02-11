#!/usr/bin/env python3
"""
create two functions
that serialize a data and save it in a file
load a file then deserialize it
"""
import json


def serialize_and_save_to_file(data, filename):
    """serialize a data and save it in a file
    data : data to initialize
    filename : file with @data saved in it"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """load a file then deserialize it
    filename : the file to load"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
