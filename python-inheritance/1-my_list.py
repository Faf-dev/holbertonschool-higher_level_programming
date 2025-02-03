#!/usr/bin/python3
"""Create MyList class"""


class MyList(list):
    """ define MyList class"""
    def print_sorted(self):
        print(sorted(self))
