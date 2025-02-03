#!/usr/bin/python3
"""create an ABC abstract class"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Create abstract class Animal"""

    @abstractmethod
    def sound(self):
        """sound abstract method"""
        pass


class Dog(Animal):
    """define dog subclass"""
    def __init__(self):
        """init method"""
        self._sound = "Bark"

    def sound(self):
        """sound abstract method"""
        return self._sound


class Cat(Animal):
    """define cat subclass"""
    def __init__(self):
        """init method"""
        self._sound = "Meow"

    def sound(self):
        """sound abstract method"""
        return self._sound
