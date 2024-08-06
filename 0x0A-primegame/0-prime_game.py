#!/usr/bin/env python3
"""
Prime Game: Maria vs. Ben

Maria and Ben play a game where they take turns choosing prime numbers
from a set of consecutive integers.
The player who cannot make a move (no more prime numbers left) loses the game.

Rules:
1. Start with a set of integers from 1 up to and including a given number, n.
2. On each turn, a player selects a prime number and removes it along with
its multiples.
3. Determine the winner based on optimal play.
"""


def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_next_prime(start):
        while True:
            start += 1
            if is_prime(start):
                return start

    def play_game(n):
        # Initialize a list to keep track of available numbers
        available_numbers = [True] * (n + 1)
        available_numbers[0] = available_numbers[1] = False

        # Maria starts
        maria_turn = True

        while True:
            prime = get_next_prime(1)
            found = False

            # Find the next available prime
            while prime <= n:
                if available_numbers[prime]:
                    found = True
                    break
                prime = get_next_prime(prime)

            if not found:
                # No more primes left
                return "Ben" if maria_turn else "Maria"

            # Remove prime and its multiples
            for i in range(prime, n + 1, prime):
                available_numbers[i] = False

            # Switch turns
            maria_turn = not maria_turn

    # Play x rounds and keep track of wins
    maria_wins = ben_wins = 0
    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
