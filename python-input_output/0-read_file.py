#!/usr/bin/python3
"""create a method to open a file"""


def read_file(filename=""):
    """method to open a file"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
