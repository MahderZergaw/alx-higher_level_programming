#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass 
    else:
        reversed_list = reversed(my_list)
        for item in reversed_list:
            print("{0:d}".format(item))
