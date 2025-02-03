#!/usr/bin/python3
"""create Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" import module with BaseGeometry class"""


class Rectangle(BaseGeometry):
    """define rectangle class"""

    def __init__(self, width, height):
        """check width and height value with integer_validator
        from BaseGeometry class
        then attribute the value to self.width and self.height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ change str() rules"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """add the BaseGeometry area function"""
        return self.__width * self.__height
