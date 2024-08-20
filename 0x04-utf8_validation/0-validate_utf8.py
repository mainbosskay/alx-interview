#!/usr/bin/python3
"""Module to verify if a list of integers are valid UTF-8 code points"""


def validUTF8(data):
    """checking if data (list of integers)  has valid UFT-8 encoding"""
    bytesRem = 0
    maskBegin = 1 << 7
    maskCount = 1 << 6

    for numBytes in data:
        maskNow = 1 << 7
        if bytesRem == 0:
            while maskNow & numBytes:
                bytesRem = bytesRem + 1
                maskNow = maskNow >> 1
            if bytesRem == 0:
                continue
            if bytesRem == 1 or bytesRem > 4:
                return False
        else:
            if not (numBytes & maskNow and not (numBytes & maskCount)):
                return False
        bytesRem = bytesRem - 1
    if bytesRem == 0:
        return True
    return False
