#!/usr/bin/python3
"""Modify int method"""


class MyInt(int):
    """MyInt : inherits from int method"""

    def __eq__(self, value):
        """rebel method : invert == return value"""
        if super().__eq__(value):
            return False
        else:
            return True

    def __ne__(self, value):
        """rebel method : invert != return value"""
        if super().__ne__(value):
            return False
        else:
            return True
