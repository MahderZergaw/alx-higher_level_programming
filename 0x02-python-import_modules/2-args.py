#!/usr/bin/python3

import sys

if __name__ == '__main__':
    num_arguments = len(sys.argv) - 1

    if num_arguments == 0:
        print("Number of argument(s): .")
    elif num_arguments == 1:
        print("Number of argument(s): 1: {0}".format(sys.argv[1]))
    else:
        print("Number of argument(s): {0}:".format(num_arguments))
        for i in range(1, num_arguments + 1):
            print("{0}: {1}".format(i, sys.argv[i]))
