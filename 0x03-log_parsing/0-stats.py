#!/usr/bin/python3

import sys


file_size = 0
status_code = 0
counter = 0
dict_sc = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}


def print_dictionary(dict_sc, file_size):
    """
    print the dict on the screen
    """

    print("File size: {}".format(file_size))
    for k, v in sorted(dict_sc.items()):
        if v != 0:
            print("{}: {}".format(k, v))


try:
    for line in sys.stdin:
        parsed = line.split()
        parsed = parsed[::-1]

        if len(parsed) > 2:
            counter += 1
        if counter <= 10:
            file_size += int(parsed[0])
            status_code = parsed[1]
        if (status_code in dict_sc.keys()):
            dict_sc[status_code] += 1

        if (counter == 10):
            print_dictionary(dict_sc, file_size)
            counter = 0

finally:
    print_dictionary(dict_sc, file_size)
