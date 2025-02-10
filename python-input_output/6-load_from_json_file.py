#!/usr/bin/python3
"""create a function that create an obj from JSON file"""
import json


def load_from_json_file(filename):
    """function that create an obj from filename
    filename : JSON file"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
