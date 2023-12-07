#!/usr/bin/python3

"""Determine lock boxes that can be opened"""


def canUnlockAll(boxes):
    initial_box_unlocked = set([0])
    remained_locked = [0]

    while remained_locked:
        current_box = remained_locked.pop(0)
        inner_box_of_current_box = boxes[current_box]
        for key in inner_box_of_current_box:
            if key not in initial_box_unlocked and 0 <= key:
                if (key < len(boxes)):
                    initial_box_unlocked.add(key)
                    remained_locked.append(key)

    return len(initial_box_unlocked) == len(boxes)
