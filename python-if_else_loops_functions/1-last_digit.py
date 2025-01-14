#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_nbr = abs(number) % 10

if number < 0:
    last_nbr = -last_nbr

if last_nbr < 6 and last_nbr != 0:
    print(f"Last digit of {number} is {last_nbr} and is less than 6 and not 0")
elif last_nbr >= 5:
    print(f"Last digit of {number} is {last_nbr} and is greater than 5")
else:
    print(f"Last digit of {number} is {last_nbr} and is 0")
