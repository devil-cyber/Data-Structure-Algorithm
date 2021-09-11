from tree import Tree

res = 0
def diameter_tree(root):
    global res
    if root is None:
        return 0
    lh = diameter_tree(root.left)
    rh = diameter_tree(root.right)
    res = max(res,1+lh+rh)
    return 1 + max(lh,rh)




if __name__ == "__main__":
    t = Tree()
    root = t.create_tree()
    diameter_tree(root)
    print('The Diameter of the tree: ',res)
   
  
