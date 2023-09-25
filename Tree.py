
class TreeNode():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class Tree():
    """
    Tree implemenation
    """

    _qCount = 0

    def __init__(self) -> None:
        self.root = None

    def getQ(self):
        if self._qCount == 0:
            self._qCount += 1
            return "Enter the value for the new node"
        else:
            self._qCount += 1
            return ""

    def create(self) -> TreeNode:
        value = input(
            f"{self.getQ()} or hit 'Enter' key for no node: ")
        if value == '':
            return

        new_node = TreeNode(val=value)

        if self._qCount == 0:
            self.root = new_node

        print("Enter the value of left child of " + value, end='')
        new_node.left = self.create()
        print("Enter the value of right child of " + value, end='')
        new_node.right = self.create()
        print(self.height())
        return new_node

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
