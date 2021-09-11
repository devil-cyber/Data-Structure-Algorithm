from tree import Tree

def path_from_root_node(root, path, x):
    if root is None:
        return False
    path.append(root.data)
    if root.data == x:
        return True
    if (path_from_root_node(root.left, path, x)) or (path_from_root_node(root.right, path, x)):
        return True
    path.pop()
    return False

    



if __name__ == "__main__":
    t = Tree()
    root = t.create_tree()
    node1 = 40
    node2 = 0
    path1 = []
    path2 = []
    path_from_root_node(root, path1, node1)
    path_from_root_node(root, path2, node2)
    print(f"path from {root.data} to {node1} is:", path1)
    print(f"path from {root.data} to {node2} is:", path2)
