#!/usr/bin/python3
"""inherits from both a Fish class and a Bird class"""


class Fish():
    """Fish class"""

    def swim(self):
        """swim method"""
        print("The fish is swimming")

    def habitat(self):
        """habitat method"""
        print("The fish lives in water")


class Bird:
    """Bird class"""

    def fly(self):
        """fly method"""
        print("The bird is flying")

    def habitat(self):
        """habitat method"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class"""

    def fly(self):
        """override fly method"""
        print("The flying fish is soaring!")

    def swim(self):
        """override swim method"""
        print("The flying fish is swimming!")

    def habitat(self):
        """override habitat method"""
        print("The flying fish lives both in water and the sky!")
