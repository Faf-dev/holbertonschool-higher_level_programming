#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        number = -number
    last_nbr = number % 10
    print("{}".format(last_nbr), end="")
    return last_nbr
