#!/usr/bin/python3
import sys


def print_dic(list_of_status):
    """
    counting the occurence of key and initialize printing
    of data on the screen
    """
    status_dict = {}
    for status in list_of_status:
        if status_dict.get(status):
            status_dict[status] += 1
        else:
            status_dict[status] = 1
    sorted_status = dict(sorted(status_dict.items()))

    for k, v in sorted_status.items():
        print("{}: {}".format(k, v))


status = []
count = 0
total_size = 0

try:
    for lines in sys.stdin:
        parsed = lines.split()
        if len(parsed) == 9:
            count = count + 1
            total_size = total_size + int(parsed[8])
            status_code = int(parsed[7])
            status.append(status_code)
            if count % 10 == 0:
                print("File size: {}".format(total_size))
                print_dic(status)

finally:
    print("File Size: {}".format(total_size))
    print_dic(status)
