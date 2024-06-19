def inorderTraversal(root) -> list[int]:
    result, stack = [], []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        result.append(root.val)
        root = root.right
    return result
