#!/usr/bin/python3
"""Module that will create Pascal's triangle"""


def pascal_triangle(n):
    """Creating Pascal's triangle to n levels
    Args: n (int): Number of levels of the triangle
    Returns:
    list: list of lists of integers representing triangle"""
    trngle = []
    if type(n) is not int or n <= 0:
        return trngle
    for lvl in range(n):
        row = []
        for indx in range(lvl + 1):
            if indx == 0 or indx == lvl:
                row.append(1)
            else:
                row.append(trngle[lvl - 1][indx - 1] + trngle[lvl - 1][indx])
        trngle.append(row)
    return trngle
