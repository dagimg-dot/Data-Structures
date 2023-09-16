
class TreeNode():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class Tree():
    """
    Tree implemenation
    """

    def __init__(self) -> None:
        self.root = None

    def maxDepth(self, root: TreeNode) -> int:
        """
        Returns the maximum depth of the tree
        """
        if root == None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
