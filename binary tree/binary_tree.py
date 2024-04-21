class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Pre-order traversal
def pre_order(node):
    if node is None:
        return []
    result = [node.data]
    result.extend(pre_order(node.left))
    result.extend(pre_order(node.right))
    return result

# In-order traversal
def in_order(node):
    if node is None:
        return []
    result = []
    result.extend(in_order(node.left))
    result.append(node.data)
    result.extend(in_order(node.right))
    return result

# Post-order traversal
def post_order(node):
    if node is None:
        return []
    result = []
    result.extend(post_order(node.left))
    result.extend(post_order(node.right))
    result.append(node.data)
    return result
