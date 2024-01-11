#!/usr/bin/python3
""" N queens ALX interview preparation"""
import sys


if len(sys.argv) < 2 or len(sys.argv) > 2:
    print("Usage: nqueens N")
    exit(1)
if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)
if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def backtracking(n, i=0, row=[], pst_track=[], ngt_track=[]):
    """ finding the possible positions for queen"""
    if i < n:
        for j in range(n):
            positiveTrack = i + j
            negativeTrack = i - j
            if j not in row and positiveTrack not in pst_track and \
                    negativeTrack not in ngt_track:
                yield from backtracking(n, i + 1, row + [j], pst_track +
                                        [positiveTrack], ngt_track + [negativeTrack])
    else:
        yield row


def print_result(n):
    """ solve function for actual operation"""
    queen_pos = []
    i = 0
    for solution in backtracking(n, 0):
        for s in solution:
            queen_pos.append([i, s])
            i += 1
        print(queen_pos)
        queen_pos = []
        i = 0


print_result(n)
