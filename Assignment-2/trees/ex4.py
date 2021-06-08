class BinarySearchTree:

    class Node:

        def __init__(self, value):
            self.val = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root=self.Node(key)
            return
        current_node = self.root
        while True:
            if key < current_node.val:
                if not current_node.left:
                    current_node.left = self.Node(key)
                    return
                else:
                    current_node = current_node.left
            else:
                if not current_node.right:
                    current_node.right = self.Node(key)
                    return
                else:
                    current_node = current_node.right

    def find(self, key):
        if not self.root: return False
        current_node = self.root
        while current_node and current_node.val != key:
            if key < current_node.val: current_node = current_node.left
            else: current_node = current_node.right
        return bool(current_node)