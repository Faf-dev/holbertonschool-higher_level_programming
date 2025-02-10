#!/usr/bin/python3
"""create a method to append a text in a file"""


def append_write(filename="", text=""):
    """method to append a text in a file"""
    with open(filename, "a", encoding="utf-8") as f:
        write_data = f.write(text)
    return write_data
