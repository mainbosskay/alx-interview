#!/usr/bin/python3
"""Module for minimal coin change calculation"""


def makeChange(coins, total):
    """Calculate minimum coins required to reach given total"""
    if total <= 0:
        return 0
    remnAmt = total
    totalCoin = 0
    coinIndx = 0
    sortCoins = sorted(coins, reverse=True)
    coinsNum = len(coins)
    while remnAmt > 0:
        if coinIndx >= coinsNum:
            return -1
        if remnAmt - sortCoins[coinIndx] >= 0:
            remnAmt -= sortCoins[coinIndx]
            totalCoin += 1
        else:
            coinIndx += 1
    return totalCoin
