from tree import Tree

def children_sum_property(root):
    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    _sum = 0
    if root.left is not None:
        _sum += root.left.data
    if root.right is not None:
        _sum += root.right.data
    return (root.data == _sum and children_sum_property(root.left) and children_sum_property(root.right))



if __name__ == "__main__":
    t = Tree()
    root = t.create_tree()
    print('Tree follow children property or not:',children_sum_property(root))
