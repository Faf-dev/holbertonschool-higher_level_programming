#!/usr/bin/python3

def remove_char_at(str, n):
    i = len(str) - 1
    j = 0
    str_cpy = ""
    if n > i or n < 0:
        return str
    else:
        while j < len(str):
            if j == n:
                j += 1
            else:
                str_cpy += str[j]
                j += 1
        return str_cpy
