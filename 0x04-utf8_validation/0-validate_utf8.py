#!/usr/bin/python3
"""Validation of utf8"""


def validUTF8(data):
    """
    check if a given list of integers is valid utf8
    arg:
    data -> List of integers
    """

    num_of_bytes = 0
    for element in data:
        mask = 1 << 7
        if num_of_bytes == 0:
            while element & mask:
                num_of_bytes += 1
                mask = mask >> 1
            if num_of_bytes == 0:
                continue
            if num_of_bytes == 1 or num_of_bytes > 4:
                return False
        else:
            if not (element & 1 << 7 and not (element & 1 << 6)):
                return False
        num_of_bytes -= 1
    if num_of_bytes == 0:
        return True
    return False
