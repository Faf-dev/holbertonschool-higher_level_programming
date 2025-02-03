#!/usr/bin/python3
"""Extend the built in iter"""


class CountedIterator:
    """CountedIterator : extends the built-in iterator
    obtained from the iter function
    The CountedIterator should keep track of the number
    of items that have been iterated over"""

    def __init__(self, iterator):
        """initialisation method"""
        self.count = 0
        self.iterator = iter(iterator)

    def __next__(self):
        """next method that increment count"""
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """Return count of iterated items"""
        return self.count
