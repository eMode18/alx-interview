#!/usr/bin/python3
"""
Island Perimeter

This function calculates the perimeter of an island described in a grid.
The grid represents land (1) and sea (0), and the perimeter is the sum
of the exposed edges around the island.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.
    """
    area_covered = 0

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            # Check if cell is land or sea
            if cell == 0:
                continue

            # Left check
            if j != 0 and row[j - 1] == 0:
                area_covered += 1
            if j == 0:
                # left edge case
                area_covered += 1

            # Right check
            if j != len(row) - 1 and row[j + 1] == 0:
                area_covered += 1
            if j == len(row) - 1:
                # right edge case
                area_covered += 1

            # Upper check
            if i != 0 and grid[i - 1][j] == 0:
                area_covered += 1
            if i == 0:
                # top edge case
                area_covered += 1

            # Bottom Check
            if i != len(grid) - 1 and grid[i + 1][j] == 0:
                area_covered += 1
            if i == len(grid) - 1:
                # bottom edge case
                area_covered += 1

    return area_covered
