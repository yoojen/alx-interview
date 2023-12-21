#!/usr/bin/python3
"""collect data from stdin and extract valuable information"""

import sys


def print_dic(list_of_status):
    """
    counting the occurence of key and initialize printing
    of data on the screen
    """
    sorted_status = dict(sorted(list_of_status.items()))
    for k, v in sorted_status.items():
        print(f"{k}: {v}")


# status = []
count = 0
total_size = 0

initial_dictionary = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

try:
    for lines in sys.stdin:
        parsed = lines.split(" ")
        if len(parsed) == 9:
            count = count + 1
            total_size = total_size + int(parsed[8])
            status_code = int(parsed[7])
            # status.append(status_code)
            if (status_code in initial_dictionary.keys()):
                    initial_dictionary[status_code] += 1
            if count % 10 == 0:
                print(f"File size: {total_size}")
                print_dic(initial_dictionary)

finally:
    print(f"File Size: {total_size}")
    print_dic(initial_dictionary)
