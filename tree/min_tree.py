from tree import Tree
import sys

# min value in tree

minval = sys.maxsize
def _min(root) -> None:
    global minval
    if root is None:
        return
    minval = min(minval, root.data)
    _min(root.left)
    _min(root.right)





if __name__ == "__main__":
    t = Tree()
    root = t.create_tree()
    _min(root)
    print('Minimum value in tree is:', minval)