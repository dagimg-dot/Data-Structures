import tkinter as tk
from BST import BST
from BST import TreeNode
from math import sqrt


class VisualizeBST():
    """
    Class to visualize a binary search tree.\n
    Args:
        tree: `BST` \n
    `visualizer = VisualizeBST(tree)`\n
    `visualizer.visualize()`
    """

    def __init__(self, tree: BST) -> None:
        self.window = tk.Tk()
        self.tree = tree
        self.width = 600
        self.height = 600
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.title("BST Visualizer")

        self.radius = 50
        self.vGap = 70
        self.canvas = self.createCanvas()

    def createCanvas(self) -> tk.Canvas:
        canvas = tk.Canvas(self.window, bg="#777")
        canvas.pack(fill='both', expand=1)
        return canvas

    def paintComponent(self) -> None:
        """
        Main method to paint the binary search tree on the canvas.
        """

        def displayTree(root: TreeNode, x: int, y: int, hGap: int) -> None:

            def connectTwoNodes(x1: int, y1: int, x2: int, y2: int) -> None:
                d = sqrt(self.vGap * self.vGap + (x2 - x1) * (x2 - x1))
                x11 = int(x1 - self.radius * (x1 - x2) / d)
                y11 = int(y1 - self.radius * (y1 - y2) / d)
                x21 = int(x2 + self.radius * (x1 - x2) / d)
                y21 = int(y2 + self.radius * (y1 - y2) / d)
                self.canvas.create_line(x11, y11, x21, y21)

            x += (self.radius / 2)

            # Display the root
            self.canvas.create_oval(x, y - self.radius, x - self.radius, y)
            self.canvas.create_text(x - 25, y - 25, text=f"{root.val}")

            if root.left != None:
                connectTwoNodes(x - hGap, y + self.vGap, x, y)
                displayTree(root.left, x - hGap, y + self.vGap, hGap / 2)

            if root.right != None:
                connectTwoNodes(x + hGap, y + self.vGap, x, y)
                displayTree(root.right, x + hGap, y + self.vGap, hGap / 2)

        if self.tree.getRoot != None:
            tree = self.tree
            displayTree(tree.getRoot(), self.width / 2,
                        70, self.width / 4)

    def visualize(self):
        """
        Display the given binary search tree in a window.
        """
        self.paintComponent()
        self.window.mainloop()


if __name__ == "__main__":
    visualizer = VisualizeBST()
    visualizer.visualize()
