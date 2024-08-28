#!/usr/bin/python3
"""Backtracking algorithm with recursion for solving N Queens"""
import sys


class NQueens:
    """Class to solve problem for N Queens algorithm"""

    def __init__(self, size):
        """Initializing the class for NQueens"""
        self.size = size
        self.queenPos = [0 for pos in range(size + 1)]
        self.solutions = []

    def queen_placement(self, posNow, column):
        """Checking if queen can be positioned in specific column"""
        for posThen in range(1, posNow):
            if self.queenPos[posThen] == column or \
                    abs(self.queenPos[posThen] - column) \
                    == abs(posThen - posNow):
                return 0
        return 1

    def nqueens(self, posNow):
        """Solving NQueens by trying to place on queens on board"""
        for column in range(1, self.size + 1):
            if self.queen_placement(posNow, column):
                self.queenPos[posNow] = column
                if posNow == self.size:
                    solution = []
                    for column in range(1, self.size + 1):
                        solution.append([column - 1, self.queenPos[column] - 1])
                    self.solutions.append(solution)
                else:
                    self.nqueens(posNow + 1)
        return self.solutions


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

N = sys.argv[1]

try:
    N = int(N)
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

queen = NQueens(N)
solutions = queen.nqueens(1)

for column in solutions:
    print(column)
