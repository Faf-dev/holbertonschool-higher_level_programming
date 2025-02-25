#!/usr/bin/python3
"""Create an empty BaseGeometry class"""


class BaseGeometry:
    """define BaseGeometry class"""

    def area(self):
        """Raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value

    Args:
        name (str): name of the value
        value (int): value to validate

    Raises:
        TypeError: If value is not an integer
        ValueError: If value is less or equal to 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """define rectangle class"""

    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
