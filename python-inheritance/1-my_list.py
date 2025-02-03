#!/usr/bin/python3
"""Create MyList class"""


class MyList(list):
    """ define MyList class"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
