from collections import deque

class Node:
    def __init__(self, left, right, v):
        self.left = left
        self.right = right
        self.value = v

def tree_by_levels(node):
    if node is None:
        return []

    result = []
    queue = deque([node])

    while queue:
        current_node = queue.popleft()
        result.append(current_node.value)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return result