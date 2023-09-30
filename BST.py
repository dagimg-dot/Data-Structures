from typing import List
from type import types


class TreeNode():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class BST():
    """
    Binary Search Tree implemenation
    """

    def __init__(self, *args) -> None:
        """
        Create a binary search tree\n\n
        - `tree = BST()` creates an empty binary search tree\n
        - `tree = BST(4)` creates a binary search tree with a root\n
        - `tree = BST([1,2,3])` creates a binary search tree from a list
        """
        if len(args) == 0:
            self.root = None
            self.size = 0
        else:
            if type(args[0]) == types.LIST:
                self.__initWithList(args[0])
            else:
                self.__initWithRoot(args[0])

    def __initWithRoot(self, root) -> None:
        """
        Create a binary search tree with the root
        """
        new_node = TreeNode(root)
        self.root = new_node
        self.size = 1

    def __initWithList(self, objects: List[any]) -> None:
        """
        Create a binary search tree from a list of objects
        """
        self.root = None
        self.size = 0
        list_size = len(objects)
        for i in range(list_size):
            self.insert(objects[i])

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

        self.size += 1
        return True

    def search(self, value: any) -> bool:
        """
        Return true if the value is in the tree
        """
        current = self.root
        while current != None:
            if value < current.val:
                current = current.left
            elif value > current.val:
                current = current.right
            else:
                return True

        return False

    def height(self) -> int:
        """
        Returns the maximum depth of the tree
        """
        return self._maxDepth(self.root)

    def getSize(self) -> int:
        """
        Get the number of nodes in the tree
        """
        return self.size

    def isEmpty(self) -> bool:
        """
        Return true if the tree is empty
        """
        return self.size == 0

    def clear(self) -> None:
        """
        Remove all elements from the tree
        """
        self.root = None
        self.size = 0

    def _maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            return max(self._maxDepth(root.left), self._maxDepth(root.right)) + 1
