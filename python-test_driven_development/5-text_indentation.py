#!/usr/bin/python3
"""
text_indentation : indent text
"""


def text_indentation(text):
    """
    text_indentation - indent text if needed

    parameters:
    text : the text to indent

    Return: Nothing
    """
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

    print(print_text)
