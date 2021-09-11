from tree import Tree
import sys

# max value in tree

maxval = -sys.maxsize
def _max(root) -> None:
    global maxval
    if root is None:
        return
    maxval = max(maxval, root.data)
    _max(root.left)
    _max(root.right)





if __name__ == "__main__":
    t = Tree()
    root = t.create_tree()
    _max(root)
    print('Maximum value in tree is:', maxval)