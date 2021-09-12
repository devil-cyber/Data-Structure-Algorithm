class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

class BST:
    def __init__(self) -> None:
        pass
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key > root.data:
            root.right = self.insert(root.right, key)
        else:
            root.left = self.insert(root.left, key)
        return root
    def create_bst(self):
        root = Node(11)
        self.insert(root,10)
        self.insert(root, 0)
        self.insert(root, 20)
        self.insert(root, 5)
        self.insert(root, 7)
        self.insert(root, 15)
        root = self.insert(root,8)
        return root

"""
             11
            /  \
          10    20
         /     /
        0     15    
         \
          5
           \
            7
             \
              8 
"""
