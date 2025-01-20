#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in range(len(i)):
            if i != 0:
                print(" ", end="")
            print("{}".format(i[j]), end="")
        print()
