#!/usr/bin/python3

import sys


def print_dictionary(status_dictionary, file_size):
    """
    print dictionary with keys sorted in ascending order
    """
    print("File size: {}".format(file_size))
    for key, value in sorted(status_dictionary.items()):
        if value != 0:
            print("{}: {}".format(key, value))


file_size = 0
code = 0
counter = 0
status_dictionary = {"200": 0,
                     "301": 0,
                     "400": 0,
                     "401": 0,
                     "403": 0,
                     "404": 0,
                     "405": 0,
                     "500": 0}

try:
    for line in sys.stdin:
        parsed = line.split()
        parsed = parsed[::-1]

        if len(parsed) > 2:
            counter += 1

            if counter <= 10:
                file_size += int(parsed[0])
                code = parsed[1]

                if (code in status_dictionary.keys()):
                    status_dictionary[code] += 1

            if (counter == 10):
                print_dictionary(status_dictionary, file_size)
                counter = 0

finally:
    print_dictionary(status_dictionary, file_size)
