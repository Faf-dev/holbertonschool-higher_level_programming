#!/usr/bin/python3
"""create a function that write an object to a txt file
using JSON repr"""
import json


def save_to_json_file(my_obj, filename):
    """function that write an object to a txt file
    using JSON repr
    my_obj : object who need to be write
    filename : txt file. Created if not existant and overwritten if exist"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
