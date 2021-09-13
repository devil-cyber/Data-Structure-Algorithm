from tree import Tree

def lca(root,p, q):
    if root is None or root.data == p or root.data == q:
        return root
    right = lca(root.right,p,q)
    left = lca(root.left,p,q)
    if right is None:
        return left
    elif left is None:
        return right
    else:
        return root

def distance(root, k, dist):
    if root is None:
        return -1
    if root.data == k:
        return dist
    left = distance(root.left, k, dist + 1)
    if left!=-1:
        return left
    return distance(root.right, k, dist + 1)

def distanceBetween(root, n1, n2):
    lca1 = lca(root, n1, n2)
    d1 = distance(lca1, n1, 0)
    d2 = distance(lca1, n2, 0)
    return d1 + d2
    



if __name__ == '__main__':
    t = Tree()
    root = t.create_tree()
    d = distanceBetween(root, 50, 0)
    print(d)
