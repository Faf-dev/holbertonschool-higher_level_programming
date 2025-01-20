#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    Cpy_list = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return Cpy_list
    else:
        Cpy_list[idx] = element
        return Cpy_list
