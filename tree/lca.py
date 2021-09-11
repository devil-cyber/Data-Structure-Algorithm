from tree import Tree

def lca_tree(p, q, root):
    if root == None or root.data == p or root.data == q:
        return root
    left = lca_tree(p, q, root.left)
    right = lca_tree(p, q, root.right)
    if left == None:
        return right
    elif right == None:
        return left
    else:
        return root


if __name__ == "__main__":
    t = Tree()
    root = t.create_tree()
    p = 30
    q = 0
    print(f'the lca of {p} and {q} is:',lca_tree(p, q, root).data)