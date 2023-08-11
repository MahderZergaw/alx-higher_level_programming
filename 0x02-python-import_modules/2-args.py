#!/usr/bin/python3
import sys

if __name__ == '__main__':
    arguments = sys.argv[1:]  # Exclude the script name

    num_arguments = len(arguments)
    if num_arguments == 0:
        print("Number of argument(s): .")
    elif num_arguments == 1:
        print("Number of argument(s): 1: {0}".format(arguments[0]))
    else:
        print("Number of argument(s): {0}: {1}".format(num_arguments, ", ".join(arguments)))

    if num_arguments > 0:
        print()
        for idx, arg in enumerate(arguments, start=1):
            print("{0}: {1}".format(idx, arg))
