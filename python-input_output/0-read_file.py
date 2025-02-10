#!/usr/bin/python3
"""create a method to open a file"""


def read_file(filename=""):
    """method to open a file"""
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
