#!/usr/bin/python3
"""Create an empty BaseGeometry class"""


class BaseGeometry:
    """define BaseGeometry class"""
    pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if isinstance(value, int) is False:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
