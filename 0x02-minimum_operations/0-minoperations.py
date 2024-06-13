#!/usr/bin/python3
"""
Minimum Operations

Given a number n, calculates the fewest number of operations needed to result
in exactly n H characters in the file.
"""


def minOperations(n: int) -> int:
    """
    Calculates the minimum number of operations to reach n 'H' characters.

    Args:
        n (int): Target number of 'H' characters.

    Returns:
        int: Minimum number of operations.
    """
    operations = 0
    clipboard = 0

    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                clipboard = i
                break

        n //= clipboard
        operations += clipboard

    return operations
