"""Реализация обходов бинарного дерева."""


def inorder_recursive(node):
    """Рекурсивный in-order обход. O(n)."""
    result = []
    if node:
        result.extend(inorder_recursive(node.left))
        result.append(node.value)
        result.extend(inorder_recursive(node.right))
    return result


def inorder_iterative(root):
    """Итеративный in-order обход со стеком. O(n)."""
    result, stack, current = [], [], root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.value)
        current = current.right

    return result


def preorder_recursive(node):
    """Рекурсивный pre-order обход. O(n)."""
    result = []
    if node:
        result.append(node.value)
        result.extend(preorder_recursive(node.left))
        result.extend(preorder_recursive(node.right))
    return result


def postorder_recursive(node):
    """Рекурсивный post-order обход. O(n)."""
    result = []
    if node:
        result.extend(postorder_recursive(node.left))
        result.extend(postorder_recursive(node.right))
        result.append(node.value)
    return result


def breadth_first(root):
    """Обход дерева в ширину (BFS). O(n)."""
    if root is None:
        return []

    result, queue = [], [root]
    while queue:
        current = queue.pop(0)
        result.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result
