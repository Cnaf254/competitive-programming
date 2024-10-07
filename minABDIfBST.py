def getMinimumDifference(root: TreeNode) -> int:
    def inorder(node):
        return inorder(node.left) + [node.val] + inorder(node.right) if node else []
    values = inorder(root)
    return min(b - a for a, b in zip(values, values[1:]))
