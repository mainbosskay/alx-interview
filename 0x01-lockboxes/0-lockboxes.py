#!/usr/bin/python3
"""Module for unlocking lockboxes has been established"""


def canUnlockAll(boxes):
    """Determine if all locked boxes can be unlocked using available keys
    Args: boxes (list of lists) int: Each element is list of keysin the box
    Return: boolean: True if all boxes can be opened, else return False"""
    boxes_num = len(boxes)
    boxes_unlocked = set([0])
    keys_check = set(boxes[0]).difference(set([0]))
    while len(keys_check) > 0:
        keyNow = keys_check.pop()
        if not keyNow or keyNow >= boxes_num or keyNow < 0:
            continue
        if keyNow not in boxes_unlocked:
            keys_check = keys_check.union(boxes[keyNow])
            boxes_unlocked.add(keyNow)
    return boxes_num == len(boxes_unlocked)
