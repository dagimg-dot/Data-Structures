
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

    def insert(self, value: any) -> bool:
        """
        Insert value into the binary search tree.

        Return true if the element is inserted successfully.
        """
        new_treeNode = TreeNode(value)
        if self.root == None:
            self.root = new_treeNode
        else:
            parent = None
            current = self.root
            while current != None:
                if value < current.val:
                    parent = current
                    current = current.left
                elif value > current.val:
                    parent = current
                    current = current.right
                else:
                    return False

            if value < parent.val:
                parent.left = new_treeNode
            else:
                parent.right = new_treeNode

        return True

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
