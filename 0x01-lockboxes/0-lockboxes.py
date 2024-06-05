#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    visited = set()
    visited.add(0)  # Start with the first box (boxes[0])

    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key not in visited:
                visited.add(key)
                queue.append(key)

    return len(visited) == len(boxes)

