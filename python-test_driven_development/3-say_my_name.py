#!/usr/bin/python3
"""
say_my_name - print My name is + first name and last name
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name : print 3 strings

    parameters:
    first_name : the first name to print
    last_name : the last name to print

    Return: Nothing
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
