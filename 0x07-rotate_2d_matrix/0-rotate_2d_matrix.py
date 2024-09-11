#!/usr/bin/python3
"""Module for 2D matrix in-place performance rotation"""


def rotate_2d_matrix(matrix):
    """Rectangular 2D list In-place rotation"""
    size = len(matrix[0])
    for column in range(size - 1, -1, -1):
        for row in range(size):
            matrix[row].append(matrix[column].pop(0))
