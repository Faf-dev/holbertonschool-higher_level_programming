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
        """check width and height value with integer_validator
        from BaseGeometry class
        then attribute the value to self.width and self.height"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ change str() rules"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """add the BaseGeometry area function"""
        super().area
        return self.__width * self.__height


class Square(Rectangle):
    """define Square class"""

    def __init__(self, size):
        """validate size with integer_validator function
        then attribute the value to self.size"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
