#!/usr/bin/python3
"""create a method to write in a file"""


def write_file(filename="", text=""):
    """method to write in a file"""
    with open(filename, "w", encoding="utf-8") as f:
        write_data = f.write(text)
    return write_data
