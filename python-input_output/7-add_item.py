#!/usr/bin/python3
"""script that add all args to a python list and save them to a file"""
from sys import argv
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """..."""
    args = argv[1:]

    if os.path.exists("add_item.json"):
        read_item = load_from_json_file("add_item.json")
    else:
        read_item = []

    read_item.extend(args)

    save_to_json_file(read_item, "add_item.json")


if __name__ == "__main__":
    main()
