from bst import BST

def search(root, key):
    if root is None:
        return False
    if key == root.data:
        return True
    elif key > root.data:
        return search(root.right, key)
    else:
        return search(root.left, key)


if __name__ == "__main__":
    b = BST()
    root = b.create_bst()
    key = 100
    print(f'Search result for {key} in bst:',search(root, key))
    