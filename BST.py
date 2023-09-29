
class TreeNode():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class BST():
    """
    Binary Search Tree implemenation
    """

    def __init__(self) -> None:
        self.root = None

    def getQ(self):
        if self._qCount == 0:
            self._qCount += 1
            return "Enter the value for the new node"
        else:
            self._qCount += 1
            return ""

    def height(self) -> int:
        """
        Returns the maximum depth of the tree
        """
        return self._maxDepth(self.root)

    def _maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            return max(self._maxDepth(root.left), self._maxDepth(root.right)) + 1
