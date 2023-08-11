#!/usr/bin/python3

import sys

if __name__ == '__main__':
    total_sum = 0

    # Skip the first argument since it's the script name
    for arg in sys.argv[1:]:
        total_sum += int(arg)

    print(total_sum)
