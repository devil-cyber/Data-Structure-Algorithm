class Node:
    def __init__(self, data) -> None:
        self.right = None
        self.left = None
        self.data = data

class Tree:
    def __init__(self):
        pass

    def create_tree(self):
        root = Node(10)
        root.left = Node(20)
        root.right = Node(30)
        root.left.left = Node(40)
        root.left.right = Node(50)
        root.right.left = Node(60)
        root.right.left.left = Node(0)
        return root
"""
Tree
                10
              /   \
            20     30
           /  \   /
          40   50 60
                 /
                0
"""
        


 