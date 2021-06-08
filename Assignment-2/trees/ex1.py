class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root):
        self.root = root

    def print(self):
        if self.root:
            print(self.root.value, end=" ")
            Tree(self.root.left).print()
            Tree(self.root.right).print()