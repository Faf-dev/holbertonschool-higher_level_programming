#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        max_value = 0
        max_key = ""
        for key, value in a_dictionary.items():
            if value > max_value:
                max_value = value
                max_key = key
        return max_key
