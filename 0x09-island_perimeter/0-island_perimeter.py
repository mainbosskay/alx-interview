#!/usr/bin/python3
"""Module for perimeter of an island in a grid to be calculated"""


def island_perimeter(grid):
    """Calculate perimeter of an island without internal water bodies"""
    perimeter = 0
    if not isinstance(grid, list):
        return 0
    k = len(grid)
    for t, rowNow in enumerate(grid):
        d = len(rowNow)
        for x, cellNow in enumerate(rowNow):
            if cellNow == 0:
                continue
            borderSides = (
                t == 0 or (len(grid[t - 1]) > x and grid[t - 1][x] == 0),
                x == d - 1 or (d > x + 1 and rowNow[x + 1] == 0),
                t == k - 1 or (
                    len(grid[t + 1]) > x and grid[t + 1][x] == 0),
                x == 0 or rowNow[x - 1] == 0
            )
            perimeter += sum(borderSides)
    return perimeter
