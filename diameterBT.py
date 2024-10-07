def diameterOfBinaryTree(root: TreeNode) -> int:
    def depth(node):
        nonlocal diameter
        if not node: return 0
        left = depth(node.left)
        right = depth(node.right)
        diameter = max(diameter, left + right)
        return 1 + max(left, right)
    diameter = 0
    depth(root)
    return diameter
