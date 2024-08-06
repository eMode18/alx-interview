#!/usr/bin/python3
"""
Define the isWinner function to solve the Prime Game problem.
"""


def primes(n):
    """Generate a list of prime numbers from 1 to n (inclusive).
       Args:
        n (int): The upper limit of the range. The lower limit is always 1.
    """
    prime_numbers = []
    is_prime = [True] * (n + 1)
    for num in range(2, n + 1):
        if is_prime[num]:
            prime_numbers.append(num)
            for multiple in range(num, n + 1, num):
                is_prime[multiple] = False
    return prime_numbers


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.
    Args:
        x (int): Number of rounds in the game.
        nums (list of int): List of upper limits for each round.
    Return:
        str: The name of the winner ('Maria' or 'Ben'), or None if no winner.
    """
    if not x or not nums:
        return None
    maria_score = ben_score = 0
    for round_index in range(x):
        prime_list = primes(nums[round_index])
        if len(prime_list) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1
    if maria_score > ben_score:
        return 'Maria'
    elif ben_score > maria_score:
        return 'Ben'
    return None
