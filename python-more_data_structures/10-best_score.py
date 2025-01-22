#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    else:
        new_dictionary = sorted(a_dictionary, reverse=True)
        for i in new_dictionary:
            return i
