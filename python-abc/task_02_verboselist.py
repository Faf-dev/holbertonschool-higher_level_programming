#!/usr/bin/python3
"""create an ABC abstract class"""


class VerboseList(list):
    """Create abstract class Shape"""
    def append(self, item):
        """append method"""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """extend method"""
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, item):
        """remove method"""
        try:
            print("Removed [{}] from the list.".format(item))
            super().remove(item)
        except ValueError:
            print("ValueError: list.remove(x): x not in list.")

    def pop(self, index=-1):
        print("Popped [{}] from the list.".format(self[index]))
        return super().pop(index)
