#!/usr/bin/python3
"""create an ABC abstract class"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Create abstract class Shape"""

    @abstractmethod
    def area(self):
        """area abstract method"""
        pass

    @abstractmethod
    def perimeter(self):
        """perimeter abstract method"""
        pass


class Circle(Shape):
    """define Circle subclass"""
    def __init__(self, radius):
        """init method"""
        self._radius = radius

    def area(self):
        """Area method"""
        return ((self._radius * self._radius) * math.pi)

    def perimeter(self):
        """perimeter method"""
        return ((self._radius * 2) * math.pi)


class Rectangle(Shape):
    """define Rectangle subclass"""
    def __init__(self, width, height):
        """init method"""
        self._width = width
        self._height = height

    def area(self):
        """Area method"""
        return self._width * self._height

    def perimeter(self):
        """perimeter method"""
        return (self._width + self._height) * 2


def shape_info(shape):
    """Print area and perimeter of a shape"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
