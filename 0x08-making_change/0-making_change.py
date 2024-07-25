#!/usr/bin/python3
"""
Change starts from Within
"""


def makeChange(coins, total):
    """
    This function calculates the fewest number of coins needed to meet a
given total amount.
Given a pile of coins of different values, it determines the optimal
combination of coins.
    """
    if total <= 0:
        return 0

    min_coins = [0] + [float("inf")] * total

    for coin in coins:
        for i in range(coin, total + 1):
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    return min_coins[-1] if min_coins[-1] != float("inf") else -1
