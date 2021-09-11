from tree import Tree

def size_tree(root):
    if root is None:
        return 0
    return 1 + size_tree(root.left) + size_tree(root.right)




if __name__ == "__main__":

    t = Tree()
    root = t.create_tree()
    print('Size of tree is: ',size_tree(root))