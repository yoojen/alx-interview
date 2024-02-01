#!/usr/bin/python3
""" simple module for making changes project"""


def makeChange(coins, total):
    """
    determine the fewest number of coins needed to meet a given amount total.

    Return: fewest number of coins needed to meet total

        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1

    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    count = 0
    coins = sorted(coins)[::-1]
    for one_coin in coins:
        while one_coin <= total:
            total -= one_coin
            count += 1
        if (total == 0):
            return count
    return -1
