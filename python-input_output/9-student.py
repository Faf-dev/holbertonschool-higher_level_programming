#!/usr/bin/python3
"""
create a student class and a public method that retrieves repr
of a student instance
"""


class Student:
    """
    student class
    first_name : first name
    last_name : last name
    age : age of the student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        method that retrives repr of a student instance
        """
        return self.__dict__
