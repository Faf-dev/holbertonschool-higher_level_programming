#!/usr/bin/python3
"""show that a Dragon instance can both swim and fly."""


class SwimMixin:
    """Mixin who create a swim method"""

    def swim(self):
        """swim method"""
        print("The creature swims!")


class FlyMixin:
    """Mixin who create a flying method"""

    def fly(self):
        """fly method"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class : inherits from swimmixin and flymixin"""

    def roar(self):
        """roar method"""
        print("The dragon roars!")
