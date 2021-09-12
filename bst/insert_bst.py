class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None


def insert(root, key):
    if root is None:
        return Node(key)
    if key > root.data:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root
        
# For testing the new built tree we will used inorder transversal
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


if __name__ == "__main__":
    root = Node(11)
    insert(root,10)
    insert(root, 0)
    insert(root, 20)
    insert(root, 5)
    insert(root, 7)
    insert(root, 15)
    root = insert(root,8)
    print('the inorder transversal of bst is:',end=" ")
    inorder(root)
    print()