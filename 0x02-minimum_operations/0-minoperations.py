#!/usr/bin/python3

"""minimum operation"""


def minOperations(n):
    """calculate minmum number of operations"""
    copy, paste = 0, 0
    characters, previous = 1, 0

    if n < 0 or n == 0:
        return 0

    while characters != n:
        if n % characters == 0:
            characters = characters * 2
            previous = characters / 2
            copy, paste = copy + 1, paste + 1
        else:
            paste = paste + 1
            characters = characters + previous
    return (copy + paste)
