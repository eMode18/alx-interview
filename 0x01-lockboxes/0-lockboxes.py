#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    num_boxes = len(boxes)
    opened_boxes = set()
    queue = [0]  # Start with the first box

    while queue:
        current_box = queue.pop(0)
        opened_boxes.add(current_box)

        for key in boxes[current_box]:
            if key != 0 and key < num_boxes and key not in opened_boxes:
                queue.append(key)

    return len(opened_boxes) == num_boxes
