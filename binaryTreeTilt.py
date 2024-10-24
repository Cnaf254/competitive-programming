def findTilt(root: TreeNode) -> int:
    def dfs(node):
        nonlocal tilt
        if not node: return 0
        left = dfs(node.left)
        right = dfs(node.right)
        tilt += abs(left - right)
        return node.val + left + right
    tilt = 0
    dfs(root)
    return tilt
