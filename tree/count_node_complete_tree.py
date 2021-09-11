from tree import Tree

def height_left(root):
    hgt = 0
    node = root
    while node:
        hgt += 1
        node = node.left
    return hgt

def height_right(root):
    hgt = 0
    node = root
    while node:
        hgt += 1
        node = node.right
    return hgt

def count_node(root):
    if root is None:
        return 0
    lh = height_left(root)
    rh = height_right(root)
    if rh==lh:
        return (1 << rh) -1
    return 1 + count_node(root.left) + count_node(root.right)


if __name__ == "__main__":
    t = Tree()
    root = t.create_tree()
    print('the number of node in complete binary tree is:', count_node(root))