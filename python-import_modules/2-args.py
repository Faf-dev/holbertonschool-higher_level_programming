#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    argv_len = len(argv)
    if argv_len == 1:
        str = "arguments."
    if argv_len == 2:
        str = "argument:"
    if argv_len > 2:
        str = "arguments:"
    print("{} {}".format(argv_len - 1, str))
    for i in range(1, argv_len):
        print("{}: {}".format(i, argv[i]))
