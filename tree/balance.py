from tree import Tree

def balance_tree(root):
    if root is None:
        return 0
    lh = balance_tree(root.left)
    if lh==-1:
        return -1
    rh = balance_tree(root.right)
    if rh==-1:
        return -1
    if abs(lh-rh) > 1:
        return -1
    else:
        return 1 + max(lh,rh)



if __name__ == "__main__":
    t = Tree()
    root = t.create_tree()
    h = balance_tree(root)
    if h==-1:
        print('Tree is not balanced')
    else:
        print('Tree is height balanced')
  
