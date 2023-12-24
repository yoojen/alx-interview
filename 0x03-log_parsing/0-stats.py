#!/usr/bin/python3
import sys


def print_dict(dict_of_status, total_size):
    """
    counting the occurence of key and initialize printing
    of data on the screen
    """
    sorted_status = dict(sorted(dict_of_status.items()))
    print(f"File Size: {total_size}")
    for k, v in sorted_status.items():
        if v != 0:
            print(f"{k}: {v}")


count = 0
total_size = 0
status_code = 0
dict_of_status = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
        }

try:
    for lines in sys.stdin:
        parsed = lines.split()
        count += 1
        total_size += int(parsed[8])
        status_code = str(parsed[7])
        if status_code in dict_of_status.keys():
            dict_of_status[status_code] += 1
        if count == 10:
            print_dict(dict_of_status, total_size)
            count = 0
finally:
    print_dict(dict_of_status, total_size)
