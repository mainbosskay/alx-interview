#!/usr/bin/python3
"""Module for minimum operations function is established"""


def minOperations(n):
    """Calculates  minimum number of operations required to transform
    single character 'H' in text file into exactly 'n'
    Args: n int: target number of H characters to get in text file"""
    if type(n) is not int:
        return 0
    oprts_count = 0
    copied_content = 0
    count_now = 1
    while count_now < n:
        if copied_content == 0:
            copied_content = count_now
            count_now += copied_content
            oprts_count += 2
        elif n - count_now > 0 and (n - count_now) % count_now == 0:
            copied_content = count_now
            count_now += copied_content
            oprts_count += 2
        elif copied_content > 0:
            count_now += copied_content
            oprts_count += 1
    return oprts_count
