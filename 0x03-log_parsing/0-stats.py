#!/usr/bin/python3
"""performing handling loggings and extracting valuable informations"""
import sys


def main():
    """get data from stdin printing whole data on the screen"""

    status = []

    try:
        count = 0
        total_size = 0
        for lines in sys.stdin:
            parsed = lines.split(" ")
            count = count + 1
            total_size = total_size + int(parsed[8])
            status_code = int(parsed[7])
            status.append(status_code)
            if count % 10 == 0:
                print(f"File size:  {total_size}")
                print_dic(status)

    except KeyboardInterrupt:
        print(f"File Size: {total_size}")


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
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
