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

    def to_json(self, attrs=None):
        """
        public method that retrieves a dict repr of a student instance
        """
        if attrs is None:
            return self.__dict__
        if type(attrs) is list and all(type(atr) is str for atr in attrs):
            self_attrs = {}
            for key in attrs:
                if key in self.__dict__:
                    self_attrs[key] = self.__dict__[key]
            return self_attrs
        return self.__dict__

    def reload_from_json(self, json):
        """
        public method that replace all attrs of the student
        json : dict with new attrs
        """
        for key, value in json.items():
            setattr(self, key, value)
