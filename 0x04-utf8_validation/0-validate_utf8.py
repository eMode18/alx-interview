#!/usr/bin/python3
"""
Module for UTF-8 validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list[int]): List of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for byte in data:
        if num_bytes == 0:
            if byte >> 7 == 0:
                continue  # Valid single-byte character
            elif byte >> 5 == 0b110:
                num_bytes = 1  # Start of a 2-byte character
            elif byte >> 4 == 0b1110:
                num_bytes = 2  # Start of a 3-byte character
            elif byte >> 3 == 0b11110:
                num_bytes = 3  # Start of a 4-byte character
            else:
                return False  # Invalid start byte
        else:
            if byte >> 6 != 0b10:
                return False  # Invalid continuation byte
            num_bytes -= 1  # reduce the remaining bytes for current character

    return num_bytes == 0  # Ensure all characters are complete
