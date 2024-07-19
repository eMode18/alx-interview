#!/usr/bin/python3
"""
2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an m by n 2D matrix in place.

    Args:
        matrix (list[list]): The input 2D matrix to be rotated.

    Returns:
        None: The matrix is modified in place.
    """
    if not isinstance(matrix, list):
        return

    if len(matrix) == 0 or not all(isinstance(row, list) for row in matrix):
        return

    rows = len(matrix)
    cols = len(matrix[0])

    if not all(len(row) == cols for row in matrix):
        return

    column_index, row_index = 0, rows - 1
    for i in range(cols * rows):
        if i % rows == 0:
            matrix.append([])

        if row_index == -1:
            row_index = rows - 1
            column_index += 1

        matrix[-1].append(matrix[row_index][column_index])

        if column_index == cols - 1 and row_index >= -1:
            matrix.pop(row_index)

        row_index -= 1
