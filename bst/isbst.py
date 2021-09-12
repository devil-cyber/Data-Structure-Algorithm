from bst import BST
import sys

def isbst(_max, _min, root):
    if root is None:
        return True
    return ((root.data > _min) and (root.data < _max) and 
    (isbst(_max,_min, root.right) and isbst(_max, _min, root.left)))


if __name__ == "__main__":
    b = BST()
    root = b.create_bst()
    _max = sys.maxsize
    _min = -sys.maxsize
    print('The given set is a bst or not:', isbst(_max, _min, root))
    