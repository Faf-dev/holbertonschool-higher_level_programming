#!/usr/bin/python3
"""

"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    print_text = ""
    i = 0
    while i < len(text):
        print_text += text[i]
        if text[i] in '.?:':
            print_text += "\n\n"
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

    print(print_text.strip())
