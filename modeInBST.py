def findMode(root: TreeNode) -> List[int]:
    from collections import Counter
    def inorder(node):
        return inorder(node.left) + [node.val] + inorder(node.right) if node else []
    counter = Counter(inorder(root))
    max_freq = max(counter.values())
    return [k for k, v in counter.items() if v == max_freq]
