#!/usr/bin/python3
"""N Queens Problem"""

import sys


def print_board(board, n):
    """Prints the positions allocated to the queens"""
    queen_positions = []

    for i in range(n):
        for j in range(n):
            if j == board[i]:
                queen_positions.append([i, j])
    print(queen_positions)


def is_position_safe(board, i, j, r):
    """Checks if a position is safe for placing a queen"""
    return board[i] in (j, j - i + r, i - r + j)


def safe_positions(board, row, n):
    """Finds all safe positions where a queen can be allocated"""
    if row == n:
        print_board(board, n)
    else:
        for j in range(n):
            allowed = True
            for i in range(row):
                if is_position_safe(board, i, j, row):
                    allowed = False
            if allowed:
                board[row] = j
                safe_positions(board, row + 1, n)


def create_board(size):
    """Generates an empty chessboard of the given size"""
    return [0] * size


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except BaseException:
    print("N must be a number")
    exit(1)

if n < 4:
    print("N must be at least 4")
    exit(1)

board = create_board(n)
row = 0
safe_positions(board, row, n)
