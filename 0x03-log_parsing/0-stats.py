#!/usr/bin/python3
"""Module for function that reads stdin line by line and computes metrics"""
import sys


def print_statistics(status_dict, total_size):
    """Printing accumulated file size and status code counts"""
    print(f"File size: {total_size}")
    for code in sorted(status_dict.keys()):
        if status_dict[code] != 0:
            print(f"{code}: {status_dict[code]}")


API_statusCodes = {"200": 0, "301": 0, "400": 0, "401": 0,
                   "403": 0, "404": 0, "405": 0, "500": 0}
count_log = 0
total_size = 0

try:
    for line in sys.stdin:
        if count_log != 0 and count_log % 10 == 0:
            print_statistics(API_statusCodes, total_size)
        line_tokens = line.split()
        count_log += 1
        try:
            total_size += int(line_tokens[-1])
        except Exception:
            pass
        try:
            if line_tokens[-2] in API_statusCodes:
                API_statusCodes[line_tokens[-2]] += 1
        except Exception:
            pass
    print_statistics(API_statusCodes, total_size)
except KeyboardInterrupt:
    print_statistics(API_statusCodes, total_size)
    raise
