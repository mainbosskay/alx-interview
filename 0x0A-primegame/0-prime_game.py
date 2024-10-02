#!/usr/bin/python3
"""Module for strategy on prime number game"""


def isWinner(x, nums):
    """Evaluating winner after playing `x` number of rounds"""
    if x < 1 or not nums:
        return None
    marias_score, bens_score = 0, 0
    n = max(nums)
    prime_flags = [True for _ in range(1, n + 1, 1)]
    prime_flags[0] = False
    for indx, flag in enumerate(prime_flags, 1):
        if indx == 1 or not flag:
            continue
        for multiple in range(indx + indx, n + 1, indx):
            prime_flags[multiple - 1] = False
    for _, n in zip(range(x), nums):
        primes_cnt = len(list(filter(lambda x: x, prime_flags[0: n])))
        bens_score += primes_cnt % 2 == 0
        marias_score += primes_cnt % 2 == 1
    if marias_score == bens_score:
        return None
    return 'Maria' if marias_score > bens_score else 'Ben'
