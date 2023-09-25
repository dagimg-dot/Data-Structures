
class TreeNode():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


"""
Code from C++

struct node *create() {
  int x; // different local variable would be created for each function call
  struct node *newNode;
  newNode = (struct node *)malloc(sizeof(struct node));
  cout << "Enter the data or enter 'n/N' for no node" << endl;
  cin >> x;
    while (dataTypeChecker(x) != 0) {
      cout << "Invalid input, please enter data again : ";
      cin >> x;
    }
  if (x == 0)
    return 0;
  newNode->data = x;
  cout << " Enter the data of left child of " << x << endl;
  newNode->left = create(); // create function always return pointer to node(address)
  cout << " Enter the data of right child of " << x << endl;
  newNode->right = create(); // this recursion
  return newNode;
}

"""


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
