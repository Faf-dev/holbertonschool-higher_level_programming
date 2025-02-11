#!/usr/bin/env python3
"""
Create a CustomObject class with:
init method
serialize method
display method
deserialize method (class method)
"""
import pickle


class CustomObject:
    """
    CustomObject class
    """

    def __init__(self, name, age, is_student):
        """
        init method
        name : a name (str)
        age : an age (int)
        is_student : False if not, True if it's a student (bool)
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def serialize(self, filename):
        """
        serialize attr of self into filename
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (FileNotFoundError, pickle.PickleError, PermissionError):
            return None
        except Exception:
            return None

    def display(self):
        """
        display method
        print the object's attributes
        """
        for i in self.__dict__:
            print("{}: {}".format(i[0].upper() + i[1:], self.__dict__[i]))

    @classmethod
    def deserialize(cls, filename):
        """
        deserialize a class instance in filename
        """
        try:
            with open(filename, "rb") as file:
                loaded_data = pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, PermissionError):
            return None
        except Exception:
            return None
        return loaded_data
